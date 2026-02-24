"""Check which batch items from PHASES_201_400 are actually done."""
import json, os

posts = json.load(open("data/blog_posts.json", "r", encoding="utf-8"))
slugs = {p["slug"] for p in posts}

# Batch 1 items 1-15 (blog posts)
batch1_slugs = [
    "sump-pump-buying-guide-chicago",
    "how-to-read-water-meter-leak-detection",
    "garbage-disposal-dos-and-donts",
    "pex-vs-copper-piping-pros-cons-cost",
    "what-causes-sewer-gas-smell",
    "how-to-prevent-basement-flooding-chicago",
    "water-softener-vs-water-filter",
    "how-to-choose-right-toilet",
    "signs-sewer-line-needs-replacement",
    "chicago-water-quality-tap-water",
    "plumbing-tips-first-time-homebuyers-chicago",
    "how-long-plumbing-fixtures-last-lifespan",
    "hydro-jetting-vs-snaking-drain-cleaning",
    "water-heater-anode-rod-guide",
    "how-to-winterize-vacant-chicago-property",
]
print("BATCH 1 (blog posts 1-15):")
for s in batch1_slugs:
    status = "DONE" if s in slugs else "MISSING"
    print(f"  [{status}] {s}")

# Batch 2 items 26-45 (neighborhoods + comparisons)
batch2_slugs = [
    "plumber-lincoln-park-chicago", "plumber-lakeview-chicago",
    "plumber-logan-square-chicago", "plumber-hyde-park-chicago",
    "plumber-wicker-park-chicago", "plumber-bucktown-chicago",
    "plumber-pilsen-chicago", "plumber-bridgeport-chicago",
    "plumber-rogers-park-chicago", "plumber-edgewater-chicago",
    "sewer-lining-vs-sewer-replacement", "copper-vs-pex-vs-cpvc-piping",
    "sump-pump-types-submersible-vs-pedestal",
    "point-of-use-vs-whole-house-water-filter",
    "electric-vs-gas-water-heater",
]
print("\nBATCH 2 (neighborhoods + comparisons 26-40):")
for s in batch2_slugs:
    status = "DONE" if s in slugs else "MISSING"
    print(f"  [{status}] {s}")

# Batch 5 items 101-125
batch5_slugs = [
    "trenchless-sewer-repair-how-it-works",
    "plumbing-emergencies-that-cant-wait",
    "how-to-find-gas-leak-home",
    "backflow-prevention-business",
    "best-time-replace-water-heater",
    "kitchen-sink-not-draining-quick-fixes",
    "toilet-wont-flush-troubleshooting",
    "leaky-faucet-water-waste",
    "plumbing-maintenance-schedule-season",
    "what-is-sewer-cleanout-where-is-mine",
    "emergency-plumber-naperville-il",
    "water-heater-repair-joliet-il",
    "drain-cleaning-schaumburg-il",
    "sewer-replacement-oak-lawn-il",
    "lake-county-plumbing-services",
    "kane-county-plumbing-services",
    "mchenry-county-plumbing-services",
    "plumbing-near-me-chicago",
    "24-hour-plumber-chicago",
]
print("\nBATCH 5 (content + combos 101-125):")
for s in batch5_slugs:
    status = "DONE" if s in slugs else "MISSING"
    print(f"  [{status}] {s}")

# Batch 6 items 126-150
batch6_slugs = [
    "plumbing-cost-estimator", "pipe-material-identifier-guide",
    "water-heater-sizing-guide", "plumbing-glossary",
    "careers-plumbing-jobs-chicago", "plumbing-financing-payment-options",
    "plumbing-warranties-guarantees", "our-plumbing-service-process",
    "plumbing-coupons-specials-chicago",
]
print("\nBATCH 6 (tools/resources 126-150):")
for s in batch6_slugs:
    status = "DONE" if s in slugs else "MISSING"
    print(f"  [{status}] {s}")

# Batch 7 items 151-175
batch7_slugs = [
    "how-to-test-sump-pump", "whole-house-water-filter-benefits",
    "fix-leaky-shower-head", "gas-vs-electric-tankless-water-heater",
    "clear-clogged-p-trap-guide", "home-plumbing-diagram-explained",
    "water-pressure-regulator-signs-need-one",
    "new-homeowner-plumbing-checklist-chicago",
    "before-you-remodel-plumbing-checklist",
    "vacation-home-winterization-checklist",
]
print("\nBATCH 7 (more content 151-175):")
for s in batch7_slugs:
    status = "DONE" if s in slugs else "MISSING"
    print(f"  [{status}] {s}")

# Count total
total_done = sum(1 for s in batch1_slugs + batch2_slugs + batch5_slugs + batch6_slugs + batch7_slugs if s in slugs)
total_items = len(batch1_slugs + batch2_slugs + batch5_slugs + batch6_slugs + batch7_slugs)
print(f"\nTotal content items: {total_done}/{total_items} done")
print(f"Total blog posts: {len(posts)}")

# Check CSS/JS features (batches 3, 4)
css = open("assets/css/styles.css", "r", encoding="utf-8").read()
js = open("assets/js/main.js", "r", encoding="utf-8").read()
print(f"\nCSS size: {len(css)} chars")
print(f"JS size: {len(js)} chars")
print(f"Has testimonial-grid CSS: {'YES' if 'testimonial-grid' in css else 'NO'}")
print(f"Has count-up animation: {'YES' if 'count-up' in js or 'countUp' in js else 'NO'}")
print(f"Has cookie consent: {'YES' if 'cookie' in js.lower() else 'NO'}")
print(f"Has back-to-top: {'YES' if 'back-to-top' in js or 'backToTop' in js else 'NO'}")
