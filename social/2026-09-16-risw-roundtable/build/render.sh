#!/usr/bin/env bash
# Renders the PharmaDS social posters from the HTML sources in this folder.
set -euo pipefail
cd "$(dirname "$0")"

CHROME="${CHROME:-/opt/pw-browsers/chromium-1194/chrome-linux/chrome}"
[ -x "$CHROME" ] || CHROME="$(command -v google-chrome || command -v chromium || echo '')"
[ -n "$CHROME" ] || { echo "No Chrome/Chromium found; set CHROME=/path/to/chrome"; exit 1; }

# Brand fonts (Inter + Space Grotesk, latin subset) — fetched once, not committed.
if [ ! -f fonts/Inter.woff2 ] || [ ! -f fonts/SpaceGrotesk.woff2 ]; then
  mkdir -p fonts
  curl -sS -A "Mozilla/5.0" \
    "https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&family=Space+Grotesk:wght@500;600;700&display=swap" \
    -o /tmp/pharmads-gf.css
  python3 - <<'PY'
import re, subprocess, os
css = open('/tmp/pharmads-gf.css').read()
os.makedirs('fonts', exist_ok=True)
for subset, body in re.findall(r'/\*\s*([a-z0-9\-\[\]]+)\s*\*/\s*@font-face\s*\{(.*?)\}', css, re.S):
    if subset != 'latin':
        continue
    fam = re.search(r"font-family:\s*'([^']+)'", body).group(1)
    url = re.search(r'url\((https://[^)]+)\)', body).group(1)
    subprocess.run(['curl', '-sS', '-o', 'fonts/%s.woff2' % fam.replace(' ', ''), url], check=True)
PY
fi

render () { # html width height output.png
  "$CHROME" --headless=new --no-sandbox --disable-gpu --hide-scrollbars \
    --force-device-scale-factor=2 --allow-file-access-from-files \
    --window-size="$2,$(( $3 + 400 ))" --screenshot=_raw.png "file://$PWD/$1" 2>/dev/null
  python3 - "$2" "$3" "$4" <<'PY'
import sys
from PIL import Image
w, h, out = int(sys.argv[1]), int(sys.argv[2]), sys.argv[3]
im = Image.open('_raw.png').convert('RGB').crop((0, 0, w * 2, h * 2))   # trim the render padding
im.save(out)
im.resize((w, h), Image.LANCZOS).save(out.replace('.png', '_1x.jpg'), quality=88)
print(out, im.size)
PY
  rm -f _raw.png
}

render poster-portrait.html 1080 1350 poster_portrait.png
render poster-square.html   1200 1200 poster_square.png
