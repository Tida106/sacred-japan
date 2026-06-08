"""Audit the Izumo Taisha addition across the site."""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent.parent

def head(s, n=92):
    return s if len(s) <= n else s[:n-1] + "…"

# 1. New article integrity
p = ROOT / "guides/izumo-taisha/index.html"
text = p.read_text(encoding="utf-8")
print("=" * 78)
print("1. NEW ARTICLE: guides/izumo-taisha/index.html")
print("=" * 78)
checks = [
    ("doctype",                        "<!DOCTYPE html>" in text),
    ("title",                          "<title>Izumo Taisha:" in text and "| Sacred Japan</title>" in text),
    ("canonical",                      'rel="canonical" href="https://sacred-japan.net/guides/izumo-taisha/"' in text),
    ("JSON-LD Article",                '"@type": "Article"' in text),
    ("JSON-LD BreadcrumbList",         '"@type": "BreadcrumbList"' in text),
    ("JSON-LD FAQPage",                '"@type": "FAQPage"' in text),
    ("no Event/Festival JSON-LD",      '"Event"' not in text and '"Festival"' not in text),
    ("FAQ 6 questions",                text.count('"@type": "Question"') == 6),
    ("FAQ 6 answers",                  text.count('"@type":"Answer"') == 6),
    ("breadcrumb Home > Guides > Izumo", "Izumo Taisha" in text and "Home" in text and "Guides" in text),
    ("hero kanji 出雲大社",              "出雲大社" in text),
    ("CULTURE dropdown nav",           'class="nav-dropdown"' in text),
    ("mobile menu sub items (5)",      text.count('class="mobile-sub"') == 5),
    ("inline link to ise",             '/guides/ise-grand-shrine/' in text),
    ("inline link to shrine-vs-temple", '/guides/shrine-vs-temple/' in text),
    ("inline link to goshuin",         '/guides/goshuin-guide/' in text),
    ("inline link to omamori",         '/guides/omamori-guide/' in text),
    ("Related Guides (ise+atsuta)",    'related_izumo_to_ise' in text and 'related_izumo_to_atsuta' in text),
    ("trackEvent labels prefix",       text.count("guide_izumo_to_") >= 5),
    ("div balance",                    len(re.findall(r"<div\b", text)) == text.count("</div>")),
    ("section balance",                len(re.findall(r"<section\b", text)) == text.count("</section>")),
    ("ld+json blocks closed",          text.count('<script type="application/ld+json">') == text.count("</script>") - text.count("<script async") - text.count("<script>")),
]
for name, ok in checks:
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}")

# 2. Homepage grid update
p2 = ROOT / "index.html"
t2 = p2.read_text(encoding="utf-8")
print()
print("=" * 78)
print("2. HOMEPAGE: index.html")
print("=" * 78)
checks2 = [
    ("Guides grid has izumo card",     "home_to_guide_izumo" in t2 and "GUIDE 10 ／ 出雲大社" in t2),
    ("Guides grid izumo accent #6b4a5e", "border-top:3px solid #6b4a5e" in t2),
    ("Footer Sacred Places has izumo", '<li><a href="/guides/izumo-taisha/">Izumo Taisha</a></li>' in t2),
]
for name, ok in checks2:
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}")

# 3. Guides hub
p3 = ROOT / "guides/index.html"
t3 = p3.read_text(encoding="utf-8")
print()
print("=" * 78)
print("3. GUIDES HUB: guides/index.html")
print("=" * 78)
checks3 = [
    ("Sacred Places hub-card izumo",   "guides_hub_to_izumo" in t3),
    ("CollectionPage izumo position 6", '"position":6,"url":"https://sacred-japan.net/guides/izumo-taisha/"' in t3),
    ("CollectionPage 10 items",        t3.count('"@type":"ListItem"') >= 10),
    ("Footer flat list has izumo",     '<li><a href="/guides/izumo-taisha/">Izumo Taisha</a></li>' in t3),
]
for name, ok in checks3:
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}")

# 4. Cross-links from ise and atsuta
for sub in ("ise-grand-shrine", "atsuta-shrine"):
    p4 = ROOT / f"guides/{sub}/index.html"
    t4 = p4.read_text(encoding="utf-8")
    print()
    print("=" * 78)
    print(f"4. CROSS-LINK: guides/{sub}/index.html")
    print("=" * 78)
    label = "ise" if sub == "ise-grand-shrine" else "atsuta"
    checks4 = [
        ("Related card to izumo",      f"related_{label}_to_izumo" in t4),
        ("Footer has izumo",           '<li><a href="/guides/izumo-taisha/">Izumo Taisha</a></li>' in t4),
    ]
    for name, ok in checks4:
        print(f"  [{'PASS' if ok else 'FAIL'}] {name}")

# 5. Culture hub footer
p5 = ROOT / "culture/index.html"
t5 = p5.read_text(encoding="utf-8")
print()
print("=" * 78)
print("5. CULTURE HUB: culture/index.html")
print("=" * 78)
print(f"  [{'PASS' if '<li><a href=\"/guides/izumo-taisha/\">Izumo Taisha</a></li>' in t5 else 'FAIL'}] Footer has izumo")

# 6. Sitemap
p6 = ROOT / "sitemap.xml"
t6 = p6.read_text(encoding="utf-8")
print()
print("=" * 78)
print("6. SITEMAP: sitemap.xml")
print("=" * 78)
checks6 = [
    ("Has izumo URL entry",            "https://sacred-japan.net/guides/izumo-taisha/" in t6),
    ("URL+lastmod 2026-06-08",         "/guides/izumo-taisha/</loc>\n    <lastmod>2026-06-08" in t6),
]
for name, ok in checks6:
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}")
