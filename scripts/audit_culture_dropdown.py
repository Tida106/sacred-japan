from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent.parent
pages = sorted(p for p in ROOT.rglob("*.html"))

print(f'{"FILE":62} {"PC":>3} {"MENU":>4} {"MOB":>4} {"SUB":>4} {"TRK":>4} {"BAL":>4}')
print("-" * 95)
all_ok = True
for p in pages:
    rel = str(p.relative_to(ROOT)).replace("\\", "/")
    text = p.read_text(encoding="utf-8")
    pc_dropdown = text.count('class="nav-dropdown"')
    nav_menu = text.count('class="nav-dropdown-menu"')
    has_mobile_menu = '<div class="mobile-menu"' in text
    mobile_sub = text.count('class="mobile-sub"')
    track_labels = sorted(set(re.findall(r"nav_culture_to_\w+", text)))
    div_open = len(re.findall(r"<div\b", text))
    div_close = text.count("</div>")
    bal = div_open - div_close
    expected_sub = 5 if has_mobile_menu else 0
    ok = (pc_dropdown == 1 and nav_menu == 1 and mobile_sub == expected_sub
          and len(track_labels) == 5 and bal == 0)
    if not ok:
        all_ok = False
    flag = "" if ok else "  <-- ISSUE"
    print(f"{rel:62} {pc_dropdown:>3} {nav_menu:>4} {('Y' if has_mobile_menu else 'N'):>4} {mobile_sub:>4} {len(track_labels):>4} {bal:>4}{flag}")

print()
print("Expected: PC=1, MENU=1, SUB=5 (or 0 if MOB=N), TRK=5 unique labels, BAL=0")
print("RESULT:", "ALL OK" if all_ok else "ISSUES FOUND")
