"""
Phases 191-200: Content scaling pages.
Creates county hubs, FAQ hub, glossary, HTML sitemap, reviews page, resources page.
These are added as blog posts that the build script renders.
"""
import json, os, math

DATA_DIR = r"C:\Users\User\OneDrive\Desktop\p911\site\data"

PAGES = [
    # Phase 191: County Hub Pages
    {
        "slug": "cook-county-plumbing-services",
        "title": "Plumbing Services in Cook County, IL",
        "categories": [{"slug": "service-areas", "name": "Service Areas"}],
        "seo": {"title": "Cook County Plumbing Services | Plumbers 911 Chicago", "description": "Licensed plumbing services throughout Cook County, IL. Serving Chicago, Park Ridge, Cicero, Oak Lawn, Des Plaines, and 50+ more cities. Call 833-758-6911."},
        "content": """<p>Plumbers 911 Chicago provides comprehensive plumbing services throughout <strong>Cook County, Illinois</strong> — the most populous county in Illinois and home to over 5 million residents. From downtown Chicago to suburban communities, our licensed plumbers are available 24/7.</p>

<h2>Cities We Serve in Cook County</h2>
<p>We serve over 60 cities and villages in Cook County including:</p>
<ul>
<li><a href="/chicago-il-plumbing/">Chicago</a> — All neighborhoods from the Loop to the Far South Side</li>
<li><a href="/park-ridge-il-plumbing/">Park Ridge</a></li>
<li><a href="/cicero-il-plumbing/">Cicero</a></li>
<li><a href="/oak-lawn-il-plumbing/">Oak Lawn</a></li>
<li><a href="/des-plaines-il-plumbing/">Des Plaines</a></li>
<li><a href="/arlington-heights-il-plumbing/">Arlington Heights</a></li>
<li><a href="/elmhurst-il-plumbing/">Elmhurst</a></li>
<li><a href="/orland-park-il-plumbing/">Orland Park</a></li>
<li><a href="/schaumburg-il-plumbing/">Schaumburg</a></li>
<li>And many more — <a href="/service-area/">view our full service area</a></li>
</ul>

<h2>Cook County Plumbing Challenges</h2>
<p>Cook County properties face unique plumbing challenges due to aging infrastructure (many homes built before 1960), Chicago's combined sewer system, hard water conditions, and extreme temperature swings. Our plumbers understand these local conditions and provide targeted solutions.</p>

<h2>Available Services</h2>
<p>All Cook County locations have access to our complete range of plumbing services including <a href="/chicago-il-plumbing/emergency-plumber/">emergency plumbing</a>, <a href="/chicago-il-plumbing/water-heater-repair/">water heater service</a>, <a href="/chicago-il-plumbing/sewer-replacement/">sewer replacement</a>, <a href="/chicago-il-plumbing/drain-cleaning/">drain cleaning</a>, and <a href="/chicago-il-plumbing/">30+ more services</a>.</p>

<p><strong>Need a plumber in Cook County?</strong> Call <a href="tel:8337586911">833-758-6911</a>. Licensed, bonded, insured. Available 24/7.</p>"""
    },
    {
        "slug": "dupage-county-plumbing-services",
        "title": "Plumbing Services in DuPage County, IL",
        "categories": [{"slug": "service-areas", "name": "Service Areas"}],
        "seo": {"title": "DuPage County Plumbing Services | Plumbers 911", "description": "Professional plumbing services in DuPage County, IL. Naperville, Wheaton, Elmhurst, Lombard, and more. 24/7 emergency service. Call 833-758-6911."},
        "content": """<p>Plumbers 911 provides expert plumbing services throughout <strong>DuPage County, Illinois</strong> — the second most populous county in Illinois. Our licensed plumbers serve homeowners and businesses across all DuPage communities.</p>

<h2>Cities We Serve in DuPage County</h2>
<ul>
<li><a href="/naperville-il-plumbing/">Naperville</a></li>
<li><a href="/elmhurst-il-plumbing/">Elmhurst</a></li>
<li><a href="/lombard-il-plumbing/">Lombard</a></li>
<li><a href="/carol-stream-il-plumbing/">Carol Stream</a></li>
<li><a href="/addison-il-plumbing/">Addison</a></li>
<li><a href="/glen-ellyn-il-plumbing/">Glen Ellyn</a></li>
<li>And more — <a href="/service-area/">view full list</a></li>
</ul>

<h2>DuPage County Plumbing Needs</h2>
<p>DuPage County homes commonly experience suburban water pressure issues, sump pump failures during spring rains, and aging copper pipe corrosion. Our plumbers are experienced with the specific plumbing systems common in DuPage County construction from the 1960s-1990s expansion era.</p>

<p><strong>Call <a href="tel:8337586911">833-758-6911</a></strong> for DuPage County plumbing service. 24/7 availability.</p>"""
    },
    {
        "slug": "will-county-plumbing-services",
        "title": "Plumbing Services in Will County, IL",
        "categories": [{"slug": "service-areas", "name": "Service Areas"}],
        "seo": {"title": "Will County Plumbing Services | Plumbers 911", "description": "Licensed plumbing in Will County, IL. Joliet, Plainfield, Romeoville, New Lenox, Homer Glen. 24/7 emergency. Call 833-758-6911."},
        "content": """<p>Plumbers 911 serves homeowners and businesses throughout <strong>Will County, Illinois</strong>. As one of the fastest-growing counties in the Chicago metro, Will County has both new construction plumbing needs and aging infrastructure requiring expert service.</p>

<h2>Cities We Serve in Will County</h2>
<ul>
<li><a href="/joliet-il-plumbing/">Joliet</a></li>
<li><a href="/lockport-il-plumbing/">Lockport</a></li>
<li><a href="/homer-glen-il-plumbing/">Homer Glen</a></li>
<li><a href="/new-lenox-il-plumbing/">New Lenox</a></li>
<li><a href="/channahon-il-plumbing/">Channahon</a></li>
<li>And more — <a href="/service-area/">view full list</a></li>
</ul>

<p><strong>Call <a href="tel:8337586911">833-758-6911</a></strong> for Will County plumbing service.</p>"""
    },
    # Phase 194: FAQ Hub Page
    {
        "slug": "plumbing-faq",
        "title": "Plumbing FAQ: Answers to Common Questions",
        "categories": [{"slug": "guides", "name": "Guides"}],
        "seo": {"title": "Plumbing FAQ - Common Questions Answered | Plumbers 911", "description": "Answers to the most common plumbing questions. Emergency procedures, costs, maintenance tips, and more from Chicago plumbing experts."},
        "content": """<p>Got a plumbing question? We've compiled answers to the most frequently asked questions from Chicago homeowners.</p>

<h2>Emergency Plumbing</h2>
<div class="faq-list">
<details class="faq-item"><summary>What should I do in a plumbing emergency?</summary><p>First, shut off the water supply (main valve for major emergencies, fixture valve for localized issues). Then call <a href="tel:8337586911">833-758-6911</a> for 24/7 emergency service. <a href="/blog/emergency-plumber-checklist-what-to-do/">Read our complete emergency checklist</a>.</p></details>
<details class="faq-item"><summary>How fast can a plumber get to my home?</summary><p>For emergencies, we typically dispatch a licensed plumber within 30-60 minutes in the Chicago metro area. Scheduled service offers same-day and next-day appointments.</p></details>
<details class="faq-item"><summary>Do you charge extra for emergency/after-hours service?</summary><p>Emergency rates may be higher than scheduled appointments, but we always provide transparent, upfront pricing before starting work. No hidden fees.</p></details>
</div>

<h2>Costs & Pricing</h2>
<div class="faq-list">
<details class="faq-item"><summary>How much does a plumber cost in Chicago?</summary><p>Common services range from $150 for drain cleaning to $25,000+ for sewer replacement. We provide free estimates with written quotes before work begins. <a href="/blog/how-much-does-plumber-cost-chicago/">See our complete pricing guide</a>.</p></details>
<details class="faq-item"><summary>Do you offer free estimates?</summary><p>Yes, we provide free estimates for all non-emergency work. Even for emergencies, you'll receive a quote before we start any paid work.</p></details>
</div>

<h2>Water Heaters</h2>
<div class="faq-list">
<details class="faq-item"><summary>Should I choose a tank or tankless water heater?</summary><p>It depends on your household size, budget, and hot water usage. Tank heaters cost less upfront ($1,500-$3,500) but last 10-12 years. Tankless costs more ($2,500-$5,500) but lasts 20+ years with unlimited hot water. <a href="/blog/tank-vs-tankless-water-heater-chicago-guide/">Read our full comparison</a>.</p></details>
<details class="faq-item"><summary>How often should I flush my water heater?</summary><p>Annually. Chicago's moderately hard water causes sediment buildup that reduces efficiency. <a href="/blog/water-heater-maintenance-annual-checklist/">See our maintenance checklist</a>.</p></details>
</div>

<h2>Drains & Sewers</h2>
<div class="faq-list">
<details class="faq-item"><summary>How do I unclog a drain without chemicals?</summary><p>Try boiling water, baking soda + vinegar, a plunger, or a drain snake before calling a professional. <a href="/blog/how-to-unclog-drain-without-chemicals/">See our 5-method guide</a>.</p></details>
<details class="faq-item"><summary>How do I know if I need sewer replacement?</summary><p>Warning signs include recurring backups, multiple slow drains, sewage odors, soggy yard patches, and foundation cracks. <a href="/blog/signs-you-need-sewer-line-replacement/">Read the 8 warning signs</a>.</p></details>
</div>

<h2>General</h2>
<div class="faq-list">
<details class="faq-item"><summary>Are your plumbers licensed and insured?</summary><p>Yes, all Plumbers 911 Chicago technicians are fully licensed by the State of Illinois, bonded, and carry comprehensive liability insurance.</p></details>
<details class="faq-item"><summary>What areas do you serve?</summary><p>We serve 188+ cities across the Chicago metropolitan area including Cook, DuPage, Will, Lake, Kane, McHenry, DeKalb, Kendall, Grundy, and LaSalle counties. <a href="/service-area/">Check our full service area</a>.</p></details>
<details class="faq-item"><summary>Do I need a permit for plumbing work in Chicago?</summary><p>Many plumbing projects require permits in Chicago, including water heater installation, sewer work, and fixture additions. We handle all permitting as part of our service. <a href="/blog/chicago-plumbing-code-homeowners-guide/">Read our permit guide</a>.</p></details>
</div>

<p><strong>Have a question not listed here?</strong> Call <a href="tel:8337586911">833-758-6911</a> — we're happy to help.</p>"""
    },
    # Phase 197: HTML Sitemap
    {
        "slug": "sitemap",
        "title": "Site Map - Plumbers 911 Chicago",
        "categories": [{"slug": "navigation", "name": "Navigation"}],
        "seo": {"title": "Site Map | Plumbers 911 Chicago", "description": "Complete site map for Plumbers 911 Chicago. Find all our plumbing services, location pages, and resources."},
        "content": """<h2>Main Pages</h2>
<ul>
<li><a href="/">Homepage</a></li>
<li><a href="/about-us/">About Us</a></li>
<li><a href="/contact-us/">Contact Us</a></li>
<li><a href="/service-area/">Service Area (188+ Cities)</a></li>
<li><a href="/blog/">Plumbing Blog</a></li>
<li><a href="/privacy-policy/">Privacy Policy</a></li>
</ul>

<h2>Service Categories</h2>
<ul>
<li><a href="/kitchen-bath/">Kitchen & Bath Plumbing</a></li>
<li><a href="/sewer-drain/">Sewer & Drain Services</a></li>
<li><a href="/hot-water/">Hot Water / Water Heater Services</a></li>
<li><a href="/water-lines/">Water Line Services</a></li>
<li><a href="/other-plumbing-services/">Other Plumbing Services</a></li>
</ul>

<h2>Plumbing Services</h2>
<ul>
<li><a href="/chicago-il-plumbing/emergency-plumber/">Emergency Plumber</a></li>
<li><a href="/chicago-il-plumbing/water-heater-repair/">Water Heater Repair</a></li>
<li><a href="/chicago-il-plumbing/water-heater-installation/">Water Heater Installation</a></li>
<li><a href="/chicago-il-plumbing/tankless-water-heater-repair/">Tankless Water Heater Repair</a></li>
<li><a href="/chicago-il-plumbing/tankless-water-heater-installation/">Tankless Water Heater Installation</a></li>
<li><a href="/chicago-il-plumbing/drain-cleaning/">Drain Cleaning</a></li>
<li><a href="/chicago-il-plumbing/drain-replacement/">Drain Replacement</a></li>
<li><a href="/chicago-il-plumbing/sewer-cleaning/">Sewer Cleaning</a></li>
<li><a href="/chicago-il-plumbing/sewer-replacement/">Sewer Replacement</a></li>
<li><a href="/chicago-il-plumbing/sewer-camera-inspection/">Sewer Camera Inspection</a></li>
<li><a href="/chicago-il-plumbing/bathroom-remodeling/">Bathroom Remodeling</a></li>
<li><a href="/chicago-il-plumbing/kitchen-remodeling/">Kitchen Remodeling</a></li>
<li><a href="/chicago-il-plumbing/faucet-repair/">Faucet Repair</a></li>
<li><a href="/chicago-il-plumbing/toilet-install/">Toilet Installation</a></li>
<li><a href="/chicago-il-plumbing/frozen-broken-pipe-repair/">Frozen Pipe Repair</a></li>
<li><a href="/chicago-il-plumbing/gas-line-install-repair/">Gas Line Services</a></li>
<li><a href="/chicago-il-plumbing/backflow-testing-installation/">Backflow Testing</a></li>
<li><a href="/chicago-il-plumbing/whole-house-repiping/">Whole House Repiping</a></li>
<li><a href="/chicago-il-plumbing/water-leak-detection-repair/">Water Leak Detection</a></li>
<li><a href="/chicago-il-plumbing/commercial-plumbing/">Commercial Plumbing</a></li>
<li><a href="/chicago-il-plumbing/residential-plumbing/">Residential Plumbing</a></li>
</ul>

<h2>Guides & Resources</h2>
<ul>
<li><a href="/blog/complete-guide-plumbing-chicago/">Complete Guide to Plumbing in Chicago</a></li>
<li><a href="/blog/sewer-replacement-cost-chicago/">Sewer Replacement Cost Guide</a></li>
<li><a href="/blog/tank-vs-tankless-water-heater-chicago-guide/">Tank vs Tankless Water Heater Guide</a></li>
<li><a href="/blog/emergency-plumber-checklist-what-to-do/">Emergency Plumber Checklist</a></li>
<li><a href="/blog/prevent-frozen-pipes-chicago-winter/">Frozen Pipe Prevention Guide</a></li>
<li><a href="/blog/chicago-plumbing-code-homeowners-guide/">Chicago Plumbing Code Guide</a></li>
<li><a href="/blog/how-much-does-plumber-cost-chicago/">Plumber Cost Guide</a></li>
</ul>"""
    },
    # Phase 199: Reviews/Testimonials Page
    {
        "slug": "reviews",
        "title": "Customer Reviews - Plumbers 911 Chicago",
        "categories": [{"slug": "about", "name": "About"}],
        "seo": {"title": "Customer Reviews | Plumbers 911 Chicago", "description": "Read what our customers say about Plumbers 911 Chicago. Real reviews from real customers across the Chicago metro area."},
        "content": """<p>We're proud of the service we provide to Chicago area homeowners and businesses. Here's what our customers have to say:</p>

<div class="testimonial-grid">
<div class="testimonial-card">
<div style="color:#f4b400;margin-bottom:.5rem;">★★★★★</div>
<p><em>"Great Service"</em></p>
<p>Great service, fast return calls. I needed a plumber for my property and I'm glad I called this company.</p>
<p><strong>— Johnny L.</strong></p>
</div>

<div class="testimonial-card">
<div style="color:#f4b400;margin-bottom:.5rem;">★★★★★</div>
<p><em>"Very helpful and responsive"</em></p>
<p>Very helpful and responsive. The plumber arrived on time and explained everything clearly before starting work.</p>
<p><strong>— Luke M.</strong></p>
</div>

<div class="testimonial-card">
<div style="color:#f4b400;margin-bottom:.5rem;">★★★★★</div>
<p><em>"Highly recommend this service!"</em></p>
<p>Highly recommend this service! Professional, punctual, and the pricing was exactly as quoted. No surprises.</p>
<p><strong>— Joyce B.</strong></p>
</div>

<div class="testimonial-card">
<div style="color:#f4b400;margin-bottom:.5rem;">★★★★★</div>
<p><em>"Punctual and professional"</em></p>
<p>Punctual and professional. They fixed our water heater issue quickly and the price was fair.</p>
<p><strong>— Pete O.</strong></p>
</div>

<div class="testimonial-card">
<div style="color:#f4b400;margin-bottom:.5rem;">★★★★★</div>
<p><em>"No hassles or mess"</em></p>
<p>No hassles or mess. The plumber was courteous, cleaned up after the work, and everything works perfectly.</p>
<p><strong>— Judy S.</strong></p>
</div>

<div class="testimonial-card">
<div style="color:#f4b400;margin-bottom:.5rem;">★★★★★</div>
<p><em>"Best plumbers in the world!"</em></p>
<p>Best plumbers in the world! Fast response, excellent work quality, and great communication throughout.</p>
<p><strong>— Wayne K.</strong></p>
</div>
</div>

<h2>Leave Us a Review</h2>
<p>Had a great experience with Plumbers 911 Chicago? We'd love to hear about it! Your feedback helps us improve and helps other homeowners find reliable plumbing service.</p>
<p><a href="https://g.co/kgs/SVdH8xQ" target="_blank" rel="noopener" class="btn btn-primary">Review Us on Google</a></p>

<h2>Need Plumbing Service?</h2>
<p>Join our growing list of satisfied customers. Call <a href="tel:8337586911">833-758-6911</a> for fast, reliable, licensed plumbing service in the Chicago area.</p>"""
    },
]


def main():
    path = os.path.join(DATA_DIR, "blog_posts.json")
    with open(path, "r", encoding="utf-8") as f:
        posts = json.load(f)

    existing = {p["slug"] for p in posts}
    added = 0
    for page in PAGES:
        if page["slug"] in existing:
            print(f"  SKIP: {page['slug']}")
            continue
        words = len(page["content"].split())
        full = {
            "id": str(12000 + added),
            "title": page["title"],
            "slug": page["slug"],
            "url_path": "/blog/" + page["slug"],
            "date": "2026-02-23 08:00:00",
            "modified": "2026-02-23 08:00:00",
            "author": "Plumbers 911 Chicago",
            "content": page["content"],
            "excerpt": "",
            "seo": page["seo"],
            "images": [],
            "categories": page.get("categories", []),
            "tags": [],
            "featured_image_id": "",
            "reading_time": str(max(1, math.ceil(words / 225))) + " min read",
        }
        posts.append(full)
        added += 1
        print(f"  ADDED: {page['slug']} ({words} words)")

    with open(path, "w", encoding="utf-8") as f:
        json.dump(posts, f, indent=2, ensure_ascii=False)
    print(f"\nDone. {added} new pages. Total: {len(posts)}")


if __name__ == "__main__":
    main()
