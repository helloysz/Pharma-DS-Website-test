# RISW 2026 roundtable — social assets

Follow-up campaign for the PharmaDS Community Roundtable (Sept 16, 2026, RISW 2026, Bethesda MD).

- `post-01-group-photo.md` — post 1 copy (two versions), first comment, pre-flight checklist
- `series-plan.md` — the four-post sequence and what each one needs
- `assets/` — upload-ready images
  - `poster-portrait-1080x1350.jpg` — **primary LinkedIn asset**
  - `poster-square-1200x1200.jpg` — square variant
  - `poster-portrait-2160x2700.png`, `poster-square-2400x2400.png` — hi-res originals (print / reuse)
  - `group-photo-enhanced.jpg` — the group photo on its own, cropped and colour-corrected
  - `group-photo-poster-crop.jpg` — the wide crop used inside the posters
- `build/` — poster source (HTML + CSS + render script) so any of the four posts can reuse the layout

## Photo edits applied to the original

Cropped out the cable-covered foreground table and the excess ceiling, so the frame is just the
group; brightness +11%, contrast +12%, saturation +8% to lift the dim hotel-meeting-room light;
unsharp mask for LinkedIn's downscaling. Nobody is cropped out of frame.

## Re-rendering the posters

```bash
cd build
./render.sh          # downloads the brand fonts, writes PNG + 1x JPG for both sizes
```

Requires the Chromium that ships with Playwright (`/opt/pw-browsers/...`) or any local Chrome —
set `CHROME=/path/to/chrome` to override. Edit text directly in `poster-portrait.html` /
`poster-square.html`; shared styling (brand palette, tiles, CTA bar) lives in `poster.css` and
matches `src/styles/global.css`.
