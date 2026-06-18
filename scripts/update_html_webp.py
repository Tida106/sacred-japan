#!/usr/bin/env python3
"""
Update HTML files to:
 - Wrap local <img> with <picture><source webp><img></picture>
 - Add loading="lazy" to off-screen images
 - Update CSS background-image URLs to .webp
"""
import re
from pathlib import Path

BASE = Path(__file__).parent.parent

def to_webp(src):
    return re.sub(r'\.(jpg|jpeg|png)$', '.webp', src, flags=re.I)

def wrap_picture(src, attrs):
    ws = to_webp(src)
    return f'<picture><source srcset="{ws}" type="image/webp"><img src="{src}"{attrs}></picture>'

# ─── index.html ──────────────────────────────────────────────────────────
HERO_IMG = 'images/ise-jingu.jpg'   # first spot-card = no lazy

def process_index(content):
    first_local = {'done': False}

    def replace_local_img(m):
        src, attrs = m.group(1), m.group(2)
        is_hero = (src == HERO_IMG and not first_local['done'])
        first_local['done'] = True
        if not is_hero and 'loading=' not in attrs:
            attrs += ' loading="lazy"'
        return wrap_picture(src, attrs)

    # local imgs (src starts with "images/")
    content = re.sub(
        r'<img\s+src="(images/[^"]+\.(?:jpg|jpeg|png))"([^>]*)>',
        replace_local_img, content, flags=re.I)

    # Unsplash spot-card imgs — add lazy (they're all off-screen cards)
    def add_lazy_unsplash(m):
        src, attrs = m.group(1), m.group(2)
        if 'loading=' not in attrs:
            attrs += ' loading="lazy"'
        return f'<img src="{src}"{attrs}>'
    content = re.sub(
        r'<img\s+src="(https://images\.unsplash\.com/[^"]+)"([^>]*)>',
        add_lazy_unsplash, content, flags=re.I)

    # CSS background-image → webp
    bg_map = {
        "url('ogp.png')":                  "url('ogp.webp')",
        "url('/images/omamori.png')":      "url('/images/omamori.webp')",
        "url('/images/ema.png')":          "url('/images/ema.webp')",
        "url('/images/omikuji.png')":      "url('/images/omikuji.webp')",
        "url('/images/ofuda.png')":        "url('/images/ofuda.webp')",
        "url('/images/dorei.png')":        "url('/images/dorei.webp')",
        "url('/images/shinsui.png')":      "url('/images/shinsui.webp')",
    }
    for old, new in bg_map.items():
        content = content.replace(old, new)

    return content

# ─── Guide pages (/images/X.jpg) — single lead-photo, no lazy ────────────
def process_guide(content):
    def replace_guide_img(m):
        src, attrs = m.group(1), m.group(2)
        return wrap_picture(src, attrs)
    content = re.sub(
        r'<img\s+src="(/images/[^"]+\.(?:jpg|jpeg|png))"([^>]*)>',
        replace_guide_img, content, flags=re.I)
    return content

# ─── Sub-pages (../images/X.jpg) — all already lazy ─────────────────────
def process_subpage(content):
    def replace_sub_img(m):
        src, attrs = m.group(1), m.group(2)
        return wrap_picture(src, attrs)
    content = re.sub(
        r'<img\s+src="(\.\./images/[^"]+\.(?:jpg|jpeg|png))"([^>]*)>',
        replace_sub_img, content, flags=re.I)
    return content

# ─── Main ────────────────────────────────────────────────────────────────
def update_file(path, processor):
    content = path.read_text(encoding='utf-8')
    updated = processor(content)
    if updated != content:
        path.write_text(updated, encoding='utf-8')
        changed = content.count('<img ') - updated.count('<img ')  # rough delta
        print(f"  Updated: {path.relative_to(BASE)}  ({content.count('<img ')} imgs)")
        return True
    print(f"  No change: {path.relative_to(BASE)}")
    return False

GUIDE_PAGES = [
    'guides/dazaifu-tenmangu/index.html',
    'guides/kinkakuji/index.html',
    'guides/todaiji/index.html',
    'guides/ise-grand-shrine/index.html',
    'guides/itsukushima-shrine/index.html',
    'guides/meiji-jingu/index.html',
    'guides/sensoji/index.html',
    'guides/sumiyoshi-taisha/index.html',
]

SUB_PAGES = [
    'castles/index.html',
    'anime/index.html',
    'crafts/index.html',
    'regional-food/index.html',
]

print("=== Updating HTML files for WebP / lazy loading ===")
changed = 0

print("\n[index.html]")
if update_file(BASE / 'index.html', process_index):
    changed += 1

print("\n[Guide pages]")
for rel in GUIDE_PAGES:
    if update_file(BASE / rel, process_guide):
        changed += 1

print("\n[Sub-pages]")
for rel in SUB_PAGES:
    if update_file(BASE / rel, process_subpage):
        changed += 1

print(f"\nDone. {changed} files updated.")
