# PharmaDS 2027 Conference & Community Website

A mobile-first Astro static site for the PharmaDS 2027 Conference and Community.

## Project Overview

This is a content-driven website designed to replace/extend the PharmaDS 2026 site. It features a modern design inspired by the AI Summit (newyork.theaisummit.com) with a focus on:

- **Conference Program**: Sessions, short courses, keynotes, panels
- **Call for Presentations**: Multiple presentation formats with abstract submission
- **Committee Management**: Board, Advisory, and Organization Committee by subteam
- **Career Growth**: Mentorship programs and professional development
- **Community Hub**: Events, networking, and ongoing community engagement
- **Partnership**: Sponsorship tiers, partner logos, and inquiries
- **Registration & Logistics**: Venue information, travel, accommodations

## Tech Stack

- **Framework**: [Astro](https://astro.build) (static site generation)
- **Styling**: Plain CSS with mobile-first responsive design
- **Content Model**: JSON data files (`src/data/*.json`) for easy updates
- **Components**: Reusable Astro components (EmbedForm, PartnerLogos, WhoShouldAttend, SessionFormat)
- **Forms**: Third-party embeds (Google Forms / Formspree placeholders)

## Project Structure

```
src/
├── data/                    # Editable content files
│   ├── key-dates.json       # Conference dates, location, registration
│   ├── committee.json       # Board, Advisory, Organization committee
│   ├── sessions.json        # Conference sessions
│   ├── short-courses.json   # Pre-conference courses
│   ├── events.json          # Community events
│   └── partners.json        # Sponsors and partners
├── layouts/
│   └── BaseLayout.astro     # Shared header, footer, navigation
├── components/
│   ├── EmbedForm.astro      # Form embedding (Google Forms / Formspree)
│   ├── PartnerLogos.astro   # Partner logo strip or wall
│   ├── WhoShouldAttend.astro # Target audience personas
│   └── SessionFormat.astro  # Presentation format legend
├── pages/                   # Page routes (auto-routing)
│   ├── index.astro          # Home page
│   ├── program.astro        # Program & Agenda
│   ├── short-courses.astro  # Short Courses
│   ├── call-for-presentations.astro
│   ├── committee.astro      # Committee page
│   ├── career-growth.astro  # Career Growth & Networking
│   ├── community-events.astro
│   ├── registration.astro
│   ├── venue.astro          # Venue & Travel
│   ├── partnership.astro    # Sponsorship opportunities
│   └── volunteer.astro      # Volunteer sign-up
└── styles/
    └── global.css           # Global styles & utilities
```

## Editable Data Files

All content is stored in JSON files in `src/data/` for easy updates by non-developers:

### key-dates.json
- Conference theme, dates, location, hotel info
- Registration status and pricing
- Call for presentations dates

### committee.json
- Board Co-Chairs
- Advisory Committee members
- Organization Committee by subteam (Session Organization, Speaker Coordination, Logistics, etc.)

### sessions.json
- Conference sessions with format (keynote, panel, traditional, rapid-demo, experience-sharing)
- Hybrid tagging
- Speaker information

### short-courses.json
- Pre-conference courses across three tracks:
  - Statistical Evidence Generation
  - AI Engineering
  - Tool Usage
- Type: Theory or Lab

### events.json
- Community events (ASA RISW roundtable, workshops, etc.)
- Event details, registration links

### partners.json
- Sponsor/partner information with tier (Platinum, Gold, Silver, Community)
- Sponsorship tiers and benefits

## Key Features

### Responsive Design
- Mobile-first approach
- Hamburger menu on mobile
- Flexible grid layouts
- CSS custom properties for theming

### Navigation
- Sticky header with logo
- Mobile hamburger menu (JavaScript-enhanced)
- Footer with LinkedIn follow, newsletter subscribe, and partner logos

### Components
- **EmbedForm**: Embeds Google Forms or Formspree forms
- **PartnerLogos**: Renders partners as strip or wall layout
- **WhoShouldAttend**: Persona cards showing target audience
- **SessionFormat**: Legend of presentation formats

### Forms
Form URLs are placeholders throughout (marked with TODO) and use `EmbedForm` component:
- Newsletter subscribe
- Mentor sign-up
- Abstract submission
- Partnership inquiries
- Volunteer applications
- Interest registration

Replace TODO placeholders with actual Google Form or Formspree URLs.

## Placeholders (TODO)

All content placeholders are clearly marked with "TODO" tags:

- **2027 theme** (key-dates.json)
- **Conference dates** (key-dates.json)
- **Venue and location** (key-dates.json)
- **Hotel partner** (key-dates.json)
- **Registration fees & links** (key-dates.json)
- **Committee member names & photos** (committee.json)
- **Session names & speakers** (sessions.json)
- **Course titles & instructors** (short-courses.json)
- **Event details** (events.json)
- **Form URLs** (throughout pages and components)
- **Newsletter provider URL** (footer)
- **LinkedIn company URL** (footer)
- **Partner logos & info** (partners.json)
- **Partnership prospectus PDF** (partnership.astro)

## Setup & Development

### Prerequisites
- Node.js 18+ (required for Astro)
- npm or yarn

### Installation
```bash
npm install
```

### Development Server
```bash
npm run dev
```
Visit http://localhost:3000 in your browser.

### Build for Production
```bash
npm run build
```
Output: `dist/` folder with static HTML files.

### Preview Production Build
```bash
npm run preview
```

## Deployment

The built `dist/` folder can be deployed to any static hosting:
- Netlify
- Vercel
- GitHub Pages
- AWS S3 + CloudFront
- Traditional web servers

**Out of scope (for now)**: Deployment to phds.nestat.org, DNS setup, custom form backend.

## Updating Content

### To Update Dates, Location, Registration
Edit `src/data/key-dates.json`

### To Update Committee Members
Edit `src/data/committee.json` (Board, Advisory, Organization by subteam)

### To Add/Update Sessions
Edit `src/data/sessions.json`

### To Add/Update Courses
Edit `src/data/short-courses.json`

### To Add/Update Events
Edit `src/data/events.json`

### To Add/Update Partners & Sponsorship Tiers
Edit `src/data/partners.json`

### To Update Form URLs
Search for "TODO:" in the page files and replace placeholder URLs with actual form links.

### To Customize Colors & Typography
Edit `src/styles/global.css` (CSS custom properties at top of file)

## References

- **Reference Site**: https://newyork.theaisummit.com/
- **Astro Docs**: https://docs.astro.build
- **AI Summit Design**: Minimal, clean, content-focused layout

## License

PharmaDS 2027. All rights reserved.

## Contact

For questions about the website, contact:
- General: info@pharmads.org
- Program: program@pharmads.org
- Registration: registration@pharmads.org
- Partnerships: partnerships@pharmads.org
- Travel: travel@pharmads.org
- Volunteers: volunteers@pharmads.org
