"""Check what content exists to determine which batch items are done."""
import json, os

# Blog posts
posts = json.load(open("data/blog_posts.json", "r", encoding="utf-8"))
print(f"Blog posts: {len(posts)}")
for p in posts[-25:]:
    print(f"  {p['slug']}")

# Check for neighborhood pages
print("\nNeighborhood pages in dist:")
nbr = os.path.join("dist", "neighborhoods")
if os.path.exists(nbr):
    for d in os.listdir(nbr):
        print(f"  /neighborhoods/{d}/")

# Check for special pages
special = ["plumbing-cost-estimator", "plumbing-glossary", "careers", 
           "financing", "warranties", "our-process", "coupons",
           "pipe-material-guide", "water-heater-sizing",
           "plumbing-near-me", "cheap-plumber-chicago", 
           "best-plumber-chicago", "licensed-plumber-chicago",
           "24-hour-plumber-chicago", "new-homeowner-checklist",
           "remodel-plumbing-checklist", "winterization-checklist"]
print("\nSpecial pages:")
for s in special:
    path = os.path.join("dist", s, "index.html")
    exists = "YES" if os.path.exists(path) else "NO"
    print(f"  /{s}/ -> {exists}")

# Check for county hubs
print("\nCounty hubs:")
for c in ["lake-county", "kane-county", "mchenry-county"]:
    path = os.path.join("dist", c, "index.html")
    exists = "YES" if os.path.exists(path) else "NO"
    print(f"  /{c}/ -> {exists}")

# Check combo pages
print("\nCombo pages:")
combos_dir = os.path.join("dist")
for slug in ["emergency-plumber-naperville", "water-heater-repair-joliet",
             "drain-cleaning-schaumburg", "sewer-replacement-oak-lawn"]:
    path = os.path.join("dist", slug, "index.html")
    exists = "YES" if os.path.exists(path) else "NO"
    print(f"  /{slug}/ -> {exists}")
