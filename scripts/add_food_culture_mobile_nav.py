"""Add tea / ikebana / food guides to the mobile menu on every page.

Inserts the new <li> items just before the "— Culture Hub →" mobile entry.
Idempotent: pages that already contain the marker are skipped.
Run: python3 scripts/add_food_culture_mobile_nav.py
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

ANCHOR = '<li><a href="/culture/" class="mobile-sub" onclick="trackEvent(\'click\',\'internal\',\'nav_culture_to_hub\')">— Culture Hub →</a></li>'
MARKER = "nav_mobile_to_tea_ceremony"

ITEMS = [
    ("tea-ceremony", "tea_ceremony", "Tea Ceremony"),
    ("ikebana", "ikebana", "Ikebana"),
    ("popular-dishes", "popular_dishes", "Japanese Dishes"),
    ("ramen", "ramen", "Ramen"),
    ("noodles", "noodles", "Noodles"),
    ("yakitori", "yakitori", "Yakitori"),
    ("bread", "bread", "Japanese Bread"),
    ("wagashi", "wagashi", "Wagashi"),
    ("japanese-sweets", "japanese_sweets", "Japanese Sweets"),
]


def build_block(indent: str) -> str:
    lines = []
    for slug, key, label in ITEMS:
        lines.append(
            f'<li><a href="/culture/{slug}/" class="mobile-sub" '
            f"onclick=\"trackEvent('click','internal','nav_mobile_to_{key}')\">— {label}</a></li>"
        )
    return ("\n" + indent).join(lines) + "\n" + indent


def main() -> None:
    changed = skipped = nomenu = 0
    for p in sorted(ROOT.rglob("*.html")):
        if any(part in {"node_modules", ".git", "_tools"} for part in p.parts):
            continue
        s = p.read_text(encoding="utf-8")
        if ANCHOR not in s:
            nomenu += 1
            continue
        if MARKER in s:
            skipped += 1
            continue
        i = s.index(ANCHOR)
        line_start = s.rfind("\n", 0, i) + 1
        indent = s[line_start:i]
        s = s[:i] + build_block(indent) + s[i:]
        p.write_text(s, encoding="utf-8")
        changed += 1
    print(f"changed={changed} already={skipped} no-anchor={nomenu}")


if __name__ == "__main__":
    main()
