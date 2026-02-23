"""
Phases 26-30: Enhance ALL remaining service pages with FAQ sections and cost info.
"""
import json
import os

DATA_DIR = r"C:\Users\User\OneDrive\Desktop\p911\site\data"

REMAINING = {
    "backflow-testing-installation": {
        "cost": "$150-$500 for testing; $800-$3,000+ for installation or replacement",
        "faq": [
            ("How often is backflow testing required in Chicago?", "Chicago requires annual backflow preventer testing for commercial properties and certain residential connections. We provide certified testing and submit reports directly to the city on your behalf."),
            ("What happens if I fail a backflow test?", "If your backflow preventer fails testing, it needs repair or replacement. We can handle both the repair and the re-test. The city typically gives a grace period to come into compliance."),
        ],
    },
    "dishwasher-install": {
        "cost": "$200-$500 for standard installation; $400-$800 if new supply/drain lines are needed",
        "faq": [
            ("Can you install a dishwasher where there wasn't one before?", "Yes, we can run new water supply and drain lines to accommodate a new dishwasher installation. This requires access to hot water supply and a drain connection, typically under the kitchen sink."),
            ("Do I need a plumber to install a dishwasher?", "While handy homeowners can sometimes swap a dishwasher, a licensed plumber ensures proper connections, prevents leaks, and meets Chicago code requirements — especially for new installations."),
        ],
    },
    "drain-cleaning": {
        "cost": "$150-$500 for standard drain cleaning; $300-$800 for main line cleaning with camera inspection",
        "faq": [
            ("How often should drains be professionally cleaned?", "We recommend professional drain cleaning annually for preventive maintenance, or immediately if you notice slow drains, gurgling sounds, or recurring clogs. Homes with older pipes or large trees nearby may need more frequent service."),
            ("What methods do you use for drain cleaning?", "We use multiple methods depending on the blockage: cable/snake machines for standard clogs, hydro-jetting for stubborn buildup and grease, and camera inspection to identify the root cause. We always diagnose before recommending a solution."),
        ],
    },
    "faucet-repair": {
        "cost": "$100-$350 for faucet repair; $200-$600 for faucet replacement including the fixture",
        "faq": [
            ("Should I repair or replace my leaky faucet?", "If your faucet is less than 5 years old, repair is usually cost-effective. For older faucets, especially with corroded valves or outdated styles, replacement is often the better investment. We'll give you an honest recommendation."),
            ("Can you install any brand of faucet?", "Yes, we install all major faucet brands including Moen, Delta, Kohler, American Standard, Grohe, and more. You can purchase your own fixture or we can source one for you."),
        ],
    },
    "frozen-broken-pipe-repair": {
        "cost": "$200-$1,000+ depending on location, damage extent, and whether walls/ceilings need to be opened",
        "faq": [
            ("What should I do if my pipes freeze in Chicago?", "First, shut off the main water valve. Then call us immediately at 833-758-6911. Do NOT use open flames to thaw pipes. We use safe, professional thawing methods and repair any damage from expansion."),
            ("How can I prevent frozen pipes in my Chicago home?", "Insulate exposed pipes in basements, garages, and crawl spaces. Keep cabinet doors open during extreme cold to allow warm air circulation. Let faucets drip slightly during sub-zero nights. We offer winterization services to protect your plumbing."),
        ],
    },
    "garbage-disposal-installation": {
        "cost": "$200-$600 including a standard disposal unit; $400-$900 for premium units with installation",
        "faq": [
            ("How long does garbage disposal installation take?", "A standard replacement takes about 1-2 hours. New installations where no disposal existed before may take 2-3 hours due to additional plumbing and electrical connections needed."),
            ("What size garbage disposal do I need?", "For most Chicago households, a 1/2 to 3/4 HP disposal is sufficient. Larger families or those who cook frequently may want a 1 HP model. We'll recommend the right size based on your usage."),
        ],
    },
    "gas-line-install-repair": {
        "cost": "$200-$800 for repairs; $500-$2,500+ for new gas line installation depending on length and complexity",
        "faq": [
            ("What should I do if I smell gas in my home?", "Leave the building immediately. Do NOT turn on/off any electrical switches or appliances. Call 911 and your gas company (Peoples Gas: 866-556-6002) from outside. Once cleared, call us for gas line repair."),
            ("Do you install gas lines for new appliances?", "Yes, we install gas lines for stoves, dryers, fireplaces, outdoor grills, and generators. All gas work requires permits in Chicago and must be performed by a licensed plumber. We handle everything."),
        ],
    },
    "kitchen-remodeling": {
        "cost": "$1,500-$8,000+ for the plumbing portion of a kitchen remodel",
        "faq": [
            ("What plumbing work is needed for a kitchen remodel?", "Common plumbing tasks include: relocating sink drains and supply lines, installing new faucets, connecting dishwashers, installing garbage disposals, adding pot filler faucets, and connecting ice makers or water filtration systems."),
            ("Can you move my kitchen sink to a different location?", "Yes, we can relocate kitchen sinks, which involves extending or rerouting drain and supply lines. This is common in kitchen remodels that change the layout. Permits are required in Chicago."),
        ],
    },
    "residential-plumbing": {
        "cost": "Varies by service — call for a free estimate on your specific residential plumbing needs",
        "faq": [
            ("What residential plumbing services do you offer?", "We provide comprehensive residential plumbing including: leak repair, pipe replacement, fixture installation, water heater service, drain cleaning, sewer service, bathroom and kitchen remodeling plumbing, and 24/7 emergency service."),
            ("How do I choose a good residential plumber in Chicago?", "Look for: proper licensing (Illinois plumbing license), insurance and bonding, positive Google reviews, transparent pricing, and 24/7 availability. Plumbers 911 Chicago meets all these criteria."),
        ],
    },
    "sewer-camera-inspection": {
        "cost": "$200-$500 for a standard sewer camera inspection with video recording",
        "faq": [
            ("What can a sewer camera inspection reveal?", "Our HD sewer cameras can identify: tree root intrusion, pipe cracks and breaks, bellied (sagging) sections, blockages and buildup, pipe material and condition, joint separations, and the exact location of problems for targeted repair."),
            ("When should I get a sewer camera inspection?", "We recommend camera inspections when: buying a home (especially older Chicago homes), experiencing recurring backups, before and after sewer cleaning, and as part of a maintenance routine every 2-3 years for older sewer lines."),
        ],
    },
    "sewer-cleaning": {
        "cost": "$200-$600 for standard sewer line cleaning; $400-$1,000 with camera inspection included",
        "faq": [
            ("How often should sewer lines be cleaned?", "For most Chicago homes, we recommend sewer cleaning every 1-2 years as preventive maintenance. Homes with large trees near the sewer line or older clay pipes may need annual cleaning."),
            ("What's the difference between sewer cleaning and sewer replacement?", "Sewer cleaning removes blockages and buildup from an otherwise intact pipe. Sewer replacement is needed when pipes are cracked, collapsed, or structurally compromised. A camera inspection after cleaning helps determine if replacement is needed."),
        ],
    },
    "sewer-cleanout-installation": {
        "cost": "$500-$2,000 for cleanout installation depending on location and access",
        "faq": [
            ("What is a sewer cleanout and do I need one?", "A sewer cleanout is an access point that allows plumbers to clear blockages and perform camera inspections. Chicago code requires accessible cleanouts. If your home doesn't have one, or it's buried/inaccessible, installing one saves significant time and money on future sewer service."),
            ("Where should a sewer cleanout be located?", "Ideally near the foundation wall where the sewer line exits your home, and/or near the property line. Chicago code has specific requirements. We install cleanouts in code-compliant locations."),
        ],
    },
    "sump-pump-install-replacement": {
        "cost": "$500-$2,000 for sump pump replacement; $1,500-$4,000 for new pit installation + pump",
        "faq": [
            ("How long do sump pumps last?", "Most sump pumps last 7-10 years with proper maintenance. In the Chicago area, heavy usage during spring rains and snowmelt can reduce lifespan. We recommend testing your pump regularly and replacing it proactively before failure."),
            ("Do I need a sump pump in my Chicago home?", "Most Chicago homes with basements benefit from a sump pump due to our high water table and heavy rainfall. If your basement has ever experienced moisture, dampness, or flooding, a sump pump is strongly recommended."),
        ],
    },
    "sump-pump-battery-backup-install": {
        "cost": "$500-$1,500 for battery backup sump pump installation",
        "faq": [
            ("Why do I need a battery backup sump pump?", "Power outages in Chicago often coincide with severe storms — exactly when you need your sump pump most. A battery backup ensures your basement stays dry even during prolonged power outages. It's inexpensive insurance against thousands in flood damage."),
            ("How long does a battery backup sump pump run?", "Most battery backup systems run 5-12 hours on a full charge, depending on how frequently the pump cycles. Some systems include monitoring that alerts you to battery status and pump activity."),
        ],
    },
    "tankless-water-heater-installation": {
        "cost": "$2,500-$5,000+ including the unit and installation; gas line upgrades may add $500-$1,500",
        "faq": [
            ("Is a tankless water heater worth it in Chicago?", "Tankless water heaters offer 24-40% energy savings, endless hot water, and last 20+ years vs. 10-12 for tank heaters. The higher upfront cost is offset by lower monthly bills and longer lifespan. They're especially beneficial for larger families."),
            ("Do I need to upgrade my gas line for a tankless water heater?", "Often yes. Tankless units typically require a larger gas supply than tank heaters. We assess your current gas line capacity and handle any necessary upgrades as part of the installation."),
        ],
    },
    "toilet-install": {
        "cost": "$200-$500 for toilet replacement; $400-$800 for new installation with rough-in work",
        "faq": [
            ("How long does toilet installation take?", "A straightforward toilet replacement takes 1-2 hours. New installations requiring drain rough-in take longer. We handle everything including removing the old toilet, installing the new one, and ensuring a watertight seal."),
            ("What type of toilet should I get?", "We recommend WaterSense-certified toilets that use 1.28 GPF or less for water savings. Popular brands we install include Kohler, TOTO, American Standard, and Gerber. We can advise on the best option for your bathroom layout and budget."),
        ],
    },
    "water-filter-installation-replacement": {
        "cost": "$200-$800 for under-sink systems; $1,500-$4,000 for whole-house filtration",
        "faq": [
            ("Does Chicago water need filtration?", "While Chicago's tap water meets federal standards, it may contain lead from older service lines, chlorine, and other contaminants. A quality filtration system provides an extra layer of protection, especially in older homes with lead plumbing."),
            ("What type of water filter is best for Chicago homes?", "For lead concerns, a reverse osmosis system is most effective. For general improvement, a carbon block filter removes chlorine and improves taste. Whole-house systems protect all fixtures. We help you choose the right system for your needs."),
        ],
    },
    "water-heater-installation": {
        "cost": "$1,500-$3,500 for tank water heater installation; $2,500-$5,500 for tankless installation",
        "faq": [
            ("How long does water heater installation take?", "A standard tank water heater replacement takes 2-4 hours. New installations or conversions (tank to tankless) may take 4-8 hours due to additional plumbing and potentially gas line work."),
            ("What size water heater do I need?", "For most Chicago households: 1-2 people need 30-40 gallons, 3-4 people need 40-50 gallons, 5+ people need 50-80 gallons or consider a tankless system for unlimited hot water. We'll help you size it correctly."),
        ],
    },
    "water-leak-detection-repair": {
        "cost": "$200-$500 for leak detection; repair costs vary from $150 for simple fixes to $2,000+ for hidden leaks",
        "faq": [
            ("How do you detect hidden water leaks?", "We use advanced technology including acoustic listening devices, thermal imaging cameras, and moisture meters to pinpoint hidden leaks without unnecessary demolition. This allows for targeted, minimally invasive repairs."),
            ("What are signs of a hidden water leak?", "Watch for: unexplained increases in your water bill, sounds of running water when nothing is on, warm spots on floors (hot water line leak), musty odors, mold growth, water stains on walls or ceilings, and low water pressure."),
        ],
    },
    "water-softener-installation": {
        "cost": "$1,500-$4,000 for a whole-house water softener including installation",
        "faq": [
            ("Does Chicago have hard water?", "Chicago's water hardness is moderate at about 8 grains per gallon. While not extremely hard, it's enough to cause mineral buildup in pipes and appliances, spots on dishes, and dry skin. A water softener can help."),
            ("How does a water softener work?", "Water softeners use ion exchange to remove calcium and magnesium minerals that cause hardness. Softened water extends appliance life, reduces soap usage, prevents scale buildup in pipes, and improves skin and hair health."),
        ],
    },
    "whole-house-repiping": {
        "cost": "$4,000-$15,000+ depending on home size, number of fixtures, and pipe material chosen",
        "faq": [
            ("When does a Chicago home need repiping?", "Consider repiping if: your home has original galvanized steel pipes (common in pre-1960s Chicago homes), you experience frequent leaks in different locations, water pressure is consistently low, or water has a rusty color."),
            ("How long does whole house repiping take?", "Most residential repiping takes 3-7 days depending on home size and accessibility. We work room by room to minimize disruption and restore water service as quickly as possible."),
        ],
    },
}


def build_faq_html(faqs):
    html = '<h2>Frequently Asked Questions</h2>\n<div class="faq-list">\n'
    for q, a in faqs:
        html += f'  <details class="faq-item">\n    <summary>{q}</summary>\n    <p>{a}</p>\n  </details>\n'
    html += '</div>\n'
    return html


def build_faq_schema(faqs):
    entities = [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faqs]
    schema = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": entities}
    return '<script type="application/ld+json">\n' + json.dumps(schema, indent=2) + '\n</script>'


def main():
    path = os.path.join(DATA_DIR, "services.json")
    with open(path, "r", encoding="utf-8") as f:
        services = json.load(f)

    enhanced = 0
    for svc in services:
        slug = svc.get("service_slug", "")
        url_path = svc.get("url_path", "")
        if slug not in REMAINING or "arlington-heights" in url_path:
            continue
        if "Frequently Asked Questions" in svc.get("content", ""):
            print(f"  SKIP (already done): {slug}")
            continue

        enh = REMAINING[slug]
        additions = f"""
<h2>{svc.get('service_name', slug.replace('-',' ').title())} Cost in Chicago</h2>
<p>Typical cost: <strong>{enh['cost']}</strong>. We provide free estimates with transparent upfront pricing. Call <a href="tel:8337586911">833-758-6911</a> for a quote.</p>
"""
        additions += build_faq_html(enh["faq"])
        additions += build_faq_schema(enh["faq"])
        additions += """
<div style="background:#f5f5f5; border-left:4px solid #e52521; padding:1.25rem; margin:2rem 0; border-radius:4px;">
<p style="margin:0; font-weight:700; font-size:1.05rem;">Ready to get started? Call Plumbers 911 Chicago at <a href="tel:8337586911">833-758-6911</a> for a free estimate. Licensed, bonded, and insured. Available 24/7.</p>
</div>
"""
        svc["content"] = svc.get("content", "") + additions
        enhanced += 1
        print(f"  ENHANCED: {slug} (+{len(additions)} chars)")

    with open(path, "w", encoding="utf-8") as f:
        json.dump(services, f, indent=2, ensure_ascii=False)
    print(f"\nDone. {enhanced} more service pages enhanced.")


if __name__ == "__main__":
    main()
