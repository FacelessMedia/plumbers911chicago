#!/usr/bin/env python3
"""Merge FAQ data into tier1_locations.json."""
import json, os

FAQS = {}

from _loc_faqs_1 import register as r1
from _loc_faqs_2 import register as r2
r1(FAQS)
r2(FAQS)

loc_path = os.path.join(os.path.dirname(__file__), "data", "tier1_locations.json")
with open(loc_path, "r", encoding="utf-8") as f:
    locations = json.load(f)

updated = 0
for loc in locations:
    slug = loc["city_slug"]
    if slug in FAQS:
        loc["faqs"] = FAQS[slug]
        updated += 1

with open(loc_path, "w", encoding="utf-8") as f:
    json.dump(locations, f, indent=2, ensure_ascii=False)

print(f"Updated {updated}/{len(locations)} locations with FAQs ({len(FAQS)} FAQ sets available)")
