import os, re
samples = set()
for r, d, fs in os.walk("dist"):
    for f in fs:
        if not f.endswith(".html"):
            continue
        html = open(os.path.join(r, f), "r", encoding="utf-8").read()
        for m in re.finditer(r'href="(https://plumbers911chicago\.com[^"]*)"', html):
            samples.add(m.group(1))
print(f"Unique old WP URLs: {len(samples)}")
for u in sorted(list(samples))[:20]:
    print(f"  {u}")
