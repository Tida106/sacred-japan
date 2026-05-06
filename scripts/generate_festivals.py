"""Generate Sacred Japan festival images via Gemini API (Nano Banana / gemini-2.5-flash-image).

Usage:
    python generate_festivals.py                # generate all 9
    python generate_festivals.py gion sanja     # generate specific ones
    python generate_festivals.py --force        # overwrite existing without prompt

Output: ../images/festival-{name}.jpg  (photorealistic, copyright-safe)

Note: gemini-2.5-flash-image returns PNG bytes at its native resolution
(typically near 1024x1024). We convert to JPEG (quality 92) for site delivery.
"""
from __future__ import annotations

import io
import os
import sys
from pathlib import Path

from dotenv import load_dotenv
from google import genai
from PIL import Image


PROMPTS: dict[str, str] = {
    "gion": (
        "A photorealistic 16:9 cinematic night scene of Kyoto's Gion Matsuri 'Yoiyama' eve. "
        "Towering wooden yamaboko festival floats decorated with intricate antique tapestries, "
        "draped with hundreds of glowing chochin paper lanterns casting warm orange light against "
        "a deep indigo evening sky. Traditional machiya wooden townhouses line a narrow Kyoto street. "
        "Light mist softens the lantern bokeh. No visible faces, no real logos, no readable text on "
        "tapestries — use only abstract floral, wave, and crane motifs. Mystical, reverent traditional "
        "atmosphere. Shot on full-frame camera, 35mm lens, shallow depth of field, rich shadows, "
        "painterly highlights."
    ),
    "sanja": (
        "A photorealistic 16:9 cinematic daytime scene of Tokyo's Sanja Matsuri in Asakusa. "
        "A golden mikoshi portable shrine with shimmering brass fittings, red ceremonial rope, and "
        "a phoenix finial on top, being hoisted high through a dense crowd. Carriers wear traditional "
        "dark indigo happi coats and white headbands, viewed from behind and side so all faces are "
        "obscured. The vermillion silhouette of a five-story pagoda rises softly in the background. "
        "Confetti petals drift through the air. Banners feature only abstract Edo-era wave and crest "
        "patterns — no readable kanji, no real logos, no trademarks. Energetic yet reverent late-spring "
        "atmosphere. Shot on full-frame, 50mm, dynamic motion blur on lifted poles."
    ),
    "tenjin": (
        "A photorealistic 16:9 cinematic night scene of Osaka's Tenjin Matsuri river procession. "
        "A traditional Japanese wooden boat strung with hundreds of glowing red and white paper "
        "lanterns drifts along a calm, dark river, the lantern reflections shimmering on the water "
        "surface. Brilliant gold and crimson fireworks burst overhead against the deep night sky. "
        "The silhouette of a traditional shrine roof sits on the distant riverbank. Figures aboard "
        "the boat appear only as backlit silhouettes — no visible faces, no modern buildings, no "
        "logos, no readable text. Mystical, ceremonial, ancestral atmosphere. Shot on full-frame, "
        "long-exposure feel, deep blacks contrasting jewel-toned highlights."
    ),
    "kanda": (
        "A photorealistic 16:9 cinematic daytime scene of Tokyo's Kanda Matsuri. An ornate gilded "
        "mikoshi portable shrine with intricate black-lacquer and gold leaf detailing and a golden "
        "phoenix on the roof, being carried through the entrance of a traditional Shinto shrine with "
        "a vermillion torii gate. Carriers wear deep blue happi coats and are viewed strictly from "
        "behind so no faces are visible. Fresh green maple leaves frame the scene. Festival banners "
        "carry only abstract family-crest-style motifs — no readable text, no logos, no real "
        "trademarks. Late-spring overcast soft light, ceremonial Edo-era atmosphere. Shot on "
        "full-frame, 35mm, slight atmospheric haze, vivid red against muted greens."
    ),
    "aoi": (
        "A photorealistic 16:9 cinematic scene of Kyoto's Aoi Matsuri imperial procession. An "
        "elegant ox-drawn wooden cart (gissha) decorated with twin-leaf hollyhock garlands, moving "
        "slowly along an ancient moss-edged path through a towering cedar forest, approaching a "
        "weathered stone shrine torii. Figures wear elaborate Heian-period twelve-layer junihitoe "
        "court kimono in muted creams, sage greens, and pale plum, walking solemnly alongside — all "
        "viewed from behind so no faces are visible. Soft dappled morning sunlight filters through "
        "tall trees, gentle forest mist. Pure Heian elegance, no modern elements, no logos, no "
        "readable text. Shot on full-frame, 85mm, painterly soft focus, muted warm palette."
    ),
    "jidai": (
        "A photorealistic 16:9 cinematic autumn scene of Kyoto's Jidai Matsuri 'Festival of the Ages.' "
        "A grand procession of figures in historically authentic Sengoku-era samurai armor and "
        "Heian-period noble court robes walks in formation along a wide Kyoto avenue lined with maple "
        "trees ablaze in vivid red and gold autumn foliage. The vermillion torii gate of a grand "
        "shrine is visible in the soft-focused distance. All figures shown from side or behind with "
        "faces obscured by helmets, hats, or shadow. Banners carry only abstract historical motifs — "
        "no readable text, no modern logos, no trademarks. Crisp October daylight, ceremonial "
        "gravitas. Shot on full-frame, 50mm, deep color saturation, cinematic grade."
    ),
    "nebuta": (
        "A photorealistic 16:9 cinematic night scene of Aomori's Nebuta Matsuri. A colossal "
        "illuminated washi-paper float depicting a fierce mythical warrior figure painted in vivid "
        "vermilion reds, jet blacks, deep blues, and burnished gold, glowing brilliantly from within "
        "against a pitch-dark August night sky. The float is mid-parade on a wide city street, with "
        "anonymous crowd silhouettes filling the foreground — no visible faces, no logos. Silhouettes "
        "of taiko drummers at the float's base. Electric, spiritual, ancestral atmosphere. Shot on "
        "full-frame, 35mm wide, dramatic internal backlighting, deep blacks contrasting glowing colors."
    ),
    "awa": (
        "A photorealistic 16:9 cinematic night scene of Tokushima's Awa Odori dance festival. A line "
        "of dancers in traditional indigo-blue cotton yukata and tall woven amigasa straw hats that "
        "fully obscure their faces, captured mid-movement with arms gracefully raised in the iconic "
        "Awa Odori pose, dancing along a lantern-lit street. Warm chochin paper lanterns strung "
        "overhead cast a golden glow. Silhouettes of shamisen and taiko musicians line the background. "
        "No logos, no readable text, no visible faces. Festive yet meditative summer Obon atmosphere. "
        "Shot on full-frame, 50mm, slight motion blur on sleeves and hands, warm golden tones."
    ),
    "yosakoi": (
        "A photorealistic 16:9 cinematic daytime scene of Kochi's Yosakoi Matsuri. A team of dancers "
        "in vibrant happi-style coats — bold purples, oranges, indigos, and crimsons with abstract "
        "wave and floral patterns — captured mid-routine holding traditional naruko wooden clappers "
        "in raised hands. Photographed from a low side angle, faces obscured by hats and motion blur. "
        "A wide Kochi street lined with palm trees under intense summer light. Confetti drifts through "
        "the air; arms blur with movement to convey energy. No logos, no readable text, no real-world "
        "brand sponsors. Joyful, modern-traditional fusion atmosphere. Shot on full-frame, 35mm, "
        "vivid saturated colors, dynamic composition."
    ),
}

MODEL = "gemini-2.5-flash-image"
JPEG_QUALITY = 92


def extract_image_bytes(response) -> bytes | None:
    """Pull the first inline image payload out of a generate_content response."""
    for candidate in getattr(response, "candidates", []) or []:
        content = getattr(candidate, "content", None)
        if not content:
            continue
        for part in getattr(content, "parts", []) or []:
            inline = getattr(part, "inline_data", None)
            if inline and getattr(inline, "data", None):
                return inline.data
    return None


def save_as_jpeg(png_bytes: bytes, out: Path) -> None:
    """Convert PNG bytes from Nano Banana into a clean JPEG on disk."""
    img = Image.open(io.BytesIO(png_bytes))
    if img.mode != "RGB":
        img = img.convert("RGB")
    img.save(str(out), format="JPEG", quality=JPEG_QUALITY, optimize=True)


def main(argv: list[str]) -> int:
    force = "--force" in argv
    targets = [a for a in argv if not a.startswith("--")]

    load_dotenv(Path(__file__).resolve().parent / ".env")
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key or api_key == "your_new_key_here":
        print("ERROR: GEMINI_API_KEY not set in scripts/.env", file=sys.stderr)
        print("Copy scripts/.env.example to scripts/.env and paste a fresh key.", file=sys.stderr)
        return 1

    client = genai.Client(api_key=api_key)
    out_dir = Path(__file__).resolve().parent.parent / "images"
    out_dir.mkdir(exist_ok=True)

    todo = targets if targets else list(PROMPTS.keys())
    failures: list[str] = []
    successes = 0

    for name in todo:
        if name not in PROMPTS:
            print(f"SKIP: unknown festival '{name}' (valid: {', '.join(PROMPTS)})")
            continue

        out = out_dir / f"festival-{name}.jpg"
        if out.exists() and not force:
            ans = input(f"{out.name} already exists. Overwrite? [y/N] ").strip().lower()
            if ans != "y":
                print(f"  skipped {out.name}")
                continue

        print(f"Generating {out.name} ...")
        try:
            response = client.models.generate_content(
                model=MODEL,
                contents=PROMPTS[name],
            )
        except Exception as e:
            print(f"  FAIL: {e}", file=sys.stderr)
            failures.append(name)
            continue

        png_bytes = extract_image_bytes(response)
        if not png_bytes:
            print(f"  FAIL: no image bytes returned (likely safety-filter block)", file=sys.stderr)
            failures.append(name)
            continue

        try:
            save_as_jpeg(png_bytes, out)
        except Exception as e:
            print(f"  FAIL on JPEG conversion: {e}", file=sys.stderr)
            failures.append(name)
            continue

        successes += 1
        print(f"  saved -> {out}")

    print()
    if failures:
        print(f"Done with {len(failures)} failure(s): {', '.join(failures)}")
        return 2
    print(f"Done. Generated {successes} image(s).")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
