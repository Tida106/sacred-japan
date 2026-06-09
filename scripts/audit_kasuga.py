"""Audit the Kasuga Taisha addition across the site."""
from pathlib import Path
import re, json

ROOT = Path(__file__).resolve().parent.parent

def section(label):
    print("=" * 78)
    print(label)
    print("=" * 78)

# 1. New article integrity
p = ROOT / "guides/kasuga-taisha/index.html"
text = p.read_text(encoding="utf-8")
section("1. NEW ARTICLE: guides/kasuga-taisha/index.html")
checks = [
    ("doctype",                          "<!DOCTYPE html>" in text),
    ("title",                            "<title>Kasuga Taisha: Nara's Shrine of 3,000 Lanterns and Sacred Deer | Sacred Japan</title>" in text),
    ("canonical",                        'rel="canonical" href="https://sacred-japan.net/guides/kasuga-taisha/"' in text),
    ("hero kanji 春日大社",                "春日大社" in text),
    ("breadcrumb Home > Guides > Kasuga", "Kasuga Taisha" in text and "Home" in text and "Guides" in text),
    ("JSON-LD Article",                  '"@type": "Article"' in text),
    ("JSON-LD BreadcrumbList",           '"@type": "BreadcrumbList"' in text),
    ("JSON-LD FAQPage",                  '"@type": "FAQPage"' in text),
    ("no Event/Festival JSON-LD",        '"Event"' not in text and '"Festival"' not in text),
    ("FAQ 6 questions",                  text.count('"@type": "Question"') == 6),
    ("FAQ 6 answers",                    text.count('"@type":"Answer"') == 6),
    ("CULTURE dropdown nav",             'class="nav-dropdown"' in text),
    ("mobile menu sub items (>=6)",      text.count('class="mobile-sub"') >= 6),
    ("kasuga mobile-sub itself",         'nav_mobile_to_kasuga' in text),
    ("inline link to shrine-vs-temple",  '/guides/shrine-vs-temple/' in text),
    ("inline link to goshuin",           '/guides/goshuin-guide/' in text),
    ("Related Guides ise + izumo",       'related_kasuga_to_ise' in text and 'related_kasuga_to_izumo' in text),
    ("trackEvent labels (>=5 unique)",   len(set(re.findall(r"guide_kasuga_to_\w+", text))) >= 5),
    ("--kasuga CSS var defined",         '--kasuga: #a8612a' in text),
    ("div balance",                      len(re.findall(r"<div\b", text)) == text.count("</div>")),
    ("section balance",                  len(re.findall(r"<section\b", text)) == text.count("</section>")),
]
for name, ok in checks:
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}")

# JSON-LD parse
blocks = re.findall(r'<script type="application/ld\+json">\s*(.*?)\s*</script>', text, re.DOTALL)
print(f"\n  JSON-LD parse: {len(blocks)} blocks")
for i, b in enumerate(blocks):
    try:
        d = json.loads(b)
        t_ = d.get('@type', '?')
        extra = ""
        if t_ == "FAQPage":
            extra = f" ({len(d['mainEntity'])} Q&A)"
        elif t_ == "BreadcrumbList":
            extra = f" ({len(d['itemListElement'])} items)"
        print(f"    [{i+1}] {t_}{extra} - parsed OK")
    except Exception as e:
        print(f"    [{i+1}] PARSE ERROR: {e}")

# 2. Surfaces
SURFACES = [
    ("index.html (home Guides grid + footer SP + mobile)",      "index.html",
     ['home_to_guide_kasuga', 'GUIDE 11 ／ 春日大社', '#a8612a',
      '<li><a href="/guides/kasuga-taisha/">Kasuga Taisha</a></li>',
      'nav_mobile_to_kasuga']),
    ("guides/index.html (hub-card + JSON-LD + footer + mobile)", "guides/index.html",
     ['guides_hub_to_kasuga', 'GUIDE 11 ／ 春日大社',
      '"position":7,"url":"https://sacred-japan.net/guides/kasuga-taisha/"',
      '<li><a href="/guides/kasuga-taisha/">Kasuga Taisha</a></li>',
      'nav_mobile_to_kasuga']),
    ("culture/index.html (footer + mobile)",                     "culture/index.html",
     ['<li><a href="/guides/kasuga-taisha/">Kasuga Taisha</a></li>',
      'nav_mobile_to_kasuga']),
    ("guides/ise-grand-shrine/ (footer + mobile)",               "guides/ise-grand-shrine/index.html",
     ['<li><a href="/guides/kasuga-taisha/">Kasuga Taisha</a></li>',
      'nav_mobile_to_kasuga']),
    ("guides/atsuta-shrine/ (footer + mobile)",                  "guides/atsuta-shrine/index.html",
     ['<li><a href="/guides/kasuga-taisha/">Kasuga Taisha</a></li>',
      'nav_mobile_to_kasuga']),
]
print()
section("2. SURFACE PLACEMENTS")
for label, rel, expected in SURFACES:
    p2 = ROOT / rel
    t2 = p2.read_text(encoding="utf-8")
    print(f"\n  {label}")
    for e in expected:
        print(f"    [{'PASS' if e in t2 else 'FAIL'}] {e[:80]}")

# 3. All mobile-menu pages have kasuga
print()
section("3. MOBILE MENU: kasuga in all 19 pages")
MOBILE_PAGES = [
    "index.html", "guides/index.html", "guides/kasuga-taisha/index.html",
    "guides/izumo-taisha/index.html", "guides/ise-grand-shrine/index.html",
    "guides/atsuta-shrine/index.html", "guides/three-sacred-treasures/index.html",
    "guides/best-time-fushimi-inari/index.html", "guides/koyasan-temple-stay/index.html",
    "guides/shrine-vs-temple/index.html", "guides/goshuin-guide/index.html",
    "guides/omamori-guide/index.html", "guides/why-did-you-come-to-japan/index.html",
    "culture/index.html", "castles/index.html", "crafts/index.html",
    "anime/index.html", "regional-food/index.html", "about/index.html",
]
all_ok = True
for rel in MOBILE_PAGES:
    t = (ROOT / rel).read_text(encoding="utf-8")
    has_kasuga = 'nav_mobile_to_kasuga' in t and 'class="mobile-sub" onclick="trackEvent(\'click\',\'internal\',\'nav_mobile_to_kasuga\')">— Kasuga Taisha' in t
    if not has_kasuga:
        all_ok = False
    print(f"  [{'PASS' if has_kasuga else 'FAIL'}] {rel}")

# 4. Sitemap
print()
section("4. SITEMAP")
t = (ROOT / "sitemap.xml").read_text(encoding="utf-8")
print(f"  [{'PASS' if '/guides/kasuga-taisha/' in t else 'FAIL'}] kasuga URL entry present")
print(f"  [{'PASS' if 'guides/kasuga-taisha/</loc>\\n    <lastmod>2026-06-09' in t else 'FAIL'}] lastmod 2026-06-09")
