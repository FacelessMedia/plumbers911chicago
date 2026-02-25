"""Comprehensive audit of the built site to find incomplete/rough areas."""
import os, re, json

dist = "dist"

print("=" * 60)
print("FULL SITE AUDIT")
print("=" * 60)

# 1. Check for placeholder/TODO content in HTML
print("\n--- PLACEHOLDER/TODO CONTENT ---")
placeholders = ["TODO", "PLACEHOLDER", "LOREM", "lorem ipsum", "TBD", "FIXME",
                 "GA_MEASUREMENT_ID", "GTM_CONTAINER_ID", "example.com"]
for r, d, fs in os.walk(dist):
    for f in fs:
        if not f.endswith(".html"):
            continue
        fp = os.path.join(r, f)
        content = open(fp, "r", encoding="utf-8").read()
        rel = os.path.relpath(fp, dist).replace("\\", "/")
        for ph in placeholders:
            if ph in content:
                # Get line number
                for i, line in enumerate(content.split("\n"), 1):
                    if ph in line:
                        print(f"  [{rel}:{i}] Contains '{ph}'")
                        break

# 2. Check for empty content sections
print("\n--- EMPTY/MISSING CONTENT ---")
for r, d, fs in os.walk(dist):
    for f in fs:
        if not f.endswith(".html"):
            continue
        fp = os.path.join(r, f)
        content = open(fp, "r", encoding="utf-8").read()
        rel = os.path.relpath(fp, dist).replace("\\", "/")
        # Empty content-body
        m = re.search(r'class="content-body">\s*</article>', content)
        if m:
            print(f"  [{rel}] Empty content-body")
        # Mustache template variables not rendered
        mustache = re.findall(r'\{\{[^}]+\}\}', content)
        if mustache:
            for mv in mustache[:3]:
                if 'schema' not in mv.lower() and 'json' not in mv.lower():
                    print(f"  [{rel}] Unrendered template var: {mv}")

# 3. Check for pages with very short content
print("\n--- VERY SHORT PAGES (< 200 chars content) ---")
short_pages = []
for r, d, fs in os.walk(dist):
    for f in fs:
        if not f.endswith(".html"):
            continue
        fp = os.path.join(r, f)
        content = open(fp, "r", encoding="utf-8").read()
        rel = os.path.relpath(fp, dist).replace("\\", "/")
        # Extract main content
        m = re.search(r'class="content-body">(.*?)</article>', content, re.DOTALL)
        if m:
            body = re.sub(r'<[^>]+>', '', m.group(1)).strip()
            if len(body) < 200 and rel != "404/index.html":
                short_pages.append((rel, len(body)))
if short_pages:
    for p, l in sorted(short_pages, key=lambda x: x[1])[:15]:
        print(f"  [{p}] {l} chars")
else:
    print("  None found")

# 4. Check CSS for incomplete/stub styles
print("\n--- CSS AUDIT ---")
css = open(os.path.join(dist, "assets/css/styles.css"), "r", encoding="utf-8").read()
print(f"  CSS size: {len(css)} chars, {len(css.split(chr(10)))} lines")
# Check for TODO in CSS
if "TODO" in css or "FIXME" in css:
    print("  WARNING: CSS contains TODO/FIXME")
else:
    print("  No TODO/FIXME in CSS")

# 5. Check JS for stubs
print("\n--- JS AUDIT ---")
js = open(os.path.join(dist, "assets/js/main.js"), "r", encoding="utf-8").read()
print(f"  JS size: {len(js)} chars, {len(js.split(chr(10)))} lines")
if "TODO" in js or "FIXME" in js:
    print("  WARNING: JS contains TODO/FIXME")
else:
    print("  No TODO/FIXME in JS")

# 6. Check for images referenced but missing
print("\n--- MISSING REFERENCED IMAGES ---")
all_html = ""
for r, d, fs in os.walk(dist):
    for f in fs:
        if f.endswith(".html"):
            all_html += open(os.path.join(r, f), "r", encoding="utf-8").read()
img_srcs = set(re.findall(r'src="(/assets/images/[^"]+)"', all_html))
for src in sorted(img_srcs):
    fp = os.path.join(dist, src.lstrip("/"))
    if not os.path.exists(fp):
        print(f"  MISSING: {src}")
if not any(not os.path.exists(os.path.join(dist, s.lstrip("/"))) for s in img_srcs):
    print("  All referenced images exist")

# 7. Check service area page specifically
print("\n--- SERVICE AREA PAGE AUDIT ---")
sa = open(os.path.join(dist, "service-area/index.html"), "r", encoding="utf-8").read()
city_links = re.findall(r'class="az-city"', sa)
print(f"  Total cities listed: {len(city_links)}")
linked_cities = re.findall(r'<a href="[^"]+"><strong>[^<]+</strong></a>', sa)
print(f"  Cities with links: {len(linked_cities)}")
gray_cities = re.findall(r'class="az-nopage"', sa)
print(f"  Cities without pages (gray): {len(gray_cities)}")
# Check the content section
has_content = 'service-area-intro' in sa
print(f"  Has intro content section: {has_content}")
has_search = 'location-search' in sa
print(f"  Has search box: {has_search}")
has_stats = 'stats-grid' in sa
print(f"  Has stats grid: {has_stats}")

# 8. Check for pages that reference old WP URLs
print("\n--- OLD WP URLs IN CONTENT ---")
wp_urls = set()
for m in re.finditer(r'href="https://plumbers911chicago\.com/([^"]*)"', all_html):
    wp_urls.add(m.group(0))
print(f"  Old WP absolute URLs still in content: {len(wp_urls)}")
for u in list(wp_urls)[:10]:
    print(f"    {u}")

# 9. Check contact form action
print("\n--- FORM ACTIONS ---")
forms = re.findall(r'<form[^>]*action="([^"]*)"[^>]*>', all_html)
form_actions = set(forms)
print(f"  Unique form actions: {form_actions if form_actions else 'None found (no action attr)'}")

# 10. Check for emoji in floating CTA (user might not want emoji)
print("\n--- EMOJI CHECK ---")
if '📞' in all_html:
    print("  WARNING: Emoji found in HTML (floating CTA button)")

# 11. Summary
print("\n" + "=" * 60)
total_html = sum(1 for r, d, fs in os.walk(dist) for f in fs if f.endswith(".html"))
total_size = sum(os.path.getsize(os.path.join(r, f)) for r, d, fs in os.walk(dist) for f in fs)
print(f"SUMMARY: {total_html} pages, {round(total_size/1024/1024, 1)} MB total")
print("=" * 60)
