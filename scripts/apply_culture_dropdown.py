"""Apply Culture dropdown nav change to all 19 remaining pages.

index.html is already done — this script handles the other 19.

Three categories of pages:
  A. 16 main pages (full structure): nav-links + mobile-menu + main CSS
     - Inject full CSS block (PC dropdown + mobile sub styles)
     - Modify PC nav Culture <li> (with or without class="current")
     - Modify mobile menu Culture <li>
  B. 3 simple pages (terms.html / privacy-policy.html / contact.html):
     - Inject PC dropdown CSS only
     - Modify PC nav Culture <li> (no mobile menu exists)
"""
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent.parent

MAIN_PAGES = [
    "regional-food/index.html", "crafts/index.html", "castles/index.html",
    "anime/index.html",
    "guides/why-did-you-come-to-japan/index.html",
    "guides/three-sacred-treasures/index.html",
    "guides/shrine-vs-temple/index.html",
    "guides/omamori-guide/index.html",
    "guides/koyasan-temple-stay/index.html",
    "guides/ise-grand-shrine/index.html",
    "guides/index.html",
    "guides/goshuin-guide/index.html",
    "guides/best-time-fushimi-inari/index.html",
    "guides/atsuta-shrine/index.html",
    "culture/index.html",
    "about/index.html",
]

SIMPLE_PAGES = ["terms.html", "privacy-policy.html", "contact.html"]

# ---- CSS blocks ----

CSS_FULL_OLD = ".mobile-menu ul li a:hover { background: var(--washi-dark); }"

CSS_FULL_NEW = """.mobile-menu ul li a:hover { background: var(--washi-dark); }
.mobile-menu ul li a.mobile-sub {
  padding-left: 44px;
  font-size: 15px;
  letter-spacing: 0.5px;
  text-transform: none;
  color: var(--enshu);
}

/* ── CULTURE DROPDOWN (PC nav) ── */
.nav-dropdown { position: relative; }
.nav-dropdown > a .nav-caret {
  display: inline-block;
  margin-left: 4px;
  font-size: 9px;
  opacity: 0.6;
  transform: translateY(-1px);
  transition: transform 0.2s;
}
.nav-dropdown:hover > a .nav-caret,
.nav-dropdown:focus-within > a .nav-caret { transform: translateY(-1px) rotate(180deg); }
.nav-dropdown-menu {
  display: none;
  position: absolute;
  top: 100%;
  left: 50%;
  transform: translateX(-50%);
  min-width: 210px;
  background: rgba(245,240,232,0.98);
  backdrop-filter: blur(10px);
  border: 1px solid var(--border-strong);
  border-radius: 2px;
  box-shadow: 0 4px 14px rgba(0,0,0,0.08);
  padding: 8px 0;
  margin-top: 8px;
  z-index: 100;
}
.nav-dropdown:hover .nav-dropdown-menu,
.nav-dropdown:focus-within .nav-dropdown-menu { display: block; }
.nav-dropdown-menu a {
  display: block;
  padding: 9px 20px;
  font-family: 'EB Garamond', serif;
  font-size: 13px;
  letter-spacing: 1px;
  color: var(--enshu);
  text-transform: uppercase;
  text-decoration: none;
  white-space: nowrap;
  transition: background 0.15s, color 0.15s;
}
.nav-dropdown-menu a:hover { background: var(--washi-dark); color: var(--sumi); }
.nav-dropdown-sep { height: 1px; background: var(--border); margin: 6px 16px; }"""

# Simple-page CSS: anchor on the .nav-links a:hover line, append dropdown styles after it.
CSS_SIMPLE_OLD = ".nav-links a:hover { color: var(--beni); }"
CSS_SIMPLE_NEW = """.nav-links a:hover { color: var(--beni); }
.nav-dropdown { position: relative; }
.nav-dropdown > a .nav-caret { display: inline-block; margin-left: 4px; font-size: 9px; opacity: 0.6; transition: transform 0.2s; }
.nav-dropdown:hover > a .nav-caret, .nav-dropdown:focus-within > a .nav-caret { transform: rotate(180deg); }
.nav-dropdown-menu {
  display: none; position: absolute; top: 100%; left: 50%; transform: translateX(-50%);
  min-width: 210px; background: rgba(253,240,243,0.98); backdrop-filter: blur(10px);
  border: 1px solid var(--border-strong); border-radius: 2px;
  box-shadow: 0 4px 14px rgba(0,0,0,0.08); padding: 8px 0; margin-top: 8px; z-index: 100;
}
.nav-dropdown:hover .nav-dropdown-menu, .nav-dropdown:focus-within .nav-dropdown-menu { display: block; }
.nav-dropdown-menu a {
  display: block; padding: 9px 20px; font-family: 'EB Garamond', serif;
  font-size: 13px; letter-spacing: 1px; color: var(--sumi-light);
  text-transform: uppercase; text-decoration: none; white-space: nowrap;
  transition: background 0.15s, color 0.15s;
}
.nav-dropdown-menu a:hover { background: var(--washi-dark); color: var(--beni); }
.nav-dropdown-sep { height: 1px; background: var(--border); margin: 6px 16px; }"""

# ---- PC nav Culture <li> replacement ----
# Two variants depending on whether the page has class="current" on Culture
PC_NAV_OLD_PLAIN = '    <li><a href="/culture/">Culture</a></li>'
PC_NAV_OLD_CURRENT = '    <li><a href="/culture/" class="current">Culture</a></li>'

def pc_nav_new(is_current: bool) -> str:
    current_class = ' class="current"' if is_current else ''
    return f'''    <li class="nav-dropdown">
      <a href="/culture/"{current_class}>Culture<span class="nav-caret" aria-hidden="true">▾</span></a>
      <div class="nav-dropdown-menu" role="menu">
        <a href="/castles/" onclick="trackEvent('click','internal','nav_culture_to_castles')">Castles</a>
        <a href="/crafts/" onclick="trackEvent('click','internal','nav_culture_to_crafts')">Crafts</a>
        <a href="/anime/" onclick="trackEvent('click','internal','nav_culture_to_anime')">Anime Pilgrimage</a>
        <a href="/regional-food/" onclick="trackEvent('click','internal','nav_culture_to_food')">Regional Food</a>
        <div class="nav-dropdown-sep"></div>
        <a href="/culture/" onclick="trackEvent('click','internal','nav_culture_to_hub')">Culture Hub →</a>
      </div>
    </li>'''

# ---- Mobile menu Culture <li> replacement (main pages only) ----
MOBILE_OLD = '    <li><a href="/culture/">Culture</a></li>\n    <li><a href="/about/">About</a></li>'
MOBILE_NEW = '''    <li><a href="/culture/">Culture</a></li>
    <li><a href="/castles/" class="mobile-sub" onclick="trackEvent('click','internal','nav_culture_to_castles')">— Castles</a></li>
    <li><a href="/crafts/" class="mobile-sub" onclick="trackEvent('click','internal','nav_culture_to_crafts')">— Crafts</a></li>
    <li><a href="/anime/" class="mobile-sub" onclick="trackEvent('click','internal','nav_culture_to_anime')">— Anime Pilgrimage</a></li>
    <li><a href="/regional-food/" class="mobile-sub" onclick="trackEvent('click','internal','nav_culture_to_food')">— Regional Food</a></li>
    <li><a href="/culture/" class="mobile-sub" onclick="trackEvent('click','internal','nav_culture_to_hub')">— Culture Hub →</a></li>
    <li><a href="/about/">About</a></li>'''


def process_main(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    report = {"file": str(path.relative_to(ROOT)), "css": False, "pc_nav": False, "mobile": False}

    # Idempotency check: skip if already processed
    if "nav-dropdown-menu" in text:
        report["status"] = "already processed"
        return report

    # CSS injection
    if CSS_FULL_OLD in text:
        text = text.replace(CSS_FULL_OLD, CSS_FULL_NEW, 1)
        report["css"] = True
    else:
        report["status"] = "CSS anchor not found"
        return report

    # PC nav: handle both variants. The PC nav appears FIRST, mobile menu SECOND.
    # Distinguish by occurrence order: replace the FIRST match (PC nav).
    if PC_NAV_OLD_CURRENT in text:
        text = text.replace(PC_NAV_OLD_CURRENT, pc_nav_new(True), 1)
        report["pc_nav"] = "current"
    elif PC_NAV_OLD_PLAIN in text:
        # First occurrence is PC nav (no class="current"). Replace just first occurrence.
        text = text.replace(PC_NAV_OLD_PLAIN, pc_nav_new(False), 1)
        report["pc_nav"] = "plain"
    else:
        report["status"] = "PC nav anchor not found"
        return report

    # Mobile menu (anchor includes the following About line so we hit only the mobile-menu block)
    if MOBILE_OLD in text:
        text = text.replace(MOBILE_OLD, MOBILE_NEW, 1)
        report["mobile"] = True
    else:
        report["status"] = "mobile anchor not found"
        return report

    path.write_text(text, encoding="utf-8")
    report["status"] = "ok"
    return report


def process_simple(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    report = {"file": str(path.relative_to(ROOT)), "css": False, "pc_nav": False}

    if "nav-dropdown-menu" in text:
        report["status"] = "already processed"
        return report

    if CSS_SIMPLE_OLD in text:
        text = text.replace(CSS_SIMPLE_OLD, CSS_SIMPLE_NEW, 1)
        report["css"] = True
    else:
        report["status"] = "CSS anchor not found"
        return report

    if PC_NAV_OLD_PLAIN in text:
        text = text.replace(PC_NAV_OLD_PLAIN, pc_nav_new(False), 1)
        report["pc_nav"] = "plain"
    else:
        report["status"] = "PC nav anchor not found"
        return report

    path.write_text(text, encoding="utf-8")
    report["status"] = "ok"
    return report


def main():
    failures = []
    for rel in MAIN_PAGES:
        r = process_main(ROOT / rel)
        flag = "OK" if r["status"] == "ok" else ("SKIP" if r["status"] == "already processed" else "FAIL")
        print(f"  [{flag}] {r['file']}  css={r['css']} pc_nav={r['pc_nav']} mobile={r['mobile']}  ({r['status']})")
        if flag == "FAIL":
            failures.append(r)

    for rel in SIMPLE_PAGES:
        r = process_simple(ROOT / rel)
        flag = "OK" if r["status"] == "ok" else ("SKIP" if r["status"] == "already processed" else "FAIL")
        print(f"  [{flag}] {r['file']}  css={r['css']} pc_nav={r['pc_nav']}  ({r['status']})")
        if flag == "FAIL":
            failures.append(r)

    if failures:
        print(f"\nFAILED: {len(failures)}")
        sys.exit(1)
    print("\nAll done.")


if __name__ == "__main__":
    main()
