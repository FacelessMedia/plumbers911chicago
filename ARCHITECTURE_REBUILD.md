# Plumbers 911 Chicago — Site Architecture Rebuild Plan

## Strategy Summary

**Service pages**: Stay at `/chicago-il-plumbing/[service-slug]/` — Chicago geo-branded, targeting the 354K+ query impression volume for Chicago plumbing searches.

**Location pages (Tier 1)**: ~20 cities with proven search demand keep individual pages at their existing URLs. Content will be rewritten to be genuinely unique (local water utility info, municipal codes, neighborhoods, etc.).

**County hub pages (Tier 2)**: ~10 new pages at `/service-area/[county]-county/` that consolidate 230+ thin city pages into substantial, useful content. Each county hub lists every city served in that county with a brief unique paragraph.

**Redirects**: Every removed city page gets a 301 redirect to its county hub. No 404s for previously indexed URLs.

**Arlington Heights combo pages**: Already redirected (existing). No city+service combos.

---

## PHASE 1: DATA PREPARATION & REDIRECT MAP
*Goal: Build all data files needed for the new architecture*

### 1.1 Determine Tier 1 Cities (Keep Individual Pages)
Based on GSC data — cities with clicks OR 5,000+ page impressions OR 3,000+ query impressions:

| # | City | Clicks | Page Imps | Query Imps | County |
|---|------|--------|-----------|------------|--------|
| 1 | Chicago | 11 | 14,974 | 354,539 | Cook |
| 2 | Park Ridge | 18 | 36,775 | 9,296 | Cook |
| 3 | Joliet | 9 | 38,574 | 19,536 | Will |
| 4 | Arlington Heights | 0 | 6 | 21,894 | Cook |
| 5 | Park Forest | 6 | 16,213 | 5,225 | Cook |
| 6 | Cicero | 4 | 11,536 | 3,921 | Cook |
| 7 | Bartlett | 3 | 17,141 | 8,810 | DuPage |
| 8 | Hickory Hills | 3 | 16,594 | 3,835 | Cook |
| 9 | Chicago Heights | 3 | 16,466 | — | Cook |
| 10 | Oak Brook | 3 | 10,503 | 2,731 | DuPage |
| 11 | Elmhurst | 3 | 10,151 | 3,565 | DuPage |
| 12 | Monee | 3 | 9,282 | — | Will |
| 13 | Orland Park | 0 | 17,065 | 7,090 | Cook/Will |
| 14 | Palos Heights | 0 | 15,461 | 3,276 | Cook |
| 15 | Flossmoor | 0 | 9,463 | 4,100 | Cook |
| 16 | Naperville | 0 | 6,140 | 1,728 | DuPage |
| 17 | Matteson | 0 | 6,171 | 3,324 | Cook |
| 18 | Franklin Park | 0 | 8,427 | 3,484 | Cook |
| 19 | Ottawa | 2 | 5,880 | 3,177 | LaSalle |
| 20 | Marengo | 4 | 1,337 | — | McHenry |

### 1.2 Determine County Hub Pages
Create hub pages for each county. Small counties (≤3 cities) get merged into regional hubs:

| # | Hub Page | URL | Cities Covered |
|---|----------|-----|----------------|
| 1 | Cook County | `/service-area/cook-county/` | ~80 cities |
| 2 | DuPage County | `/service-area/dupage-county/` | ~28 cities |
| 3 | Will County | `/service-area/will-county/` | ~22 cities |
| 4 | Lake County | `/service-area/lake-county/` | ~25 cities |
| 5 | Kane County | `/service-area/kane-county/` | ~19 cities |
| 6 | McHenry County | `/service-area/mchenry-county/` | ~17 cities |
| 7 | Kendall County | `/service-area/kendall-county/` | 5 cities |
| 8 | DeKalb County | `/service-area/dekalb-county/` | 10 cities |
| 9 | Grundy County | `/service-area/grundy-county/` | 6 cities |
| 10 | Southwest IL (LaSalle, Bureau, Marshall, Livingston, Lee, Boone) | `/service-area/extended-service-area/` | ~25 cities |

### 1.3 Build Complete Redirect Map
Every removed city page → its county hub:

- [ ] **1.3.1** Generate list of ALL current location page URLs (248 URLs)
- [ ] **1.3.2** Mark which 20 are kept (Tier 1)
- [ ] **1.3.3** Map remaining ~228 city URLs → their county hub URL
- [ ] **1.3.4** Keep existing dead location redirects
- [ ] **1.3.5** Keep existing Arlington Heights combo redirects
- [ ] **1.3.6** Add dead blog post redirects (existing)
- [ ] **1.3.7** Validate: every URL in GSC Pages.csv maps to either a live page or a redirect

### 1.4 Create County Hub Data File
- [ ] **1.4.1** Create `data/county_hubs.json` with:
  - county_name, slug, url_path
  - seo.title, seo.description (unique per county)
  - intro_text (unique paragraph about plumbing services in this county/region)
  - cities[] array with: name, slug, has_tier1_page, brief_description
  - services_highlight (top services relevant to that region)
  - local_info (water utility, permit office, unique regional plumbing challenges)

### 1.5 Enrich Tier 1 Location Data
- [ ] **1.5.1** Create `data/tier1_locations.json` with enriched fields for each of the 20 cities:
  - city_name, slug, county, url_path
  - population (approximate)
  - water_utility (name of water provider)
  - permit_info (building permit requirements)
  - neighborhoods (notable neighborhoods/areas)
  - common_issues (genuine local plumbing challenges — e.g., age of infrastructure, soil type, flood zone)
  - nearby_cities (3-5 nearby served cities)
  - services_available (full list of 28 services)
  - seo.title, seo.description (unique, hand-crafted)
  - intro_paragraph (unique 2-3 sentence intro)
  - local_content (2-3 unique paragraphs about plumbing in this specific city)
  - cta_text (city-specific call to action)

---

## PHASE 2: TEMPLATES
*Goal: Create new templates for county hubs and improved location pages*

### 2.1 County Hub Template (`templates/county_hub.html`)
- [ ] **2.1.1** Hero section with county name, city count, CTA
- [ ] **2.1.2** Breadcrumb: Home > Service Area > [County] County
- [ ] **2.1.3** County intro section with unique regional content
- [ ] **2.1.4** "Common Plumbing Issues in [County]" section
- [ ] **2.1.5** City grid: cards for each city in the county
  - Tier 1 cities: linked card with brief description
  - Other cities: text-only mention with county hub anchor
- [ ] **2.1.6** Services available section linking to `/chicago-il-plumbing/[service]/`
- [ ] **2.1.7** Local info sidebar (water utility, permit office, emergency contacts)
- [ ] **2.1.8** CTA banner at bottom
- [ ] **2.1.9** Nearby county links section
- [ ] **2.1.10** Schema: Service schema with areaServed = county

### 2.2 Improved Location Template (`templates/location.html`)
Rebuild the location template to be modular and data-driven:
- [ ] **2.2.1** Hero: city name, county, trust badges, dual CTA buttons
- [ ] **2.2.2** Breadcrumb: Home > Service Area > [County] County > [City], IL
- [ ] **2.2.3** Trust strip (licensed, 24/7, serving [city])
- [ ] **2.2.4** City intro section: `{{intro_paragraph}}` + `{{local_content}}` (unique per city)
- [ ] **2.2.5** "Why [City] Residents Choose Us" — data-driven, pulls from `{{common_issues}}`
- [ ] **2.2.6** Local info card: water utility, permit info, neighborhoods
- [ ] **2.2.7** Services grid linking to Chicago service pages
- [ ] **2.2.8** Sidebar: CTA + quick quote form + city-specific messaging
- [ ] **2.2.9** Nearby cities section (links to other Tier 1 cities + county hub)
- [ ] **2.2.10** CTA banner at bottom
- [ ] **2.2.11** Schema: Service + areaServed (City), provider (Plumber/LocalBusiness)
- [ ] **2.2.12** BreadcrumbList schema

### 2.3 Update Service Page Template (`templates/service.html`)
- [ ] **2.3.1** Add "Areas We Serve" section at bottom linking to Tier 1 cities + county hubs
- [ ] **2.3.2** Add "service + Chicago" geo signals in content naturally
- [ ] **2.3.3** Ensure schema has serviceArea = Chicago metropolitan area
- [ ] **2.3.4** Add related services internal links section
- [ ] **2.3.5** Ensure BreadcrumbList schema present

### 2.4 Update Service Area Index (`templates/service_area.html`)
- [ ] **2.4.1** Keep interactive county card grid
- [ ] **2.4.2** Each county card now links to its county hub page
- [ ] **2.4.3** Featured cities section highlighting Tier 1 cities
- [ ] **2.4.4** Update stats (counties served, cities served)
- [ ] **2.4.5** Keep A-Z directory but link Tier 1 cities to their pages, others to county hubs
- [ ] **2.4.6** Update schema

---

## PHASE 3: BUILD SYSTEM UPDATES
*Goal: Update build.py to generate the new architecture*

### 3.1 Update build.py — Data Loading
- [ ] **3.1.1** Load `county_hubs.json`
- [ ] **3.1.2** Load `tier1_locations.json`
- [ ] **3.1.3** Remove `DEAD_LOCATION_SLUGS` set (replaced by Tier 1 logic)
- [ ] **3.1.4** Remove `INDEXABLE_LOCATION_SLUGS` set (all Tier 1 pages are indexable)
- [ ] **3.1.5** Define `TIER1_SLUGS` set from tier1_locations.json

### 3.2 Update build.py — Page Generation
- [ ] **3.2.1** Generate county hub pages (10 pages) using county_hub.html template
- [ ] **3.2.2** Generate Tier 1 location pages (20 pages) using improved location.html
- [ ] **3.2.3** STOP generating thin location pages (remove the loop over locations.json for non-Tier1)
- [ ] **3.2.4** Update service page generation to include "Areas We Serve" data
- [ ] **3.2.5** Update service area index page to link to county hubs
- [ ] **3.2.6** Update nearby_locations logic to only reference Tier 1 cities

### 3.3 Update build.py — Redirects
- [ ] **3.3.1** Generate 301 redirects: every removed city URL → county hub
- [ ] **3.3.2** Keep existing Arlington Heights combo redirects
- [ ] **3.3.3** Keep existing dead blog redirects
- [ ] **3.3.4** Update `generate_redirects_json()` with new redirect map
- [ ] **3.3.5** Verify no redirect loops or chains

### 3.4 Update build.py — Sitemap
- [ ] **3.4.1** Add county hub pages to sitemap (priority 0.8)
- [ ] **3.4.2** Tier 1 location pages in sitemap (priority 0.7)
- [ ] **3.4.3** Service pages in sitemap (priority 0.8)
- [ ] **3.4.4** Remove noindexed pages from sitemap
- [ ] **3.4.5** Update robots.txt if needed

---

## PHASE 4: SCHEMA & SEO
*Goal: Proper structured data on every page type*

### 4.1 Location Page Schema (Tier 1)
- [ ] **4.1.1** `@type: Service` with `provider: @type Plumber`
- [ ] **4.1.2** `areaServed: @type City` with name, containedInPlace State
- [ ] **4.1.3** `serviceType: Plumbing`
- [ ] **4.1.4** Provider address, telephone, URL
- [ ] **4.1.5** `BreadcrumbList` schema

### 4.2 County Hub Page Schema
- [ ] **4.2.1** `@type: Service` with `provider: @type Plumber`
- [ ] **4.2.2** `areaServed: @type AdministrativeArea` (county)
- [ ] **4.2.3** `BreadcrumbList` schema

### 4.3 Service Page Schema
- [ ] **4.3.1** `@type: Service` with specific serviceType
- [ ] **4.3.2** `areaServed: @type City` (Chicago) + `@type State` (Illinois)
- [ ] **4.3.3** Provider with full LocalBusiness details
- [ ] **4.3.4** `BreadcrumbList` schema
- [ ] **4.3.5** `offers` with priceRange if applicable

### 4.4 Homepage Schema
- [ ] **4.4.1** `@type: Plumber` (LocalBusiness) — already exists, verify complete
- [ ] **4.4.2** `areaServed` array with all counties
- [ ] **4.4.3** `hasOfferCatalog` linking to services

### 4.5 Meta Tags
- [ ] **4.5.1** Unique `<title>` for every page (verify no duplicates)
- [ ] **4.5.2** Unique `<meta description>` for every page
- [ ] **4.5.3** Proper `<link rel="canonical">` on every page
- [ ] **4.5.4** `robots` meta: index,follow on all live pages; noindex on 404
- [ ] **4.5.5** Open Graph tags on all pages

---

## PHASE 5: INTERNAL LINKING
*Goal: Create a strong internal link web between all page types*

### 5.1 Service Pages → Location Pages
- [ ] **5.1.1** Each service page has "Areas We Serve" section with links to Tier 1 cities
- [ ] **5.1.2** Each service page links to county hub pages

### 5.2 Location Pages → Service Pages
- [ ] **5.2.1** Each Tier 1 location page has services grid linking to all 28 service pages
- [ ] **5.2.2** Service links use descriptive anchor text (not just "Learn More")

### 5.3 County Hubs → Everything
- [ ] **5.3.1** County hubs link to Tier 1 city pages within that county
- [ ] **5.3.2** County hubs link to service pages
- [ ] **5.3.3** County hubs link to neighboring county hubs
- [ ] **5.3.4** County hubs link back to service area index

### 5.4 Service Area Index → Hubs
- [ ] **5.4.1** Service area index links to all county hubs
- [ ] **5.4.2** Service area index features Tier 1 cities with direct links
- [ ] **5.4.3** A-Z directory: Tier 1 cities link to their pages, others link to county hubs

### 5.5 Blog → Service/Location Pages
- [ ] **5.5.1** Blog posts link to relevant service pages
- [ ] **5.5.2** Blog posts link to relevant location pages where appropriate

### 5.6 Navigation
- [ ] **5.6.1** Header nav: Home, Services (dropdown), Service Area, About, Contact, Blog
- [ ] **5.6.2** Footer: links to all county hubs + top services
- [ ] **5.6.3** Breadcrumbs on every page

---

## PHASE 6: CSS & DESIGN
*Goal: Ensure new page types look professional and consistent*

### 6.1 County Hub Styles
- [ ] **6.1.1** County hub hero styling
- [ ] **6.1.2** City card grid (responsive)
- [ ] **6.1.3** Local info sidebar styling
- [ ] **6.1.4** Nearby counties section styling

### 6.2 Improved Location Page Styles
- [ ] **6.2.1** Local info card styling
- [ ] **6.2.2** Neighborhoods section styling
- [ ] **6.2.3** Ensure consistent with existing design system

---

## PHASE 7: BUILD, TEST, DEPLOY
*Goal: Build everything, verify, deploy live*

### 7.1 Build & Local Verification
- [ ] **7.1.1** Run `python build.py` — verify no errors
- [ ] **7.1.2** Verify page counts: ~20 Tier 1 locations + 10 county hubs + 28 services + blog + misc = ~80 pages
- [ ] **7.1.3** Verify 0 duplicate titles
- [ ] **7.1.4** Verify 0 broken internal links
- [ ] **7.1.5** Verify all 228 removed city URLs have redirects
- [ ] **7.1.6** Verify sitemap only contains indexable pages
- [ ] **7.1.7** Verify schema is valid JSON-LD on all page types
- [ ] **7.1.8** Spot-check 5 county hub pages visually
- [ ] **7.1.9** Spot-check 5 Tier 1 location pages visually
- [ ] **7.1.10** Verify redirect count matches expected

### 7.2 Deploy
- [ ] **7.2.1** Git add, commit with descriptive message
- [ ] **7.2.2** Push to main branch
- [ ] **7.2.3** Deploy to Vercel via CLI
- [ ] **7.2.4** Verify live URL loads correctly
- [ ] **7.2.5** Test 5 redirects manually (old city URLs → county hubs)
- [ ] **7.2.6** Test homepage, service area, a service page, a location page, a county hub

### 7.3 Post-Deploy SEO
- [ ] **7.3.1** Submit updated sitemap to Google Search Console
- [ ] **7.3.2** Request indexing of new county hub pages
- [ ] **7.3.3** Monitor for crawl errors over next 7 days
- [ ] **7.3.4** Verify no 404s in Search Console

---

## SUMMARY: Page Count Before vs After

| Page Type | Before | After |
|-----------|--------|-------|
| Homepage | 1 | 1 |
| Service pages (Chicago) | 28 | 28 |
| Service category hubs | 5 | 5 |
| Location pages (thin) | 188 (+ 60 noindexed) | 0 |
| Tier 1 location pages | 0 | 20 |
| County hub pages | 0 | 10 |
| Blog posts | ~14 | ~14 |
| Other (about, contact, legal, service area) | ~6 | ~6 |
| **Total indexable pages** | **~120** | **~84** |
| **Total redirects** | **~78** | **~300+** |
| **Thin/doorway pages** | **~188** | **0** |
