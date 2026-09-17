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
  - `pharmads-logo.svg` — logo mark (density curve + ascending bars), see caveat below
- `build/` — poster source (HTML + CSS, `render.sh`, `fetch-fonts.py`, `process-photo.py`)
  so posts 2–4 can reuse the layout

## Poster layout

Built as a sibling of the announcement poster, so the two read as one series: a single
photographic field (the group shot sharp at the top, the same shot blurred behind the type below),
white left-aligned headings in the announcement's hierarchy ("Thank you for joining us at" /
**RISW 2026** / event name), the strapline in italics, hairline rules with letterspaced section
labels, a translucent bordered panel for "What's coming next", and the announcement's own white
logo panel at the foot carrying the RISW/ASA logo and the PharmaDS lockup.

It carries only what the announcement didn't: what came out of the room, and what's coming next.
Date, time, room, Zoom details, agenda and facilitators are all left off on purpose — the
announcement post already had them.

`assets/risw-asa-logo.png` is cropped from the announcement poster's own footer panel and
upscaled; replace it with the original ASA/RISW logo file if you have one.

## Photo edits applied to the original

Cropped out the cable-covered foreground table and the excess ceiling, so the frame is just the
group; brightness +11%, contrast +12%, saturation +8% to lift the dim hotel-meeting-room light;
unsharp mask for LinkedIn's downscaling. Nobody is cropped out of frame.

## Logo

`assets/pharmads-logo.svg` is the PharmaDS mark rebuilt as vector from the deck: navy `#003889`
tile, white ECG trace, three ascending bars in `#b6adfb` / `#7db1fd` / `#02c0d1`, geometry and
colours measured off the artwork.

The lockup next to it follows the event poster's logo: two-tone wordmark in Montserrat ExtraBold
(`Pharma` white, `DS` lavender `#a99bff` — the light-background original is navy `#003078` +
violet `#5448d8`) over the tagline "Data-driven. Future-defining." If you have the original logo
vector, drop it in at `assets/pharmads-logo.svg` and re-render; the wordmark lives in
`build/poster.css` (`.wordmark`).

## Re-rendering the posters

```bash
cd build
./render.sh          # downloads the brand fonts, writes PNG + 1x JPG for both sizes
```

Requires the Chromium that ships with Playwright (`/opt/pw-browsers/...`) or any local Chrome —
set `CHROME=/path/to/chrome` to override. Edit text directly in `poster-portrait.html` /
`poster-square.html`; shared styling (brand palette, photo treatment, CTA bar) lives in
`poster.css` and matches `src/styles/global.css`.
