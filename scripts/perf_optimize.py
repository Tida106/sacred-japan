#!/usr/bin/env python3
"""
Perf optimizations for all HTML files:
  1. Google Fonts: render-blocking -> non-blocking (media=print onload pattern)
  2. Inline <style> blocks: remove CSS comments + blank lines (minify)
"""
import re
from pathlib import Path

BASE = Path(__file__).parent.parent

# ── Collect all HTML files ─────────────────────────────────────────────────
html_files = sorted(BASE.rglob('*.html'))

# ── 1. Google Fonts non-blocking ───────────────────────────────────────────
FONTS_PATTERN = re.compile(
    r'<link\s+href="(https://fonts\.googleapis\.com/css2\?[^"]+)"\s+rel="stylesheet">'
)

def make_fonts_nonblocking(content):
    def replace_font_link(m):
        url = m.group(1)
        return (
            f'<link rel="stylesheet" media="print" onload="this.media=\'all\'" href="{url}">'
            f'<noscript><link rel="stylesheet" href="{url}"></noscript>'
        )
    return FONTS_PATTERN.sub(replace_font_link, content)

# ── 2. CSS minification (inline <style> blocks only) ──────────────────────
STYLE_PATTERN = re.compile(r'(<style(?:[^>]*)>)(.*?)(</style>)', re.DOTALL)
CSS_COMMENT   = re.compile(r'/\*.*?\*/', re.DOTALL)

def minify_css(css):
    # remove /* ... */ comments
    css = CSS_COMMENT.sub('', css)
    # strip each line, drop blank lines
    lines = [l.strip() for l in css.splitlines()]
    lines = [l for l in lines if l]
    return '\n'.join(lines)

def minify_styles(content):
    def replace_style(m):
        open_tag, css, close_tag = m.group(1), m.group(2), m.group(3)
        return open_tag + '\n' + minify_css(css) + '\n' + close_tag
    return STYLE_PATTERN.sub(replace_style, content)

# ── Main ───────────────────────────────────────────────────────────────────
fonts_changed = []
css_changed   = []
unchanged     = []

for path in html_files:
    original = path.read_text(encoding='utf-8')
    updated  = original

    after_fonts = make_fonts_nonblocking(updated)
    after_css   = minify_styles(after_fonts)

    if after_css != original:
        path.write_text(after_css, encoding='utf-8')
        f_changed = after_fonts != original
        c_changed = after_css   != after_fonts
        label = []
        if f_changed: label.append('fonts')
        if c_changed: label.append('css')
        print(f"  Updated [{','.join(label)}]: {path.relative_to(BASE)}")
        if f_changed: fonts_changed.append(path)
        if c_changed: css_changed.append(path)
    else:
        unchanged.append(path)

print(f"\nGoogle Fonts non-blocking: {len(fonts_changed)} files")
print(f"CSS minified:              {len(css_changed)} files")
print(f"Unchanged:                 {len(unchanged)} files")
