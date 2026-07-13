# PharmaDS 2027 — Conference & Community Website

A mobile-first [Astro](https://astro.build) static site for the Pharmaceutical Data Science
Conference 2027 and the growing PharmaDS community (hosted by the New England Statistical Society).

## Getting started

This repo uses Node + npm. If you don't have Node installed system-wide, a portable copy was placed
at `~/.local/pharmads-toolchain`. Load it with:

```bash
source ~/.local/pharmads-toolchain/env.sh   # adds node/npm to PATH for this shell
```

Then, from the project folder:

```bash
npm install      # first time only
npm run dev      # start the local dev server (http://localhost:4321)
npm run build    # build the static site into dist/
npm run preview  # preview the production build
```

## Project structure

```
src/
  layouts/BaseLayout.astro      # shared <head>, header, footer, global styles
  components/                   # Header, Footer, EmbedForm, SubscribeForm,
                                # PartnerLogos, WhoShouldAttend, SessionFormats,
                                # PersonCard, KeyDates, PageHero, SectionHead, CTASection
  pages/                        # one file per route (index, program, short-courses,
                                # call-for-presentations, committee, career-growth,
                                # community, registration, venue, partnership, volunteer)
  data/                         # all editable content (see below)
  styles/global.css             # design system / theme
public/                         # static assets (favicon, partner logos, people photos)
```

## Editing content (no code required)

All content that changes year to year lives in `src/data/*.json`:

| File | What it controls |
| --- | --- |
| `site.json` | Conference name, theme, dates, venue, contact, **LinkedIn URL**, and **all form URLs** (abstract, mentor, volunteer, register-interest, partner, newsletter) |
| `key-dates.json` | The key-dates table (home, registration, CfP) |
| `committee.json` | Board, Advisory Committee, and Organization Committee (by subteam) |
| `sessions.json` | Presentation formats + the 2027 session list (hybrid / summit tags) |
| `short-courses.json` | Short courses by track (stat-evidence / ai-engineering / tools) and type (theory / lab) |
| `events.json` | Community "Upcoming Events" (ASA RISW round table, workshops, conference) |
| `partners.json` | Sponsors/partners by tier (logo strip + partnership wall) |
| `audience.json` | The "Who should attend" personas and value points |

### Things to fill in (search the code for `TODO`)

- 2027 theme, dates, venue/hotel, registration rates & portal link
- Committee member names, roles, affiliations, and headshots (put images in `public/people/`)
- Session names + which formats each runs, and which are "summit style"
- Short course titles, instructors, levels
- Form URLs (Google Forms / Formspree) and the newsletter provider URL
- LinkedIn company URL
- Partner names, logos (`public/partners/`), tiers, and the prospectus PDF

## Contributing website updates (workstreams)

Website changes are coordinated through GitHub Issues so the seven conference workstreams and the
website maintainer share one workflow. **Don't edit content by DM or email** — open an issue:

1. Go to the [**Issues** tab → **New issue**](../../issues/new/choose) and pick a template:
   - **📝 Website Content Update** — change copy/assets on a page (main one).
   - **💡 Topic / Feedback** — an early idea before final copy exists.
   - **🎨 Formatting / Styling Fix** — how a page looks (color, layout, spacing).
   - **🔗 Downstream Activity** — a follow-up (e.g. an Outreach LinkedIn post) triggered once a change is live.
2. Each request moves through visible `status:` labels; **open = pending, closed = live/handled**.
3. Once a change ships, downstream activities are opened as new linked issues so nothing gets lost.

See the [**Workstream Playbook**](.github/WORKSTREAM_PLAYBOOK.md) for page ownership, the request
lifecycle, downstream triggers, and ready-made [request-tracking searches](.github/WORKSTREAM_PLAYBOOK.md#track-requests).

Colored labels (`ws:`, `type:`, `status:`, `priority:`) are defined in
[`.github/labels.yml`](.github/labels.yml); create them in the repo once with `bash scripts/setup-labels.sh`.

## Forms

Forms are handled by third-party services (Google Forms / Formspree). Each form is rendered by the
`EmbedForm` component and reads its URL from `site.json`. Until a real URL is provided, the form
shows a "coming soon" placeholder. Swap the placeholder URL in `site.json` to go live.

## Deployment

The site is fully static (`npm run build` → `dist/`) and is wired for Git-based hosting on
**Netlify** or **Cloudflare Pages**, served at a root URL (no base-path config needed).

Repo: https://github.com/helloysz/Pharma-DS-Website

### Netlify (recommended — auto PR previews)

1. https://app.netlify.com → **Add new site → Import an existing project → GitHub** → pick
   `helloysz/Pharma-DS-Website`.
2. Build settings are auto-detected from `netlify.toml` (build `npm run build`, publish `dist`,
   Node 22). Click **Deploy**.
3. Every push to `main` redeploys; every pull request gets its own **Deploy Preview** URL — ideal
   for assigning reviewers.

### Cloudflare Pages (alternative)

1. Cloudflare dashboard → **Workers & Pages → Create → Pages → Connect to Git** → pick the repo.
2. Framework preset: **Astro**. Build command `npm run build`, output dir `dist`
   (`NODE_VERSION` 22 is read from `.nvmrc`).

### Custom domain (`phds.nestat.org`)

Add the domain in the host's dashboard and update DNS when you're ready to move off the current
2026 site. Because the site is served at root, no code changes are needed for the custom domain.
