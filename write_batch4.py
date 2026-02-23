"""Items 26-45: 10 Chicago neighborhood pages + 5 comparison pages + neighborhoods hub."""
import json, os, math

DATA_DIR = r"C:\Users\User\OneDrive\Desktop\p911\site\data"

NEIGHBORHOODS = [
    ("lincoln-park", "Lincoln Park", "One of Chicago's most desirable neighborhoods, Lincoln Park features a mix of vintage brownstones, modern condos, and converted lofts. The older buildings (1880s-1920s) commonly have galvanized steel supply pipes and clay sewer lines that may need replacement. Newer condos may have copper or PEX. The neighborhood's proximity to the lake means higher water tables and more sump pump reliance."),
    ("lakeview", "Lakeview", "Home to Wrigley Field and a dense mix of vintage three-flats and modern developments, Lakeview's plumbing ranges from 100-year-old galvanized systems in classic buildings to modern PEX in new construction. Common issues include shared sewer laterals in multi-unit buildings, aging cast iron drain stacks, and frozen pipes in uninsulated porches."),
    ("logan-square", "Logan Square", "Logan Square's beautiful boulevards are lined with Greystone buildings from the early 1900s. These homes typically have original cast iron drain pipes, galvanized supply lines, and clay sewer laterals — all approaching or past their expected lifespan. Repiping and sewer replacement are among the most requested services in this neighborhood."),
    ("hyde-park", "Hyde Park", "Home to the University of Chicago, Hyde Park has a mix of large single-family homes, historic mansions, and mid-century apartment buildings. The neighborhood's older homes often have complex plumbing systems with multiple bathrooms, and the aging infrastructure frequently requires water heater upgrades, repiping, and sewer camera inspections."),
    ("wicker-park", "Wicker Park", "Wicker Park's trendy restaurants and renovated vintage buildings create unique plumbing challenges. Many buildings have been converted from single-family to multi-unit and back again, resulting in modified plumbing systems that may not meet current code. Grease trap issues from restaurants and aging sewer lines are common service calls."),
    ("bucktown", "Bucktown", "Adjacent to Wicker Park, Bucktown features renovated workers' cottages and new construction townhomes. The older homes (1890s-1920s) frequently need whole-house repiping, while newer builds occasionally have issues with improperly installed PEX or undersized water heaters for the large open-concept designs popular in the area."),
    ("pilsen", "Pilsen", "Pilsen's vibrant community features many older brick buildings with original plumbing from the early 1900s. Lead service lines are common, and the city's replacement program is active here. Common needs include water filtration systems, sewer line repair, and water heater replacement in aging two-flats."),
    ("bridgeport", "Bridgeport", "One of Chicago's oldest neighborhoods, Bridgeport has homes dating to the 1860s alongside newer development. The extremely old infrastructure means galvanized pipes, clay sewers, and outdated fixtures are the norm. Many homes here benefit from complete plumbing modernization during renovation projects."),
    ("rogers-park", "Rogers Park", "Chicago's northernmost lakefront neighborhood, Rogers Park has a high concentration of vintage apartment buildings and multi-unit residences. Common plumbing issues include aging building risers, shared water heater systems, and basement flooding due to the neighborhood's flat terrain and proximity to the lake."),
    ("edgewater", "Edgewater", "Known for its large vintage apartment buildings along the lakefront, Edgewater properties frequently need drain stack replacements, water heater upgrades for multi-unit buildings, and sump pump systems to handle the high water table. Single-family homes in the area often date to the 1920s with corresponding plumbing age."),
]

COMPARISONS = [
    {"slug": "sewer-lining-vs-sewer-replacement", "title": "Sewer Lining vs Sewer Replacement: Complete Comparison", 
     "seo": {"title": "Sewer Lining vs Sewer Replacement: Cost & Comparison", "description": "Trenchless sewer lining or full replacement? Compare cost, durability, timeline, and when each method is appropriate for your Chicago home."},
     "content": """<p>When your sewer line fails, you have two main options: trenchless lining (cured-in-place pipe or CIPP) or traditional replacement. Here's how they compare.</p>

<h2 id="comparison">Side-by-Side Comparison</h2>
<table>
<tr><th>Factor</th><th>Sewer Lining (CIPP)</th><th>Traditional Replacement</th></tr>
<tr><td>Cost</td><td>$4,000-$15,000</td><td>$3,000-$25,000</td></tr>
<tr><td>Timeline</td><td>1 day</td><td>2-5 days</td></tr>
<tr><td>Excavation</td><td>Minimal (1-2 small access points)</td><td>Full trench along pipe</td></tr>
<tr><td>Landscape damage</td><td>Minimal</td><td>Significant (yard, driveway, sidewalk)</td></tr>
<tr><td>Lifespan</td><td>50+ years</td><td>50-100+ years</td></tr>
<tr><td>Pipe diameter</td><td>Slightly reduced (liner thickness)</td><td>Same or larger</td></tr>
<tr><td>Works for</td><td>Cracks, root damage, joint failures</td><td>Collapsed pipes, severe bellying, complete failure</td></tr>
</table>

<h2 id="lining">Choose Lining When:</h2>
<ul>
<li>Pipe is structurally intact but has cracks, root intrusion, or joint failures</li>
<li>Pipe runs under a driveway, patio, or landscaping you want to preserve</li>
<li>You need the fastest possible repair</li>
<li>Budget allows for the typically higher per-foot cost</li>
</ul>

<h2 id="replacement">Choose Replacement When:</h2>
<ul>
<li>Pipe has collapsed or has severe bellying (sag)</li>
<li>Pipe diameter is too small (can upsize during replacement)</li>
<li>Multiple problems along the entire length</li>
<li>The line runs through easily accessible yard</li>
</ul>

<p><strong>Need a sewer diagnosis?</strong> A <a href="/chicago-il-plumbing/sewer-camera-inspection/">sewer camera inspection</a> determines which method is right. Call <a href="tel:8337586911">833-758-6911</a>.</p>"""},

    {"slug": "submersible-vs-pedestal-sump-pump", "title": "Submersible vs Pedestal Sump Pump: Which Is Better?",
     "seo": {"title": "Submersible vs Pedestal Sump Pump Comparison", "description": "Submersible or pedestal sump pump? Compare noise, lifespan, cost, power, and which type is best for Chicago basements."},
     "content": """<p>Choosing between submersible and pedestal sump pumps is the first decision when installing or replacing your pump. Here's a detailed comparison.</p>

<h2 id="table">Comparison Table</h2>
<table>
<tr><th>Feature</th><th>Submersible</th><th>Pedestal</th></tr>
<tr><td>Motor location</td><td>Sealed inside pit, underwater</td><td>On a shaft above the pit</td></tr>
<tr><td>Noise</td><td>Quiet (water muffles motor)</td><td>Louder (motor exposed to air)</td></tr>
<tr><td>Lifespan</td><td>5-15 years</td><td>15-25 years</td></tr>
<tr><td>Cost</td><td>$100-$400</td><td>$60-$200</td></tr>
<tr><td>Horsepower</td><td>1/3 to 1 HP</td><td>1/3 to 1/2 HP</td></tr>
<tr><td>Handles solids</td><td>Yes (screened intake)</td><td>Less effectively</td></tr>
<tr><td>Pit size needed</td><td>Standard 18"+ diameter</td><td>Can work in smaller pits</td></tr>
<tr><td>Maintenance</td><td>Must remove from pit to service</td><td>Easy access above pit</td></tr>
<tr><td>Finished basement</td><td>Better (hidden, quiet)</td><td>Visible shaft above pit</td></tr>
</table>

<h2 id="recommendation">Our Recommendation for Chicago</h2>
<p><strong>Submersible is the better choice for most Chicago homes.</strong> It's quieter, more powerful, handles debris better, and is completely hidden in the pit — important for finished basements. The shorter lifespan is offset by the superior performance during Chicago's heavy storms.</p>

<p>Call <a href="tel:8337586911">833-758-6911</a> for <a href="/chicago-il-plumbing/sump-pump-install-replacement/">sump pump installation</a>.</p>"""},

    {"slug": "point-of-use-vs-whole-house-water-filter", "title": "Point-of-Use vs Whole-House Water Filter: Which Is Right?",
     "seo": {"title": "Point-of-Use vs Whole-House Water Filter Comparison", "description": "Point-of-use under-sink filter or whole-house system? Compare cost, what each removes, maintenance, and which suits your needs."},
     "content": """<p>Water filtration systems come in two main categories: point-of-use (POU) filters that treat water at a single faucet, and whole-house (POE) systems that treat all water entering your home.</p>

<h2 id="comparison">Comparison</h2>
<table>
<tr><th>Factor</th><th>Point-of-Use (Under-Sink)</th><th>Whole-House</th></tr>
<tr><td>Treats</td><td>One faucet (drinking/cooking water)</td><td>All water in the home</td></tr>
<tr><td>Cost</td><td>$150-$500 installed</td><td>$1,000-$3,000+ installed</td></tr>
<tr><td>Filter changes</td><td>Every 6-12 months ($20-$60)</td><td>Every 3-12 months ($50-$200)</td></tr>
<tr><td>Removes chlorine</td><td>Yes</td><td>Yes</td></tr>
<tr><td>Removes lead</td><td>Yes (if NSF 53 certified)</td><td>Some models (check specs)</td></tr>
<tr><td>Protects appliances</td><td>No</td><td>Yes (removes sediment, chlorine)</td></tr>
<tr><td>Better shower water</td><td>No</td><td>Yes (less chlorine, softer skin/hair)</td></tr>
</table>

<h2 id="recommendation">Which Should You Choose?</h2>
<ul>
<li><strong>Just want better drinking water?</strong> Point-of-use under-sink filter is the cost-effective choice</li>
<li><strong>Concerned about lead?</strong> Under-sink reverse osmosis system (best lead removal)</li>
<li><strong>Want filtered water everywhere?</strong> Whole-house carbon filter</li>
<li><strong>Maximum protection?</strong> Whole-house filter + under-sink RO for drinking water</li>
</ul>

<p>Call <a href="tel:8337586911">833-758-6911</a> for <a href="/chicago-il-plumbing/water-filter-installation-replacement/">water filter installation</a>.</p>"""},

    {"slug": "electric-vs-gas-water-heater", "title": "Electric vs Gas Water Heater: Complete Comparison for Chicago",
     "seo": {"title": "Electric vs Gas Water Heater: Chicago Comparison", "description": "Electric or gas water heater? Compare cost, efficiency, recovery time, and which is better for Chicago homes."},
     "content": """<p>Most Chicago homes have access to natural gas (Peoples Gas or Nicor Gas), giving you the choice between electric and gas water heaters. Here's how to decide.</p>

<h2 id="comparison">Comparison</h2>
<table>
<tr><th>Factor</th><th>Gas</th><th>Electric</th></tr>
<tr><td>Purchase cost</td><td>$400-$1,000</td><td>$300-$800</td></tr>
<tr><td>Installation cost</td><td>Higher (gas line, venting)</td><td>Lower (electrical connection)</td></tr>
<tr><td>Monthly operating cost</td><td>$30-$50 (cheaper in Chicago)</td><td>$40-$80</td></tr>
<tr><td>Recovery rate (50 gal)</td><td>~40 gallons/hour</td><td>~20 gallons/hour</td></tr>
<tr><td>Lifespan</td><td>8-12 years</td><td>10-15 years</td></tr>
<tr><td>Efficiency</td><td>60-70% standard, 90%+ high-eff</td><td>95-100% (nearly all energy heats water)</td></tr>
<tr><td>Works during power outage</td><td>Yes (if pilot/standing pilot)</td><td>No</td></tr>
<tr><td>Venting required</td><td>Yes (exhaust gases)</td><td>No</td></tr>
<tr><td>Safety</td><td>CO risk if improperly vented</td><td>No combustion risks</td></tr>
</table>

<h2 id="chicago">For Chicago Homes</h2>
<p><strong>Gas is usually the better choice</strong> because natural gas is significantly cheaper than electricity in the Chicago area. A gas water heater also recovers faster, which matters for larger families. However, electric is better if you don't have a gas line to the water heater location, or if you're planning to go all-electric with solar panels.</p>

<p>Call <a href="tel:8337586911">833-758-6911</a> for <a href="/chicago-il-plumbing/water-heater-installation/">water heater installation</a>.</p>"""},
]

def make_neighborhood_content(name, description):
    return f"""<p>Looking for a licensed plumber in <strong>{name}, Chicago</strong>? Plumbers 911 provides 24/7 plumbing services to {name} residents and businesses. Our licensed, bonded, and insured plumbers know the unique plumbing challenges of this neighborhood.</p>

<h2 id="about">Plumbing in {name}</h2>
<p>{description}</p>

<h2 id="services">Services Available in {name}</h2>
<ul>
<li><a href="/chicago-il-plumbing/emergency-plumber/">24/7 Emergency Plumbing</a></li>
<li><a href="/chicago-il-plumbing/drain-cleaning/">Drain Cleaning</a></li>
<li><a href="/chicago-il-plumbing/sewer-replacement/">Sewer Line Repair & Replacement</a></li>
<li><a href="/chicago-il-plumbing/water-heater-repair/">Water Heater Repair & Installation</a></li>
<li><a href="/chicago-il-plumbing/whole-house-repiping/">Whole House Repiping</a></li>
<li><a href="/chicago-il-plumbing/bathroom-remodeling/">Bathroom & Kitchen Remodeling</a></li>
<li><a href="/chicago-il-plumbing/water-leak-detection-repair/">Water Leak Detection</a></li>
<li><a href="/chicago-il-plumbing/sump-pump-install-replacement/">Sump Pump Installation</a></li>
<li><a href="/chicago-il-plumbing/">View all 30+ services</a></li>
</ul>

<h2 id="why">Why {name} Residents Choose Plumbers 911</h2>
<ul>
<li>Licensed Illinois plumbers who know {name}'s building stock</li>
<li>24/7 emergency response — typically 30-60 minutes</li>
<li>Upfront pricing with written estimates</li>
<li>All permits handled for you</li>
<li>Satisfaction guaranteed</li>
</ul>

<p><strong>Need a plumber in {name}?</strong> Call <a href="tel:8337586911">833-758-6911</a> now. Available 24/7.</p>"""


def main():
    path = os.path.join(DATA_DIR, "blog_posts.json")
    with open(path, "r", encoding="utf-8") as f:
        posts = json.load(f)
    existing = {p["slug"] for p in posts}
    added = 0

    # Neighborhood pages
    for slug, name, desc in NEIGHBORHOODS:
        full_slug = f"plumber-{slug}-chicago"
        if full_slug in existing:
            print(f"  SKIP: {full_slug}")
            continue
        content = make_neighborhood_content(name, desc)
        words = len(content.split())
        posts.append({
            "id": str(14000 + added), "title": f"Plumber in {name}, Chicago — 24/7 Plumbing Service",
            "slug": full_slug, "url_path": f"/blog/{full_slug}",
            "date": "2026-02-23 12:00:00", "modified": "2026-02-23 12:00:00",
            "author": "Plumbers 911 Chicago", "content": content, "excerpt": "",
            "seo": {"title": f"Plumber in {name} Chicago | Plumbers 911", "description": f"Licensed plumber in {name}, Chicago. 24/7 emergency service, drain cleaning, sewer repair, water heaters. Call 833-758-6911."},
            "images": [], "categories": [{"slug": "neighborhoods", "name": "Chicago Neighborhoods"}],
            "tags": [{"slug": "chicago", "name": "chicago"}], "featured_image_id": "",
            "reading_time": str(max(1, math.ceil(words / 225))) + " min read",
        })
        added += 1
        print(f"  ADDED: {full_slug} ({words} words)")

    # Comparison pages
    for comp in COMPARISONS:
        if comp["slug"] in existing:
            print(f"  SKIP: {comp['slug']}")
            continue
        words = len(comp["content"].split())
        posts.append({
            "id": str(14100 + added), "title": comp["title"], "slug": comp["slug"],
            "url_path": "/blog/" + comp["slug"], "date": "2026-02-23 11:00:00",
            "modified": "2026-02-23 11:00:00", "author": "Plumbers 911 Chicago",
            "content": comp["content"], "excerpt": "", "seo": comp["seo"], "images": [],
            "categories": [{"slug": "guides", "name": "Guides"}], "tags": [],
            "featured_image_id": "",
            "reading_time": str(max(1, math.ceil(words / 225))) + " min read",
        })
        added += 1
        print(f"  ADDED: {comp['slug']} ({words} words)")

    # Neighborhoods hub page
    hub_slug = "chicago-neighborhoods-we-serve"
    if hub_slug not in existing:
        hub_content = '<p>Plumbers 911 Chicago serves every neighborhood in the city. Here are some of the communities where we\'re most active:</p>\n<ul>\n'
        for slug, name, _ in NEIGHBORHOODS:
            hub_content += f'<li><a href="/blog/plumber-{slug}-chicago/">Plumber in {name}</a></li>\n'
        hub_content += '</ul>\n<p>Don\'t see your neighborhood? We serve all of Chicago. Call <a href="tel:8337586911">833-758-6911</a>.</p>'
        words = len(hub_content.split())
        posts.append({
            "id": "14200", "title": "Chicago Neighborhoods We Serve | Plumbers 911",
            "slug": hub_slug, "url_path": "/blog/" + hub_slug,
            "date": "2026-02-23 13:00:00", "modified": "2026-02-23 13:00:00",
            "author": "Plumbers 911 Chicago", "content": hub_content, "excerpt": "",
            "seo": {"title": "Chicago Neighborhoods We Serve | Plumbers 911", "description": "Plumbers 911 serves every Chicago neighborhood. Lincoln Park, Lakeview, Logan Square, Hyde Park, Wicker Park, and more. Call 833-758-6911."},
            "images": [], "categories": [{"slug": "service-areas", "name": "Service Areas"}],
            "tags": [], "featured_image_id": "", "reading_time": "1 min read",
        })
        added += 1
        print(f"  ADDED: {hub_slug}")

    with open(path, "w", encoding="utf-8") as f:
        json.dump(posts, f, indent=2, ensure_ascii=False)
    print(f"\nDone. {added} new pages. Total: {len(posts)}")

if __name__ == "__main__":
    main()
