"""Final SEO audit: verify schema, OG, canonical, robots on all pages."""
import os, re, json

dist = "dist"
results = {
    "total": 0,
    "missing_title": [],
    "missing_description": [],
    "missing_canonical": [],
    "missing_og_title": [],
    "missing_robots": [],
    "missing_schema": [],
    "has_multiple_h1": [],
}

for r, d, fs in os.walk(dist):
    for f in fs:
        if not f.endswith(".html"):
            continue
        fp = os.path.join(r, f)
        content = open(fp, "r", encoding="utf-8").read()
        rel = os.path.relpath(fp, dist).replace("\\", "/")
        results["total"] += 1

        if not re.search(r"<title>.+?</title>", content):
            results["missing_title"].append(rel)
        if not re.search(r'<meta name="description"', content):
            results["missing_description"].append(rel)
        if not re.search(r'<link rel="canonical"', content):
            results["missing_canonical"].append(rel)
        if not re.search(r'<meta property="og:title"', content):
            results["missing_og_title"].append(rel)
        if not re.search(r'<meta name="robots"', content):
            results["missing_robots"].append(rel)
        if not re.search(r'application/ld\+json', content):
            results["missing_schema"].append(rel)
        
        h1s = re.findall(r"<h1[^>]*>", content)
        if len(h1s) > 1:
            results["has_multiple_h1"].append((rel, len(h1s)))

print(f"=== FINAL SEO AUDIT ({results['total']} pages) ===\n")
for key in ["missing_title", "missing_description", "missing_canonical", "missing_og_title", "missing_robots", "missing_schema"]:
    count = len(results[key])
    status = "PASS" if count == 0 else f"FAIL ({count})"
    print(f"  {key}: {status}")
    if count > 0 and count <= 5:
        for p in results[key]:
            print(f"    - {p}")

print(f"\n  Multiple H1 tags: {len(results['has_multiple_h1'])} pages")
if results["has_multiple_h1"]:
    for p, c in results["has_multiple_h1"][:10]:
        print(f"    - {p} ({c} H1s)")

# Check sitemap accuracy
sitemap = open(os.path.join(dist, "sitemap.xml"), "r", encoding="utf-8").read()
sitemap_urls = re.findall(r"<loc>(.*?)</loc>", sitemap)
print(f"\n  Sitemap URLs: {len(sitemap_urls)}")

# Check robots.txt
robots = open(os.path.join(dist, "robots.txt"), "r", encoding="utf-8").read()
print(f"  robots.txt has sitemap ref: {'YES' if 'sitemap' in robots.lower() else 'NO'}")

# Check vercel.json redirects
vj = json.load(open("vercel.json", "r", encoding="utf-8"))
print(f"  Vercel redirects: {len(vj.get('redirects', []))}")
print(f"  trailingSlash: {vj.get('trailingSlash')}")
print(f"  cleanUrls: {vj.get('cleanUrls')}")

print("\n=== AUDIT COMPLETE ===")
