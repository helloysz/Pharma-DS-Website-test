#!/usr/bin/env python3
"""Crop + colour-correct the roundtable group photo for the posters.

Usage: python3 process-photo.py /path/to/original.jpg
Writes group_wide.jpg (poster crop) and group_full.jpg (standalone photo post).
"""
import sys
from PIL import Image, ImageEnhance, ImageFilter

src = sys.argv[1] if len(sys.argv) > 1 else 'original.jpg'
im = Image.open(src)
W, H = im.size


def finish(crop, name, width=2400):
    c = ImageEnhance.Brightness(crop).enhance(1.11)   # lift the dim meeting-room light
    c = ImageEnhance.Contrast(c).enhance(1.12)
    c = ImageEnhance.Color(c).enhance(1.08)
    if c.width > width:
        c = c.resize((width, int(c.height * width / c.width)), Image.LANCZOS)
    c = c.filter(ImageFilter.UnsharpMask(radius=1.6, percent=85, threshold=3))
    c.save(name, quality=92, subsampling=1)
    print(name, c.size)


finish(im.crop((0, int(0.125 * H), W, int(0.795 * H))), 'group_wide.jpg')  # drops table + ceiling
finish(im.crop((0, int(0.055 * H), W, int(0.860 * H))), 'group_full.jpg')  # gentler crop
