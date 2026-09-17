#!/usr/bin/env python3
"""Crop, colour-correct and grade the roundtable group photo for the posters.

Usage: python3 process-photo.py /path/to/original.jpg

Writes three files into this folder:
  group_wide.jpg          poster crop, plain colour-correction (drops table + ceiling)
  group_full.jpg          gentler crop, for a standalone photo post
  group_fineart.jpg       group_wide graded for the editorial/fine-art poster:
                          a soft ink-to-parchment duotone blended in, a light
                          vignette, and fine print grain
Copy group_fineart.jpg to ../assets/group-photo-fineart.jpg to update the poster.
"""
import sys
from PIL import Image, ImageEnhance, ImageFilter, ImageOps, ImageChops, ImageDraw

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
    return c


def fine_art_grade(base, name):
    """Grade a photo-corrected crop toward the poster's ink/parchment/gold palette:
    a soft duotone blended in, a gentle vignette, and fine print grain — a printed-plate
    look rather than a flat phone photo, while keeping faces true to life."""
    w, h = base.size
    graded = ImageEnhance.Color(base).enhance(0.86)

    gray = ImageOps.grayscale(graded)
    shadow, mid, highlight = (14, 20, 46), (140, 128, 112), (241, 229, 199)
    luts = ([], [], [])
    for i in range(256):
        t = i / 255
        lo, hi = (shadow, mid) if t < 0.5 else (mid, highlight)
        k = (t if t < 0.5 else t - 0.5) / 0.5
        for ch, lut in enumerate(luts):
            lut.append(int(lo[ch] + (hi[ch] - lo[ch]) * k))
    duotone = Image.merge('RGB', tuple(gray.point(lut) for lut in luts))
    graded = Image.blend(graded, duotone, 0.22)

    vignette = Image.new('L', (w, h), 0)
    ImageDraw.Draw(vignette).ellipse((-w * 0.28, -h * 0.35, w * 1.28, h * 1.35), fill=255)
    vignette = ImageOps.invert(vignette.filter(ImageFilter.GaussianBlur(w * 0.10))).point(lambda p: int(p * 0.35))
    graded = ImageChops.subtract(graded, Image.merge('RGB', (vignette, vignette, vignette)))

    grain = Image.effect_noise((w, h), 26).convert('L').point(lambda p: int(p * 0.10))
    graded = ImageChops.add(graded, Image.merge('RGB', (grain, grain, grain)))

    graded = ImageEnhance.Contrast(graded).enhance(1.02)
    graded.save(name, quality=92, subsampling=1)
    print(name, graded.size)


wide = finish(im.crop((0, int(0.10 * H), W, int(0.775 * H))), 'group_wide.jpg')
finish(im.crop((0, int(0.055 * H), W, int(0.860 * H))), 'group_full.jpg')
fine_art_grade(wide, 'group_fineart.jpg')
