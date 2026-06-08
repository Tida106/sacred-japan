"""Verify that all 18 pages now have the Sacred Places group in mobile menu."""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent.parent
PAGES = [
    "index.html", "guides/index.html", "guides/izumo-taisha/index.html",
    "guides/ise-grand-shrine/index.html", "guides/atsuta-shrine/index.html",
    "guides/three-sacred-treasures/index.html", "guides/best-time-fushimi-inari/index.html",
    "guides/koyasan-temple-stay/index.html", "guides/shrine-vs-temple/index.html",
    "guides/goshuin-guide/index.html", "guides/omamori-guide/index.html",
    "guides/why-did-you-come-to-japan/index.html", "culture/index.html",
    "castles/index.html", "crafts/index.html", "anime/index.html",
    "regional-food/index.html", "about/index.html",
]

LABELS = ["nav_mobile_to_ise", "nav_mobile_to_atsuta", "nav_mobile_to_treasures",
          "nav_mobile_to_fushimi", "nav_mobile_to_koyasan", "nav_mobile_to_izumo"]

print(f"{'FILE':50} {'HEAD':>5} {'TRK':>4} {'IZUMO':>6} {'DIVS':>5}")
print("-" * 80)
all_ok = True
for rel in PAGES:
    p = ROOT / rel
    t = p.read_text(encoding="utf-8")
    has_head = "Sacred Places to Visit ／ 聖地を訪ねる" in t
    trk_count = sum(1 for L in LABELS if L in t)
    has_izumo = '/guides/izumo-taisha/' in t and 'nav_mobile_to_izumo' in t
    divs_open = len(re.findall(r"<div\b", t))
    divs_close = t.count("</div>")
    div_bal = divs_open - divs_close
    ok = has_head and trk_count == 6 and has_izumo
    if not ok:
        all_ok = False
    flag = "" if ok else "  <-- ISSUE"
    print(f"{rel:50} {('Y' if has_head else 'N'):>5} {trk_count:>4} {('Y' if has_izumo else 'N'):>6} {div_bal:>5}{flag}")

print()
print("Expected: HEAD=Y, TRK=6, IZUMO=Y")
print("RESULT:", "ALL OK" if all_ok else "ISSUES FOUND")
