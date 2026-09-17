#!/usr/bin/env python3
"""Download the brand webfonts (latin subset) used by the posters into ./fonts.

Fraunces (serif, display + italic) for the fine-art/editorial poster
typography, Inter for supporting body text and labels, Montserrat
ExtraBold for the PharmaDS wordmark in the logo lockup (unchanged brand
mark), Space Grotesk kept for any older poster variants that still use it.
"""
import os
import re
import subprocess

URL = ("https://fonts.googleapis.com/css2?"
       "family=Inter:ital,wght@0,400;0,500;0,600;0,700;0,800;0,900;1,400;1,600;1,700"
       "&family=Fraunces:ital,opsz,wght@0,9..144,400;0,9..144,500;0,9..144,600;"
       "0,9..144,700;1,9..144,400;1,9..144,500;1,9..144,600"
       "&family=Space+Grotesk:wght@500;600;700"
       "&family=Montserrat:wght@700;800&display=swap")
# The full Chrome UA matters: with a short UA, Google Fonts serves legacy TTF instead of woff2.
UA = ("Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) "
      "Chrome/120.0.0.0 Safari/537.36")

css = subprocess.run(['curl', '-sS', '-A', UA, URL], check=True,
                     capture_output=True, text=True).stdout
os.makedirs('fonts', exist_ok=True)

for block in re.findall(r'@font-face\s*\{(.*?)\}', css, re.S):
    rng = re.search(r'unicode-range:\s*([^;]+);', block)
    if rng and 'U+0000-00FF' not in rng.group(1):   # keep the basic-latin subset only
        continue
    family = re.search(r"font-family:\s*'([^']+)'", block).group(1).replace(' ', '')
    weight = re.search(r'font-weight:\s*([^;]+);', block).group(1).strip().split()[-1]
    style = re.search(r'font-style:\s*([^;]+);', block)
    style = style.group(1).strip() if style else 'normal'
    url = re.search(r'url\((https://[^)]+)\)', block).group(1)
    suffix = '' if style == 'normal' else '-italic'
    names = ['fonts/%s%s.woff2' % (family, suffix),
             'fonts/%s%s-%s.woff2' % (family, suffix, weight)]
    for name in names:
        subprocess.run(['curl', '-sS', '-o', name, url], check=True)
    print('font %s %s %s' % (family, style, weight))
