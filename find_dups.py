"""Find duplicate titles and descriptions in dist."""
import os, re

dist = "dist"
titles = {}
descs = {}
for r, d, fs in os.walk(dist):
    for f in fs:
        if not f.endswith(".html"):
            continue
        fp = os.path.join(r, f)
        content = open(fp, "r", encoding="utf-8").read()
        rel = os.path.relpath(fp, dist)
        tm = re.search(r"<title>(.*?)</title>", content)
        if tm:
            titles.setdefault(tm.group(1), []).append(rel)
        dm = re.search(r'<meta name="description" content="(.*?)"', content)
        if dm:
            descs.setdefault(dm.group(1), []).append(rel)

print("DUPLICATE TITLES:")
for t, ps in sorted(titles.items()):
    if len(ps) > 1:
        print(f"  '{t[:60]}...' -> {ps}")

print("\nDUPLICATE DESCRIPTIONS:")
for d, ps in sorted(descs.items()):
    if len(ps) > 1:
        print(f"  '{d[:60]}...' -> {ps}")
