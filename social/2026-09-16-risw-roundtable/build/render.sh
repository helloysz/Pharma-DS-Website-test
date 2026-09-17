#!/usr/bin/env bash
# Renders the PharmaDS social posters from the HTML sources in this folder.
set -euo pipefail
cd "$(dirname "$0")"

CHROME="${CHROME:-/opt/pw-browsers/chromium-1194/chrome-linux/chrome}"
[ -x "$CHROME" ] || CHROME="$(command -v google-chrome || command -v chromium || echo '')"
[ -n "$CHROME" ] || { echo "No Chrome/Chromium found; set CHROME=/path/to/chrome"; exit 1; }

# Brand fonts (Inter + Space Grotesk + Tinos) - fetched once, not committed.
if [ ! -f fonts/Inter.woff2 ] || [ ! -f fonts/SpaceGrotesk.woff2 ] || [ ! -f fonts/Tinos-700.woff2 ]; then
  python3 fetch-fonts.py
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
