"""Insert a 'Sacred Places to Visit' group into the mobile menu of all
18 pages that have a mobile-menu block.

The group goes between the existing 'Guides' link and the 'Culture' link,
with the same indented mobile-sub treatment used by Culture sub-items.
"""
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent.parent

PAGES = [
    "index.html",
    "guides/index.html",
    "guides/izumo-taisha/index.html",
    "guides/ise-grand-shrine/index.html",
    "guides/atsuta-shrine/index.html",
    "guides/three-sacred-treasures/index.html",
    "guides/best-time-fushimi-inari/index.html",
    "guides/koyasan-temple-stay/index.html",
    "guides/shrine-vs-temple/index.html",
    "guides/goshuin-guide/index.html",
    "guides/omamori-guide/index.html",
    "guides/why-did-you-come-to-japan/index.html",
    "culture/index.html",
    "castles/index.html",
    "crafts/index.html",
    "anime/index.html",
    "regional-food/index.html",
    "about/index.html",
]

OLD = '''    <li><a href="/guides/">Guides</a></li>
    <li><a href="/culture/">Culture</a></li>'''

NEW = '''    <li><a href="/guides/">Guides</a></li>
    <li style="padding:14px 24px 6px;font-family:'Noto Serif JP',serif;font-size:10px;letter-spacing:3px;color:var(--beni);text-transform:uppercase;background:var(--washi-dark);border-bottom:1px solid var(--border);">Sacred Places to Visit ／ 聖地を訪ねる</li>
    <li><a href="/guides/ise-grand-shrine/" class="mobile-sub" onclick="trackEvent('click','internal','nav_mobile_to_ise')">— Ise Grand Shrine</a></li>
    <li><a href="/guides/atsuta-shrine/" class="mobile-sub" onclick="trackEvent('click','internal','nav_mobile_to_atsuta')">— Atsuta Shrine</a></li>
    <li><a href="/guides/three-sacred-treasures/" class="mobile-sub" onclick="trackEvent('click','internal','nav_mobile_to_treasures')">— Three Sacred Treasures</a></li>
    <li><a href="/guides/best-time-fushimi-inari/" class="mobile-sub" onclick="trackEvent('click','internal','nav_mobile_to_fushimi')">— Fushimi Inari</a></li>
    <li><a href="/guides/koyasan-temple-stay/" class="mobile-sub" onclick="trackEvent('click','internal','nav_mobile_to_koyasan')">— Koyasan Temple Stay</a></li>
    <li><a href="/guides/izumo-taisha/" class="mobile-sub" onclick="trackEvent('click','internal','nav_mobile_to_izumo')">— Izumo Taisha</a></li>
    <li><a href="/culture/">Culture</a></li>'''


def process(p: Path) -> str:
    text = p.read_text(encoding="utf-8")
    if "nav_mobile_to_izumo" in text:
        return "already processed"
    if OLD not in text:
        return "anchor not found"
    text = text.replace(OLD, NEW, 1)
    p.write_text(text, encoding="utf-8")
    return "ok"


def main():
    fails = 0
    for rel in PAGES:
        p = ROOT / rel
        status = process(p)
        flag = "OK" if status == "ok" else ("SKIP" if status == "already processed" else "FAIL")
        print(f"  [{flag}] {rel}  ({status})")
        if flag == "FAIL":
            fails += 1
    print()
    if fails:
        print(f"FAILED: {fails}")
        sys.exit(1)
    print("All done.")


if __name__ == "__main__":
    main()
