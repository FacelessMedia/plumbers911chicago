"""
Phases 101-103: Create 3 pillar content pages (ultimate guides).
These are long-form, comprehensive guides that serve as hub content.
"""
import json, os

DATA_DIR = r"C:\Users\User\OneDrive\Desktop\p911\site\data"

PILLAR_PAGES = [
    {
        "slug": "complete-guide-plumbing-chicago",
        "title": "The Complete Guide to Plumbing Services in Chicago (2026)",
        "date": "2026-02-22 08:00:00",
        "modified": "2026-02-22 08:00:00",
        "author": "Plumbers 911 Chicago",
        "categories": [{"slug": "guides", "name": "Guides"}],
        "tags": [{"slug": "chicago", "name": "chicago"}, {"slug": "plumbing-guide", "name": "plumbing guide"}],
        "seo": {
            "title": "Complete Guide to Plumbing Services in Chicago (2026)",
            "description": "Everything Chicago homeowners need to know about plumbing: services, costs, codes, seasonal tips, and how to choose a plumber. Comprehensive 2026 guide."
        },
        "content": """<p>Whether you've just bought your first Chicago bungalow or you've been maintaining a vintage Greystone for decades, plumbing is one of those systems you can't ignore. Chicago's unique combination of aging infrastructure, extreme weather swings, and strict building codes means plumbing here works differently than most other cities.</p>

<p>This comprehensive guide covers everything a Chicago homeowner needs to know about residential plumbing — from understanding your home's systems to choosing the right plumber, managing costs, and preventing the most common problems.</p>

<nav class="toc">
<h2>Table of Contents</h2>
<ol>
<li><a href="#understanding">Understanding Your Chicago Home's Plumbing</a></li>
<li><a href="#services">Types of Plumbing Services</a></li>
<li><a href="#costs">Plumbing Costs in Chicago</a></li>
<li><a href="#codes">Chicago Plumbing Codes & Permits</a></li>
<li><a href="#seasonal">Seasonal Plumbing Concerns</a></li>
<li><a href="#choosing">How to Choose a Plumber</a></li>
<li><a href="#emergency">Emergency Plumbing</a></li>
<li><a href="#maintenance">Preventive Maintenance</a></li>
</ol>
</nav>

<h2 id="understanding">1. Understanding Your Chicago Home's Plumbing</h2>

<p>Chicago's housing stock is diverse — from pre-1900 workers' cottages to modern high-rises — and each era brought different plumbing materials and practices.</p>

<h3>Common Pipe Materials in Chicago Homes</h3>

<table>
<tr><th>Material</th><th>Era</th><th>Lifespan</th><th>Common Issues</th></tr>
<tr><td>Lead</td><td>Pre-1940s</td><td>100+ years (but toxic)</td><td>Health hazard — Chicago is actively replacing these</td></tr>
<tr><td>Galvanized Steel</td><td>1920s-1960s</td><td>40-70 years</td><td>Corrosion, reduced flow, rust-colored water</td></tr>
<tr><td>Cast Iron (drain)</td><td>Pre-1970s</td><td>75-100 years</td><td>Corrosion, cracks, root intrusion at joints</td></tr>
<tr><td>Copper</td><td>1960s-present</td><td>50-70 years</td><td>Pinhole leaks from water chemistry, joint failures</td></tr>
<tr><td>PVC/ABS (drain)</td><td>1970s-present</td><td>50-100+ years</td><td>Joint failures, not for hot water supply</td></tr>
<tr><td>PEX</td><td>1990s-present</td><td>40-50+ years</td><td>Fewer issues; flexible, freeze-resistant</td></tr>
<tr><td>Clay (sewer)</td><td>Pre-1960s</td><td>50-60 years</td><td>Root intrusion, cracking, bellying</td></tr>
</table>

<p>If your Chicago home was built before 1960, there's a good chance you have galvanized supply pipes and clay sewer lines — both of which may be at or past their expected lifespan. Homes built between 1960-1990 likely have copper supply lines, which are still serviceable but may develop pinhole leaks. Modern homes (1990+) often use PEX supply lines and PVC drains.</p>

<h3>Chicago's Water Supply</h3>
<p>Chicago draws its water from Lake Michigan, one of the cleanest large-city water sources in the country. The city's water treatment facilities produce water that meets or exceeds all federal standards. However, the journey from the treatment plant to your faucet may introduce contaminants — particularly if your home or the city's service line is made of lead.</p>

<p><strong>Water hardness:</strong> Chicago's water is moderately hard at approximately 8 grains per gallon (140 ppm). This isn't extreme, but it's enough to cause mineral buildup in water heaters, faucet aerators, and dishwashers over time. A water softener can help, but isn't strictly necessary for most Chicago homes.</p>

<h3>Chicago's Sewer System</h3>
<p>Chicago operates a <strong>combined sewer system</strong>, meaning both stormwater and wastewater flow through the same pipes. During heavy rainfall, this system can become overwhelmed, leading to basement backups — a common and costly problem for Chicago homeowners. The Metropolitan Water Reclamation District (MWRD) manages the system, and the city has invested billions in the Tunnel and Reservoir Plan (TARP, or "Deep Tunnel") to reduce flooding, but backups still occur.</p>

<h2 id="services">2. Types of Plumbing Services</h2>

<p>Plumbing services fall into several categories. Here's what each involves:</p>

<h3>Emergency Plumbing</h3>
<p>Available 24/7, <a href="/chicago-il-plumbing/emergency-plumber/">emergency plumbing</a> covers situations that can't wait: burst pipes, sewer backups, gas leaks, and complete loss of water. In Chicago, the most common winter emergency is frozen and burst pipes, while summer storms drive sewer backup calls. Emergency service typically costs more than scheduled visits, but the speed of response prevents far greater damage.</p>

<h3>Drain & Sewer Services</h3>
<p>The most frequently requested plumbing services in Chicago:</p>
<ul>
<li><a href="/chicago-il-plumbing/drain-cleaning/">Drain Cleaning</a> — Clearing clogs using cables, hydro-jetting, or enzymatic treatments</li>
<li><a href="/chicago-il-plumbing/sewer-camera-inspection/">Sewer Camera Inspection</a> — HD video to diagnose sewer line problems without excavation</li>
<li><a href="/chicago-il-plumbing/sewer-cleaning/">Sewer Cleaning</a> — Clearing main sewer line blockages</li>
<li><a href="/chicago-il-plumbing/sewer-replacement/">Sewer Replacement</a> — Full line replacement when repair isn't viable</li>
<li><a href="/chicago-il-plumbing/drain-replacement/">Drain Replacement</a> — Replacing deteriorated interior drain lines</li>
</ul>

<h3>Water Heater Services</h3>
<p>Water heaters are the second-most expensive appliance in most homes to operate. Chicago homeowners choose between:</p>
<ul>
<li><a href="/chicago-il-plumbing/water-heater-repair/">Tank Water Heater Repair</a> — Fixing thermostat, element, valve, or anode rod issues</li>
<li><a href="/chicago-il-plumbing/water-heater-installation/">Tank Water Heater Installation</a> — Replacing units typically every 10-12 years</li>
<li><a href="/chicago-il-plumbing/tankless-water-heater-repair/">Tankless Water Heater Repair</a> — Descaling, igniter, and component repairs</li>
<li><a href="/chicago-il-plumbing/tankless-water-heater-installation/">Tankless Water Heater Installation</a> — Upgrading to on-demand hot water</li>
</ul>

<h3>Bathroom & Kitchen Plumbing</h3>
<ul>
<li><a href="/chicago-il-plumbing/bathroom-remodeling/">Bathroom Remodeling</a> — Fixture installation, pipe rerouting, rough-in work</li>
<li><a href="/chicago-il-plumbing/kitchen-remodeling/">Kitchen Remodeling</a> — Sink relocation, dishwasher, garbage disposal, pot fillers</li>
<li><a href="/chicago-il-plumbing/faucet-repair/">Faucet Repair & Replacement</a></li>
<li><a href="/chicago-il-plumbing/toilet-install/">Toilet Installation</a></li>
</ul>

<h3>Water Line Services</h3>
<ul>
<li><a href="/chicago-il-plumbing/whole-house-repiping/">Whole House Repiping</a> — Replacing all supply pipes (common in pre-1960 homes)</li>
<li><a href="/chicago-il-plumbing/frozen-broken-pipe-repair/">Frozen & Broken Pipe Repair</a></li>
<li><a href="/chicago-il-plumbing/backflow-testing-installation/">Backflow Testing & Installation</a></li>
<li><a href="/chicago-il-plumbing/water-leak-detection-repair/">Water Leak Detection & Repair</a></li>
</ul>

<h2 id="costs">3. Plumbing Costs in Chicago (2026)</h2>

<p>Chicago plumbing costs are influenced by the high cost of living, strict code requirements, and the complexity of working with aging infrastructure. Here are typical ranges:</p>

<table>
<tr><th>Service</th><th>Typical Cost Range</th></tr>
<tr><td>Emergency service call</td><td>$150 - $300</td></tr>
<tr><td>Drain cleaning</td><td>$150 - $500</td></tr>
<tr><td>Sewer camera inspection</td><td>$200 - $500</td></tr>
<tr><td>Sewer replacement</td><td>$3,000 - $25,000+</td></tr>
<tr><td>Water heater repair</td><td>$150 - $800</td></tr>
<tr><td>Water heater replacement (tank)</td><td>$1,500 - $3,500</td></tr>
<tr><td>Water heater replacement (tankless)</td><td>$2,500 - $5,500</td></tr>
<tr><td>Faucet replacement</td><td>$200 - $600</td></tr>
<tr><td>Toilet replacement</td><td>$200 - $500</td></tr>
<tr><td>Whole house repiping</td><td>$4,000 - $15,000+</td></tr>
<tr><td>Frozen pipe repair</td><td>$200 - $1,000+</td></tr>
<tr><td>Bathroom remodel (plumbing only)</td><td>$2,000 - $10,000+</td></tr>
</table>

<p>These ranges reflect plumbing labor and materials only. Permits, surface restoration, and contractor coordination (for remodels) are additional. Always get at least 2-3 written estimates from licensed plumbers before committing to major work.</p>

<h2 id="codes">4. Chicago Plumbing Codes & Permits</h2>

<p>Chicago has its own plumbing code, separate from the state of Illinois. Key things homeowners should know:</p>

<ul>
<li><strong>Licensed plumbers required</strong> — All plumbing work (beyond simple fixture swaps) must be performed by or supervised by a licensed plumber</li>
<li><strong>Permits required</strong> for: water heater installation, sewer work, gas lines, new fixture installations, remodeling, and any work that modifies the plumbing system</li>
<li><strong>Inspections</strong> are required after permitted work before walls are closed</li>
<li><strong>Backflow prevention</strong> testing is required annually for commercial properties</li>
<li><strong>Lead service line replacement</strong> is being managed citywide — check chicagowaterquality.org for your address</li>
</ul>

<p>A reputable plumber handles all permitting and inspections as part of their service. If a plumber suggests skipping the permit, that's a red flag. <a href="/blog/chicago-plumbing-code-homeowners-guide/">Read our detailed Chicago plumbing code guide</a>.</p>

<h2 id="seasonal">5. Seasonal Plumbing Concerns in Chicago</h2>

<h3>Winter (December - March)</h3>
<ul>
<li><strong>Frozen pipes</strong> — Chicago's #1 winter plumbing problem. Insulate exposed pipes, let faucets drip during extreme cold</li>
<li><strong>Water heater strain</strong> — Incoming water drops to 37-42°F, making heaters work harder</li>
<li><strong>Sump pump ice</strong> — Discharge lines can freeze, causing pump failure</li>
</ul>
<p><a href="/blog/prevent-frozen-pipes-chicago-winter/">Read our complete frozen pipe prevention guide</a>.</p>

<h3>Spring (April - June)</h3>
<ul>
<li><strong>Sump pump testing</strong> — Test before spring rains hit</li>
<li><strong>Sewer backups</strong> — Heavy spring rains overwhelm combined sewers</li>
<li><strong>Outdoor faucet restoration</strong> — Reconnect hoses, check for winter damage</li>
</ul>

<h3>Summer (July - September)</h3>
<ul>
<li><strong>Sewer line stress</strong> — Tree roots are most active, seeking water</li>
<li><strong>Garbage disposal overload</strong> — Cookout season increases disposal usage</li>
<li><strong>Sprinkler system issues</strong> — Backflow prevention required</li>
</ul>

<h3>Fall (October - November)</h3>
<ul>
<li><strong>Winterization</strong> — Disconnect hoses, insulate pipes, service water heater</li>
<li><strong>Drain maintenance</strong> — Clear drains before heavy use over holidays</li>
<li><strong>Water heater flushing</strong> — Annual maintenance before winter demand increases</li>
</ul>

<h2 id="choosing">6. How to Choose a Plumber in Chicago</h2>

<p>Not all plumbers are created equal. Here's what to look for:</p>

<ol>
<li><strong>Valid Illinois plumbing license</strong> — Verify at idfpr.illinois.gov</li>
<li><strong>Insurance</strong> — Liability insurance and workers' compensation are essential</li>
<li><strong>Google reviews</strong> — Look for 4+ stars with 50+ reviews</li>
<li><strong>Transparent pricing</strong> — Written estimates before work begins, no "discovery" fees</li>
<li><strong>24/7 availability</strong> — Emergencies don't wait for business hours</li>
<li><strong>Warranty</strong> — Reputable plumbers stand behind their work</li>
<li><strong>Permits</strong> — They should handle all permitting without you asking</li>
</ol>

<p><strong>Red flags:</strong> Unusually low quotes (often leads to upselling), no license, cash-only, no written estimate, pressure to decide immediately.</p>

<h2 id="emergency">7. Emergency Plumbing in Chicago</h2>

<p>If you have a plumbing emergency:</p>
<ol>
<li><strong>Gas leak?</strong> Leave the building, call 911, then call Peoples Gas (866-556-6002)</li>
<li><strong>Water emergency?</strong> Shut off the main water valve, then call a plumber</li>
<li><strong>Sewer backup?</strong> Stop using all water fixtures, call a plumber</li>
</ol>

<p>Plumbers 911 Chicago is available 24/7 for emergencies at <a href="tel:8337586911">833-758-6911</a>. We typically dispatch a licensed plumber within 30-60 minutes in the Chicago metro area.</p>

<p><a href="/blog/emergency-plumber-checklist-what-to-do/">Read our complete emergency plumber checklist</a>.</p>

<h2 id="maintenance">8. Preventive Maintenance Checklist</h2>

<p>The best plumbing repair is the one you never need. Here's an annual maintenance schedule:</p>

<h3>Monthly</h3>
<ul>
<li>Check under sinks for leaks</li>
<li>Test sump pump (pour water in pit)</li>
<li>Run water in unused fixtures to prevent trap drying</li>
</ul>

<h3>Quarterly</h3>
<ul>
<li>Clean faucet aerators</li>
<li>Check water heater for leaks or unusual sounds</li>
<li>Clear slow drains before they become clogs</li>
</ul>

<h3>Annually</h3>
<ul>
<li>Flush water heater tank</li>
<li>Inspect/replace water heater anode rod (every 2-3 years)</li>
<li>Professional drain cleaning for main lines</li>
<li>Test water pressure (should be 40-80 PSI)</li>
<li>Inspect visible pipes for corrosion or leaks</li>
<li>Test all shutoff valves to ensure they work</li>
</ul>

<h2>Get Expert Help</h2>

<p>Whether you need emergency service, routine maintenance, or a major plumbing project, Plumbers 911 Chicago is here to help. Our licensed, bonded, and insured plumbers serve over 188 cities across the Chicago metropolitan area.</p>

<p><strong>Call <a href="tel:8337586911">833-758-6911</a></strong> for a free estimate or to schedule service. We're available 24/7 for emergencies.</p>

<ul>
<li><a href="/chicago-il-plumbing/">View all our plumbing services</a></li>
<li><a href="/service-area/">Check if we serve your area</a></li>
<li><a href="/contact-us/">Request a call back</a></li>
<li><a href="/blog/">Read more plumbing tips and guides</a></li>
</ul>"""
    },
]


def main():
    path = os.path.join(DATA_DIR, "blog_posts.json")
    with open(path, "r", encoding="utf-8") as f:
        posts = json.load(f)

    existing_slugs = {p["slug"] for p in posts}
    added = 0

    for post in PILLAR_PAGES:
        if post["slug"] in existing_slugs:
            print(f"  SKIP: {post['slug']}")
            continue
        import math
        word_count = len(post["content"].split())
        full_post = {
            "id": str(10000 + added),
            "title": post["title"],
            "slug": post["slug"],
            "url_path": "/guide/" + post["slug"],
            "date": post["date"],
            "modified": post["modified"],
            "author": post["author"],
            "content": post["content"],
            "excerpt": "",
            "seo": post["seo"],
            "images": [],
            "categories": post.get("categories", []),
            "tags": post.get("tags", []),
            "featured_image_id": "",
            "reading_time": str(max(1, math.ceil(word_count / 225))) + " min read",
        }
        posts.append(full_post)
        added += 1
        print(f"  ADDED: {post['slug']} ({len(post['content'])} chars, {word_count} words)")

    with open(path, "w", encoding="utf-8") as f:
        json.dump(posts, f, indent=2, ensure_ascii=False)

    print(f"\nDone. {added} pillar pages added. Total posts: {len(posts)}")


if __name__ == "__main__":
    main()
