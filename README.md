# Plumbers 911 Chicago — Rebuilt Site Data & Templates

## Overview
This directory contains all published content extracted from the WordPress WXR export (`plumbers911chicago.WordPress.2026-02-23.xml`), organized as JSON data files and HTML templates. All 2,577 draft items have been discarded.

---

## Directory Structure

```
site/
├── data/                        # JSON data files
│   ├── site_meta.json           # Site name, URL, phone, language
│   ├── navigation.json          # Resolved nav menu tree (6 top-level items)
│   ├── categories.json          # 12 blog categories
│   ├── tags.json                # 59 tags
│   ├── attachments.json         # 25 media attachment records
│   ├── image_urls.json          # 31 unique image URLs to download
│   │
│   ├── blog_posts.json          # 9 published blog posts
│   │
│   ├── services.json            # 57 service pages (full content)
│   ├── service_index.json       # Service listing (name, slug, url — no content)
│   │
│   ├── locations.json           # 248 city/location pages (full content)
│   ├── location_index.json      # Location listing (city, slug, url — no content)
│   │
│   ├── pages_home.json          # 1 home page
│   ├── pages_about.json         # 1 about page
│   ├── pages_contact.json       # 1 contact page
│   ├── pages_legal.json         # 1 privacy policy page
│   ├── pages_service_area.json  # 1 service area page
│   └── pages_page.json          # 6 nav category landing pages
│
├── templates/                   # HTML templates (Handlebars/Mustache-style placeholders)
│   ├── _base.html               # Base layout: header, nav, footer
│   ├── home.html                # Homepage
│   ├── service.html             # Individual service page
│   ├── location.html            # City/location page
│   ├── blog_post.html           # Single blog post
│   ├── blog_index.html          # Blog listing page
│   ├── about.html               # About page
│   ├── contact.html             # Contact page
│   ├── legal.html               # Privacy policy / terms
│   ├── service_area.html        # Service area directory with search
│   └── page.html                # Generic page (nav landing pages)
│
└── README.md                    # This file
```

---

## Content Summary

| Type             | Count | Data File              | Template          |
|------------------|-------|------------------------|-------------------|
| Blog posts       | 9     | `blog_posts.json`      | `blog_post.html`  |
| Service pages    | 57    | `services.json`        | `service.html`    |
| Location pages   | 248   | `locations.json`       | `location.html`   |
| Home             | 1     | `pages_home.json`      | `home.html`       |
| About            | 1     | `pages_about.json`     | `about.html`      |
| Contact          | 1     | `pages_contact.json`   | `contact.html`    |
| Legal            | 1     | `pages_legal.json`     | `legal.html`      |
| Service Area     | 1     | `pages_service_area.json` | `service_area.html` |
| Generic pages    | 6     | `pages_page.json`      | `page.html`       |
| **Total**        | **325** |                      |                   |

---

## JSON Data Shape

### Blog Post
```json
{
  "id": "123",
  "title": "Post Title",
  "slug": "post-slug",
  "url_path": "/post-slug/",
  "date": "2024-02-28 15:30:21",
  "modified": "2024-02-28 15:30:21",
  "author": "ryan@faceless.media",
  "content": "<p>Clean HTML content...</p>",
  "excerpt": "",
  "seo": {
    "title": "SEO Title",
    "description": "Meta description"
  },
  "images": ["https://..."],
  "categories": [{"slug": "blog", "name": "Blog"}],
  "tags": [{"slug": "drain", "name": "drain"}],
  "featured_image_id": "456"
}
```

### Service Page
```json
{
  "id": "789",
  "title": "Emergency Plumber",
  "slug": "emergency-plumber",
  "service_slug": "emergency-plumber",
  "service_name": "Emergency Plumber",
  "url_path": "/chicago-il-plumbing/emergency-plumber/",
  "content": "<p>Clean HTML...</p>",
  "seo": { ... }
}
```

### Location Page
```json
{
  "id": "101",
  "title": "Chicago",
  "slug": "chicago-il-plumbing",
  "city_slug": "chicago",
  "city_name": "Chicago",
  "state": "IL",
  "url_path": "/chicago-il-plumbing/",
  "content": "<p>Clean HTML...</p>",
  "seo": { ... }
}
```

---

## Template Placeholder Syntax

Templates use Handlebars-compatible `{{variable}}` syntax:

- `{{variable}}` — escaped text output
- `{{{variable}}}` — raw HTML output (for content fields)
- `{{#each items}}...{{/each}}` — iteration
- `{{#if condition}}...{{/if}}` — conditionals
- `{{> partial}}` — partial/include

These work with Handlebars, Mustache, Eleventy, or can be adapted to Jinja2, Nunjucks, Go templates, etc.

---

## Images

`image_urls.json` contains 31 image URLs hosted on `plumbers911chicago.com`. These should be downloaded and saved locally before the original site goes offline. A download script can be generated on request.

---

## Next Steps

1. **Choose a framework** — Static site generator (Eleventy, Astro, Hugo) or full framework (Next.js, SvelteKit)
2. **Design the UI** — All templates are unstyled; add CSS/design system
3. **Download images** — Scrape the 31 image URLs from the live site
4. **Wire up the form** — The contact form needs a backend (Netlify Forms, Formspree, custom API)
5. **Set up routing** — Map JSON data to URL paths using your framework's routing
6. **Deploy** — Netlify, Vercel, Cloudflare Pages, etc.
