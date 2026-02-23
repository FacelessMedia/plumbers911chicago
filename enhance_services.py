"""
Phase 18-25: Enhance priority service pages with FAQ sections, cost info, and process steps.
Appends new content to existing service page content in services.json.
"""
import json
import os

DATA_DIR = r"C:\Users\User\OneDrive\Desktop\p911\site\data"

# Service-specific enhancements: FAQ, cost ranges, process steps
ENHANCEMENTS = {
    "sewer-replacement": {
        "cost_section": """
<h2>Sewer Replacement Cost in Chicago</h2>
<p>The cost of sewer replacement in Chicago typically ranges from <strong>$3,000 to $25,000+</strong> depending on several factors:</p>
<ul>
<li><strong>Length of sewer line</strong> — Longer lines require more excavation and materials</li>
<li><strong>Depth of the pipe</strong> — Deeper pipes in Chicago's clay soil increase labor costs</li>
<li><strong>Method used</strong> — Traditional dig vs. trenchless (pipe bursting or pipe lining)</li>
<li><strong>Permits</strong> — Chicago requires plumbing permits for sewer work, typically $50-$500</li>
<li><strong>Landscaping restoration</strong> — Replacing driveways, sidewalks, or landscaping after excavation</li>
</ul>
<p>We provide <strong>free estimates</strong> with transparent, upfront pricing. No hidden fees. Call <a href="tel:8337586911">833-758-6911</a> for a quote specific to your property.</p>
""",
        "process_section": """
<h2>Our Sewer Replacement Process</h2>
<ol>
<li><strong>Sewer Camera Inspection</strong> — We start with a video inspection to identify the exact location, type, and extent of damage</li>
<li><strong>Assessment &amp; Options</strong> — We explain your options: traditional replacement, trenchless pipe bursting, or pipe lining</li>
<li><strong>Transparent Quote</strong> — You receive a detailed, written estimate before any work begins</li>
<li><strong>Permit &amp; Utility Locating</strong> — We handle all Chicago permits and JULIE utility locates</li>
<li><strong>Excavation or Trenchless Install</strong> — Our licensed plumbers complete the replacement using the agreed-upon method</li>
<li><strong>Inspection &amp; Backfill</strong> — City inspection, backfill, and surface restoration</li>
<li><strong>Warranty &amp; Follow-Up</strong> — All work comes with a warranty and we follow up to ensure satisfaction</li>
</ol>
""",
        "faq": [
            ("How long does sewer replacement take in Chicago?", "Most residential sewer replacements in Chicago take 1-3 days. Trenchless methods can sometimes be completed in a single day. Factors like pipe depth, length, and soil conditions can affect the timeline."),
            ("Does homeowners insurance cover sewer replacement?", "Standard homeowners insurance typically does not cover sewer line replacement due to normal wear and tear. However, some policies offer optional sewer line coverage. We recommend checking with your insurance provider. We can provide documentation to support any claims."),
            ("What are signs I need sewer replacement vs. repair?", "Signs you may need full replacement include: recurring backups despite cleaning, multiple sections of pipe damage visible on camera inspection, bellied (sagging) pipe sections, pipes made of Orangeburg or deteriorated clay, and persistent sewer odors in your yard."),
            ("Is trenchless sewer replacement available in Chicago?", "Yes, we offer trenchless sewer replacement methods including pipe bursting and pipe lining for qualifying properties in Chicago. These methods minimize yard disruption and can reduce costs. A camera inspection determines if your line qualifies for trenchless repair."),
        ],
    },
    "drain-replacement": {
        "cost_section": """
<h2>Drain Replacement Cost in Chicago</h2>
<p>Drain replacement costs in the Chicago area typically range from <strong>$500 to $5,000+</strong> depending on:</p>
<ul>
<li><strong>Location of the drain</strong> — Under-slab drains cost more than accessible pipe runs</li>
<li><strong>Type of drain</strong> — Kitchen, bathroom, floor drains, and main drain lines vary in complexity</li>
<li><strong>Material</strong> — PVC, ABS, or cast iron replacement options</li>
<li><strong>Access requirements</strong> — Whether walls, floors, or concrete need to be opened</li>
</ul>
<p>Call <a href="tel:8337586911">833-758-6911</a> for a free estimate. We provide upfront pricing with no hidden fees.</p>
""",
        "process_section": """
<h2>Our Drain Replacement Process</h2>
<ol>
<li><strong>Drain Camera Inspection</strong> — We use HD cameras to locate the exact problem area</li>
<li><strong>Diagnosis &amp; Options</strong> — We determine if repair, partial replacement, or full replacement is needed</li>
<li><strong>Upfront Quote</strong> — Clear pricing before any work starts</li>
<li><strong>Professional Replacement</strong> — Licensed plumbers replace the damaged section with code-compliant materials</li>
<li><strong>Testing &amp; Cleanup</strong> — We test the new drain for proper flow and clean up the work area</li>
</ol>
""",
        "faq": [
            ("How do I know if my drain needs replacement vs. cleaning?", "If you experience recurring clogs despite professional cleaning, slow drains throughout the house, gurgling sounds, or foul odors, you may need drain replacement. A camera inspection can definitively show the condition of your pipes."),
            ("What causes drain pipes to fail in Chicago homes?", "Common causes include: age (many Chicago homes have original clay or cast iron pipes from 50-100+ years ago), tree root intrusion, ground settling causing pipe bellies, corrosion from Chicago's hard water, and freeze-thaw cycles damaging pipe joints."),
            ("Can you replace drains without tearing up my floor?", "In many cases, yes. We offer trenchless and minimally invasive techniques. However, under-slab drains in basements sometimes require concrete removal. We always discuss the least disruptive option first."),
        ],
    },
    "emergency-plumber": {
        "cost_section": """
<h2>Emergency Plumbing Costs in Chicago</h2>
<p>Emergency plumbing service rates depend on the type of repair needed:</p>
<ul>
<li><strong>Emergency service call</strong> — Starting from $150-$300 for diagnosis and minor repairs</li>
<li><strong>Burst pipe repair</strong> — $200-$1,000+ depending on location and damage</li>
<li><strong>Sewer backup</strong> — $300-$800 for emergency clearing</li>
<li><strong>Water heater failure</strong> — $200-$500 for emergency repair, more for replacement</li>
<li><strong>Gas leak response</strong> — Varies; always call 911 first for gas emergencies</li>
</ul>
<p>We offer transparent pricing even for emergencies. <strong>No surprise fees.</strong> Call <a href="tel:8337586911">833-758-6911</a> — available 24/7.</p>
""",
        "process_section": """
<h2>What to Do in a Plumbing Emergency</h2>
<ol>
<li><strong>Shut off the water</strong> — Locate your main water shutoff valve and turn it off to prevent flooding</li>
<li><strong>Call us immediately</strong> — <a href="tel:8337586911">833-758-6911</a>. We dispatch a plumber right away, 24/7</li>
<li><strong>Contain the damage</strong> — Use towels, buckets, or a wet/dry vacuum to manage water while you wait</li>
<li><strong>Don't attempt DIY fixes</strong> — Improper repairs can worsen the situation and void warranties</li>
<li><strong>Document the damage</strong> — Take photos for insurance purposes before cleanup begins</li>
</ol>
""",
        "faq": [
            ("How fast can an emergency plumber get to my Chicago home?", "We typically dispatch a licensed plumber within 30-60 minutes for emergencies in the Chicago metro area. Response times may vary based on location and current demand, but we prioritize emergencies 24/7."),
            ("What qualifies as a plumbing emergency?", "Plumbing emergencies include: burst or frozen pipes, sewer backups into your home, no water supply, gas leaks (call 911 first), overflowing toilets that can't be stopped, and water heater leaks or failures. If in doubt, call us — we'll help you assess the situation."),
            ("Do you charge extra for nights, weekends, or holidays?", "Our emergency rates are competitive and transparent. While emergency service may cost more than scheduled appointments, we never add hidden surcharges. You'll receive a clear quote before any work begins."),
        ],
    },
    "water-heater-repair": {
        "cost_section": """
<h2>Water Heater Repair Costs in Chicago</h2>
<p>Water heater repair in Chicago typically costs <strong>$150 to $800</strong> depending on the issue:</p>
<ul>
<li><strong>Thermostat replacement</strong> — $150-$300</li>
<li><strong>Heating element replacement</strong> — $200-$400</li>
<li><strong>Anode rod replacement</strong> — $200-$350</li>
<li><strong>Gas valve replacement</strong> — $300-$600</li>
<li><strong>Pilot light / igniter repair</strong> — $150-$300</li>
<li><strong>Tank leak repair</strong> — Often requires full replacement ($800-$2,500+)</li>
</ul>
<p>Not sure if you need repair or replacement? We provide honest assessments. If your water heater is over 10-12 years old, replacement may be more cost-effective. Call <a href="tel:8337586911">833-758-6911</a> for a free diagnosis.</p>
""",
        "process_section": "",
        "faq": [
            ("Should I repair or replace my water heater?", "Consider replacement if: your water heater is over 10-12 years old, repair costs exceed 50% of replacement cost, you're experiencing frequent breakdowns, or you notice rust in your hot water. We'll give you an honest recommendation."),
            ("Why is my water heater not producing hot water?", "Common causes include: a tripped circuit breaker (electric), a pilot light that went out (gas), a faulty thermostat, a broken heating element, or sediment buildup in the tank. Our plumbers diagnose the exact issue and explain your options."),
            ("How long does water heater repair take?", "Most water heater repairs are completed in 1-2 hours. Parts availability can sometimes extend this. We stock common replacement parts on our trucks to minimize wait times."),
        ],
    },
    "tankless-water-heater-repair": {
        "cost_section": """
<h2>Tankless Water Heater Repair Costs</h2>
<p>Tankless water heater repair in Chicago ranges from <strong>$200 to $1,200</strong> depending on the issue and brand:</p>
<ul>
<li><strong>Descaling / flushing</strong> — $150-$300 (Chicago's hard water makes this essential annually)</li>
<li><strong>Igniter / flame rod replacement</strong> — $200-$400</li>
<li><strong>Heat exchanger repair</strong> — $500-$1,200</li>
<li><strong>Flow sensor replacement</strong> — $200-$400</li>
<li><strong>Control board replacement</strong> — $400-$800</li>
</ul>
<p>We service all major brands including Rinnai, Navien, Noritz, Rheem, and Takagi. Call <a href="tel:8337586911">833-758-6911</a> for expert tankless water heater service.</p>
""",
        "process_section": "",
        "faq": [
            ("Why does my tankless water heater keep shutting off?", "Common causes include: mineral buildup from Chicago's hard water restricting flow, a dirty air filter, inadequate gas supply, frozen condensate lines in winter, or error codes indicating a specific component failure. Our technicians diagnose the exact issue using the unit's diagnostic codes."),
            ("How often should a tankless water heater be serviced?", "In the Chicago area, we recommend annual flushing/descaling due to our hard water conditions. Hard water causes mineral buildup that reduces efficiency and can damage the heat exchanger. Regular maintenance extends the life of your unit to 20+ years."),
            ("Do you work on all tankless water heater brands?", "Yes, our licensed plumbers are experienced with all major brands including Rinnai, Navien, Noritz, Rheem, Takagi, Bosch, and EcoSmart. We stock common parts for faster repairs."),
        ],
    },
    "bathroom-remodeling": {
        "cost_section": """
<h2>Bathroom Remodeling Plumbing Costs in Chicago</h2>
<p>Plumbing costs for bathroom remodeling in Chicago typically range from <strong>$2,000 to $10,000+</strong> depending on scope:</p>
<ul>
<li><strong>Fixture replacement</strong> (faucets, toilet, showerhead) — $500-$2,000</li>
<li><strong>Bathtub/shower replacement</strong> — $1,500-$5,000 including plumbing</li>
<li><strong>Pipe rerouting</strong> — $1,000-$4,000 for moving drain or supply lines</li>
<li><strong>Full rough-in</strong> (new bathroom layout) — $3,000-$8,000+</li>
</ul>
<p>We work with your contractor or handle the plumbing portion independently. Free estimates available — call <a href="tel:8337586911">833-758-6911</a>.</p>
""",
        "process_section": "",
        "faq": [
            ("Do I need a plumber for a bathroom remodel?", "Yes. Any work involving drain lines, supply lines, or fixture installation requires a licensed plumber in Chicago. This includes moving or adding plumbing fixtures, replacing pipes behind walls, and connecting new showers, tubs, or toilets."),
            ("Can you move plumbing fixtures to a new location?", "Yes, we can relocate toilets, sinks, showers, and bathtubs. This involves rerouting drain and supply lines, which requires permits in Chicago. We handle all permitting and ensure work meets code."),
            ("How long does bathroom remodel plumbing take?", "The plumbing portion typically takes 2-5 days depending on complexity. Simple fixture swaps may take a single day, while full rough-ins with pipe rerouting can take a week. We coordinate with your general contractor's timeline."),
        ],
    },
    "bathtub-install": {
        "cost_section": """
<h2>Bathtub Installation Cost in Chicago</h2>
<p>Bathtub installation plumbing costs in Chicago range from <strong>$1,000 to $5,000+</strong>:</p>
<ul>
<li><strong>Standard bathtub replacement</strong> (same location) — $1,000-$2,500</li>
<li><strong>Bathtub-to-shower conversion</strong> — $2,000-$4,000</li>
<li><strong>Freestanding tub installation</strong> — $1,500-$3,500</li>
<li><strong>Whirlpool/jetted tub installation</strong> — $2,500-$5,000+ (requires electrical work too)</li>
</ul>
<p>These prices include plumbing labor and connections. Tub cost is separate. Call <a href="tel:8337586911">833-758-6911</a> for a precise quote.</p>
""",
        "process_section": "",
        "faq": [
            ("Can you convert my bathtub to a walk-in shower?", "Yes, bathtub-to-shower conversions are one of our most popular services. We handle all plumbing modifications including drain relocation, supply line adjustments, and valve installation. We work with your contractor for the finished installation."),
            ("How long does bathtub installation take?", "A straightforward bathtub replacement in the same location typically takes 1-2 days for the plumbing work. Conversions or new installations requiring pipe rerouting may take 2-3 days."),
            ("Do I need a permit for bathtub installation in Chicago?", "Yes, plumbing permits are typically required in Chicago for bathtub installations, especially if drain lines are being modified. We handle all permit applications and inspections as part of our service."),
        ],
    },
    "commercial-plumbing": {
        "cost_section": """
<h2>Commercial Plumbing Services &amp; Pricing</h2>
<p>Commercial plumbing costs vary significantly based on the scope of work:</p>
<ul>
<li><strong>Commercial drain cleaning</strong> — $200-$800</li>
<li><strong>Grease trap installation/cleaning</strong> — $300-$2,000</li>
<li><strong>Backflow preventer testing &amp; certification</strong> — $100-$300</li>
<li><strong>Commercial water heater service</strong> — $300-$1,500</li>
<li><strong>Tenant improvement plumbing</strong> — Custom quotes based on scope</li>
<li><strong>Preventive maintenance contracts</strong> — Monthly plans available</li>
</ul>
<p>We serve restaurants, retail, offices, multi-unit residential, and industrial facilities throughout Chicago. Call <a href="tel:8337586911">833-758-6911</a> for a commercial plumbing consultation.</p>
""",
        "process_section": "",
        "faq": [
            ("Do you offer commercial plumbing maintenance contracts?", "Yes, we offer preventive maintenance plans for commercial properties. Regular maintenance prevents costly emergencies and ensures compliance with Chicago plumbing codes. Plans include scheduled inspections, drain cleaning, water heater service, and priority emergency response."),
            ("Can you work around our business hours?", "Absolutely. We understand that plumbing work in commercial spaces needs to minimize business disruption. We offer after-hours, weekend, and overnight service to accommodate your schedule."),
            ("Are you licensed for commercial plumbing in Chicago?", "Yes, all our plumbers are fully licensed, bonded, and insured for both residential and commercial work in Chicago and throughout Illinois. We carry the required liability and workers' compensation insurance for commercial projects."),
        ],
    },
}


def build_faq_html(faqs):
    """Build FAQ accordion HTML."""
    html = '<h2>Frequently Asked Questions</h2>\n<div class="faq-list">\n'
    for q, a in faqs:
        html += f'  <details class="faq-item">\n'
        html += f'    <summary>{q}</summary>\n'
        html += f'    <p>{a}</p>\n'
        html += f'  </details>\n'
    html += '</div>\n'
    return html


def build_faq_schema(service_name, faqs):
    """Build FAQ schema JSON-LD."""
    entities = []
    for q, a in faqs:
        entities.append({
            "@type": "Question",
            "name": q,
            "acceptedAnswer": {"@type": "Answer", "text": a}
        })
    schema = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": entities
    }
    return '<script type="application/ld+json">\n' + json.dumps(schema, indent=2) + '\n</script>'


def enhance_services():
    path = os.path.join(DATA_DIR, "services.json")
    with open(path, "r", encoding="utf-8") as f:
        services = json.load(f)

    enhanced = 0
    for svc in services:
        slug = svc.get("service_slug", "")
        url_path = svc.get("url_path", "")

        # Only enhance Chicago service pages (not Arlington Heights)
        if slug not in ENHANCEMENTS:
            continue
        if "arlington-heights" in url_path:
            continue

        enh = ENHANCEMENTS[slug]
        content = svc.get("content", "")

        # Don't re-enhance if already done
        if "Frequently Asked Questions" in content:
            print(f"  SKIP (already enhanced): {slug}")
            continue

        additions = ""

        # Add cost section
        if enh.get("cost_section"):
            additions += enh["cost_section"]

        # Add process section
        if enh.get("process_section"):
            additions += enh["process_section"]

        # Add FAQ HTML
        if enh.get("faq"):
            additions += build_faq_html(enh["faq"])
            additions += build_faq_schema(svc.get("service_name", ""), enh["faq"])

        # Add CTA
        additions += """
<div style="background:#f5f5f5; border-left:4px solid #e52521; padding:1.25rem; margin:2rem 0; border-radius:4px;">
<p style="margin:0; font-weight:700; font-size:1.05rem;">Ready to get started? Call Plumbers 911 Chicago at <a href="tel:8337586911">833-758-6911</a> for a free estimate. Licensed, bonded, and insured. Available 24/7.</p>
</div>
"""

        svc["content"] = content + additions
        enhanced += 1
        print(f"  ENHANCED: {slug} (+{len(additions)} chars)")

    # Write back
    with open(path, "w", encoding="utf-8") as f:
        json.dump(services, f, indent=2, ensure_ascii=False)

    print(f"\nDone. {enhanced} service pages enhanced.")


if __name__ == "__main__":
    enhance_services()
