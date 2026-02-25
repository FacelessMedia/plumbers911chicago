"""Analyze Search Console data to inform site architecture decisions."""
import csv
import json
import os
from collections import defaultdict

# Load Pages.csv
pages_data = []
csv_path = r"C:\Users\User\OneDrive\Desktop\p911\plumbers911chicago.com-Performance-on-Search-2026-02-22\Pages.csv"
with open(csv_path, encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        pages_data.append({
            'url': row['Top pages'],
            'clicks': int(row['Clicks']),
            'impressions': int(row['Impressions'].replace(',', '')),
            'ctr': row['CTR'],
            'position': float(row['Position'])
        })

# Load Queries.csv
queries_data = []
q_path = r"C:\Users\User\OneDrive\Desktop\p911\plumbers911chicago.com-Performance-on-Search-2026-02-22\Queries.csv"
with open(q_path, encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        queries_data.append({
            'query': row['Top queries'],
            'clicks': int(row['Clicks']),
            'impressions': int(row['Impressions'].replace(',', '')),
            'ctr': row['CTR'],
            'position': float(row['Position'])
        })

# Categorize pages
location_pages = []
service_pages = []  # chicago-il-plumbing/service-slug
combo_pages = []    # arlington-heights-il-plumbing/service-slug
blog_pages = []
other_pages = []

for p in pages_data:
    url = p['url'].replace('https://plumbers911chicago.com/', '').rstrip('/')
    if '/chicago-il-plumbing/' in p['url'] and url.count('/') >= 2:
        service_pages.append(p)
    elif '/arlington-heights-il-plumbing/' in p['url'] and url.count('/') >= 2:
        combo_pages.append(p)
    elif '-il-plumbing' in url and '/' not in url.strip('/'):
        location_pages.append(p)
    elif any(kw in url for kw in ['how-', 'what-', 'can-', 'do-', 'why-']):
        blog_pages.append(p)
    else:
        other_pages.append(p)

print("=" * 80)
print("PLUMBERS 911 CHICAGO — SITE ARCHITECTURE ANALYSIS")
print("=" * 80)

# ---- OVERALL STATS ----
total_clicks = sum(p['clicks'] for p in pages_data)
total_impressions = sum(p['impressions'] for p in pages_data)
print(f"\nOVERALL: {total_clicks} clicks, {total_impressions:,} impressions across {len(pages_data)} pages")

# ---- PAGE TYPE PERFORMANCE ----
print("\n" + "=" * 80)
print("PAGE TYPE PERFORMANCE BREAKDOWN")
print("=" * 80)

for label, group in [
    ("Homepage", [p for p in pages_data if p['url'].rstrip('/') == 'https://plumbers911chicago.com']),
    ("Location Pages (city-il-plumbing)", location_pages),
    ("Service Pages (chicago-il-plumbing/X)", service_pages),
    ("Combo Pages (arlington-heights/X)", combo_pages),
    ("Blog Posts", blog_pages),
    ("Other (about, contact, service-area)", other_pages),
]:
    clicks = sum(p['clicks'] for p in group)
    imps = sum(p['impressions'] for p in group)
    avg_pos = sum(p['position'] for p in group) / len(group) if group else 0
    with_clicks = sum(1 for p in group if p['clicks'] > 0)
    print(f"\n  {label}:")
    print(f"    Pages: {len(group)} | With clicks: {with_clicks}")
    print(f"    Clicks: {clicks} | Impressions: {imps:,}")
    print(f"    Avg Position: {avg_pos:.1f}")

# ---- LOCATION PAGE DEEP DIVE ----
print("\n" + "=" * 80)
print("LOCATION PAGES — DEEP DIVE")
print("=" * 80)

loc_with_clicks = [p for p in location_pages if p['clicks'] > 0]
loc_zero_clicks = [p for p in location_pages if p['clicks'] == 0]

print(f"\nTotal location pages in GSC: {len(location_pages)}")
print(f"  With clicks: {len(loc_with_clicks)} ({len(loc_with_clicks)/len(location_pages)*100:.1f}%)")
print(f"  Zero clicks: {len(loc_zero_clicks)} ({len(loc_zero_clicks)/len(location_pages)*100:.1f}%)")

print(f"\nTotal location clicks: {sum(p['clicks'] for p in location_pages)}")
print(f"Total location impressions: {sum(p['impressions'] for p in location_pages):,}")

print("\nTOP 20 LOCATION PAGES BY CLICKS:")
for p in sorted(location_pages, key=lambda x: x['clicks'], reverse=True)[:20]:
    city = p['url'].split('/')[-2] if p['url'].endswith('/') else p['url'].split('/')[-1]
    print(f"  {p['clicks']:3d} clicks | {p['impressions']:6,} imps | pos {p['position']:5.1f} | {city}")

print("\nTOP 20 LOCATION PAGES BY IMPRESSIONS (0 clicks):")
for p in sorted(loc_zero_clicks, key=lambda x: x['impressions'], reverse=True)[:20]:
    city = p['url'].split('/')[-2] if p['url'].endswith('/') else p['url'].split('/')[-1]
    print(f"  {p['impressions']:6,} imps | pos {p['position']:5.1f} | {city}")

# ---- IMPRESSION TIERS ----
print("\n" + "=" * 80)
print("LOCATION PAGE IMPRESSION TIERS")
print("=" * 80)
tiers = [
    (10000, "10K+"),
    (5000, "5K-10K"),
    (2000, "2K-5K"),
    (1000, "1K-2K"),
    (500, "500-1K"),
    (100, "100-500"),
    (0, "Under 100"),
]
prev = float('inf')
for threshold, label in tiers:
    tier_pages = [p for p in location_pages if threshold <= p['impressions'] < prev]
    avg_pos = sum(p['position'] for p in tier_pages) / len(tier_pages) if tier_pages else 0
    clicks = sum(p['clicks'] for p in tier_pages)
    print(f"  {label:12s}: {len(tier_pages):3d} pages | {clicks:3d} clicks | avg pos {avg_pos:.1f}")
    prev = threshold

# ---- SERVICE PAGES ----
print("\n" + "=" * 80)
print("SERVICE PAGES (chicago-il-plumbing/X) — PERFORMANCE")
print("=" * 80)
for p in sorted(service_pages, key=lambda x: x['impressions'], reverse=True)[:30]:
    slug = p['url'].split('chicago-il-plumbing/')[-1].rstrip('/')
    print(f"  {p['clicks']:3d} clicks | {p['impressions']:6,} imps | pos {p['position']:5.1f} | {slug}")

# ---- COMBO PAGES (Arlington Heights) ----
print("\n" + "=" * 80)
print("COMBO PAGES (arlington-heights-il-plumbing/X)")
print("=" * 80)
total_combo_clicks = sum(p['clicks'] for p in combo_pages)
total_combo_imps = sum(p['impressions'] for p in combo_pages)
print(f"Total: {len(combo_pages)} pages | {total_combo_clicks} clicks | {total_combo_imps:,} impressions")
for p in sorted(combo_pages, key=lambda x: x['impressions'], reverse=True)[:15]:
    slug = p['url'].split('arlington-heights-il-plumbing/')[-1].rstrip('/')
    print(f"  {p['clicks']:3d} clicks | {p['impressions']:6,} imps | pos {p['position']:5.1f} | {slug}")

# ---- QUERY ANALYSIS: CITY-SPECIFIC QUERIES ----
print("\n" + "=" * 80)
print("CITY-SPECIFIC SEARCH QUERIES WITH HIGHEST DEMAND")
print("=" * 80)

city_queries = defaultdict(lambda: {'impressions': 0, 'clicks': 0, 'queries': []})
city_keywords = set()

# Load location index to get city names
loc_index_path = r"C:\Users\User\OneDrive\Desktop\p911\site\data\location_index.json"
with open(loc_index_path) as f:
    loc_index = json.load(f)
for loc in loc_index:
    city_keywords.add(loc['city_name'].lower())

for q in queries_data:
    query_lower = q['query'].lower()
    for city in city_keywords:
        if city in query_lower and city not in ('summit', 'union', 'bristol', 'wayne', 'harvard', 'geneva', 'morris', 'peru'):
            city_queries[city]['impressions'] += q['impressions']
            city_queries[city]['clicks'] += q['clicks']
            city_queries[city]['queries'].append(q)
            break

print("\nTOP 30 CITIES BY SEARCH DEMAND (query impressions):")
for city, data in sorted(city_queries.items(), key=lambda x: x[1]['impressions'], reverse=True)[:30]:
    print(f"  {city:25s}: {data['impressions']:7,} imps | {data['clicks']:3d} clicks | {len(data['queries']):3d} unique queries")

# ---- DOORWAY PAGE RISK ANALYSIS ----
print("\n" + "=" * 80)
print("DOORWAY PAGE RISK ANALYSIS")
print("=" * 80)

# Count location pages with very low engagement
ultra_low = [p for p in location_pages if p['impressions'] < 50]
low = [p for p in location_pages if 50 <= p['impressions'] < 500]
medium = [p for p in location_pages if 500 <= p['impressions'] < 5000]
high = [p for p in location_pages if p['impressions'] >= 5000]

print(f"\n  Ultra-low engagement (<50 imps):  {len(ultra_low)} pages — HIGH doorway risk")
print(f"  Low engagement (50-500 imps):     {len(low)} pages — MODERATE doorway risk")
print(f"  Medium engagement (500-5K imps):  {len(medium)} pages — LOW doorway risk")
print(f"  High engagement (5K+ imps):       {len(high)} pages — NO doorway risk")

# How many of the 248 cities DON'T have pages yet?
county_map_path = r"C:\Users\User\OneDrive\Desktop\p911\site\data\county_map.json"
with open(county_map_path) as f:
    county_map = json.load(f)

all_248_cities = set()
for county, cities in county_map.items():
    for city_obj in cities:
        if isinstance(city_obj, dict):
            all_248_cities.add(city_obj.get('name', ''))
        else:
            all_248_cities.add(city_obj)

existing_cities = set(loc['city_name'] for loc in loc_index)
missing_cities = all_248_cities - existing_cities

print(f"\n  Total cities in service area: {len(all_248_cities)}")
print(f"  Cities WITH pages currently: {len(existing_cities)}")
print(f"  Cities WITHOUT pages:        {len(missing_cities)}")
if missing_cities:
    print(f"  Missing: {sorted(missing_cities)[:20]}...")

# ---- CONTENT SIMILARITY CHECK ----
print("\n" + "=" * 80)
print("CONTENT TEMPLATE ANALYSIS")
print("=" * 80)

loc_path = r"C:\Users\User\OneDrive\Desktop\p911\site\data\locations.json"
with open(loc_path, encoding='utf-8') as f:
    locations = json.load(f)

# Check how similar the content is across pages
first_content = locations[0]['content'] if locations else ''
template_phrases = [
    "When you need a reliable plumber in",
    "is your trusted local choice",
    "Our team of fully licensed, bonded, and insured",
    "Fast Response Times",
    "Local Expertise",
    "Transparent Pricing",
    "Satisfaction Guaranteed",
]

matches = 0
for loc in locations:
    content = loc.get('content', '')
    matching = sum(1 for phrase in template_phrases if phrase in content)
    if matching >= 5:
        matches += 1

print(f"  Pages using near-identical template structure: {matches}/{len(locations)} ({matches/len(locations)*100:.0f}%)")
print(f"  Average content length: {sum(len(l.get('content','')) for l in locations)/len(locations):.0f} chars")

# Check for unique local details
unique_mentions = 0
for loc in locations:
    content = loc.get('content', '').lower()
    city = loc.get('city_name', '').lower()
    # Check for genuinely unique content beyond template
    has_local = any(kw in content for kw in ['population', 'founded', 'history', 'neighborhood', 'school district', 'water district', 'municipal'])
    if has_local:
        unique_mentions += 1

print(f"  Pages with genuinely unique local details: {unique_mentions}/{len(locations)}")

print("\n" + "=" * 80)
print("FINAL RECOMMENDATION DATA SUMMARY")
print("=" * 80)
print(f"""
KEY METRICS:
  - Total site clicks over period: {total_clicks}
  - Homepage accounts for: {906}/{total_clicks} clicks ({906/total_clicks*100:.0f}%)
  - Brand queries ("plumbers 911") drive: ~{334+117+50+28+28+23+14+9} clicks ({(334+117+50+28+28+23+14+9)/total_clicks*100:.0f}% of total)
  - Location pages collectively: {sum(p['clicks'] for p in location_pages)} clicks
  - Service pages collectively: {sum(p['clicks'] for p in service_pages)} clicks  
  - Combo pages collectively: {total_combo_clicks} clicks
  
LOCATION PAGES WITH ACTUAL CLICKS: {len(loc_with_clicks)}/{len(location_pages)}
  - Only {len([p for p in location_pages if p['clicks'] >= 3])} location pages got 3+ clicks
  - {len([p for p in location_pages if p['impressions'] > 10000])} pages with 10K+ impressions
  
SEARCH INTENT SIGNALS:
  - "plumber near me" type queries: massive impression volume, low position
  - City-specific queries exist for ~{len(city_queries)} unique cities
  - Most city queries are 0-click with positions 20-80+
  - Chicago is by far the dominant city in queries
  - Joliet, Arlington Heights, Park Ridge, Park Forest are distant 2nd-5th
""")
