"""Surface the new Kasuga Taisha guide across the site.

Inserts kasuga immediately after izumo-taisha in every surface that lists
the Sacred Places shrines:

- index.html: Guides grid Sacred Places group + footer Sacred Places sublist
- guides/index.html: hub-card grid + CollectionPage JSON-LD + footer
- culture/index.html: footer
- guides/ise-grand-shrine/, guides/atsuta-shrine/: footer
- All 17 other pages with a mobile-menu block: insert kasuga mobile-sub
  immediately after izumo in the Sacred Places group

Idempotent — re-running is safe.
"""
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent.parent

# ──────────────────────────────────────────────────────────────────────────
# 1. Homepage Guides grid (Sacred Places group)
HOME_GRID_OLD = '''        <a href="/guides/izumo-taisha/" onclick="trackEvent('click','internal','home_to_guide_izumo')" style="display:block;padding:20px 24px;background:var(--washi);border:1px solid var(--border-strong);border-top:3px solid #6b4a5e;text-decoration:none;border-radius:2px;transition:background 0.2s,transform 0.15s;">
          <div style="font-family:'Noto Serif JP',serif;font-size:10px;letter-spacing:2px;color:#6b4a5e;margin-bottom:4px;">GUIDE 10 ／ 出雲大社</div>
          <div style="font-family:'Shippori Mincho',serif;font-size:17px;color:var(--sumi);margin-bottom:6px;">⛩️ Izumo Taisha: The Shrine of Marriage &amp; the Gathering of the Gods →</div>
          <div style="font-size:13px;color:var(--enshu);line-height:1.6;">Japan's shrine of <em>enmusubi</em> (bonds) — Okuninushi, the annual gathering of all 8 million gods, the 2-bow-4-clap etiquette, and the colossal shimenawa.</div>
        </a>
      </div>'''

HOME_GRID_NEW = '''        <a href="/guides/izumo-taisha/" onclick="trackEvent('click','internal','home_to_guide_izumo')" style="display:block;padding:20px 24px;background:var(--washi);border:1px solid var(--border-strong);border-top:3px solid #6b4a5e;text-decoration:none;border-radius:2px;transition:background 0.2s,transform 0.15s;">
          <div style="font-family:'Noto Serif JP',serif;font-size:10px;letter-spacing:2px;color:#6b4a5e;margin-bottom:4px;">GUIDE 10 ／ 出雲大社</div>
          <div style="font-family:'Shippori Mincho',serif;font-size:17px;color:var(--sumi);margin-bottom:6px;">⛩️ Izumo Taisha: The Shrine of Marriage &amp; the Gathering of the Gods →</div>
          <div style="font-size:13px;color:var(--enshu);line-height:1.6;">Japan's shrine of <em>enmusubi</em> (bonds) — Okuninushi, the annual gathering of all 8 million gods, the 2-bow-4-clap etiquette, and the colossal shimenawa.</div>
        </a>
        <a href="/guides/kasuga-taisha/" onclick="trackEvent('click','internal','home_to_guide_kasuga')" style="display:block;padding:20px 24px;background:var(--washi);border:1px solid var(--border-strong);border-top:3px solid #a8612a;text-decoration:none;border-radius:2px;transition:background 0.2s,transform 0.15s;">
          <div style="font-family:'Noto Serif JP',serif;font-size:10px;letter-spacing:2px;color:#a8612a;margin-bottom:4px;">GUIDE 11 ／ 春日大社</div>
          <div style="font-family:'Shippori Mincho',serif;font-size:17px;color:var(--sumi);margin-bottom:6px;">⛩️ Kasuga Taisha: Nara's Shrine of 3,000 Lanterns &amp; Sacred Deer →</div>
          <div style="font-size:13px;color:var(--enshu);line-height:1.6;">Nara's UNESCO World Heritage shrine — 3,000 stone and bronze lanterns, the sacred Nara deer, the Fujiwara clan, and the Mantōrō festivals.</div>
        </a>
      </div>'''

# 2. Homepage footer Sacred Places sublist
HOME_FOOTER_OLD = '''    <li><a href="/guides/koyasan-temple-stay/">Koyasan Temple Stay</a></li>
    <li><a href="/guides/izumo-taisha/">Izumo Taisha</a></li>
    <li style="flex-basis:100%;padding-top:8px;font-family:'Noto Serif JP',serif;font-size:10px;letter-spacing:3px;color:var(--beni);text-transform:uppercase;">Know Before You Go ／ 参拝の作法</li>'''
HOME_FOOTER_NEW = '''    <li><a href="/guides/koyasan-temple-stay/">Koyasan Temple Stay</a></li>
    <li><a href="/guides/izumo-taisha/">Izumo Taisha</a></li>
    <li><a href="/guides/kasuga-taisha/">Kasuga Taisha</a></li>
    <li style="flex-basis:100%;padding-top:8px;font-family:'Noto Serif JP',serif;font-size:10px;letter-spacing:3px;color:var(--beni);text-transform:uppercase;">Know Before You Go ／ 参拝の作法</li>'''

# 3. /guides/ hub hub-card
HUB_CARD_OLD = '''    <a class="hub-card" href="/guides/izumo-taisha/" onclick="trackEvent('click','internal','guides_hub_to_izumo')" style="border-top:3px solid #6b4a5e;">
      <div class="hub-card-label" style="color:#6b4a5e;">GUIDE 10 ／ 出雲大社</div>
      <div class="hub-card-title">⛩️ Izumo Taisha: The Shrine of Marriage &amp; the Gathering of the Gods →</div>
      <div class="hub-card-desc">Japan's shrine of <em>enmusubi</em> (bonds) — Okuninushi, the annual gathering of all 8 million gods, the 2-bow-4-clap etiquette, and the colossal shimenawa.</div>
    </a>

  </div>'''
HUB_CARD_NEW = '''    <a class="hub-card" href="/guides/izumo-taisha/" onclick="trackEvent('click','internal','guides_hub_to_izumo')" style="border-top:3px solid #6b4a5e;">
      <div class="hub-card-label" style="color:#6b4a5e;">GUIDE 10 ／ 出雲大社</div>
      <div class="hub-card-title">⛩️ Izumo Taisha: The Shrine of Marriage &amp; the Gathering of the Gods →</div>
      <div class="hub-card-desc">Japan's shrine of <em>enmusubi</em> (bonds) — Okuninushi, the annual gathering of all 8 million gods, the 2-bow-4-clap etiquette, and the colossal shimenawa.</div>
    </a>

    <a class="hub-card" href="/guides/kasuga-taisha/" onclick="trackEvent('click','internal','guides_hub_to_kasuga')" style="border-top:3px solid #a8612a;">
      <div class="hub-card-label" style="color:#a8612a;">GUIDE 11 ／ 春日大社</div>
      <div class="hub-card-title">⛩️ Kasuga Taisha: Nara's Shrine of 3,000 Lanterns &amp; Sacred Deer →</div>
      <div class="hub-card-desc">Nara's UNESCO World Heritage shrine — 3,000 stone and bronze lanterns, the sacred Nara deer, the Fujiwara clan, and the Mantōrō festivals.</div>
    </a>

  </div>'''

# 4. /guides/ hub CollectionPage JSON-LD
HUB_JSONLD_OLD = '''      {"@type":"ListItem","position":6,"url":"https://sacred-japan.net/guides/izumo-taisha/","name":"Izumo Taisha: Japan's Shrine of Marriage and the Gathering of the Gods"},
      {"@type":"ListItem","position":7,"url":"https://sacred-japan.net/guides/shrine-vs-temple/","name":"Shrine vs Temple in Japan"},
      {"@type":"ListItem","position":8,"url":"https://sacred-japan.net/guides/goshuin-guide/","name":"The Complete Goshuin Guide"},
      {"@type":"ListItem","position":9,"url":"https://sacred-japan.net/guides/omamori-guide/","name":"The Complete Omamori Guide"},
      {"@type":"ListItem","position":10,"url":"https://sacred-japan.net/guides/why-did-you-come-to-japan/","name":"Japanese TV Shows That Make You Want to Visit Japan"}
    ]'''
HUB_JSONLD_NEW = '''      {"@type":"ListItem","position":6,"url":"https://sacred-japan.net/guides/izumo-taisha/","name":"Izumo Taisha: Japan's Shrine of Marriage and the Gathering of the Gods"},
      {"@type":"ListItem","position":7,"url":"https://sacred-japan.net/guides/kasuga-taisha/","name":"Kasuga Taisha: Nara's Shrine of 3,000 Lanterns and Sacred Deer"},
      {"@type":"ListItem","position":8,"url":"https://sacred-japan.net/guides/shrine-vs-temple/","name":"Shrine vs Temple in Japan"},
      {"@type":"ListItem","position":9,"url":"https://sacred-japan.net/guides/goshuin-guide/","name":"The Complete Goshuin Guide"},
      {"@type":"ListItem","position":10,"url":"https://sacred-japan.net/guides/omamori-guide/","name":"The Complete Omamori Guide"},
      {"@type":"ListItem","position":11,"url":"https://sacred-japan.net/guides/why-did-you-come-to-japan/","name":"Japanese TV Shows That Make You Want to Visit Japan"}
    ]'''

# 5. Flat-list footer (guides/index.html, culture/index.html,
#    guides/ise-grand-shrine/index.html, guides/atsuta-shrine/index.html)
FLAT_FOOTER_OLD = '''    <li><a href="/guides/izumo-taisha/">Izumo Taisha</a></li>
    <li><a href="/#tips">Travel Tips</a></li>'''
FLAT_FOOTER_NEW = '''    <li><a href="/guides/izumo-taisha/">Izumo Taisha</a></li>
    <li><a href="/guides/kasuga-taisha/">Kasuga Taisha</a></li>
    <li><a href="/#tips">Travel Tips</a></li>'''

# 6. Mobile menu Sacred Places insertion
MOBILE_OLD = '''    <li><a href="/guides/izumo-taisha/" class="mobile-sub" onclick="trackEvent('click','internal','nav_mobile_to_izumo')">— Izumo Taisha</a></li>
    <li><a href="/culture/">Culture</a></li>'''
MOBILE_NEW = '''    <li><a href="/guides/izumo-taisha/" class="mobile-sub" onclick="trackEvent('click','internal','nav_mobile_to_izumo')">— Izumo Taisha</a></li>
    <li><a href="/guides/kasuga-taisha/" class="mobile-sub" onclick="trackEvent('click','internal','nav_mobile_to_kasuga')">— Kasuga Taisha</a></li>
    <li><a href="/culture/">Culture</a></li>'''


def patch(p: Path, replacements: list[tuple[str, str, str]]) -> dict:
    """Apply (label, old, new) tuples to a file. Returns dict of labels→status."""
    text = p.read_text(encoding="utf-8")
    out = {}
    for label, old, new in replacements:
        if new.split("\n")[0] in text and old in text:
            # Both old anchor and the new line co-exist?
            # Check more carefully — re-run safety.
            if "kasuga" in old.lower():
                # patch was applied last time already
                out[label] = "skip(already)"
                continue
        if old in text:
            text = text.replace(old, new, 1)
            out[label] = "ok"
        else:
            # idempotency check: did this patch already apply?
            new_marker = new.replace(old, "").strip()
            if "kasuga" in text.lower() and "/guides/kasuga-taisha/" in text:
                out[label] = "skip(already)"
            else:
                out[label] = "ANCHOR-NOT-FOUND"
    p.write_text(text, encoding="utf-8")
    return out


# ──────────────────────────────────────────────────────────────────────────
# Page targets
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

# All other pages get only mobile menu update
MOBILE_ONLY_PAGES = [
    "guides/izumo-taisha/index.html",
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
for rel in MOBILE_ONLY_PAGES:
    PAGE_PATCHES[rel] = [("mobile menu", MOBILE_OLD, MOBILE_NEW)]


def main():
    fails = 0
    for rel, patches in PAGE_PATCHES.items():
        p = ROOT / rel
        if not p.exists():
            print(f"  [MISS] {rel} — file does not exist")
            fails += 1
            continue
        text = p.read_text(encoding="utf-8")
        # Idempotency: already processed?
        if "home_to_guide_kasuga" in text and rel == "index.html":
            print(f"  [SKIP] {rel} (already processed)")
            continue
        if "nav_mobile_to_kasuga" in text and "mobile menu" in [p[0] for p in patches] and len(patches) == 1:
            print(f"  [SKIP] {rel} (already processed)")
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
