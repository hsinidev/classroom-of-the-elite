# Classroom of the Elite Online

> **Vibe Focus:** Strategic Academic / Cyber-Terminal Aesthetic  
> **Tech Stack:** Static HTML/JS + Tailwind CSS 4.0 + Python Generators

Welcome to the **Classroom of the Elite Online** web portal. This is a high-performance, immersive manga reader site designed specifically for fans of the series. The project leverages modern web optimization techniques to deliver a fast, localized, and beautiful experience.

---

## 🌟 Key Features

- Academic-terminal layout with CSS crt-scanline overlays.
- Immersive dark-mode reader view with smooth progress tracking.
- Complete SEO localization for US, FR, and JP markets.
- Automated Rich Snippet schemas (ComicSeries structured data) for SEO.

---

## 🛠️ Getting Started

### 📋 Prerequisites
- **For Web Server:** Python 3.10+ (to serve static files or run generators) or Node.js 18+ (if package dependencies are needed).
- **GitHub CLI (`gh`)**: Recommended for pushing updates.

### 🔑 API Key Configuration
This project includes automated content generation and SEO optimization scripts that use the **Zhipu AI / BigModel API**. 

To utilize these scripts:
1. Copy the `.env.example` file to create a `.env` file:
   ```bash
   cp .env.example .env
   ```
2. Open `.env` and fill in your API key:
   ```env
   BIGMODEL_API_KEY=your_actual_api_key_here
   ```
   *Note: If you have multiple keys, you can specify them as a comma-separated list.*

---

## 🚀 Local Development

Start a local static server:
```bash
python -m http.server 8000
```

Then open your browser and navigate to the local server URL (usually `http://localhost:8000` or `http://localhost:5173`).

---

## 🤖 Content Generation & Automation
The project is equipped with local AI-powered generation scripts to build and update the site content dynamically.

You can run these scripts to regenerate and optimize the portal content:

- **`python generate_legal_pages.py`**: Generates Privacy, DMCA, Cookies, and Terms pages via AI.
- **`python generate_seo_article.py`**: Synthesizes the primary SEO text for the landing page.
- **`python generate_all_chapter_articles.py`**: Compiles chapter analysis and review summaries.


---

## 📦 Production Deployment

This is a static site. Deploy the root files directly to Netlify, Vercel, or Nginx.

- **Ignored Assets:** Large `manga/` chapter image directories and local archives are excluded from this repository (configured in `.gitignore`) for performance and size constraints. Ensure image files are uploaded directly to your hosting server's path structure.
- **SEO Ready:** Sitemap (`sitemap.xml`) and `.htaccess` file rules are fully configured to rewrite paths and provide Google-friendly crawler access.
