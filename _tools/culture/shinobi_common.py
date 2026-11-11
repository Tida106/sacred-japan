"""Shared helpers for the samurai / ninja / hub builders.

Each builder (samurai.py, ninja.py, samurai_ninja.py) imports this module,
builds its own <main> body, and calls finish(). The page shell (head, JSON-LD,
hero, breadcrumb, footer, sticky CTA) comes from the same skeleton that
tea.py/yakitori.py use (omamori-guide), so styling stays identical.
Output HTML is overwritten on rebuild: make every change in the builders.
"""
import re, os, json
from PIL import Image

R = '/home/claude/sacred-japan'
VIA = 'via Wikimedia Commons (resized)'


def lic(n, u):
    return f'<a href="{u}" target="_blank" rel="noopener" style="color:var(--enshu);">{n}</a>'


CC0 = lic('CC0', 'https://creativecommons.org/publicdomain/zero/1.0/')
BYSA4 = lic('CC BY-SA 4.0', 'https://creativecommons.org/licenses/by-sa/4.0/')
BYSA3 = lic('CC BY-SA 3.0', 'https://creativecommons.org/licenses/by-sa/3.0/')
BY4 = lic('CC BY 4.0', 'https://creativecommons.org/licenses/by/4.0/')
PDM = lic('Public Domain Mark', 'https://creativecommons.org/publicdomain/mark/1.0/')


def link(href, txt, lab):
    return f'<a href="{href}" class="inline-link" onclick="trackEvent(\'click\',\'internal\',\'{lab}\')">{txt}</a>'


def ext(href, txt, lab):
    return f'<a href="{href}" target="_blank" rel="noopener" onclick="trackEvent(\'click\',\'external\',\'{lab}\')">{txt}</a>'


def aff(href, txt, lab):
    """Affiliate link (Viator etc.): sponsored + affiliate event."""
    return f'<a href="{href}" target="_blank" rel="noopener sponsored" onclick="trackEvent(\'click\',\'affiliate\',\'{lab}\')">{txt}</a>'


def viator(term):
    return f'https://www.viator.com/search/{term}?pid=P00298374&amp;mcid=42383&amp;medium=link&amp;campaign=sacred-japan'


def make_fig(S):
    """Return fig() bound to the culture/<S>/ images folder."""
    def fig(k, alt, cap, credit, hero=False, maxw=760):
        st = 'margin:0 0 48px;' if hero else f'margin:36px auto;max-width:{maxw}px;'
        img_st = ('width:100%;max-height:420px;object-fit:cover;border-radius:4px;display:block;'
                  if hero else 'width:100%;height:auto;border-radius:4px;display:block;')
        ld = 'eager' if hero else 'lazy'
        return f'''<figure style="{st}">
      <picture><source srcset="/culture/{S}/images/{k}.webp" type="image/webp"><img src="/culture/{S}/images/{k}.jpg" alt="{alt}" loading="{ld}" style="{img_st}"></picture>
      <figcaption style="font-size:13px;color:var(--enshu);margin-top:10px;text-align:center;line-height:1.6;">{cap}<br>{credit}</figcaption>
    </figure>'''
    return fig


def copy_photos(S, photos, maxw=1200):
    """photos: {key: repo-relative source jpg}. Writes jpg+webp into culture/<S>/images."""
    out = f'{R}/culture/{S}/images'
    os.makedirs(out, exist_ok=True)
    for k, src in photos.items():
        im = Image.open(f'{R}/{src}').convert('RGB')
        w, h = im.size
        if w > maxw:
            im = im.resize((maxw, round(h * maxw / w)), Image.LANCZOS)
        im.save(f'{out}/{k}.jpg', quality=84, optimize=True)
        im.save(f'{out}/{k}.webp', quality=80)


def faq_blocks(faqs):
    html = ''.join(f'''      <details class="faq-item">
        <summary>{q}</summary>
        <div class="faq-answer">{a}</div>
      </details>

''' for q, a in faqs)
    ld = json.dumps({"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": re.sub('<[^>]+>', '', a)}}
        for q, a in faqs]}, ensure_ascii=False, indent=2)
    return html, ld


def finish(S, TITLE, DESC, KEYWORDS, kanji, h1_html, hero_jp, subtitle, name, evt,
           viator_term, main, faq_ld, published='2026-11-11'):
    """Assemble culture/<S>/index.html from the shared skeleton (tea.py's tail)."""
    URL = f'https://sacred-japan.net/culture/{S}/'
    OG = f'https://sacred-japan.net/images/og/og-culture-{S}.jpg'
    OUT = f'{R}/culture/{S}'
    os.makedirs(OUT, exist_ok=True)
    t = open(f'{R}/_tools/culture/tea.py', encoding='utf-8').read()
    tail = t[t.index("s=open(f'{R}/culture/omamori-guide"):]
    tail = tail.replace('<div class="hero-bg-kanji">茶道</div>', f'<div class="hero-bg-kanji">{kanji}</div>')
    tail = tail.replace('<h1>The Japanese <em>Tea Ceremony</em> Guide</h1>', f'<h1>{h1_html}</h1>')
    tail = tail.replace('<div class="hero-jp">茶道ガイド</div>', f'<div class="hero-jp">{hero_jp}</div>')
    tail = tail.replace('What Happens, What to Do as a Guest, and Where to Try It', subtitle)
    tail = tail.replace('Tea Ceremony Guide', name)
    tail = tail.replace('guide_tea', evt).replace('japanese+tea+ceremony', viator_term)
    tail = tail.replace('"2026-11-08"', f'"{published}"')
    tail = re.sub(r'(<meta name="keywords" content=")[^"]*(")', lambda m: m.group(1) + KEYWORDS + m.group(2), tail)
    g = dict(re=re, os=os, json=json, R=R, OUT=OUT, TITLE=TITLE, DESC=DESC, URL=URL, OG=OG,
             faq_ld=faq_ld, main=main)
    exec(tail, g)
    return URL
