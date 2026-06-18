#!/usr/bin/env python3
"""
Comprehensive image compression:
1. ogp.webp  → 1200x633, quality=65  (hero desktop)
   ogp-sm.webp → 750x396, quality=65  (hero mobile, NEW)
2. ise-jingu-card.jpg/webp → 800x533  (spot card, guide lead kept at 1200x800)
3. dazaifu / sumiyoshi → 1200x675  (guide lead photos)
4. All other 1376+ px thumbnail images → 800px max dim, proportional
"""
import sys
from pathlib import Path
from PIL import Image

sys.stdout.reconfigure(encoding='utf-8')
BASE = Path(__file__).parent.parent
IMAGES = BASE / 'images'

# ── helpers ────────────────────────────────────────────────────────────────
def save_jpg(img, path, quality=87):
    mode = 'RGB' if img.mode not in ('RGB',) else img.mode
    img.convert(mode).save(path, 'JPEG', quality=quality, optimize=True)

def save_webp(img, path, quality=75):
    mode = 'RGBA' if img.mode in ('RGBA','LA','P') else 'RGB'
    img.convert(mode).save(path, 'WEBP', quality=quality, method=4)

def resize_to_width(img, target_w):
    w, h = img.size
    target_h = round(h * target_w / w)
    return img.resize((target_w, target_h), Image.LANCZOS)

def resize_fit(img, max_dim):
    """Resize so largest dimension == max_dim, keep aspect ratio."""
    w, h = img.size
    if w >= h:
        return resize_to_width(img, max_dim)
    else:
        target_h = max_dim
        target_w = round(w * max_dim / h)
        return img.resize((target_w, target_h), Image.LANCZOS)

# ── skip list: images already appropriately sized or handled separately ────
SKIP_STEMS = {
    # guide lead photos handled separately
    'dazaifu', 'sumiyoshi', 'ise-jingu',
    # small guide card photos (already ≤460px)
    'kinkakuji', 'sensoji', 'itsukushima', 'meijijingu', 'todaiji',
    # shukubo section (already 800×450)
    'shukubo-koyasan', 'shukubo-miyajima', 'shukubo-prayer',
    # food hero photos (already 800×450)
    'food-shojin', 'food-inari',
    # large PNG CSS backgrounds (not served directly, WebP already used)
    # Their .webp versions are at 1024x1024 — skip for now
    'omamori', 'ema', 'shinsui', 'ofuda', 'dorei', 'omikuji',
    # map (WebP already only 43KB)
    'japan-map',
    # ogp (handled separately)
    'ogp',
}

results = []

# ── 1. ogp.webp (desktop hero) ────────────────────────────────────────────
print("=== ogp images ===")
ogp_src = BASE / 'ogp.png'
ogp_dst = BASE / 'ogp.webp'
ogp_sm  = BASE / 'ogp-sm.webp'

with Image.open(ogp_src) as img:
    before_webp = ogp_dst.stat().st_size
    desk = resize_to_width(img, 1200)
    save_webp(desk, ogp_dst, quality=65)
    after_webp = ogp_dst.stat().st_size
    print(f"  ogp.webp:    1424x752 → {desk.size[0]}x{desk.size[1]}  {before_webp//1024}KB → {after_webp//1024}KB")

    mob = resize_to_width(img, 750)
    save_webp(mob, ogp_sm, quality=65)
    print(f"  ogp-sm.webp: NEW {mob.size[0]}x{mob.size[1]}  {ogp_sm.stat().st_size//1024}KB")

# ── 2. ise-jingu-card (spot card only) ────────────────────────────────────
print("\n=== ise-jingu-card (spot card) ===")
ise_src = IMAGES / 'ise-jingu.jpg'
ise_card_jpg = IMAGES / 'ise-jingu-card.jpg'
ise_card_webp = IMAGES / 'ise-jingu-card.webp'

with Image.open(ise_src) as img:
    card = resize_to_width(img, 800)
    save_jpg(card, ise_card_jpg, quality=87)
    save_webp(card, ise_card_webp, quality=75)
    print(f"  ise-jingu-card.jpg:  {card.size[0]}x{card.size[1]}  {ise_card_jpg.stat().st_size//1024}KB")
    print(f"  ise-jingu-card.webp: {card.size[0]}x{card.size[1]}  {ise_card_webp.stat().st_size//1024}KB")

# ── 3. dazaifu / sumiyoshi (guide lead photos) ────────────────────────────
print("\n=== Guide lead photos → 1200x675 ===")
for stem in ('dazaifu', 'sumiyoshi'):
    src_jpg = IMAGES / f'{stem}.jpg'
    src_webp = IMAGES / f'{stem}.webp'
    if src_jpg.exists():
        with Image.open(src_jpg) as img:
            before = src_jpg.stat().st_size
            resized = img.resize((1200, 675), Image.LANCZOS)
            save_jpg(resized, src_jpg, quality=87)
            save_webp(resized, src_webp, quality=78)
            print(f"  {stem}.jpg:  {img.size} → 1200x675  {before//1024}KB → {src_jpg.stat().st_size//1024}KB")
            print(f"  {stem}.webp: {img.size} → 1200x675  {src_webp.stat().st_size//1024}KB")

# ── 4. Batch thumbnail images → 800px max dim ─────────────────────────────
print("\n=== Thumbnail images → 800px max dim ===")
for jpg in sorted(IMAGES.glob('*.jpg')):
    stem = jpg.stem
    if stem in SKIP_STEMS:
        continue
    with Image.open(jpg) as img:
        w, h = img.size
        if max(w, h) <= 800:
            continue  # already small enough

        before_jpg = jpg.stat().st_size
        resized = resize_fit(img, 800)
        save_jpg(resized, jpg, quality=85)
        after_jpg = jpg.stat().st_size

        # regenerate WebP
        webp = jpg.with_suffix('.webp')
        webp_before = webp.stat().st_size if webp.exists() else 0
        save_webp(resized, webp, quality=75)
        webp_after = webp.stat().st_size

        results.append((stem, w, h, resized.size[0], resized.size[1],
                        before_jpg, after_jpg, webp_before, webp_after))

for stem, ow, oh, nw, nh, bj, aj, bw, aw in results:
    print(f"  {stem}: {ow}x{oh} → {nw}x{nh}  "
          f"jpg {bj//1024}→{aj//1024}KB  webp {bw//1024}→{aw//1024}KB")

total_saved_jpg  = sum(r[5]-r[6] for r in results)
total_saved_webp = sum(r[7]-r[8] for r in results)
print(f"\nBatch: {len(results)} images processed")
print(f"  JPG total saved:  {total_saved_jpg//1024}KB")
print(f"  WebP total saved: {total_saved_webp//1024}KB")
