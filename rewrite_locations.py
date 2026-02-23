"""
Phases 37-42: Rewrite ALL location pages with unique city-specific content.
Generates SEO-rich content with local references, service highlights, and FAQs.
"""
import json
import os
import random

DATA_DIR = r"C:\Users\User\OneDrive\Desktop\p911\site\data"

# Chicago area geography data for content generation
COUNTY_MAP = {
    # Cook County
    "chicago": "Cook", "park-ridge": "Cook", "cicero": "Cook", "oak-brook": "Cook",
    "elmhurst": "DuPage", "bartlett": "DuPage/Cook", "hickory-hills": "Cook",
    "chicago-heights": "Cook", "berwyn": "Cook", "oak-lawn": "Cook",
    "des-plaines": "Cook", "evanston": "Cook", "skokie": "Cook", "niles": "Cook",
    "arlington-heights": "Cook", "palatine": "Cook", "schaumburg": "Cook",
    "elk-grove-village": "Cook", "mount-prospect": "Cook", "prospect-heights": "Cook",
    "buffalo-grove": "Cook/Lake", "northbrook": "Cook", "glenview": "Cook",
    "morton-grove": "Cook", "wilmette": "Cook", "park-forest": "Cook",
    "flossmoor": "Cook", "homewood": "Cook", "matteson": "Cook",
    "country-club-hills": "Cook", "hazel-crest": "Cook", "midlothian": "Cook",
    "oak-forest": "Cook", "tinley-park": "Cook", "orland-park": "Cook",
    "palos-heights": "Cook", "palos-hills": "Cook", "evergreen-park": "Cook",
    "bridgeview": "Cook", "burbank": "Cook", "justice": "Cook",
    "bedford-park": "Cook", "dolton": "Cook", "harvey": "Cook",
    "markham": "Cook", "robbins": "Cook", "alsip": "Cook", "blue-island": "Cook",
    "calumet-city": "Cook", "lansing": "Cook", "south-holland": "Cook",
    "posen": "Cook", "steger": "Cook", "chicago-ridge": "Cook",
    "franklin-park": "Cook", "bellwood": "Cook", "maywood": "Cook",
    "broadview": "Cook", "brookfield": "Cook", "la-grange": "Cook",
    "la-grange-park": "Cook", "western-springs": "Cook", "riverside": "Cook",
    "forest-park": "Cook", "oak-park": "Cook", "northlake": "Cook",
    "stone-park": "Cook", "melrose-park": "Cook", "hillside": "Cook",
    "berkeley": "Cook", "harwood-heights": "Cook", "norridge": "Cook",
    "schiller-park": "Cook", "streamwood": "Cook",
    # DuPage County
    "naperville": "DuPage", "wheaton": "DuPage", "glen-ellyn": "DuPage",
    "lombard": "DuPage", "carol-stream": "DuPage", "bloomingdale": "DuPage",
    "addison": "DuPage", "bensenville": "DuPage", "wood-dale": "DuPage",
    "roselle": "DuPage", "lisle": "DuPage", "downers-grove": "DuPage",
    "westmont": "DuPage", "darien": "DuPage", "woodridge": "DuPage",
    "bolingbrook": "Will/DuPage", "warrenville": "DuPage", "winfield": "DuPage",
    "west-chicago": "DuPage", "villa-park": "DuPage", "hinsdale": "DuPage",
    "clarendon-hills": "DuPage", "willowbrook": "DuPage",
    # Will County
    "joliet": "Will", "plainfield": "Will", "romeoville": "Will",
    "lockport": "Will", "homer-glen": "Will", "new-lenox": "Will",
    "mokena": "Will", "frankfort": "Will", "manhattan": "Will",
    "channahon": "Will", "minooka": "Will", "shorewood": "Will",
    "crest-hill": "Will", "elwood": "Will", "wilmington": "Will",
    "braidwood": "Will", "coal-city": "Will", "peotone": "Will",
    "monee": "Will", "university-park": "Will", "beecher": "Will",
    "oswego": "Kendall",
    # Lake County
    "waukegan": "Lake", "highland-park": "Lake", "lake-forest": "Lake",
    "lake-bluff": "Lake", "libertyville": "Lake", "mundelein": "Lake",
    "vernon-hills": "Lake", "buffalo-grove": "Lake", "gurnee": "Lake",
    "grayslake": "Lake", "round-lake": "Lake", "lake-villa": "Lake",
    "antioch": "Lake", "wauconda": "Lake", "island-lake": "Lake",
    "lake-zurich": "Lake", "north-chicago": "Lake", "zion": "Lake",
    "fort-sheridan": "Lake", "highwood": "Lake", "deerfield": "Lake",
    "lincolnshire": "Lake", "lake-in-the-hills": "McHenry",
    # Kane County
    "aurora": "Kane", "elgin": "Kane", "st-charles": "Kane",
    "geneva": "Kane", "batavia": "Kane", "carpentersville": "Kane",
    "south-elgin": "Kane", "north-aurora": "Kane", "sugar-grove": "Kane",
    "big-rock": "Kane", "elburn": "Kane", "hampshire": "Kane",
    "gilberts": "Kane", "montgomery": "Kane",
    # DeKalb County
    "dekalb": "DeKalb", "sycamore": "DeKalb", "genoa": "DeKalb",
    "cortland": "DeKalb", "malta": "DeKalb", "shabbona": "DeKalb",
    "kirkland": "DeKalb", "kingston": "DeKalb", "hinckley": "DeKalb",
    # McHenry County
    "mchenry": "McHenry", "crystal-lake": "McHenry", "woodstock": "McHenry",
    "algonquin": "McHenry", "cary": "McHenry", "fox-river-grove": "McHenry",
    "harvard": "McHenry", "marengo": "McHenry", "wonder-lake": "McHenry",
    "hebron": "McHenry", "ringwood": "McHenry", "spring-grove": "McHenry",
    "richmond": "McHenry", "union": "McHenry", "dundee": "Kane/McHenry",
    # Kendall County
    "yorkville": "Kendall", "plainfield": "Kendall/Will",
    "plano": "Kendall", "bristol": "Kendall",
    # Grundy County
    "morris": "Grundy", "channahon": "Will/Grundy", "coal-city": "Grundy",
    "braceville": "Grundy", "mazon": "Grundy", "seneca": "LaSalle/Grundy",
    # LaSalle County
    "ottawa": "LaSalle", "la-salle": "LaSalle", "peru": "LaSalle",
    "mendota": "LaSalle", "streator": "LaSalle", "marseilles": "LaSalle",
    "tonica": "LaSalle", "lostant": "LaSalle", "oglesby": "LaSalle",
    "grand-ridge": "LaSalle", "seneca": "LaSalle",
    # Kankakee County
    "blackstone": "Livingston", "pontiac": "Livingston",
    "dwight": "Livingston",
    # Livingston/Other
    "minonk": "Woodford", "rutland": "LaSalle",
}

# Common plumbing issues by region
REGIONAL_ISSUES = {
    "Cook": "aging infrastructure from pre-1960s construction, hard water mineral buildup, and winter freeze damage",
    "DuPage": "suburban water pressure issues, sump pump failures during heavy rains, and aging copper pipe corrosion",
    "Will": "new construction plumbing needs, well water system maintenance, and sewer line issues from expanding development",
    "Lake": "lakefront moisture problems, basement flooding, and freeze-thaw pipe damage during harsh winters",
    "Kane": "hard water deposits from municipal well systems, sump pump needs, and older home repiping",
    "DeKalb": "rural water system maintenance, well pump service, and agricultural area drainage issues",
    "McHenry": "well water treatment needs, septic-to-sewer conversions, and cold weather pipe protection",
    "Kendall": "rapid growth area plumbing for new construction, water softener needs, and drainage solutions",
    "Grundy": "older home plumbing upgrades, water heater replacements, and drain maintenance",
    "LaSalle": "older infrastructure maintenance, water heater service, and winter plumbing protection",
    "Livingston": "rural plumbing service, water treatment, and emergency repairs for remote properties",
    "Woodford": "agricultural area plumbing needs and water system maintenance",
}

SERVICES_LIST = [
    ("Emergency Plumbing", "/chicago-il-plumbing/emergency-plumber/"),
    ("Water Heater Repair", "/chicago-il-plumbing/water-heater-repair/"),
    ("Sewer Replacement", "/chicago-il-plumbing/sewer-replacement/"),
    ("Drain Cleaning", "/chicago-il-plumbing/drain-cleaning/"),
    ("Bathroom Remodeling", "/chicago-il-plumbing/bathroom-remodeling/"),
    ("Kitchen Plumbing", "/chicago-il-plumbing/kitchen-remodeling/"),
    ("Tankless Water Heater", "/chicago-il-plumbing/tankless-water-heater-repair/"),
    ("Sewer Camera Inspection", "/chicago-il-plumbing/sewer-camera-inspection/"),
    ("Backflow Testing", "/chicago-il-plumbing/backflow-testing-installation/"),
    ("Gas Line Service", "/chicago-il-plumbing/gas-line-install-repair/"),
    ("Frozen Pipe Repair", "/chicago-il-plumbing/frozen-broken-pipe-repair/"),
    ("Water Leak Detection", "/chicago-il-plumbing/water-leak-detection-repair/"),
]


def get_county(slug):
    return COUNTY_MAP.get(slug, "Cook")


def get_regional_issues(county):
    primary = county.split("/")[0]
    return REGIONAL_ISSUES.get(primary, "common residential and commercial plumbing challenges")


def generate_city_content(city_name, city_slug, state="IL"):
    county = get_county(city_slug)
    issues = get_regional_issues(county)

    # Pick 6 random services to highlight (different for each city for uniqueness)
    random.seed(hash(city_slug))
    highlighted = random.sample(SERVICES_LIST, min(6, len(SERVICES_LIST)))

    content = f"""<h2>Professional Plumbing Services in {city_name}, {state}</h2>

<p>When you need a reliable plumber in {city_name}, Illinois, Plumbers 911 Chicago is your trusted local choice. We provide comprehensive plumbing services to homeowners and businesses throughout {city_name} and the greater {county} County area. Our team of fully licensed, bonded, and insured plumbing professionals is available 24 hours a day, 7 days a week — including holidays and emergencies.</p>

<p>{city_name} residents face unique plumbing challenges including {issues}. Our experienced plumbers understand these local conditions and provide solutions tailored to the specific needs of {county} County properties.</p>

<h3>Why {city_name} Residents Choose Plumbers 911</h3>

<ul>
<li><strong>Fast Response Times</strong> — We dispatch licensed plumbers to {city_name} quickly, with typical arrival times of 30-60 minutes for emergencies</li>
<li><strong>Local Expertise</strong> — Our plumbers are familiar with {city_name}'s building codes, permit requirements, and common plumbing issues in {county} County</li>
<li><strong>Transparent Pricing</strong> — Free estimates with upfront pricing. No hidden fees or surprise charges</li>
<li><strong>Fully Licensed &amp; Insured</strong> — All our plumbers carry proper Illinois plumbing licenses and comprehensive insurance</li>
<li><strong>Satisfaction Guaranteed</strong> — We stand behind every job with our satisfaction guarantee</li>
</ul>

<h3>Plumbing Services Available in {city_name}</h3>

<p>We offer a complete range of residential and commercial plumbing services to {city_name} and surrounding {county} County communities:</p>

<ul>
"""
    for svc_name, svc_url in highlighted:
        content += f'<li><a href="{svc_url}"><strong>{svc_name}</strong></a> — Professional {svc_name.lower()} service for {city_name} homes and businesses</li>\n'

    content += f"""</ul>

<p>Don't see the service you need? We offer many additional plumbing services. <a href="/chicago-il-plumbing/">View all our plumbing services</a> or call us at <a href="tel:8337586911">833-758-6911</a> to discuss your specific needs.</p>

<h3>Emergency Plumbing in {city_name}, {state}</h3>

<p>Plumbing emergencies don't wait for business hours, and neither do we. If you're experiencing a burst pipe, sewer backup, gas leak, or any other plumbing emergency in {city_name}, call <a href="tel:8337586911">833-758-6911</a> immediately. We have plumbers on call 24/7 ready to respond to {city_name} emergencies.</p>

<h3>Common Plumbing Issues in {city_name}</h3>

<p>Properties in {city_name} and throughout {county} County commonly experience:</p>

<ul>
<li><strong>Sewer line problems</strong> — Tree root intrusion, aging pipes, and ground settling can damage sewer lines</li>
<li><strong>Water heater failures</strong> — Tank and tankless water heaters require regular maintenance, especially with {county} County's water conditions</li>
<li><strong>Drain clogs and backups</strong> — Kitchen, bathroom, and main line clogs are among the most common service calls</li>
<li><strong>Frozen pipes in winter</strong> — Illinois winters are harsh. Proper insulation and winterization prevent costly burst pipes</li>
<li><strong>Fixture leaks and drips</strong> — Even small leaks waste water and money. We repair and replace all types of plumbing fixtures</li>
</ul>

<h3>Serving {city_name} and Surrounding Areas</h3>

<p>In addition to {city_name}, we serve all communities throughout {county} County and the greater Chicago metropolitan area. Whether you need routine maintenance, a major repair, or a complete plumbing renovation, Plumbers 911 Chicago has you covered.</p>
"""

    # Add FAQ section
    faqs = [
        (f"How quickly can a plumber get to {city_name}?",
         f"For emergencies, we typically dispatch a licensed plumber to {city_name} within 30-60 minutes. For scheduled service, we offer same-day and next-day appointments. Call 833-758-6911 to check current availability."),
        (f"What does a plumber cost in {city_name}, IL?",
         f"Plumbing costs in {city_name} vary by service. Common services range from $150 for minor repairs to $5,000+ for major projects like sewer replacement. We provide free estimates with transparent upfront pricing — no hidden fees."),
        (f"Do you need a permit for plumbing work in {city_name}?",
         f"Many plumbing projects in {city_name} ({county} County) require permits, especially work involving sewer lines, water heaters, gas lines, and new fixture installations. Our licensed plumbers handle all permit applications and inspections as part of our service."),
    ]

    content += '<h2>Frequently Asked Questions</h2>\n<div class="faq-list">\n'
    for q, a in faqs:
        content += f'  <details class="faq-item">\n    <summary>{q}</summary>\n    <p>{a}</p>\n  </details>\n'
    content += '</div>\n'

    # FAQ Schema
    entities = [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faqs]
    schema = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": entities}
    content += '<script type="application/ld+json">\n' + json.dumps(schema, indent=2) + '\n</script>\n'

    # Final CTA
    content += f"""
<div style="background:#f5f5f5; border-left:4px solid #e52521; padding:1.25rem; margin:2rem 0; border-radius:4px;">
<p style="margin:0; font-weight:700; font-size:1.05rem;">Need a plumber in {city_name}? Call Plumbers 911 Chicago at <a href="tel:8337586911">833-758-6911</a>. Licensed, bonded, and insured. Available 24/7 for emergencies.</p>
</div>
"""
    return content


def generate_seo(city_name, city_slug):
    county = get_county(city_slug)
    return {
        "title": f"Plumber in {city_name}, IL | 24/7 Plumbing Services",
        "description": f"Licensed plumber in {city_name}, IL. 24/7 emergency plumbing, water heater repair, sewer service & more. Free estimates. Call 833-758-6911. Serving {county} County."
    }


def main():
    path = os.path.join(DATA_DIR, "locations.json")
    with open(path, "r", encoding="utf-8") as f:
        locations = json.load(f)

    rewritten = 0
    for loc in locations:
        city_name = loc.get("city_name", "")
        city_slug = loc.get("city_slug", "")
        if not city_name or not city_slug:
            continue

        # Generate new content
        new_content = generate_city_content(city_name, city_slug)
        new_seo = generate_seo(city_name, city_slug)

        loc["content"] = new_content
        loc["seo"] = new_seo
        rewritten += 1

        if rewritten <= 5 or rewritten % 50 == 0:
            print(f"  {rewritten}: {city_name} ({len(new_content)} chars)")

    with open(path, "w", encoding="utf-8") as f:
        json.dump(locations, f, indent=2, ensure_ascii=False)

    print(f"\nDone. {rewritten} location pages rewritten with unique city-specific content.")


if __name__ == "__main__":
    main()
