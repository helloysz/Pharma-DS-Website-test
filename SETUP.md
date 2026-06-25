# 🚀 PharmaDS 2027 Website - Initialization Guide

## Prerequisites

Before initializing, ensure you have:
- **Node.js 18+** (https://nodejs.org/)
- **npm** (comes with Node.js)
- **Git** (for version control)
- A code editor (VS Code recommended)

### Verify Installation
```bash
node --version
npm --version
git --version
```

---

## Step 1: Navigate to Project Directory

```bash
cd "/Users/E0443159/Library/CloudStorage/OneDrive-Sanofi/Documents/Non-project/Pharma DS/2027/Website VS Code"
```

Or in VS Code:
- Open the folder: `File > Open Folder` → select the "Website VS Code" directory

---

## Step 2: Install Dependencies

Install all required npm packages:

```bash
npm install
```

This reads `package.json` and installs:
- `astro` (latest version)
- All necessary dependencies

**Time**: ~1-2 minutes depending on your internet speed.

---

## Step 3: Start Development Server

Launch the local development server:

```bash
npm run dev
```

**Expected output:**
```
  ➜  Local:     http://localhost:3000/
  ➜  press h to show help
```

Open your browser to **http://localhost:3000** 

✅ You should see the PharmaDS 2027 home page!

---

## Step 4: Hot Reload Development

The development server automatically reloads when you make changes:

1. **Edit any file** in `src/` (pages, components, data, styles)
2. **Save the file**
3. Browser automatically refreshes
4. **See changes instantly**

---

## Step 5: Update Content

### To Edit Conference Details

Edit `src/data/key-dates.json`:
```json
{
  "theme": "Your 2027 Theme Here",
  "dates": {
    "conferenceStart": "June 10, 2027",
    "conferenceEnd": "June 12, 2027"
  },
  "location": {
    "city": "New York",
    "venue": "Your Venue Name",
    "address": "123 Main St, New York, NY"
  }
  // ... more fields
}
```

**Save** → Browser auto-refreshes → Changes appear instantly!

### To Add Committee Members

Edit `src/data/committee.json`:
```json
{
  "board": [
    {
      "name": "Dr. Jane Smith",
      "role": "Co-Chair",
      "affiliation": "Pharma Corp Inc.",
      "photoUrl": "https://example.com/photo.jpg",
      "bio": "Dr. Smith has 20 years of experience..."
    }
  ]
  // ... more members
}
```

### To Add/Update Partners

Edit `src/data/partners.json`:
```json
{
  "partners": [
    {
      "name": "Partner Company Name",
      "tier": "platinum",
      "logoUrl": "https://example.com/logo.png",
      "website": "https://example.com"
    }
  ]
}
```

### To Update Form URLs

Search for "TODO:" in page files and replace placeholder URLs:

**Example**: In `src/pages/call-for-presentations.astro`:
```astro
<EmbedForm 
  title="Submit Your Abstract"
  formUrl="TODO: Google Form or Formspree URL"  <!-- REPLACE THIS -->
  embedType="google-form"
/>
```

Replace with your actual form URL:
```astro
<EmbedForm 
  title="Submit Your Abstract"
  formUrl="https://docs.google.com/forms/d/e/YOUR_FORM_ID/viewform"
  embedType="google-form"
/>
```

---

## Step 6: Build for Production

When ready to deploy:

```bash
npm run build
```

This creates:
- **`dist/` folder** with static HTML files ready for deployment
- Optimized CSS, JavaScript, and assets
- Can be deployed to any static hosting

---

## Step 7: Preview Production Build

Test the production build locally:

```bash
npm run preview
```

Visit http://localhost:3000 to preview the built site.

---

## Common Tasks

### Stop Development Server
Press `Ctrl+C` (or `Cmd+C` on Mac) in terminal

### Restart Development Server
```bash
npm run dev
```

### Clear Cache & Reinstall
```bash
rm -rf node_modules package-lock.json
npm install
npm run dev
```

### Search for TODOs
Find all placeholder content that needs updating:
```bash
grep -r "TODO:" src/
```

---

## Project File Structure

```
Website VS Code/
├── src/
│   ├── data/              ← Edit these JSON files for content
│   │   ├── key-dates.json
│   │   ├── committee.json
│   │   ├── sessions.json
│   │   ├── short-courses.json
│   │   ├── events.json
│   │   └── partners.json
│   ├── pages/             ← Website pages (auto-routed)
│   ├── components/        ← Reusable components
│   ├── layouts/           ← BaseLayout (header, footer, nav)
│   └── styles/            ← Global CSS
├── package.json           ← Dependencies & scripts
├── astro.config.mjs       ← Astro configuration
├── tsconfig.json          ← TypeScript config
└── README.md              ← Full documentation
```

---

## Troubleshooting

### Port 3000 Already in Use
```bash
# Kill process on port 3000
lsof -i :3000
kill -9 <PID>

# Or use a different port
npm run dev -- --port 3001
```

### Changes Not Showing
1. **Clear browser cache** (Cmd+Shift+R or Ctrl+Shift+R)
2. **Check terminal** for any error messages
3. **Restart dev server** (Ctrl+C, then `npm run dev`)

### npm not found
- Install Node.js: https://nodejs.org/
- Restart terminal after installation
- Verify: `npm --version`

### Module not found errors
```bash
# Reinstall all dependencies
rm -rf node_modules
npm install
npm run dev
```

---

## Next Steps After Setup

1. ✅ **Development**: Run `npm run dev` and make edits
2. 📝 **Update Content**: Edit JSON files in `src/data/`
3. 🔗 **Add Form URLs**: Replace TODO placeholders with actual form links
4. 📸 **Add Images**: Place logo/partner images in `src/images/`
5. 🧪 **Test Responsive**: Use browser dev tools (F12) to test mobile
6. 🏗️ **Build**: Run `npm run build` when ready
7. 🚀 **Deploy**: Upload `dist/` folder to hosting platform

---

## Deployment Platforms

Once built, the `dist/` folder can be deployed to:

### Free Options
- **Netlify**: Drag & drop `dist/` folder
- **Vercel**: Connect GitHub repo or upload folder
- **GitHub Pages**: Push to gh-pages branch
- **Cloudflare Pages**: Connect repo or upload

### Paid Options
- **AWS S3 + CloudFront**: Scalable, fast CDN
- **Traditional Web Server**: Any hosting with HTTP support

### Manual Deployment
```bash
# Build the site
npm run build

# Upload dist/ folder to your web server
# Example with scp:
scp -r dist/* user@server.com:/var/www/html/
```

---

## Support

For issues or questions:
- 📧 Email: info@pharmads.org
- 📚 Docs: See README.md in project root
- 🔗 Reference: https://docs.astro.build

---

**Happy building! 🎉**
