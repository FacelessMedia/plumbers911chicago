#!/usr/bin/env python3
"""Generate service_rewrites.json - run this script to produce the data file."""
import json, os

R = {}

def svc(slug, title, desc, html):
    R[slug] = {"seo": {"title": title, "description": desc}, "content": html}

# Import all service content modules
from _svc_content_1 import register as r1
from _svc_content_2 import register as r2
from _svc_content_3 import register as r3
from _svc_content_4 import register as r4

r1(svc)
r2(svc)
r3(svc)
r4(svc)

out = os.path.join(os.path.dirname(__file__), "data", "service_rewrites.json")
with open(out, "w", encoding="utf-8") as f:
    json.dump(R, f, indent=2, ensure_ascii=False)
print(f"Wrote {len(R)} service rewrites to {out}")
