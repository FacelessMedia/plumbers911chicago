"""
Static site builder for Plumbers 911 Chicago.
Reads JSON data files and generates static HTML pages in /dist.
"""
import json
import os
import re
import shutil

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
    """Convert absolute plumbers911chicago.com URLs to relative paths and clean Rank Math variables."""
    html = html.replace("https://plumbers911chicago.com/", "/")
    html = html.replace("http://plumbers911chicago.com/", "/")
    # Clean Rank Math SEO variables that weren't resolved
    html = html.replace(" %sep% %sitename%", "")
    html = html.replace("%sep%", "-")
    html = html.replace("%sitename%", "Plumbers 911 Chicago")
    return html


def build_page(base_tpl, content_tpl_str, ctx):
    """Render content template, inject into base layout."""
    content_html = render(content_tpl_str, ctx)
    full_ctx = {**ctx, "content_block": content_html}
    # Replace the {{> content}} partial in base with the rendered content
    page_html = base_tpl.replace("{{> content}}", content_html)
    page_html = render(page_html, full_ctx)
    page_html = normalize_urls(page_html)
    return page_html


def build():
    print("Building static site...")

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

    # Load global data
    site_meta = load_json("site_meta.json")
    navigation = load_json("navigation.json")
    service_index = load_json("service_index.json")
    location_index = load_json("location_index.json")
    categories = load_json("categories.json")
    tags = load_json("tags.json")

    global_ctx = {
        "site": site_meta,
        "navigation": navigation,
        "service_index": service_index,
        "location_index": location_index,
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
        ctx = {**global_ctx, **home, "page_type": "home"}
        if home.get("seo"):
            ctx["seo"] = home["seo"]
        html = build_page(base_tpl, home_tpl, ctx)
        write_page("/", html)
        print("  / (home)")

    # --- SERVICES ---
    services = load_json("services.json")
    svc_tpl = load_template("service.html")
    for svc in services:
        ctx = {**global_ctx, **svc, "page_type": "service"}
        if svc.get("seo"):
            ctx["seo"] = svc["seo"]
        html = build_page(base_tpl, svc_tpl, ctx)
        write_page(svc["url_path"], html)
    print("  " + str(len(services)) + " service pages")

    # --- LOCATIONS ---
    locations = load_json("locations.json")
    loc_tpl = load_template("location.html")
    for loc in locations:
        ctx = {**global_ctx, **loc, "page_type": "location"}
        if loc.get("seo"):
            ctx["seo"] = loc["seo"]
        # Add nearby locations (simple: same first letter or nearby in alpha sort)
        idx = next((i for i, l in enumerate(location_index) if l["city_slug"] == loc.get("city_slug")), 0)
        start = max(0, idx - 3)
        nearby = [l for l in location_index[start:start+7] if l["city_slug"] != loc.get("city_slug")]
        ctx["nearby_locations"] = nearby[:6]
        html = build_page(base_tpl, loc_tpl, ctx)
        write_page(loc["url_path"], html)
    print("  " + str(len(locations)) + " location pages")

    # --- BLOG POSTS ---
    blog_posts = load_json("blog_posts.json")
    post_tpl = load_template("blog_post.html")
    for post in blog_posts:
        ctx = {**global_ctx, **post, "page_type": "blog-post"}
        if post.get("seo"):
            ctx["seo"] = post["seo"]
        # Format date
        date_str = post.get("date", "")
        ctx["date_formatted"] = date_str[:10] if date_str else ""
        # Related posts (others in same category)
        post_cats = [c["slug"] for c in post.get("categories", [])]
        related = [p for p in blog_posts if p["id"] != post["id"] and any(c["slug"] in post_cats for c in p.get("categories", []))]
        ctx["related_posts"] = related[:3]
        html = build_page(base_tpl, post_tpl, ctx)
        # Blog posts go under /blog/slug/
        write_page("/blog/" + post["slug"], html)
    print("  " + str(len(blog_posts)) + " blog posts")

    # --- BLOG INDEX ---
    blog_idx_tpl = load_template("blog_index.html")
    ctx = {**global_ctx, "blog_posts": blog_posts, "page_type": "blog", "active_all": True,
           "seo": {"title": "Blog", "description": "Plumbing tips and resources from Plumbers 911 Chicago."}}
    for p in ctx["blog_posts"]:
        p["date_formatted"] = p.get("date", "")[:10]
    html = build_page(base_tpl, blog_idx_tpl, ctx)
    write_page("/blog", html)
    print("  /blog (index)")

    # --- ABOUT ---
    about_pages = load_json("pages_about.json")
    about_tpl = load_template("about.html")
    if about_pages:
        pg = about_pages[0]
        ctx = {**global_ctx, **pg, "page_type": "about"}
        if pg.get("seo"):
            ctx["seo"] = pg["seo"]
        html = build_page(base_tpl, about_tpl, ctx)
        write_page(pg["url_path"], html)
        print("  " + pg["url_path"])

    # --- CONTACT ---
    contact_pages = load_json("pages_contact.json")
    contact_tpl = load_template("contact.html")
    if contact_pages:
        pg = contact_pages[0]
        ctx = {**global_ctx, **pg, "page_type": "contact"}
        if pg.get("seo"):
            ctx["seo"] = pg["seo"]
        html = build_page(base_tpl, contact_tpl, ctx)
        write_page(pg["url_path"], html)
        print("  " + pg["url_path"])

    # --- LEGAL ---
    legal_pages = load_json("pages_legal.json")
    legal_tpl = load_template("legal.html")
    for pg in legal_pages:
        ctx = {**global_ctx, **pg, "page_type": "legal"}
        if pg.get("seo"):
            ctx["seo"] = pg["seo"]
        html = build_page(base_tpl, legal_tpl, ctx)
        write_page(pg["url_path"], html)
        print("  " + pg["url_path"])

    # --- SERVICE AREA ---
    sa_pages = load_json("pages_service_area.json")
    sa_tpl = load_template("service_area.html")
    if sa_pages:
        pg = sa_pages[0]
        ctx = {**global_ctx, **pg, "page_type": "service-area"}
        if pg.get("seo"):
            ctx["seo"] = pg["seo"]
        html = build_page(base_tpl, sa_tpl, ctx)
        write_page(pg["url_path"], html)
        print("  " + pg["url_path"])

    # --- GENERIC PAGES ---
    gen_pages = load_json("pages_page.json")
    gen_tpl = load_template("page.html")
    for pg in gen_pages:
        ctx = {**global_ctx, **pg, "page_type": "page"}
        if pg.get("seo"):
            ctx["seo"] = pg["seo"]
        html = build_page(base_tpl, gen_tpl, ctx)
        write_page(pg["url_path"], html)
    print("  " + str(len(gen_pages)) + " generic pages")

    # Count total files
    total = sum(len(files) for _, _, files in os.walk(DIST_DIR) if any(f.endswith(".html") for f in files))
    print("\nBuild complete! " + str(total) + " HTML files in " + DIST_DIR)


if __name__ == "__main__":
    build()
