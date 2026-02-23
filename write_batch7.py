"""Items 151-175: 10 blog posts + resource/checklist pages."""
import json, os, math

DATA_DIR = r"C:\Users\User\OneDrive\Desktop\p911\site\data"

POSTS = [
    {"slug": "how-to-test-sump-pump", "title": "How to Test Your Sump Pump (5-Minute Check)",
     "categories": [{"slug": "diy-tips", "name": "DIY Tips"}],
     "seo": {"title": "How to Test Your Sump Pump (5-Minute Check)", "description": "Test your sump pump in 5 minutes. Step-by-step instructions plus signs your pump needs repair or replacement."},
     "content": """<p>Your sump pump sits quietly in your basement until you desperately need it. Testing it monthly takes 5 minutes and can save you from a flooded basement.</p>

<h2 id="test">The 5-Minute Test</h2>
<ol>
<li><strong>Find your sump pit</strong> — Usually in the lowest part of your basement, covered by a lid</li>
<li><strong>Remove the lid</strong> and look inside. Check for debris that could clog the pump</li>
<li><strong>Pour water slowly into the pit</strong> — Use a 5-gallon bucket. Pour until the float rises</li>
<li><strong>Watch the pump activate</strong> — It should turn on automatically, pump the water out, and shut off</li>
<li><strong>Listen</strong> — The pump should run smoothly. Grinding, rattling, or humming without pumping indicates a problem</li>
</ol>

<h2 id="signs">Signs Your Pump Needs Attention</h2>
<ul>
<li><strong>Doesn't turn on:</strong> Float switch may be stuck, motor may be dead, or power may be disconnected</li>
<li><strong>Runs but doesn't pump water:</strong> Impeller may be broken or check valve may be failed</li>
<li><strong>Runs continuously:</strong> Float switch may be stuck in the "on" position, or the pump can't keep up with incoming water</li>
<li><strong>Cycles on and off rapidly:</strong> Check valve may be missing or failed, causing water to flow back into the pit</li>
<li><strong>Makes unusual noises:</strong> Bearings may be worn, or debris may be hitting the impeller</li>
<li><strong>Vibrates excessively:</strong> Impeller may be damaged or unbalanced</li>
</ul>

<h2 id="battery">Test the Battery Backup Too</h2>
<p>If you have a battery backup pump, unplug the primary pump and test the backup the same way. Replace backup batteries every 2-3 years.</p>

<p><strong>Pump not working?</strong> Call <a href="tel:8337586911">833-758-6911</a> for <a href="/chicago-il-plumbing/sump-pump-install-replacement/">sump pump service</a>.</p>"""},

    {"slug": "whole-house-water-filter-benefits", "title": "Whole House Water Filter Benefits: Is It Worth It?",
     "categories": [{"slug": "guides", "name": "Guides"}],
     "seo": {"title": "Whole House Water Filter: Benefits & Is It Worth It?", "description": "Is a whole house water filter worth the investment? Benefits for health, appliances, skin/hair, and home value. Chicago water analysis."},
     "content": """<p>A whole house water filter treats every drop of water entering your home — from the kitchen faucet to the shower to the washing machine. Here's whether it's worth the investment for Chicago homeowners.</p>

<h2 id="benefits">Key Benefits</h2>

<h3>1. Cleaner Drinking Water Everywhere</h3>
<p>Every faucet in your home delivers filtered water. No need to remember to use a specific tap for drinking or cooking.</p>

<h3>2. Better Skin and Hair</h3>
<p>Chlorine in shower water dries out skin and hair. A whole house filter removes chlorine before it reaches your shower, resulting in softer skin and healthier hair.</p>

<h3>3. Protects Appliances</h3>
<p>Filtered water extends the life of your water heater, dishwasher, and washing machine by reducing sediment and mineral buildup. This alone can save hundreds in appliance repairs.</p>

<h3>4. Cleaner Clothes</h3>
<p>Chlorine and minerals in water can dull colors and wear out fabrics faster. Filtered water keeps clothes looking newer longer.</p>

<h3>5. Reduces Plumbing Buildup</h3>
<p>Sediment and minerals in Chicago's water gradually build up inside pipes. Filtration reduces this buildup, extending pipe life.</p>

<h2 id="cost">Cost vs Value</h2>
<table>
<tr><th>Item</th><th>Cost</th></tr>
<tr><td>System purchase</td><td>$500 - $2,000</td></tr>
<tr><td>Professional installation</td><td>$500 - $1,000</td></tr>
<tr><td>Annual filter replacement</td><td>$50 - $200</td></tr>
<tr><td>Estimated savings (appliance life, bottled water)</td><td>$200 - $500/year</td></tr>
</table>

<p>For most Chicago homes, a whole house filter pays for itself within 3-5 years through appliance savings and eliminated bottled water purchases.</p>

<p><strong>Interested?</strong> Call <a href="tel:8337586911">833-758-6911</a> for <a href="/chicago-il-plumbing/water-filter-installation-replacement/">water filter installation</a>.</p>"""},

    {"slug": "fix-leaky-shower-head", "title": "How to Fix a Leaky Shower Head (DIY Guide)",
     "categories": [{"slug": "diy-tips", "name": "DIY Tips"}],
     "seo": {"title": "How to Fix a Leaky Shower Head (DIY Guide)", "description": "Fix a dripping shower head yourself. Step-by-step guide for the 3 most common causes. No plumber needed for most fixes."},
     "content": """<p>A dripping shower head wastes water and creates annoying mineral stains. Most fixes take 10-15 minutes with basic tools.</p>

<h2 id="cause1">Fix 1: Tighten the Connection</h2>
<p>The most common cause is a loose connection between the shower arm and head.</p>
<ol>
<li>Unscrew the shower head by hand (turn counterclockwise)</li>
<li>Clean old Teflon tape from the threads</li>
<li>Wrap 3-4 layers of new Teflon tape clockwise around the threads</li>
<li>Screw the head back on firmly by hand</li>
<li>Tighten 1/4 turn more with pliers (use a cloth to prevent scratching)</li>
</ol>

<h2 id="cause2">Fix 2: Clean Mineral Buildup</h2>
<p>Chicago's moderately hard water causes mineral deposits that block the shower head openings, causing water to back up and drip from the connection.</p>
<ol>
<li>Remove the shower head</li>
<li>Soak in white vinegar for 2-4 hours (or overnight for heavy buildup)</li>
<li>Scrub the nozzle holes with an old toothbrush</li>
<li>Rinse and reinstall</li>
</ol>

<h2 id="cause3">Fix 3: Replace the Washer</h2>
<p>Inside the shower head where it connects to the arm, there's a small rubber washer. If it's cracked, flattened, or missing, water leaks at the connection.</p>
<ol>
<li>Remove the shower head</li>
<li>Find the rubber washer inside the connecting end</li>
<li>Take it to a hardware store to match the size</li>
<li>Install the new washer and reconnect</li>
</ol>

<h2 id="valve">If the Shower Drips From the Head (Not the Connection)</h2>
<p>If water continues to drip from the shower head after you turn it off, the problem is the <strong>shower valve</strong> inside the wall, not the head. This usually requires a plumber to replace the cartridge or valve.</p>

<p><strong>Need valve repair?</strong> Call <a href="tel:8337586911">833-758-6911</a>.</p>"""},

    {"slug": "gas-vs-electric-tankless-water-heater", "title": "Gas vs Electric Tankless Water Heater: Which Is Better?",
     "categories": [{"slug": "guides", "name": "Guides"}],
     "seo": {"title": "Gas vs Electric Tankless Water Heater Comparison", "description": "Gas or electric tankless? Compare flow rate, cost, installation requirements, and which is better for Chicago homes."},
     "content": """<p>Going tankless? Your first decision is gas or electric. The differences are significant, especially in Chicago's climate.</p>

<h2 id="comparison">Comparison</h2>
<table>
<tr><th>Factor</th><th>Gas Tankless</th><th>Electric Tankless</th></tr>
<tr><td>Flow rate</td><td>8-11 GPM (whole house)</td><td>2-5 GPM (1-2 fixtures)</td></tr>
<tr><td>Unit cost</td><td>$1,000 - $2,500</td><td>$500 - $1,500</td></tr>
<tr><td>Installation cost</td><td>$1,500 - $3,000</td><td>$1,000 - $2,500</td></tr>
<tr><td>Operating cost</td><td>Lower (gas cheaper in Chicago)</td><td>Higher (electricity more expensive)</td></tr>
<tr><td>Venting required</td><td>Yes (direct vent or power vent)</td><td>No</td></tr>
<tr><td>Gas line upgrade</td><td>Often needed (3/4" line)</td><td>N/A</td></tr>
<tr><td>Electrical upgrade</td><td>N/A</td><td>Often needs 200+ amp panel</td></tr>
<tr><td>Winter performance</td><td>Excellent (high BTU output)</td><td>Reduced (cold inlet water)</td></tr>
<tr><td>Best for</td><td>Whole-house hot water</td><td>Single point-of-use or small homes</td></tr>
</table>

<h2 id="chicago">For Chicago: Gas Wins</h2>
<p><strong>Gas tankless is the clear winner for most Chicago homes.</strong> The reason: Chicago's cold winter water (37-42°F incoming) requires a massive temperature rise. Gas units produce enough BTUs to handle this. Electric units struggle with the cold inlet temperature and can only serve 1-2 fixtures simultaneously in winter.</p>

<p>Electric tankless works well as a <strong>point-of-use</strong> unit — under a bathroom sink or for a remote bathroom far from the main heater.</p>

<p><strong>Ready for tankless?</strong> Call <a href="tel:8337586911">833-758-6911</a> for <a href="/chicago-il-plumbing/tankless-water-heater-installation/">tankless water heater installation</a>.</p>"""},

    {"slug": "clear-clogged-p-trap-guide", "title": "How to Clear a Clogged P-Trap (Under-Sink Fix)",
     "categories": [{"slug": "diy-tips", "name": "DIY Tips"}],
     "seo": {"title": "How to Clear a Clogged P-Trap (Under-Sink Fix)", "description": "Clear a clogged P-trap in 10 minutes. Simple under-sink fix that resolves most sink drainage problems. No tools needed."},
     "content": """<p>The P-trap is the curved pipe under your sink that catches debris and holds water to block sewer gases. It's also the most common location for sink clogs. Clearing it is a simple 10-minute DIY job.</p>

<h2 id="steps">Step-by-Step</h2>
<ol>
<li><strong>Place a bucket under the P-trap</strong> — Water will spill when you remove it</li>
<li><strong>Unscrew the slip nuts</strong> — The two large nuts on either end of the curved section. Most unscrew by hand. If they're tight, use channel-lock pliers</li>
<li><strong>Remove the P-trap</strong> — Pull it straight down. Water and debris will drain into the bucket</li>
<li><strong>Clean it out</strong> — Remove hair, grease, soap scum, and any objects caught in the trap. A bottle brush works great for scrubbing the interior</li>
<li><strong>Check the pipe going into the wall</strong> — Shine a flashlight. If you see a blockage, use a straightened wire hanger to pull it out</li>
<li><strong>Reinstall</strong> — Put the P-trap back, tighten both slip nuts hand-tight, then 1/4 turn more with pliers</li>
<li><strong>Test</strong> — Run water and check for leaks at both connections</li>
</ol>

<h2 id="tips">Pro Tips</h2>
<ul>
<li>Take a photo before removing so you remember how it goes back together</li>
<li>If the slip nuts are corroded and won't budge, you may need to replace the entire P-trap ($5-$15 at a hardware store)</li>
<li>If cleaning the P-trap doesn't fix the slow drain, the clog is deeper in the wall pipe — call a plumber</li>
</ul>

<p><strong>Drain still slow?</strong> Call <a href="tel:8337586911">833-758-6911</a> for professional <a href="/chicago-il-plumbing/drain-cleaning/">drain cleaning</a>.</p>"""},

    {"slug": "home-plumbing-diagram-explained", "title": "Understanding Your Home's Plumbing: A Simple Diagram Guide",
     "categories": [{"slug": "guides", "name": "Guides"}],
     "seo": {"title": "Home Plumbing Diagram Explained (Simple Guide)", "description": "Understand how your home's plumbing works. Simple explanation of supply lines, drain lines, vents, and how they connect."},
     "content": """<p>Every home has two separate plumbing systems that work together: the <strong>supply system</strong> (clean water in) and the <strong>drain-waste-vent system</strong> (used water out). Here's how they work.</p>

<h2 id="supply">The Supply System (Water In)</h2>
<p>Clean water enters your home from the city main through a single pipe (the service line). It passes through your water meter and main shutoff valve, then splits into two paths:</p>
<ul>
<li><strong>Cold water lines</strong> — Go directly to every fixture (sinks, toilets, hose bibs, etc.)</li>
<li><strong>Hot water line</strong> — Cold water goes to the water heater first, then hot water lines run to fixtures that need it</li>
</ul>
<p>Supply lines are under pressure (40-80 PSI), which is what pushes water up to second-floor fixtures and out of faucets.</p>

<h2 id="dwv">The Drain-Waste-Vent (DWV) System (Water Out)</h2>
<p>Used water flows by gravity (not pressure) through drain pipes. The system has three components:</p>
<ul>
<li><strong>Drain pipes</strong> — Carry used water from fixtures downward. Each fixture has a P-trap that holds water to block sewer gas</li>
<li><strong>Waste pipe (main stack)</strong> — A large vertical pipe (3-4 inches) that all drains connect to. Runs from basement to roof</li>
<li><strong>Vent pipes</strong> — Allow air into the drain system so water flows properly (like removing your thumb from a straw). Exit through the roof</li>
</ul>
<p>All drain water flows into the <strong>main sewer line</strong>, which exits your home underground and connects to the city sewer.</p>

<h2 id="key">Key Components to Know</h2>
<ul>
<li><strong>Main shutoff valve</strong> — Stops all water. Know where this is. <a href="/blog/how-to-shut-off-water-emergency-chicago/">Find yours</a></li>
<li><strong>Water meter</strong> — Measures usage. Use it to <a href="/blog/how-to-read-water-meter-leak-detection/">detect leaks</a></li>
<li><strong>Water heater</strong> — Heats and stores (or heats on-demand) hot water</li>
<li><strong>Sewer cleanout</strong> — Access point for sewer line maintenance. <a href="/blog/what-is-sewer-cleanout-where-is-mine/">Find yours</a></li>
<li><strong>Sump pump</strong> — Removes groundwater from under your basement</li>
</ul>

<p><strong>Questions about your plumbing?</strong> Call <a href="tel:8337586911">833-758-6911</a>.</p>"""},

    {"slug": "water-pressure-regulator-signs-need-one", "title": "Water Pressure Regulator: Signs You Need One (or a New One)",
     "categories": [{"slug": "tips", "name": "Tips"}],
     "seo": {"title": "Water Pressure Regulator: Signs You Need One", "description": "Is your water pressure too high? Signs you need a pressure regulator, what it does, and how it protects your plumbing. Chicago guide."},
     "content": """<p>Water pressure that's too high is just as problematic as pressure that's too low. Excessive pressure damages pipes, fixtures, appliances, and wastes water. A pressure-reducing valve (PRV) protects your entire system.</p>

<h2 id="signs">Signs of High Water Pressure</h2>
<ul>
<li><strong>Banging pipes</strong> (water hammer) when faucets are turned off</li>
<li><strong>Leaking faucets</strong> that keep dripping despite new washers</li>
<li><strong>Running toilets</strong> that won't stop cycling</li>
<li><strong>Appliance failures</strong> — Dishwashers, washing machines, ice makers failing prematurely</li>
<li><strong>High water bills</strong> without increased usage</li>
<li><strong>Burst supply hoses</strong> (washing machine, toilet, dishwasher)</li>
</ul>

<h2 id="ideal">What's the Ideal Pressure?</h2>
<p>Residential water pressure should be <strong>40-80 PSI</strong>. You can check yours with a $10 pressure gauge from a hardware store — screw it onto a hose bib and turn the water on.</p>
<ul>
<li><strong>Below 40 PSI:</strong> Too low. May need a pressure booster</li>
<li><strong>40-60 PSI:</strong> Ideal range</li>
<li><strong>60-80 PSI:</strong> Acceptable but on the high side</li>
<li><strong>Above 80 PSI:</strong> Too high. Install or replace a PRV</li>
</ul>

<h2 id="prv">What a PRV Does</h2>
<p>A pressure-reducing valve is installed on the main water line where it enters your home. It automatically reduces incoming city pressure (which can be 100-150 PSI) to a safe level for your plumbing. PRVs last 10-15 years and cost $200-$400 to replace.</p>

<p><strong>Need pressure testing?</strong> Call <a href="tel:8337586911">833-758-6911</a>.</p>"""},

    # Resource/checklist pages
    {"slug": "new-homeowner-plumbing-checklist-chicago", "title": "New Homeowner Plumbing Checklist (Chicago Edition)",
     "categories": [{"slug": "guides", "name": "Guides"}],
     "seo": {"title": "New Homeowner Plumbing Checklist (Chicago)", "description": "Just bought a Chicago home? Complete plumbing checklist for your first 30 days. What to locate, test, inspect, and schedule."},
     "content": """<p>Congratulations on your new Chicago home! Use this checklist to familiarize yourself with your plumbing system and prevent surprises.</p>

<h2 id="day1">Day 1: Locate Critical Components</h2>
<ul>
<li>☐ <strong>Main water shutoff valve</strong> — Usually in the basement near the front wall. Test it (turn off and on). <a href="/blog/how-to-shut-off-water-emergency-chicago/">Full guide</a></li>
<li>☐ <strong>Water meter</strong> — Note the current reading</li>
<li>☐ <strong>Water heater</strong> — Check age (serial number), set temperature to 120°F</li>
<li>☐ <strong>Sump pump</strong> — Locate the pit. <a href="/blog/how-to-test-sump-pump/">Test it</a></li>
<li>☐ <strong>Sewer cleanout</strong> — Locate inside and/or outside. <a href="/blog/what-is-sewer-cleanout-where-is-mine/">Full guide</a></li>
<li>☐ <strong>Gas shutoff</strong> — Near the meter or at each appliance</li>
</ul>

<h2 id="week1">Week 1: Inspect and Test</h2>
<ul>
<li>☐ Run every faucet (hot and cold) and check for leaks under sinks</li>
<li>☐ Flush every toilet and check for running/leaking</li>
<li>☐ Check water pressure (should be 40-80 PSI)</li>
<li>☐ Check for visible pipe material — copper, galvanized, PEX? <a href="/blog/pipe-material-identifier-guide/">Identification guide</a></li>
<li>☐ Run all appliances (dishwasher, washing machine) and check for leaks</li>
<li>☐ Check caulking around tubs, showers, and toilets</li>
</ul>

<h2 id="month1">First Month: Schedule</h2>
<ul>
<li>☐ <a href="/chicago-il-plumbing/sewer-camera-inspection/">Sewer camera inspection</a> (if home is 30+ years old)</li>
<li>☐ Water heater flush (if no record of recent maintenance)</li>
<li>☐ <a href="/blog/chicago-lead-pipe-replacement-program/">Check lead service line status</a> at chicagowaterquality.org</li>
<li>☐ Save a plumber's number: <a href="tel:8337586911">833-758-6911</a></li>
</ul>"""},

    {"slug": "before-you-remodel-plumbing-checklist", "title": "Before You Remodel: Plumbing Checklist",
     "categories": [{"slug": "guides", "name": "Guides"}],
     "seo": {"title": "Before You Remodel: Plumbing Checklist", "description": "Planning a kitchen or bathroom remodel? Here's what to consider for the plumbing before, during, and after your renovation."},
     "content": """<p>Plumbing is the most disruptive part of any remodel. Planning it properly prevents delays, change orders, and budget overruns.</p>

<h2 id="before">Before Starting</h2>
<ul>
<li>☐ <strong>Get a plumbing assessment</strong> — Have a plumber inspect existing pipes before your GC starts demo. Old pipes may need replacing</li>
<li>☐ <strong>Finalize fixture locations</strong> — Moving a toilet, sink, or shower requires rerouting drains (expensive). Keeping fixtures in place saves thousands</li>
<li>☐ <strong>Select fixtures early</strong> — The plumber needs specifications for rough-in. Buy fixtures before wall work begins</li>
<li>☐ <strong>Check pipe material</strong> — If you have galvanized supply pipes, remodel time is the cheapest time to repipe (walls are already open)</li>
<li>☐ <strong>Budget for permits</strong> — Chicago requires plumbing permits for remodel work ($100-$300)</li>
<li>☐ <strong>Plan for ventilation</strong> — Every new fixture needs a vent connection. This affects wall framing</li>
</ul>

<h2 id="during">During Remodel</h2>
<ul>
<li>☐ <strong>Rough-in inspection</strong> — City inspector must approve plumbing before walls are closed</li>
<li>☐ <strong>Photograph everything</strong> — Take photos of all pipe locations before drywall goes up. Future you will thank you</li>
<li>☐ <strong>Pressure test</strong> — All new supply lines should be pressure tested before closing walls</li>
</ul>

<h2 id="after">After Remodel</h2>
<ul>
<li>☐ <strong>Test everything</strong> — Run all fixtures, check for leaks, test drainage</li>
<li>☐ <strong>Get warranty docs</strong> — Keep all fixture and labor warranty paperwork</li>
<li>☐ <strong>Final inspection</strong> — City final inspection closes the permit</li>
</ul>

<p><strong>Need a plumber for your remodel?</strong> Call <a href="tel:8337586911">833-758-6911</a> for <a href="/chicago-il-plumbing/bathroom-remodeling/">bathroom</a> or <a href="/chicago-il-plumbing/kitchen-remodeling/">kitchen remodeling</a> plumbing.</p>"""},

    {"slug": "vacation-home-winterization-checklist", "title": "Vacation Home Winterization Checklist (Illinois)",
     "categories": [{"slug": "seasonal-tips", "name": "Seasonal Tips"}],
     "seo": {"title": "Vacation Home Winterization Checklist (Illinois)", "description": "Leaving your Illinois vacation home or investment property for winter? Complete winterization checklist to prevent frozen pipes and flooding."},
     "content": """<p>If you're leaving an Illinois property unoccupied during winter, proper winterization is the difference between a safe return and a catastrophic pipe burst. Use this checklist.</p>

<h2 id="full">Full Winterization (Heat OFF)</h2>
<ul>
<li>☐ Shut off main water supply</li>
<li>☐ Open all faucets (hot and cold) to drain lines</li>
<li>☐ Flush all toilets and hold handle to drain tanks</li>
<li>☐ Drain water heater completely</li>
<li>☐ Pour RV antifreeze (non-toxic) into every drain trap (1-2 cups each)</li>
<li>☐ Pour RV antifreeze into toilet bowls</li>
<li>☐ Disconnect and drain washing machine hoses</li>
<li>☐ Disconnect and drain dishwasher</li>
<li>☐ Shut off gas to water heater</li>
<li>☐ Disconnect outdoor hoses</li>
<li>☐ Shut off and drain outdoor faucets from inside</li>
<li>☐ Drain sprinkler system with compressed air</li>
<li>☐ Leave cabinet doors open on exterior walls</li>
<li>☐ Set sump pump to run (ensure power stays on to sump pump)</li>
</ul>

<h2 id="partial">Partial Winterization (Heat ON at 55°F+)</h2>
<ul>
<li>☐ Set thermostat to minimum 55°F</li>
<li>☐ Open cabinet doors on exterior walls</li>
<li>☐ Disconnect outdoor hoses</li>
<li>☐ Ensure sump pump is working</li>
<li>☐ Have someone check weekly</li>
<li>☐ Set up temperature monitoring (smart thermostat with alerts)</li>
</ul>

<p><strong>Need professional winterization?</strong> Call <a href="tel:8337586911">833-758-6911</a>. We handle full and partial winterization for homes and commercial properties.</p>"""},
]


def main():
    path = os.path.join(DATA_DIR, "blog_posts.json")
    with open(path, "r", encoding="utf-8") as f:
        posts = json.load(f)
    existing = {p["slug"] for p in posts}
    added = 0
    for post in POSTS:
        if post["slug"] in existing:
            print(f"  SKIP: {post['slug']}")
            continue
        words = len(post["content"].split())
        full = {
            "id": str(17000 + added), "title": post["title"], "slug": post["slug"],
            "url_path": "/blog/" + post["slug"], "date": "2026-02-23 16:00:00",
            "modified": "2026-02-23 16:00:00", "author": "Plumbers 911 Chicago",
            "content": post["content"], "excerpt": "", "seo": post["seo"], "images": [],
            "categories": post.get("categories", []), "tags": [],
            "featured_image_id": "",
            "reading_time": str(max(1, math.ceil(words / 225))) + " min read",
        }
        posts.append(full)
        added += 1
        print(f"  ADDED: {post['slug']} ({words} words)")
    with open(path, "w", encoding="utf-8") as f:
        json.dump(posts, f, indent=2, ensure_ascii=False)
    print(f"\nDone. {added} new pages. Total: {len(posts)}")

if __name__ == "__main__":
    main()
