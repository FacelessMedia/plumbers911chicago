import os, re
head_count = 0
body_count = 0
body_samples = set()
for r, d, fs in os.walk("dist"):
    for f in fs:
        if not f.endswith(".html"):
            continue
        html = open(os.path.join(r, f), "r", encoding="utf-8").read()
        parts = html.split("</head>", 1)
        if len(parts) == 2:
            head_urls = re.findall(r'href="https://plumbers911chicago\.com[^"]*"', parts[0])
            body_urls = re.findall(r'href="https://plumbers911chicago\.com[^"]*"', parts[1])
            head_count += len(head_urls)
            body_count += len(body_urls)
            for u in body_urls:
                rel = os.path.relpath(os.path.join(r, f), "dist").replace("\\","/")
                body_samples.add((rel, u))
# Also check src= attributes
src_count = 0
for r, d, fs in os.walk("dist"):
    for f in fs:
        if not f.endswith(".html"):
            continue
        html = open(os.path.join(r, f), "r", encoding="utf-8").read()
        srcs = re.findall(r'src="https://plumbers911chicago\.com[^"]*"', html)
        src_count += len(srcs)

print(f"In <head> (expected): {head_count}")
print(f"In <body> (BUG): {body_count}")
print(f"In src= attrs: {src_count}")
print(f"\nBody URL samples:")
for rel, u in sorted(list(body_samples))[:15]:
    print(f"  [{rel}] {u[:70]}")

# Check wp-admin form action
form_count = 0
for r, d, fs in os.walk("dist"):
    for f in fs:
        if not f.endswith(".html"):
            continue
        html = open(os.path.join(r, f), "r", encoding="utf-8").read()
        if "wp-admin" in html:
            rel = os.path.relpath(os.path.join(r, f), "dist").replace("\\","/")
            print(f"\nwp-admin found in: {rel}")
            form_count += 1
print(f"\nTotal pages with wp-admin: {form_count}")
