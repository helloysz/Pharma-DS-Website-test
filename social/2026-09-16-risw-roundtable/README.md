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

## Poster layout — an editorial/print treatment, not a tech-dashboard one

Redesigned around a museum-catalog mood: a deep ink-navy canvas, warm parchment-cream type, and
antique gold as the one accent color — no neon glows, no rounded UI cards. Typography is Fraunces
(a serif built for this kind of display work, italic for the strapline, the caption and the
thank-you line) paired with Inter for labels and body copy, the same pairing a gallery invitation
or a printed program uses.

The group photo runs full-bleed at the top like a printed plate — a thin gold hairline rule above
and below it — graded toward the same ink/parchment/gold palette (see below) rather than left as a
flat phone photo, with a Bethesda/date stamp underneath in italic serif. The two content sections
below it are hairline-ruled, tracked-caps labels in the announcement's own hierarchy pattern
("Thank you for joining us at" / **RISW 2026** / event name / strapline in quotes):

- **"What the room gave us"** — three em-dash lines on what actually happened in the room.
- **"What's coming next"** — a roman-numeral table of contents (I / II / III) for the next three
  posts, deliberately worded as headlines rather than restating the same two nouns as the list
  above it.

The foot keeps the announcement's own white logo panel — now a plain hairline-bordered card, not a
drop-shadowed one — carrying the RISW/ASA logo and the PharmaDS lockup.

It carries only what the announcement didn't: what came out of the room, and what's coming next.
Date, time, room, Zoom details, agenda and facilitators are all left off on purpose — the
announcement post already had them.

`assets/risw-asa-logo.png` is cropped from the announcement poster's own footer panel and
upscaled; replace it with the original ASA/RISW logo file if you have one.

## The photo grade

`assets/group-photo-fineart.jpg` is the group photo run through a fine-art grade rather than left
as a corrected phone photo: a light desaturation, a soft duotone (ink-navy shadows → warm
parchment highlights) blended in at ~22%, a gentle vignette, and fine print grain — a printed
photograph, not a screen grab. `build/process-photo.py` does the whole pipeline from the original
photo (crop → colour-correct → grade); run it and copy `group_fineart.jpg` over this file to
regenerate. `assets/grain-tile.png` is a small tileable noise texture laid over the whole poster
at low opacity (`.grain`, `mix-blend-mode: overlay`) for the same printed-paper feel.

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
