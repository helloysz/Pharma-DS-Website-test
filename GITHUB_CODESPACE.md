# 🚀 GitHub Codespace Setup Guide

Run PharmaDS 2027 website in the cloud with **GitHub Codespaces** - no local installation needed!

## What is GitHub Codespace?

- **Cloud-based VS Code** - your browser
- **Full development environment** - pre-configured with Node.js
- **Automatic setup** - dependencies install automatically
- **Free tier** - 120 core-hours/month free (more than enough!)
- **Instant access** - code, edit, deploy from anywhere

---

## 📋 Prerequisites

1. **GitHub account** (free at https://github.com)
2. **Project pushed to GitHub** (see Step 1 below)

---

## Step 1: Push Project to GitHub

First, you need to push this project to a GitHub repository.

### Option A: Create NEW Repository on GitHub

1. Go to **https://github.com/new**
2. **Repository name**: `pharmads-2027-website`
3. **Description**: "PharmaDS 2027 Conference Website - Astro Static Site"
4. **Public** or **Private** (your choice)
5. Click **Create repository**

You'll see commands like:
```bash
git remote add origin https://github.com/YOUR_USERNAME/pharmads-2027-website.git
git branch -M main
git push -u origin main
```

Copy these commands and run them in your terminal.

### Option B: Push from Terminal (Mac/Linux)

```bash
# Navigate to project
cd "/Users/E0443159/Library/CloudStorage/OneDrive-Sanofi/Documents/Non-project/Pharma DS/2027/Website VS Code"

# Add remote (replace YOUR_USERNAME with your GitHub username)
git remote add origin https://github.com/YOUR_USERNAME/pharmads-2027-website.git

# Set main branch
git branch -M main

# Push to GitHub
git push -u origin main
```

**Expected output:**
```
Enumerating objects: 30, done.
Counting objects: 100% (30/30), done.
...
To https://github.com/YOUR_USERNAME/pharmads-2027-website.git
 * [new branch]      main -> main
Branch 'main' set up to track remote branch 'main' from 'origin'.
```

✅ **Project is now on GitHub!**

---

## Step 2: Create a GitHub Codespace

### Option A: From GitHub Web

1. Go to your repository: `https://github.com/YOUR_USERNAME/pharmads-2027-website`
2. Click the **<> Code** button (green button)
3. Click **Codespaces** tab
4. Click **Create codespace on main**

**Wait 1-2 minutes** for setup...

✅ VS Code opens in your browser automatically!

### Option B: From Command Palette (Quick)

1. Ensure you're on the GitHub repository page
2. Press `.` (period) on your keyboard
3. VS Code opens in your browser instantly (instant editor mode)
4. From menu: `Codespaces > Create codespace`

---

## Step 3: Start Development

Once Codespace opens in your browser:

### 1. Open Terminal
- Menu: `Terminal > New Terminal`
- Or: `` Ctrl+` `` (backtick)

### 2. Install & Run
```bash
npm install
npm run dev
```

**Expected output:**
```
  ➜  Local:     http://localhost:3000/
  ➜  press h to show help
```

### 3. Preview Your Site

You should see a notification: **"Your application running on port 3000 is available"**

Click **Open in Browser** (or visit the forwarded URL)

✅ **Your website is live!**

---

## Step 4: Edit Content

Edit files in Codespace just like your local editor:

- **Conference details**: `src/data/key-dates.json`
- **Committee**: `src/data/committee.json`
- **Partners**: `src/data/partners.json`
- **Events**: `src/data/events.json`
- **Courses**: `src/data/short-courses.json`
- **Sessions**: `src/data/sessions.json`

**Save** → **Browser auto-refreshes** ✨

---

## Step 5: Commit Changes

Push your changes back to GitHub:

```bash
# Stage all changes
git add .

# Commit
git commit -m "Update conference details and committee members"

# Push to GitHub
git push
```

---

## 💡 Codespace Tips

### Accessing Your Codespace Later

1. Go to **https://github.com/codespaces**
2. Find your codespace in the list
3. Click to open it

### Stopping Your Codespace

- Menu: `Codespaces > Stop Current Codespace`
- Stops billing of compute hours (storage still costs minimal)

### Deleting Your Codespace

- Menu: `Codespaces > Delete Codespace`
- Or on https://github.com/codespaces

### Customizing Codespace

- Pre-installed: Node.js 18+, npm, git
- VS Code extensions auto-installed (Astro, Prettier, TailwindCSS)
- Settings configured in `.devcontainer/devcontainer.json`

---

## 🏗️ Building for Deployment

When ready to deploy:

```bash
npm run build
```

Creates `dist/` folder with static HTML files ready to deploy.

### Deploy to Netlify (Free)

1. Download `dist/` folder locally
2. Go to **https://netlify.com**
3. Click **Drop files here**
4. Drag & drop `dist/` folder
5. Your site is live! 🚀

### Deploy from Codespace

```bash
# Export dist folder
# Go to Netlify > New site > Deploy manually
# Upload dist/ folder
```

---

## 📊 Codespace Pricing (Free Tier)

- **Storage**: 15 GB free per account
- **Compute**: 120 core-hours/month free
- **Typical usage**: ~2 hours/day = plenty for free tier
- **Pro**: $4/month for additional hours if needed

[Learn more](https://docs.github.com/en/billing/managing-github-codespaces-billing)

---

## 🆘 Troubleshooting

### Codespace won't start
- Wait 2 minutes (initial setup can be slow)
- Check browser console (F12)
- Delete Codespace & create a new one

### Port 3000 not accessible
- Wait a few seconds after `npm run dev`
- Hard refresh browser: Ctrl+Shift+R
- Check terminal for errors

### npm install fails
- Delete `node_modules` folder: `rm -rf node_modules`
- Try again: `npm install`

### Changes not showing
- Hard refresh: Ctrl+Shift+R or Cmd+Shift+R
- Check terminal for build errors
- Restart: Ctrl+C, then `npm run dev`

---

## 📚 Resources

- [GitHub Codespaces Docs](https://docs.github.com/en/codespaces)
- [Astro Documentation](https://docs.astro.build)
- [VS Code in Browser Tips](https://code.visualstudio.com/docs/editor/vscode-web)

---

## ✅ You're Ready!

1. ✅ Push project to GitHub
2. ✅ Create Codespace
3. ✅ `npm install && npm run dev`
4. ✅ Start editing!

**Next**: Go to https://github.com/new and create your repository!

---

**Happy coding! 🎉**
