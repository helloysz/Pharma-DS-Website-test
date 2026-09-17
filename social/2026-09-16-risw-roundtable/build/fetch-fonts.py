#!/usr/bin/env python3
"""Download the brand webfonts (latin subset) used by the posters into ./fonts.

Inter + Space Grotesk for the poster typography, Montserrat ExtraBold for the
PharmaDS wordmark in the logo lockup.
"""
import os
import re
import subprocess

URL = ("https://fonts.googleapis.com/css2?"
       "family=Inter:wght@400;500;600;700;800;900"
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
    url = re.search(r'url\((https://[^)]+)\)', block).group(1)
    for name in ('fonts/%s.woff2' % family, 'fonts/%s-%s.woff2' % (family, weight)):
        subprocess.run(['curl', '-sS', '-o', name, url], check=True)
    print('font %s %s' % (family, weight))
