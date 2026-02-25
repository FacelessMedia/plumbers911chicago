"""
Static site builder for Plumbers 911 Chicago.
Reads JSON data files and generates static HTML pages in /dist.
"""
import json
import os
import re
import shutil
import time

SITE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(SITE_DIR, "data")
TEMPLATE_DIR = os.path.join(SITE_DIR, "templates")
DIST_DIR = os.path.join(SITE_DIR, "dist")
ASSETS_SRC = os.path.join(SITE_DIR, "assets")
ASSETS_DIST = os.path.join(DIST_DIR, "assets")


def load_json(filename):
    path = os.path.join(DATA_DIR, filename)
    if not os.path.exists(path):
        return []
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def load_template(name):
    path = os.path.join(TEMPLATE_DIR, name)
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def find_block_end(text, start_after_open):
    """Find the matching {{/each}} or {{/if}} for a block, handling nesting.
    start_after_open is the position right after the opening tag."""
    # Detect which block type we're in by scanning backwards
    depth = 1
    pos = start_after_open
    while pos < len(text):
        next_open_each = text.find("{{#each ", pos)
        next_open_if = text.find("{{#if ", pos)
        next_close_each = text.find("{{/each}}", pos)
        next_close_if = text.find("{{/if}}", pos)

        # Find earliest close
        closes = []
        if next_close_each != -1: closes.append(("each", next_close_each))
        if next_close_if != -1: closes.append(("if", next_close_if))
        if not closes:
            return -1
        closes.sort(key=lambda x: x[1])

        # Find earliest open
        opens = []
        if next_open_each != -1: opens.append(("each", next_open_each))
        if next_open_if != -1: opens.append(("if", next_open_if))
        opens.sort(key=lambda x: x[1])

        earliest_close = closes[0]
        if opens and opens[0][1] < earliest_close[1]:
            # An open tag comes before the next close tag — increase depth
            depth += 1
            pos = opens[0][1] + 3  # skip past {{#
        else:
            depth -= 1
            if depth == 0:
                return earliest_close[1]
            pos = earliest_close[1] + 3  # skip past {{/
    return -1


def render(template_str, ctx):
    """Template renderer: {{var}}, {{{html}}}, {{#each}}, {{#if}}/{{else}}.
    Processes #each OUTSIDE-IN so nested loops get parent context.
    Processes #if INSIDE-OUT so conditions resolve correctly."""
    output = template_str

    # Handle {{{raw_html}}} (triple braces = unescaped)
    def replace_raw(m):
        key = m.group(1).strip()
        return str(resolve_var(key, ctx))
    output = re.sub(r"\{\{\{(.+?)\}\}\}", replace_raw, output)

    # --- Process {{#each}} blocks OUTSIDE-IN ---
    # Find the FIRST (outermost) {{#each ...}} and its matching {{/each}}
    safety = 0
    while safety < 30:
        safety += 1
        m = re.search(r"\{\{#each\s+(\S+?)\}\}", output)
        if not m:
            break
        var_name = m.group(1).strip()
        body_start = m.end()
        block_end = find_block_end(output, body_start)
        if block_end == -1:
            break  # malformed template
        body = output[body_start:block_end]
        close_end = block_end + len("{{/each}}")

        items = resolve_var(var_name, ctx)
        if not items or not isinstance(items, list):
            replacement = ""
        else:
            parts = []
            for item in items:
                child_ctx = {**ctx}
                if isinstance(item, dict):
                    child_ctx.update(item)
                for k, v in ctx.items():
                    child_ctx["../" + k] = v
                parts.append(render(body, child_ctx))
            replacement = "".join(parts)
        output = output[:m.start()] + replacement + output[close_end:]

    # --- Process {{#if}} blocks INSIDE-OUT ---
    safety = 0
    while safety < 30:
        safety += 1
        if_match = re.search(
            r"\{\{#if\s+(.+?)\}\}((?:(?!\{\{#if\b).)*?)\{\{/if\}\}",
            output, re.DOTALL
        )
        if not if_match:
            break
        var_name = if_match.group(1).strip()
        inner = if_match.group(2)
        val = resolve_var(var_name, ctx)
        else_parts = re.split(r"\{\{else\}\}", inner, maxsplit=1)
        true_body = else_parts[0]
        false_body = else_parts[1] if len(else_parts) > 1 else ""
        truthy = val and val != "0" and val != "false" and val != [] and val != ""
        if truthy:
            replacement = render(true_body, ctx)
        else:
            replacement = render(false_body, ctx)
        output = output[:if_match.start()] + replacement + output[if_match.end():]

    # Handle {{variable}}
    def replace_var(m):
        key = m.group(1).strip()
        val = resolve_var(key, ctx)
        if val is None or val == "":
            return ""
        if isinstance(val, (list, dict)):
            return ""
        return escape_html(str(val))
    output = re.sub(r"\{\{([^#/!>].*?)\}\}", replace_var, output)

    # Handle {{> content}} partial includes
    output = re.sub(r"\{\{>\s*\w+\s*\}\}", "", output)

    # Clean up any remaining unrendered block tags
    output = re.sub(r"\{\{/(?:if|each|unless)\}\}", "", output)

    return output


def resolve_var(key, ctx):
    """Resolve dotted variable paths like seo.title"""
    parts = key.split(".")
    val = ctx
    for p in parts:
        if isinstance(val, dict):
            val = val.get(p, "")
        else:
            return ""
    return val


def escape_html(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;")


def write_page(url_path, html):
    """Write HTML to dist directory, creating index.html files for clean URLs."""
    url_path = url_path.strip("/")
    if not url_path:
        out_path = os.path.join(DIST_DIR, "index.html")
    else:
        out_dir = os.path.join(DIST_DIR, url_path)
        os.makedirs(out_dir, exist_ok=True)
        out_path = os.path.join(out_dir, "index.html")

    with open(out_path, "w", encoding="utf-8") as f:
        f.write(html)


def normalize_urls(html):
    """Convert absolute plumbers911chicago.com URLs to relative paths in body only.
    Preserves absolute URLs in <head> (canonical, OG tags, schema)."""
    # Clean Rank Math SEO variables that weren't resolved
    html = html.replace(" %sep% %sitename%", "")
    html = html.replace("%sep%", "-")
    html = html.replace("%sitename%", "Plumbers 911 Chicago")

    # Split at </head> to preserve head URLs but normalize body links
    parts = html.split("</head>", 1)
    if len(parts) == 2:
        body = re.sub(
            r'href="https://plumbers911chicago\.com/',
            r'href="/',
            parts[1]
        )
        # Also convert src= attributes pointing to old WP domain
        body = re.sub(
            r'src="https://plumbers911chicago\.com/',
            r'src="/',
            body
        )
        # Strip old WP form actions and hidden input values
        body = body.replace('action="/wp-admin/admin-ajax.php"', 'action="/api/contact"')
        body = re.sub(r'value="https?://plumbers911chicago\.com/wp-admin/[^"]*"', 'value=""', body)
        # Remove entire old WP contact forms (they won't work on static site)
        body = re.sub(
            r'<div[^>]*class="[^"]*wpcf7[^"]*"[^>]*>.*?</div>\s*</div>',
            '<div class="sidebar-cta-form"><p>Call <a href="tel:8337586911" class="phone-number">833-758-6911</a> for immediate assistance or <a href="/contact-us/">use our contact form</a>.</p></div>',
            body,
            flags=re.DOTALL
        )
        # Remove WPForms embedded forms — entire <form> block containing wpforms
        body = re.sub(
            r'<form[^>]*id="wpforms-form-\d+"[^>]*>.*?</form>',
            '',
            body,
            flags=re.DOTALL
        )
        # Also catch "Please enable JavaScript" text that precedes the form
        body = re.sub(
            r'Please enable JavaScript in your browser to complete this form\.',
            '',
            body
        )
        # Remove WPForms inline styles block
        body = re.sub(
            r'<style[^>]*id="wpforms-lead-forms-inline-styles"[^>]*>.*?</style>',
            '',
            body,
            flags=re.DOTALL
        )
        # Remove any remaining wpforms noscript/container divs
        body = re.sub(
            r'<div[^>]*class="[^"]*wpforms[^"]*"[^>]*>.*?</div>',
            '',
            body,
            flags=re.DOTALL
        )
        # Remove wpforms spinner images
        body = re.sub(r'<img[^>]*wpforms[^>]*/?>', '', body)
        # Remove orphaned "Schedule Your Plumbing Service Appointment" headings left from form removal
        body = re.sub(
            r'\s*Schedule Your Plumbing Service Appointment\s*',
            '',
            body
        )
        html = parts[0] + "</head>" + body
    return html


def ensure_seo(ctx):
    """Ensure ctx has seo.title and seo.description, falling back to page title."""
    seo = ctx.get("seo", {})
    if isinstance(seo, dict):
        if not seo.get("title"):
            # Try service_name, city_name, or title
            name = ctx.get("service_name") or ctx.get("city_name") or ctx.get("title") or ""
            if name:
                page_type = ctx.get("page_type", "")
                if page_type == "service":
                    seo["title"] = name + " Services Chicago"
                elif page_type == "location":
                    seo["title"] = "Plumber " + name + ", IL"
                else:
                    seo["title"] = name
            else:
                seo["title"] = "Plumbers 911 Chicago"
        if not seo.get("description"):
            name = ctx.get("service_name") or ctx.get("city_name") or ctx.get("title") or ""
            page_type = ctx.get("page_type", "")
            if page_type == "service":
                seo["description"] = "Professional " + name.lower() + " services in Chicago. Licensed, insured plumbers available 24/7. Call 833-758-6911."
            elif page_type == "location":
                seo["description"] = "Licensed plumber in " + name + ", IL. 24/7 emergency service, free estimates. Call 833-758-6911."
            else:
                seo["description"] = "Licensed plumbing services in Chicago and surrounding areas. Call 833-758-6911."
    ctx["seo"] = seo
    return ctx


def build_page(base_tpl, content_tpl_str, ctx):
    """Render content template, inject into base layout."""
    ctx = ensure_seo(ctx)
    content_html = render(content_tpl_str, ctx)
    full_ctx = {**ctx, "content_block": content_html}
    # Replace the {{> content}} partial in base with the rendered content
    page_html = base_tpl.replace("{{> content}}", content_html)
    page_html = render(page_html, full_ctx)
    page_html = normalize_urls(page_html)
    page_html = fix_broken_links(page_html)
    page_html = minify_html(page_html)
    return page_html


# ================================================================
# ARCHITECTURE REBUILD — Tier 1 cities get individual pages
# All other city URLs redirect to their county hub page
# ================================================================

TIER1_SLUGS = {
    "chicago", "park-ridge", "joliet", "arlington-heights", "park-forest",
    "cicero", "bartlett", "hickory-hills", "chicago-heights", "oak-brook",
    "elmhurst", "monee", "orland-park", "palos-heights", "flossmoor",
    "naperville", "matteson", "franklin-park", "ottawa", "marengo",
}

# Map every city slug to its county hub slug for redirects
CITY_TO_COUNTY_HUB = {}

def _build_city_county_map():
    """Build city-slug → county-hub-slug mapping from county_hubs.json."""
    hubs = load_json("county_hubs.json")
    for hub in hubs:
        hub_slug = hub["slug"]
        for city in hub.get("cities", []):
            CITY_TO_COUNTY_HUB[city["slug"]] = hub_slug

DEAD_BLOG_SLUGS = {
    "can-drain-cleaner-damage-pipes",
    "what-can-you-put-in-your-garbage-disposal",
    "how-does-a-gas-tankless-water-heater-work",
    "what-can-i-use-at-home-to-unclog-a-drain",
    "why-wont-my-sump-pump-stop-running",
    "what-causes-bathroom-sink-to-clog",
    "do-water-heater-blankets-work",
    "plumbing-fixture-lifespan-guide",
}


DEAD_SERVICE_SLUGS = {
    "residential-plumbing-coupon",
}


def is_arlington_service_page(url_path):
    """Check if this is an Arlington Heights service sub-page (not the main city page)."""
    return "/arlington-heights-il-plumbing/" in url_path and url_path.strip("/") != "arlington-heights-il-plumbing"


def get_county_hub_slug(city_slug):
    """Get the county hub slug for a city, or 'cook-county' as fallback."""
    return CITY_TO_COUNTY_HUB.get(city_slug, "cook-county")


def generate_redirects_json(all_location_slugs):
    """Generate Vercel-compatible redirects config.
    all_location_slugs: set of ALL city slugs from location_index (248 cities)."""
    redirects = []

    # Non-Tier1 location pages → their county hub
    removed_count = 0
    for slug in sorted(all_location_slugs):
        if slug in TIER1_SLUGS:
            continue  # Tier 1 cities keep their pages
        county_hub = get_county_hub_slug(slug)
        redirects.append({
            "source": "/" + slug + "-il-plumbing/",
            "destination": "/service-area/" + county_hub + "/",
            "permanent": True,
        })
        # Also catch without trailing slash
        redirects.append({
            "source": "/" + slug + "-il-plumbing",
            "destination": "/service-area/" + county_hub + "/",
            "permanent": True,
        })
        removed_count += 1

    # Arlington Heights service sub-pages → main city page
    redirects.append({
        "source": "/arlington-heights-il-plumbing/:service((?!index\\.html$).+)",
        "destination": "/arlington-heights-il-plumbing/",
        "permanent": True,
    })

    # Chicago service sub-pages that were at /chicago-il-plumbing/SERVICE → keep (these are service pages)
    # No redirect needed — they are still built

    # Dead blog posts → /blog/
    for slug in DEAD_BLOG_SLUGS:
        redirects.append({
            "source": "/" + slug + "/",
            "destination": "/blog/",
            "permanent": True,
        })
        redirects.append({
            "source": "/blog/" + slug + "/",
            "destination": "/blog/",
            "permanent": True,
        })

    # request-a-call-back → contact
    redirects.append({
        "source": "/request-a-call-back/",
        "destination": "/contact-us/",
        "permanent": True,
    })

    print("  Redirect map: " + str(removed_count) + " city pages → county hubs")
    return redirects


def generate_404_page(base_tpl, global_ctx):
    """Generate a custom 404 page."""
    content = """
<section class="page-hero">
  <div class="container" style="text-align:center; padding: 4rem 0;">
    <h1>Page Not Found</h1>
    <p style="color:rgba(255,255,255,.8); font-size:1.1rem; margin: 1rem 0 2rem;">
      Sorry, the page you're looking for doesn't exist or has been moved.
    </p>
    <div style="display:flex; gap:1rem; justify-content:center; flex-wrap:wrap;">
      <a href="/" class="btn btn-primary">Go to Homepage</a>
      <a href="/service-area/" class="btn btn-cta-outline" style="color:#fff; border-color:rgba(255,255,255,.4);">View Service Area</a>
      <a href="tel:8337586911" class="btn btn-cta-outline" style="color:#fff; border-color:rgba(255,255,255,.4);">Call 833-758-6911</a>
    </div>
  </div>
</section>
"""
    ctx = {**global_ctx, "page_type": "404",
           "canonical_path": "/404.html",
           "breadcrumb_schema": "",
           "robots_meta": "noindex, nofollow",
           "seo": {"title": "Page Not Found", "description": "The page you're looking for doesn't exist."}}
    page_html = base_tpl.replace("{{> content}}", content)
    page_html = render(page_html, ctx)
    page_html = normalize_urls(page_html)
    page_html = fix_broken_links(page_html)
    return page_html


def make_breadcrumb_schema(crumbs):
    """Generate BreadcrumbList JSON-LD from list of (name, url) tuples."""
    items = []
    for i, (name, url) in enumerate(crumbs, 1):
        items.append({
            "@type": "ListItem",
            "position": i,
            "name": name,
            "item": "https://plumbers911chicago.com" + url if not url.startswith("http") else url,
        })
    schema = {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": items,
    }
    return json.dumps(schema)


def make_canonical(url_path):
    """Create canonical path with trailing slash."""
    p = url_path.strip("/")
    return "/" + p + "/" if p else "/"


def generate_xml_sitemap(built_pages):
    """Generate XML sitemap from list of built URL paths."""
    lines = ['<?xml version="1.0" encoding="UTF-8"?>']
    lines.append('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">')
    for path in sorted(built_pages):
        url = "https://plumbers911chicago.com" + path
        if not url.endswith("/"):
            url += "/"
        priority = "1.0" if path == "/" else "0.8" if "/chicago-il-plumbing/" in path else "0.6"
        lines.append("  <url>")
        lines.append("    <loc>" + url + "</loc>")
        lines.append("    <changefreq>monthly</changefreq>")
        lines.append("    <priority>" + priority + "</priority>")
        lines.append("  </url>")
    lines.append("</urlset>")
    return "\n".join(lines)


def minify_html(html):
    """Lightweight HTML minification: strip comments, collapse whitespace."""
    html = re.sub(r'<!--(?!\[if).*?-->', '', html, flags=re.DOTALL)
    html = re.sub(r'\n\s*\n+', '\n', html)
    html = re.sub(r'>\s{2,}<', '> <', html)
    # Add loading="lazy" to images missing it (Item 90)
    html = re.sub(r'<img(?!.*?loading=)', '<img loading="lazy"', html)
    return html.strip()


def fix_broken_links(html):
    """Post-process HTML to fix known broken internal links."""
    # 1. /contact/ → /contact-us/
    html = html.replace('href="/contact/"', 'href="/contact-us/"')
    html = html.replace('href="/contact"', 'href="/contact-us/"')

    # 2. /category/* → /blog/
    html = re.sub(r'href="/category/[^"]*"', 'href="/blog/"', html)

    # 3. Non-Tier1 location links → redirect to county hub (strip <a>, keep text)
    # This catches any hardcoded links to removed city pages in content
    for slug, county_hub in CITY_TO_COUNTY_HUB.items():
        if slug in TIER1_SLUGS:
            continue
        pattern = re.compile(
            r'<a\s[^>]*href="/' + re.escape(slug) + r'-il-plumbing/?"[^>]*>(.*?)</a>',
            re.DOTALL
        )
        html = pattern.sub(r'\1', html)

    # 4. Blog posts referenced at root level → /blog/slug
    BLOG_SLUGS_AT_ROOT = [
        "chicago-plumbing-code-homeowners-guide",
        "prevent-frozen-pipes-chicago-winter",
        "sewer-replacement-cost-chicago",
        "tank-vs-tankless-water-heater-chicago-guide",
        "water-heater-maintenance-annual-checklist",
        "what-is-the-average-life-expectancy-of-a-water-heater",
        "do-hot-water-heater-blankets-work",
        "when-to-call-emergency-plumber-vs-diy",
        "bathroom-remodel-plumbing-cost-timeline",
        "commercial-plumbing-maintenance-checklist",
        "emergency-plumber-checklist-what-to-do",
        "how-does-a-garbage-disposal-work",
        "signs-you-need-sewer-line-replacement",
    ]
    for slug in BLOG_SLUGS_AT_ROOT:
        html = html.replace('href="/' + slug + '"', 'href="/blog/' + slug + '/"')
        html = html.replace('href="/' + slug + '/"', 'href="/blog/' + slug + '/"')

    # 5. /guide/* → /blog/
    html = re.sub(r'href="/guide/[^"]*"', 'href="/blog/"', html)

    return html


def build():
    build_start = time.time()
    print("Building static site...")
    print("Architecture: Tier 1 cities + County Hubs")

    # Build city→county mapping from county_hubs.json
    _build_city_county_map()

    # Clean dist
    if os.path.exists(DIST_DIR):
        shutil.rmtree(DIST_DIR)
    os.makedirs(DIST_DIR)

    # Copy assets
    if os.path.exists(ASSETS_SRC):
        shutil.copytree(ASSETS_SRC, ASSETS_DIST)
    else:
        os.makedirs(ASSETS_DIST, exist_ok=True)
        os.makedirs(os.path.join(ASSETS_DIST, "css"), exist_ok=True)

    # Track all built pages for sitemap (only indexable ones go in sitemap)
    built_pages = []
    ROBOTS_INDEX = "index, follow, max-snippet:-1, max-image-preview:large"
    ROBOTS_NOINDEX = "noindex, follow"

    # Load global data
    site_meta = load_json("site_meta.json")
    navigation = load_json("navigation.json")
    service_index = load_json("service_index.json")
    location_index = load_json("location_index.json")
    tier1_locations = load_json("tier1_locations.json")
    county_hubs = load_json("county_hubs.json")
    categories = load_json("categories.json")
    tags = load_json("tags.json")

    # Tier 1 location index (for navigation, linking)
    tier1_index = [{"city_name": t["city_name"], "city_slug": t["city_slug"], "state": "IL",
                    "url_path": t["url_path"], "county": t["county"]} for t in tier1_locations]

    # Full location list for service area page (ALL 248 cities)
    location_index_full = []
    for l in sorted(location_index, key=lambda x: x.get("city_name", "")):
        is_tier1 = l.get("city_slug") in TIER1_SLUGS
        county_slug = get_county_hub_slug(l.get("city_slug", ""))
        entry = {**l, "has_page": is_tier1, "county_hub_slug": county_slug,
                 "link_url": l["url_path"] + "/" if is_tier1 else "/service-area/" + county_slug + "/"}
        location_index_full.append(entry)

    # All location slugs for redirect generation
    all_location_slugs = set(l.get("city_slug", "") for l in location_index)

    global_ctx = {
        "site": site_meta,
        "navigation": navigation,
        "service_index": service_index,
        "location_index": tier1_index,
        "location_index_full": location_index_full,
        "tier1_locations": tier1_index,
        "county_hubs": county_hubs,
        "categories": categories,
        "tags": tags,
        "current_year": "2026",
        "page_type": "",
        "seo": {"title": "Plumbers 911 Chicago", "description": "Licensed plumbing services in Chicago and surrounding areas."},
    }

    base_tpl = load_template("_base.html")

    # --- HOME ---
    home_pages = load_json("pages_home.json")
    home_tpl = load_template("home.html")
    if home_pages:
        home = home_pages[0]
        ctx = {**global_ctx, **home, "page_type": "home",
               "canonical_path": "/",
               "breadcrumb_schema": "",
               "robots_meta": ROBOTS_INDEX}
        if home.get("seo"):
            ctx["seo"] = home["seo"]
        html = build_page(base_tpl, home_tpl, ctx)
        write_page("/", html)
        built_pages.append("/")
        print("  / (home)")

    # --- SERVICES (Chicago only — skip Arlington Heights sub-pages) ---
    services = load_json("services.json")
    svc_tpl = load_template("service.html")
    svc_built = 0
    svc_skipped = 0
    for svc in services:
        if is_arlington_service_page(svc.get("url_path", "")):
            svc_skipped += 1
            continue
        svc_slug = svc.get("url_path", "").strip("/").split("/")[-1]
        if svc_slug in DEAD_SERVICE_SLUGS:
            svc_skipped += 1
            continue
        cp = make_canonical(svc["url_path"])
        crumbs = [("Home", "/"), ("Services", "/chicago-il-plumbing/"), (svc.get("service_name", svc.get("title", "")), cp)]
        ctx = {**global_ctx, **svc, "page_type": "service",
               "canonical_path": cp,
               "breadcrumb_schema": make_breadcrumb_schema(crumbs),
               "robots_meta": ROBOTS_INDEX}
        if svc.get("seo"):
            ctx["seo"] = svc["seo"]
        html = build_page(base_tpl, svc_tpl, ctx)
        write_page(svc["url_path"], html)
        built_pages.append(svc["url_path"])
        svc_built += 1
    print("  " + str(svc_built) + " service pages (" + str(svc_skipped) + " Arlington Heights sub-pages removed)")

    # --- TIER 1 LOCATION PAGES (20 cities with genuinely unique content) ---
    loc_tpl = load_template("location.html")
    loc_built = 0
    for t1 in tier1_locations:
        city_slug = t1["city_slug"]
        county = t1.get("county", "Cook")
        county_hub_slug = get_county_hub_slug(city_slug)
        # Find how many cities are in this county hub
        county_city_count = 0
        for hub in county_hubs:
            if hub["slug"] == county_hub_slug:
                county_city_count = len(hub.get("cities", []))
                break
        cp = make_canonical(t1["url_path"])
        crumbs = [("Home", "/"), ("Service Area", "/service-area/"),
                  (county + " County", "/service-area/" + county_hub_slug + "/"),
                  (t1["city_name"] + ", IL", cp)]
        # Build nearby Tier 1 links
        nearby_slugs = t1.get("nearby_tier1", [])
        nearby_tier1_links = []
        for ns in nearby_slugs:
            for ti in tier1_index:
                if ti["city_slug"] == ns:
                    nearby_tier1_links.append(ti)
                    break
        # Join neighborhoods into text
        neighborhoods = t1.get("neighborhoods", [])
        neighborhoods_text = ", ".join(neighborhoods) if neighborhoods else ""
        ctx = {**global_ctx, **t1, "page_type": "location",
               "canonical_path": cp,
               "breadcrumb_schema": make_breadcrumb_schema(crumbs),
               "robots_meta": ROBOTS_INDEX,
               "county_hub_slug": county_hub_slug,
               "county_city_count": str(county_city_count),
               "neighborhoods_text": neighborhoods_text,
               "nearby_tier1_links": nearby_tier1_links}
        if t1.get("seo"):
            ctx["seo"] = t1["seo"]
        html = build_page(base_tpl, loc_tpl, ctx)
        write_page(t1["url_path"], html)
        built_pages.append(t1["url_path"])
        loc_built += 1
    print("  " + str(loc_built) + " Tier 1 location pages (unique content)")

    # --- COUNTY HUB PAGES (10 pages consolidating 228+ city pages) ---
    county_tpl = load_template("county_hub.html")
    county_built = 0
    for hub in county_hubs:
        cp = make_canonical(hub["url_path"])
        crumbs = [("Home", "/"), ("Service Area", "/service-area/"), (hub["county_name"], cp)]
        city_count = str(len(hub.get("cities", [])))
        # Build nearby county links
        nearby_county_links = []
        for nc_slug in hub.get("nearby_counties", []):
            for other_hub in county_hubs:
                if other_hub["slug"] == nc_slug:
                    nearby_county_links.append({"county_name": other_hub["county_name"],
                                                "url_path": other_hub["url_path"]})
                    break
        ctx = {**global_ctx, **hub, "page_type": "county-hub",
               "canonical_path": cp,
               "breadcrumb_schema": make_breadcrumb_schema(crumbs),
               "robots_meta": ROBOTS_INDEX,
               "city_count": city_count,
               "nearby_county_links": nearby_county_links}
        if hub.get("seo"):
            ctx["seo"] = hub["seo"]
        html = build_page(base_tpl, county_tpl, ctx)
        write_page(hub["url_path"], html)
        built_pages.append(hub["url_path"])
        county_built += 1
    print("  " + str(county_built) + " county hub pages")

    # --- BLOG POSTS (skip dead posts) ---
    blog_posts = load_json("blog_posts.json")
    kept_posts = [p for p in blog_posts if p["slug"] not in DEAD_BLOG_SLUGS]
    removed_posts = [p for p in blog_posts if p["slug"] in DEAD_BLOG_SLUGS]
    post_tpl = load_template("blog_post.html")
    for post in kept_posts:
        cp = make_canonical("/blog/" + post["slug"])
        crumbs = [("Home", "/"), ("Blog", "/blog/"), (post.get("title", ""), cp)]
        ctx = {**global_ctx, **post, "page_type": "blog-post",
               "canonical_path": cp,
               "breadcrumb_schema": make_breadcrumb_schema(crumbs),
               "robots_meta": ROBOTS_INDEX}
        if post.get("seo"):
            ctx["seo"] = post["seo"]
        date_str = post.get("date", "")
        ctx["date_formatted"] = date_str[:10] if date_str else ""
        post_cats = [c["slug"] for c in post.get("categories", [])]
        related = [p for p in kept_posts if p["id"] != post["id"] and any(c["slug"] in post_cats for c in p.get("categories", []))]
        ctx["related_posts"] = related[:3]
        html = build_page(base_tpl, post_tpl, ctx)
        write_page("/blog/" + post["slug"], html)
        built_pages.append("/blog/" + post["slug"])
    print("  " + str(len(kept_posts)) + " blog posts (" + str(len(removed_posts)) + " removed)")

    # --- BLOG INDEX (only kept posts) ---
    blog_idx_tpl = load_template("blog_index.html")
    ctx = {**global_ctx, "blog_posts": kept_posts, "page_type": "blog", "active_all": True,
           "canonical_path": "/blog/",
           "breadcrumb_schema": make_breadcrumb_schema([("Home", "/"), ("Blog", "/blog/")]),
           "robots_meta": ROBOTS_INDEX,
           "seo": {"title": "Plumbing Blog - Tips & Resources", "description": "Expert plumbing tips, guides, and resources from the Plumbers 911 Chicago team."}}
    for p in ctx["blog_posts"]:
        p["date_formatted"] = p.get("date", "")[:10]
    html = build_page(base_tpl, blog_idx_tpl, ctx)
    write_page("/blog", html)
    built_pages.append("/blog")
    print("  /blog (index)")

    # --- ABOUT ---
    about_pages = load_json("pages_about.json")
    about_tpl = load_template("about.html")
    if about_pages:
        pg = about_pages[0]
        cp = make_canonical(pg["url_path"])
        crumbs = [("Home", "/"), ("About Us", cp)]
        ctx = {**global_ctx, **pg, "page_type": "about",
               "canonical_path": cp,
               "breadcrumb_schema": make_breadcrumb_schema(crumbs),
               "robots_meta": ROBOTS_INDEX}
        if pg.get("seo"):
            ctx["seo"] = pg["seo"]
        html = build_page(base_tpl, about_tpl, ctx)
        write_page(pg["url_path"], html)
        built_pages.append(pg["url_path"])
        print("  " + pg["url_path"])

    # --- CONTACT ---
    contact_pages = load_json("pages_contact.json")
    contact_tpl = load_template("contact.html")
    if contact_pages:
        pg = contact_pages[0]
        cp = make_canonical(pg["url_path"])
        crumbs = [("Home", "/"), ("Contact Us", cp)]
        ctx = {**global_ctx, **pg, "page_type": "contact",
               "canonical_path": cp,
               "breadcrumb_schema": make_breadcrumb_schema(crumbs),
               "robots_meta": ROBOTS_INDEX}
        if pg.get("seo"):
            ctx["seo"] = pg["seo"]
        html = build_page(base_tpl, contact_tpl, ctx)
        write_page(pg["url_path"], html)
        built_pages.append(pg["url_path"])
        print("  " + pg["url_path"])

    # --- LEGAL ---
    legal_pages = load_json("pages_legal.json")
    legal_tpl = load_template("legal.html")
    for pg in legal_pages:
        cp = make_canonical(pg["url_path"])
        crumbs = [("Home", "/"), (pg.get("title", "Legal"), cp)]
        ctx = {**global_ctx, **pg, "page_type": "legal",
               "canonical_path": cp,
               "breadcrumb_schema": make_breadcrumb_schema(crumbs),
               "robots_meta": ROBOTS_INDEX}
        if pg.get("seo"):
            ctx["seo"] = pg["seo"]
        html = build_page(base_tpl, legal_tpl, ctx)
        write_page(pg["url_path"], html)
        built_pages.append(pg["url_path"])
        print("  " + pg["url_path"])

    # --- SERVICE AREA ---
    sa_pages = load_json("pages_service_area.json")
    sa_tpl = load_template("service_area.html")
    if sa_pages:
        pg = sa_pages[0]
        cp = make_canonical(pg["url_path"])
        crumbs = [("Home", "/"), ("Service Area", cp)]
        # Group all cities by first letter for A-Z directory
        from collections import OrderedDict
        letter_groups = OrderedDict()
        for city in location_index_full:
            letter = city["city_name"][0].upper()
            if letter not in letter_groups:
                letter_groups[letter] = []
            letter_groups[letter].append(city)
        city_letters = [{"letter": k, "cities": v} for k, v in letter_groups.items()]
        total_cities = len(location_index_full)
        cities_with_pages = len(TIER1_SLUGS)
        # Load county map data for interactive SVG map
        county_map_path = os.path.join(DATA_DIR, "county_map.json")
        if os.path.exists(county_map_path):
            county_map_data = json.dumps(json.load(open(county_map_path, "r", encoding="utf-8")))
        else:
            county_map_data = "{}"
        ctx = {**global_ctx, **pg, "page_type": "service-area",
               "canonical_path": cp,
               "breadcrumb_schema": make_breadcrumb_schema(crumbs),
               "robots_meta": ROBOTS_INDEX,
               "city_letters": city_letters,
               "total_cities": str(total_cities),
               "cities_with_pages": str(cities_with_pages),
               "county_map_json": county_map_data}
        if pg.get("seo"):
            ctx["seo"] = pg["seo"]
        html = build_page(base_tpl, sa_tpl, ctx)
        write_page(pg["url_path"], html)
        built_pages.append(pg["url_path"])
        print("  " + pg["url_path"])

    # --- Phase 33: SERVICE CATEGORY HUB PAGES ---
    hub_pages = [
        {
            "title": "Kitchen & Bath Plumbing",
            "url_path": "/kitchen-bath",
            "content": """<h2>Kitchen &amp; Bath Plumbing Services in Chicago</h2>
<p>From complete kitchen remodels to bathroom renovations, Plumbers 911 Chicago provides expert plumbing services for every room in your home. Our licensed plumbers handle fixture installation, pipe rerouting, and everything in between.</p>
<h3>Kitchen Plumbing Services</h3>
<ul><li><a href="/chicago-il-plumbing/kitchen-remodeling/">Kitchen Remodeling</a></li><li><a href="/chicago-il-plumbing/faucet-repair/">Faucet Repair &amp; Installation</a></li><li><a href="/chicago-il-plumbing/garbage-disposal-installation/">Garbage Disposal Services</a></li><li><a href="/chicago-il-plumbing/dishwasher-install/">Dishwasher Installation</a></li></ul>
<h3>Bathroom Plumbing Services</h3>
<ul><li><a href="/chicago-il-plumbing/bathroom-remodeling/">Bathroom Remodeling</a></li><li><a href="/chicago-il-plumbing/toilet-install/">Toilet Installation</a></li><li><a href="/chicago-il-plumbing/bathtub-install/">Bathtub Installation</a></li><li><a href="/chicago-il-plumbing/shower-install/">Shower Installation</a></li></ul>
<p>Call <a href="tel:8337586911">833-758-6911</a> for a free estimate on any kitchen or bathroom plumbing project.</p>""",
            "seo": {"title": "Kitchen & Bath Plumbing Services", "description": "Expert kitchen and bathroom plumbing services in Chicago. Remodeling, fixture installation, faucet repair, and more. Call 833-758-6911."},
        },
        {
            "title": "Sewer & Drain Services",
            "url_path": "/sewer-drain",
            "content": """<h2>Sewer &amp; Drain Services in Chicago</h2>
<p>Don't let sewer and drain problems disrupt your life. Plumbers 911 Chicago offers comprehensive sewer and drain services using the latest technology including HD camera inspections and hydro-jetting.</p>
<h3>Sewer Services</h3>
<ul><li><a href="/chicago-il-plumbing/sewer-cleaning/">Sewer Cleaning</a></li><li><a href="/chicago-il-plumbing/sewer-replacement/">Sewer Replacement</a></li><li><a href="/chicago-il-plumbing/sewer-camera-inspection/">Sewer Camera Inspection</a></li><li><a href="/chicago-il-plumbing/sewer-cleanout-installation/">Sewer Cleanout Installation</a></li></ul>
<h3>Drain Services</h3>
<ul><li><a href="/chicago-il-plumbing/drain-cleaning/">Drain Cleaning</a></li><li><a href="/chicago-il-plumbing/drain-replacement/">Drain Replacement</a></li></ul>
<p>Experiencing slow drains or sewer backups? Call <a href="tel:8337586911">833-758-6911</a> for fast, reliable service.</p>""",
            "seo": {"title": "Sewer & Drain Services Chicago", "description": "Professional sewer and drain services in Chicago. Cleaning, replacement, camera inspection, and more. Available 24/7. Call 833-758-6911."},
        },
        {
            "title": "Hot Water Services",
            "url_path": "/hot-water",
            "content": """<h2>Hot Water Heater Services in Chicago</h2>
<p>No hot water? Plumbers 911 Chicago provides fast, reliable water heater repair and installation for both traditional tank and tankless systems. We service all major brands.</p>
<h3>Tank Water Heaters</h3>
<ul><li><a href="/chicago-il-plumbing/water-heater-repair/">Water Heater Repair</a></li><li><a href="/chicago-il-plumbing/water-heater-installation/">Water Heater Installation</a></li></ul>
<h3>Tankless Water Heaters</h3>
<ul><li><a href="/chicago-il-plumbing/tankless-water-heater-repair/">Tankless Water Heater Repair</a></li><li><a href="/chicago-il-plumbing/tankless-water-heater-installation/">Tankless Water Heater Installation</a></li></ul>
<p>We service Rheem, A.O. Smith, Bradford White, Rinnai, Navien, and all other brands. Call <a href="tel:8337586911">833-758-6911</a>.</p>""",
            "seo": {"title": "Water Heater Repair & Installation Chicago", "description": "Tank and tankless water heater repair and installation in Chicago. All brands serviced. 24/7 emergency service. Call 833-758-6911."},
        },
        {
            "title": "Water Line Services",
            "url_path": "/water-lines",
            "content": """<h2>Water Line Services in Chicago</h2>
<p>From whole-house repiping to water filtration, Plumbers 911 Chicago handles all your water line needs. Our licensed plumbers ensure clean, safe water throughout your home.</p>
<ul><li><a href="/chicago-il-plumbing/whole-house-repiping/">Whole House Repiping</a></li><li><a href="/chicago-il-plumbing/frozen-broken-pipe-repair/">Frozen &amp; Broken Pipe Repair</a></li><li><a href="/chicago-il-plumbing/backflow-testing-installation/">Backflow Testing &amp; Installation</a></li><li><a href="/chicago-il-plumbing/water-softener-installation/">Water Softener Installation</a></li><li><a href="/chicago-il-plumbing/water-filter-installation-replacement/">Water Filter Services</a></li></ul>
<p>Protect your home's water supply. Call <a href="tel:8337586911">833-758-6911</a> for a free consultation.</p>""",
            "seo": {"title": "Water Line Services Chicago", "description": "Water line repair, repiping, backflow testing, water softener and filter installation in Chicago. Call 833-758-6911."},
        },
        {
            "title": "Other Plumbing Services",
            "url_path": "/other-plumbing-services",
            "content": """<h2>Additional Plumbing Services in Chicago</h2>
<p>Beyond our specialty services, Plumbers 911 Chicago offers a full range of residential and commercial plumbing solutions to meet any need.</p>
<ul><li><a href="/chicago-il-plumbing/residential-plumbing/">Residential Plumbing</a></li><li><a href="/chicago-il-plumbing/commercial-plumbing/">Commercial Plumbing</a></li><li><a href="/chicago-il-plumbing/gas-line-install-repair/">Gas Line Services</a></li><li><a href="/chicago-il-plumbing/sump-pump-install-replacement/">Sump Pump Installation &amp; Repair</a></li><li><a href="/chicago-il-plumbing/sump-pump-battery-backup-install/">Sump Pump Battery Backup</a></li><li><a href="/chicago-il-plumbing/water-leak-detection-repair/">Water Leak Detection &amp; Repair</a></li></ul>
<p>Whatever your plumbing needs, we're here to help. Call <a href="tel:8337586911">833-758-6911</a>.</p>""",
            "seo": {"title": "Residential & Commercial Plumbing Chicago", "description": "Full-service residential and commercial plumbing in Chicago. Gas lines, sump pumps, leak detection, and more. Call 833-758-6911."},
        },
    ]
    page_tpl = load_template("page.html")
    for hub in hub_pages:
        cp = make_canonical(hub["url_path"])
        crumbs = [("Home", "/"), (hub["title"], cp)]
        ctx = {**global_ctx, **hub, "page_type": "page",
               "canonical_path": cp,
               "breadcrumb_schema": make_breadcrumb_schema(crumbs),
               "robots_meta": ROBOTS_INDEX}
        html = build_page(base_tpl, page_tpl, ctx)
        write_page(hub["url_path"], html)
        built_pages.append(hub["url_path"])
    print("  " + str(len(hub_pages)) + " service category hub pages (Phase 33)")

    # --- GENERIC PAGES (skip request-a-call-back) ---
    gen_pages = load_json("pages_page.json")
    gen_tpl = load_template("page.html")
    gen_built = 0
    for pg in gen_pages:
        if pg.get("slug") == "request-a-call-back":
            continue
        if is_arlington_service_page(pg.get("url_path", "")):
            continue
        cp = make_canonical(pg["url_path"])
        crumbs = [("Home", "/"), (pg.get("title", ""), cp)]
        ctx = {**global_ctx, **pg, "page_type": "page",
               "canonical_path": cp,
               "breadcrumb_schema": make_breadcrumb_schema(crumbs),
               "robots_meta": ROBOTS_INDEX}
        if pg.get("seo"):
            ctx["seo"] = pg["seo"]
        html = build_page(base_tpl, gen_tpl, ctx)
        write_page(pg["url_path"], html)
        built_pages.append(pg["url_path"])
        gen_built += 1
    print("  " + str(gen_built) + " generic pages")

    # --- 404 PAGE ---
    html_404 = generate_404_page(base_tpl, global_ctx)
    write_page("/404", html_404)
    print("  /404 (custom error page)")

    # --- XML SITEMAP ---
    sitemap_xml = generate_xml_sitemap(built_pages)
    with open(os.path.join(DIST_DIR, "sitemap.xml"), "w", encoding="utf-8") as f:
        f.write(sitemap_xml)
    print("  /sitemap.xml (" + str(len(built_pages)) + " URLs)")

    # --- ROBOTS.TXT ---
    robots = "User-agent: *\nAllow: /\n\nSitemap: https://plumbers911chicago.com/sitemap.xml\n"
    with open(os.path.join(DIST_DIR, "robots.txt"), "w", encoding="utf-8") as f:
        f.write(robots)
    print("  /robots.txt")

    # --- VERCEL CONFIG WITH REDIRECTS (written to project root) ---
    redirects = generate_redirects_json(all_location_slugs)
    root_vercel = os.path.join(SITE_DIR, "vercel.json")
    if os.path.exists(root_vercel):
        with open(root_vercel, "r", encoding="utf-8") as f:
            vercel_config = json.load(f)
    else:
        vercel_config = {}
    vercel_config["redirects"] = redirects
    vercel_config["trailingSlash"] = True
    vercel_config["cleanUrls"] = True
    with open(root_vercel, "w", encoding="utf-8") as f:
        json.dump(vercel_config, f, indent=2)
    print("  vercel.json updated at project root (" + str(len(redirects)) + " redirects)")

    # --- SEO QUALITY CHECK ---
    print("\n  SEO Quality Check:")
    titles_seen = {}
    descs_seen = {}
    issues = 0
    for r, d, fs in os.walk(DIST_DIR):
        for f in fs:
            if not f.endswith(".html"):
                continue
            fp = os.path.join(r, f)
            content = open(fp, "r", encoding="utf-8").read()
            rel = os.path.relpath(fp, DIST_DIR)
            # Check title
            tm = re.search(r"<title>(.*?)</title>", content)
            if tm:
                t = tm.group(1)
                if t in titles_seen:
                    issues += 1
                titles_seen.setdefault(t, []).append(rel)
            # Check meta description
            dm = re.search(r'<meta name="description" content="(.*?)"', content)
            if dm:
                d_val = dm.group(1)
                if d_val in descs_seen:
                    issues += 1
                descs_seen.setdefault(d_val, []).append(rel)
    dup_titles = sum(1 for t, ps in titles_seen.items() if len(ps) > 1)
    dup_descs = sum(1 for d, ps in descs_seen.items() if len(ps) > 1)
    print("    Duplicate titles: " + str(dup_titles))
    print("    Duplicate descriptions: " + str(dup_descs))

    # --- TOTAL SIZE ---
    total_size = sum(os.path.getsize(os.path.join(r, f)) for r, d, fs in os.walk(DIST_DIR) for f in fs)

    # Count total
    total = sum(1 for _, _, files in os.walk(DIST_DIR) for f in files if f.endswith(".html"))
    build_time = time.time() - build_start
    print("\n" + "=" * 50)
    print("BUILD COMPLETE! (Architecture Rebuild)")
    print("  HTML pages: " + str(total))
    print("  Tier 1 location pages: " + str(loc_built))
    print("  County hub pages: " + str(county_built))
    print("  Service pages: " + str(svc_built))
    print("  Redirects configured: " + str(len(redirects)))
    print("  Sitemap URLs: " + str(len(built_pages)))
    print("  Total dist size: " + str(round(total_size / 1024 / 1024, 1)) + " MB")
    print("  Build time: " + str(round(build_time, 2)) + "s")
    print("  Output: " + DIST_DIR)
    print("=" * 50)


if __name__ == "__main__":
    build()
