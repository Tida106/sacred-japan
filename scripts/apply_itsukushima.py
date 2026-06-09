"""Surface the new Itsukushima Shrine guide across the site.

Inserts itsukushima immediately after kasuga-taisha in every Sacred Places
surface. Idempotent.
"""
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent.parent

# 1. Homepage Guides grid (Sacred Places group)
HOME_GRID_OLD = '''        <a href="/guides/kasuga-taisha/" onclick="trackEvent('click','internal','home_to_guide_kasuga')" style="display:block;padding:20px 24px;background:var(--washi);border:1px solid var(--border-strong);border-top:3px solid #a8612a;text-decoration:none;border-radius:2px;transition:background 0.2s,transform 0.15s;">
          <div style="font-family:'Noto Serif JP',serif;font-size:10px;letter-spacing:2px;color:#a8612a;margin-bottom:4px;">GUIDE 11 ／ 春日大社</div>
          <div style="font-family:'Shippori Mincho',serif;font-size:17px;color:var(--sumi);margin-bottom:6px;">⛩️ Kasuga Taisha: Nara's Shrine of 3,000 Lanterns &amp; Sacred Deer →</div>
          <div style="font-size:13px;color:var(--enshu);line-height:1.6;">Nara's UNESCO World Heritage shrine — 3,000 stone and bronze lanterns, the sacred Nara deer, the Fujiwara clan, and the Mantōrō festivals.</div>
        </a>
      </div>'''

HOME_GRID_NEW = '''        <a href="/guides/kasuga-taisha/" onclick="trackEvent('click','internal','home_to_guide_kasuga')" style="display:block;padding:20px 24px;background:var(--washi);border:1px solid var(--border-strong);border-top:3px solid #a8612a;text-decoration:none;border-radius:2px;transition:background 0.2s,transform 0.15s;">
          <div style="font-family:'Noto Serif JP',serif;font-size:10px;letter-spacing:2px;color:#a8612a;margin-bottom:4px;">GUIDE 11 ／ 春日大社</div>
          <div style="font-family:'Shippori Mincho',serif;font-size:17px;color:var(--sumi);margin-bottom:6px;">⛩️ Kasuga Taisha: Nara's Shrine of 3,000 Lanterns &amp; Sacred Deer →</div>
          <div style="font-size:13px;color:var(--enshu);line-height:1.6;">Nara's UNESCO World Heritage shrine — 3,000 stone and bronze lanterns, the sacred Nara deer, the Fujiwara clan, and the Mantōrō festivals.</div>
        </a>
        <a href="/guides/itsukushima-shrine/" onclick="trackEvent('click','internal','home_to_guide_itsukushima')" style="display:block;padding:20px 24px;background:var(--washi);border:1px solid var(--border-strong);border-top:3px solid #2a6b8c;text-decoration:none;border-radius:2px;transition:background 0.2s,transform 0.15s;">
          <div style="font-family:'Noto Serif JP',serif;font-size:10px;letter-spacing:2px;color:#2a6b8c;margin-bottom:4px;">GUIDE 12 ／ 厳島神社</div>
          <div style="font-family:'Shippori Mincho',serif;font-size:17px;color:var(--sumi);margin-bottom:6px;">⛩️ Itsukushima Shrine: The Floating Torii Gate of Miyajima →</div>
          <div style="font-size:13px;color:var(--enshu);line-height:1.6;">Japan's iconic floating torii — UNESCO World Heritage Site, the sacred reason it sits in the sea, Taira no Kiyomori's Heian masterpiece, and high tide vs. low tide planning.</div>
        </a>
      </div>'''

# 2. Homepage footer Sacred Places sublist
HOME_FOOTER_OLD = '''    <li><a href="/guides/izumo-taisha/">Izumo Taisha</a></li>
    <li><a href="/guides/kasuga-taisha/">Kasuga Taisha</a></li>
    <li style="flex-basis:100%;padding-top:8px;font-family:'Noto Serif JP',serif;font-size:10px;letter-spacing:3px;color:var(--beni);text-transform:uppercase;">Know Before You Go ／ 参拝の作法</li>'''
HOME_FOOTER_NEW = '''    <li><a href="/guides/izumo-taisha/">Izumo Taisha</a></li>
    <li><a href="/guides/kasuga-taisha/">Kasuga Taisha</a></li>
    <li><a href="/guides/itsukushima-shrine/">Itsukushima Shrine</a></li>
    <li style="flex-basis:100%;padding-top:8px;font-family:'Noto Serif JP',serif;font-size:10px;letter-spacing:3px;color:var(--beni);text-transform:uppercase;">Know Before You Go ／ 参拝の作法</li>'''

# 3. /guides/ hub hub-card
HUB_CARD_OLD = '''    <a class="hub-card" href="/guides/kasuga-taisha/" onclick="trackEvent('click','internal','guides_hub_to_kasuga')" style="border-top:3px solid #a8612a;">
      <div class="hub-card-label" style="color:#a8612a;">GUIDE 11 ／ 春日大社</div>
      <div class="hub-card-title">⛩️ Kasuga Taisha: Nara's Shrine of 3,000 Lanterns &amp; Sacred Deer →</div>
      <div class="hub-card-desc">Nara's UNESCO World Heritage shrine — 3,000 stone and bronze lanterns, the sacred Nara deer, the Fujiwara clan, and the Mantōrō festivals.</div>
    </a>

  </div>'''
HUB_CARD_NEW = '''    <a class="hub-card" href="/guides/kasuga-taisha/" onclick="trackEvent('click','internal','guides_hub_to_kasuga')" style="border-top:3px solid #a8612a;">
      <div class="hub-card-label" style="color:#a8612a;">GUIDE 11 ／ 春日大社</div>
      <div class="hub-card-title">⛩️ Kasuga Taisha: Nara's Shrine of 3,000 Lanterns &amp; Sacred Deer →</div>
      <div class="hub-card-desc">Nara's UNESCO World Heritage shrine — 3,000 stone and bronze lanterns, the sacred Nara deer, the Fujiwara clan, and the Mantōrō festivals.</div>
    </a>

    <a class="hub-card" href="/guides/itsukushima-shrine/" onclick="trackEvent('click','internal','guides_hub_to_itsukushima')" style="border-top:3px solid #2a6b8c;">
      <div class="hub-card-label" style="color:#2a6b8c;">GUIDE 12 ／ 厳島神社</div>
      <div class="hub-card-title">⛩️ Itsukushima Shrine: The Floating Torii Gate of Miyajima →</div>
      <div class="hub-card-desc">Japan's iconic floating torii — UNESCO World Heritage Site, the sacred reason it sits in the sea, Taira no Kiyomori's Heian masterpiece, and high tide vs. low tide planning.</div>
    </a>

  </div>'''

# 4. /guides/ hub CollectionPage JSON-LD
HUB_JSONLD_OLD = '''      {"@type":"ListItem","position":7,"url":"https://sacred-japan.net/guides/kasuga-taisha/","name":"Kasuga Taisha: Nara's Shrine of 3,000 Lanterns and Sacred Deer"},
      {"@type":"ListItem","position":8,"url":"https://sacred-japan.net/guides/shrine-vs-temple/","name":"Shrine vs Temple in Japan"},
      {"@type":"ListItem","position":9,"url":"https://sacred-japan.net/guides/goshuin-guide/","name":"The Complete Goshuin Guide"},
      {"@type":"ListItem","position":10,"url":"https://sacred-japan.net/guides/omamori-guide/","name":"The Complete Omamori Guide"},
      {"@type":"ListItem","position":11,"url":"https://sacred-japan.net/guides/why-did-you-come-to-japan/","name":"Japanese TV Shows That Make You Want to Visit Japan"}
    ]'''
HUB_JSONLD_NEW = '''      {"@type":"ListItem","position":7,"url":"https://sacred-japan.net/guides/kasuga-taisha/","name":"Kasuga Taisha: Nara's Shrine of 3,000 Lanterns and Sacred Deer"},
      {"@type":"ListItem","position":8,"url":"https://sacred-japan.net/guides/itsukushima-shrine/","name":"Itsukushima Shrine: The Floating Torii Gate of Miyajima"},
      {"@type":"ListItem","position":9,"url":"https://sacred-japan.net/guides/shrine-vs-temple/","name":"Shrine vs Temple in Japan"},
      {"@type":"ListItem","position":10,"url":"https://sacred-japan.net/guides/goshuin-guide/","name":"The Complete Goshuin Guide"},
      {"@type":"ListItem","position":11,"url":"https://sacred-japan.net/guides/omamori-guide/","name":"The Complete Omamori Guide"},
      {"@type":"ListItem","position":12,"url":"https://sacred-japan.net/guides/why-did-you-come-to-japan/","name":"Japanese TV Shows That Make You Want to Visit Japan"}
    ]'''

# 5. Flat-list footer (guides/, culture/, ise/, atsuta/)
FLAT_FOOTER_OLD = '''    <li><a href="/guides/kasuga-taisha/">Kasuga Taisha</a></li>
    <li><a href="/#tips">Travel Tips</a></li>'''
FLAT_FOOTER_NEW = '''    <li><a href="/guides/kasuga-taisha/">Kasuga Taisha</a></li>
    <li><a href="/guides/itsukushima-shrine/">Itsukushima Shrine</a></li>
    <li><a href="/#tips">Travel Tips</a></li>'''

# 6. Mobile menu Sacred Places insertion (anchor: kasuga line + Culture line)
MOBILE_OLD = '''    <li><a href="/guides/kasuga-taisha/" class="mobile-sub" onclick="trackEvent('click','internal','nav_mobile_to_kasuga')">— Kasuga Taisha</a></li>
    <li><a href="/culture/">Culture</a></li>'''
MOBILE_NEW = '''    <li><a href="/guides/kasuga-taisha/" class="mobile-sub" onclick="trackEvent('click','internal','nav_mobile_to_kasuga')">— Kasuga Taisha</a></li>
    <li><a href="/guides/itsukushima-shrine/" class="mobile-sub" onclick="trackEvent('click','internal','nav_mobile_to_itsukushima')">— Itsukushima Shrine</a></li>
    <li><a href="/culture/">Culture</a></li>'''


def patch(p, replacements):
    text = p.read_text(encoding="utf-8")
    results = {}
    for label, old, new in replacements:
        if old in text:
            text = text.replace(old, new, 1)
            results[label] = "ok"
        else:
            results[label] = "ANCHOR-NOT-FOUND"
    p.write_text(text, encoding="utf-8")
    return results


PAGE_PATCHES = {
    "index.html": [
        ("home guides grid",  HOME_GRID_OLD,  HOME_GRID_NEW),
        ("home footer SP",    HOME_FOOTER_OLD, HOME_FOOTER_NEW),
        ("home mobile menu",  MOBILE_OLD,     MOBILE_NEW),
    ],
    "guides/index.html": [
        ("hub-card",          HUB_CARD_OLD,   HUB_CARD_NEW),
        ("hub JSON-LD",       HUB_JSONLD_OLD, HUB_JSONLD_NEW),
        ("hub flat footer",   FLAT_FOOTER_OLD, FLAT_FOOTER_NEW),
        ("hub mobile menu",   MOBILE_OLD,     MOBILE_NEW),
    ],
    "culture/index.html": [
        ("flat footer",       FLAT_FOOTER_OLD, FLAT_FOOTER_NEW),
        ("mobile menu",       MOBILE_OLD,     MOBILE_NEW),
    ],
    "guides/ise-grand-shrine/index.html": [
        ("flat footer",       FLAT_FOOTER_OLD, FLAT_FOOTER_NEW),
        ("mobile menu",       MOBILE_OLD,     MOBILE_NEW),
    ],
    "guides/atsuta-shrine/index.html": [
        ("flat footer",       FLAT_FOOTER_OLD, FLAT_FOOTER_NEW),
        ("mobile menu",       MOBILE_OLD,     MOBILE_NEW),
    ],
}

# Mobile-only pages
MOBILE_ONLY = [
    "guides/izumo-taisha/index.html",
    "guides/kasuga-taisha/index.html",
    "guides/three-sacred-treasures/index.html",
    "guides/best-time-fushimi-inari/index.html",
    "guides/koyasan-temple-stay/index.html",
    "guides/shrine-vs-temple/index.html",
    "guides/goshuin-guide/index.html",
    "guides/omamori-guide/index.html",
    "guides/why-did-you-come-to-japan/index.html",
    "castles/index.html",
    "crafts/index.html",
    "anime/index.html",
    "regional-food/index.html",
    "about/index.html",
]
for rel in MOBILE_ONLY:
    PAGE_PATCHES[rel] = [("mobile menu", MOBILE_OLD, MOBILE_NEW)]


def main():
    fails = 0
    for rel, patches in PAGE_PATCHES.items():
        p = ROOT / rel
        if not p.exists():
            print(f"  [MISS] {rel}")
            fails += 1
            continue
        text = p.read_text(encoding="utf-8")
        if "nav_mobile_to_itsukushima" in text and "home_to_guide_itsukushima" in text:
            print(f"  [SKIP] {rel} (already processed)")
            continue
        if len(patches) == 1 and "nav_mobile_to_itsukushima" in text:
            print(f"  [SKIP] {rel} (mobile already processed)")
            continue
        results = patch(p, patches)
        statuses = ", ".join(f"{k}={v}" for k, v in results.items())
        any_fail = any(v.startswith("ANCHOR") for v in results.values())
        flag = "OK" if not any_fail else "FAIL"
        if any_fail:
            fails += 1
        print(f"  [{flag}] {rel}  ({statuses})")

    print()
    if fails:
        print(f"FAILED: {fails}")
        sys.exit(1)
    print("All done.")


if __name__ == "__main__":
    main()
