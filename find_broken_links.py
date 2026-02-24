"""Scan dist/ for broken internal links."""
import os, re

dist = "dist"
built = set()
for r, d, fs in os.walk(dist):
    for f in fs:
        rel = os.path.relpath(os.path.join(r, f), dist).replace("\\", "/")
        if rel.endswith("/index.html"):
            built.add("/" + rel[:-len("/index.html")] + "/")
        elif rel == "index.html":
            built.add("/")
        else:
            built.add("/" + rel)

broken = {}
for r, d, fs in os.walk(dist):
    for f in fs:
        if not f.endswith(".html"):
            continue
        fp = os.path.join(r, f)
        html = open(fp, "r", encoding="utf-8").read()
        links = re.findall(r'href="(/[^"#?]+)"', html)
        for link in links:
            norm = link.rstrip("/") + "/"
            bare = link.rstrip("/")
            if norm not in built and bare not in built and link not in built:
                broken.setdefault(link, set()).add(fp)

print(f"Unique broken targets: {len(broken)}")
for link in sorted(broken):
    print(f"  {link}  ({len(broken[link])} pages)")
