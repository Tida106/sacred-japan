#!/usr/bin/env python3
"""
Step 1: Convert all JPG/PNG in images/ and ogp.png to WebP.
Keeps originals. Skips if .webp already exists.
"""
import sys
from pathlib import Path
from PIL import Image

BASE = Path(__file__).parent.parent
IMAGES_DIR = BASE / 'images'

converted = []
skipped = []
failed = []

# images/ folder
for ext in ('*.jpg', '*.jpeg', '*.png', '*.JPG', '*.JPEG', '*.PNG'):
    for src in sorted(IMAGES_DIR.glob(ext)):
        dst = src.with_suffix('.webp')
        if dst.exists():
            skipped.append(src.name)
            continue
        try:
            with Image.open(src) as img:
                mode = 'RGBA' if img.mode in ('RGBA', 'LA', 'P') else 'RGB'
                img.convert(mode).save(dst, 'WEBP', quality=82, method=4)
            orig = src.stat().st_size
            out  = dst.stat().st_size
            converted.append((src.name, orig, out))
        except Exception as e:
            failed.append((src.name, str(e)))

# root ogp.png
for root_img in ['ogp.png']:
    src = BASE / root_img
    if not src.exists():
        continue
    dst = src.with_suffix('.webp')
    if dst.exists():
        skipped.append(root_img)
    else:
        try:
            with Image.open(src) as img:
                img.convert('RGB').save(dst, 'WEBP', quality=85, method=4)
            orig = src.stat().st_size
            out  = dst.stat().st_size
            converted.append((root_img, orig, out))
        except Exception as e:
            failed.append((root_img, str(e)))

total_orig = sum(o for _, o, _ in converted)
total_out  = sum(w for _, _, w in converted)

print(f"=== WebP Conversion Results ===")
for name, orig, out in converted:
    pct = int((1 - out/orig) * 100) if orig else 0
    print(f"  {name}: {orig//1024}KB → {out//1024}KB  (-{pct}%)")
if skipped:
    print(f"  [skipped {len(skipped)} already-converted files]")
if failed:
    for name, err in failed:
        print(f"  FAILED {name}: {err}", file=sys.stderr)

print(f"\nConverted: {len(converted)} files")
print(f"Total size: {total_orig//1024}KB → {total_out//1024}KB  (-{int((1-total_out/total_orig)*100) if total_orig else 0}%)")
