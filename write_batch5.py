"""Items 101-125: 10 blog posts + 5 location combos + 3 county hubs + 5 landing pages + 2 hub pages."""
import json, os, math

DATA_DIR = r"C:\Users\User\OneDrive\Desktop\p911\site\data"

POSTS = [
    {"slug": "trenchless-sewer-repair-how-it-works", "title": "Trenchless Sewer Repair: How It Works and What It Costs",
     "categories": [{"slug": "guides", "name": "Guides"}],
     "seo": {"title": "Trenchless Sewer Repair: How It Works (2026)", "description": "Trenchless sewer repair explained: pipe lining, pipe bursting, costs, and when it's the right choice. No-dig sewer repair in Chicago."},
     "content": """<p>Trenchless sewer repair lets plumbers fix or replace your sewer line <strong>without digging up your yard, driveway, or landscaping</strong>. Here's how it works.</p>

<h2 id="methods">Two Trenchless Methods</h2>
<h3>1. Pipe Lining (CIPP — Cured-in-Place Pipe)</h3>
<p>A flexible liner coated with epoxy resin is inserted into the existing pipe and inflated. The resin hardens, creating a smooth new pipe inside the old one. It's like putting a new pipe inside your old pipe without removing it.</p>
<ul>
<li><strong>Best for:</strong> Pipes with cracks, root damage, joint failures, or minor corrosion</li>
<li><strong>Cost:</strong> $80-$250 per linear foot ($4,000-$15,000 typical)</li>
<li><strong>Time:</strong> Usually completed in 1 day</li>
<li><strong>Lifespan:</strong> 50+ years</li>
</ul>

<h3>2. Pipe Bursting</h3>
<p>A bursting head is pulled through the old pipe, breaking it apart while simultaneously pulling a new HDPE pipe into place. This actually replaces the pipe rather than lining it.</p>
<ul>
<li><strong>Best for:</strong> Collapsed pipes, severely damaged lines, upsizing pipe diameter</li>
<li><strong>Cost:</strong> $60-$200 per linear foot ($3,000-$12,000 typical)</li>
<li><strong>Time:</strong> 1-2 days</li>
<li><strong>Lifespan:</strong> 50-100+ years</li>
</ul>

<h2 id="when">When Trenchless Won't Work</h2>
<ul>
<li>Pipe has completely collapsed or has severe bellying (sag)</li>
<li>Multiple 90-degree bends in the line</li>
<li>Pipe is back-pitched (slopes wrong direction)</li>
<li>Access points are inaccessible</li>
</ul>

<p>The first step is always a <a href="/chicago-il-plumbing/sewer-camera-inspection/">sewer camera inspection</a> to determine which method is right. Call <a href="tel:8337586911">833-758-6911</a> for a free assessment.</p>"""},

    {"slug": "plumbing-emergencies-that-cant-wait", "title": "5 Plumbing Emergencies That Can't Wait Until Morning",
     "categories": [{"slug": "tips", "name": "Tips"}],
     "seo": {"title": "5 Plumbing Emergencies That Can't Wait", "description": "Not every plumbing problem is an emergency. Here are 5 that absolutely cannot wait — and what to do while you wait for the plumber."},
     "content": """<p>At 2 AM, it's tempting to think "I'll deal with this in the morning." For some plumbing issues, that's fine. For these five, waiting can turn a repair into a disaster.</p>

<h2 id="burst">1. Burst Pipe</h2>
<p>A burst pipe can release <strong>250+ gallons per hour</strong>. Every minute of delay means more water damage to floors, walls, ceilings, and belongings.</p>
<p><strong>Do now:</strong> Shut off the main water supply immediately. Open faucets to drain remaining pressure. Call a plumber.</p>

<h2 id="sewer">2. Sewer Backup</h2>
<p>Raw sewage in your home is a health hazard. Bacteria, viruses, and parasites in sewage can cause serious illness. The longer it sits, the worse the contamination.</p>
<p><strong>Do now:</strong> Stop using all water fixtures. Don't try to clean it yourself without protective gear. Call a plumber and keep children and pets away from affected areas.</p>

<h2 id="gas">3. Gas Leak</h2>
<p>If you smell rotten eggs (the odorant added to natural gas), this is a life-threatening emergency.</p>
<p><strong>Do now:</strong> Leave the building immediately. Don't flip any switches, light matches, or use your phone inside. Call 911 and Peoples Gas (866-556-6002) from outside.</p>

<h2 id="nowater">4. Complete Loss of Water</h2>
<p>If you have zero water flow and neighbors have water, you likely have a main line break. Without water, you can't flush toilets, wash hands, or fight a fire.</p>
<p><strong>Do now:</strong> Check with neighbors. If it's just your home, call a plumber. If the whole block is affected, call 311.</p>

<h2 id="overflowing">5. Overflowing Toilet That Won't Stop</h2>
<p>If the toilet keeps overflowing after plunging and the shutoff valve behind it doesn't work, contaminated water is flooding your bathroom and potentially reaching other rooms.</p>
<p><strong>Do now:</strong> Shut off the main water supply. Contain the water with towels. Call a plumber.</p>

<p><strong>24/7 emergency plumbing:</strong> <a href="tel:8337586911">833-758-6911</a>. We dispatch within 30-60 minutes in the Chicago metro.</p>"""},

    {"slug": "how-to-find-gas-leak-home", "title": "How to Find a Gas Leak in Your Home: Detection Guide",
     "categories": [{"slug": "tips", "name": "Tips"}],
     "seo": {"title": "How to Find a Gas Leak in Your Home", "description": "Suspect a gas leak? How to detect it safely, what to do, and when to evacuate. Gas leak safety guide for Chicago homeowners."},
     "content": """<p>Natural gas leaks are dangerous — gas is explosive and can cause carbon monoxide poisoning. Knowing the signs and what to do could save your life.</p>

<h2 id="signs">Signs of a Gas Leak</h2>
<ul>
<li><strong>Rotten egg smell</strong> — Natural gas is odorless; utilities add mercaptan (smells like rotten eggs) so you can detect leaks</li>
<li><strong>Hissing sound</strong> — Near gas lines, appliances, or the meter</li>
<li><strong>Dead plants</strong> — Vegetation dying above a buried gas line</li>
<li><strong>Bubbling water</strong> — Standing water bubbling near a gas line</li>
<li><strong>Physical symptoms</strong> — Headache, dizziness, nausea, fatigue (signs of gas exposure)</li>
<li><strong>Higher gas bill</strong> — Unexplained increase without usage change</li>
</ul>

<h2 id="small">For Small, Suspected Leaks</h2>
<p>If you smell a faint odor near an appliance connection:</p>
<ol>
<li>Mix dish soap and water in a spray bottle</li>
<li>Spray on gas connections and fittings</li>
<li>If bubbles form, there's a leak at that joint</li>
<li>Turn off the gas to that appliance</li>
<li>Call a plumber to repair the connection</li>
</ol>

<h2 id="major">For Major Leaks: EVACUATE</h2>
<p>If the smell is strong or you feel symptoms:</p>
<ol>
<li><strong>Leave immediately</strong> — Get everyone out</li>
<li><strong>Don't use anything electrical</strong> — No switches, phones, or appliances inside</li>
<li><strong>Don't light anything</strong></li>
<li><strong>Call 911</strong> from outside or a neighbor's home</li>
<li><strong>Call Peoples Gas:</strong> 866-556-6002</li>
</ol>

<p><strong>Gas line service:</strong> Call <a href="tel:8337586911">833-758-6911</a> for <a href="/chicago-il-plumbing/gas-line-install-repair/">gas line installation and repair</a>.</p>"""},

    {"slug": "backflow-prevention-business-guide", "title": "Backflow Prevention: Why Your Chicago Business Needs Testing",
     "categories": [{"slug": "guides", "name": "Guides"}],
     "seo": {"title": "Backflow Prevention for Chicago Businesses", "description": "Chicago requires annual backflow testing for commercial properties. What it is, why it matters, and how to stay compliant."},
     "content": """<p>Backflow occurs when contaminated water flows backward into the clean water supply. It's a serious public health risk, and Chicago requires annual testing for commercial properties and some residential ones.</p>

<h2 id="what">What Is Backflow?</h2>
<p>Normally, water flows one direction: from the city main to your building. Backflow happens when pressure changes (a water main break, fire hydrant use, or pump failure) cause water to flow backward, potentially pulling contaminated water from your property into the public supply.</p>

<h2 id="preventer">What Is a Backflow Preventer?</h2>
<p>A mechanical device installed on your water line that only allows water to flow in one direction. If pressure reverses, the device closes and prevents contaminated water from entering the supply.</p>

<h2 id="testing">Annual Testing Requirements</h2>
<ul>
<li>Chicago requires <strong>annual testing</strong> of all backflow prevention assemblies</li>
<li>Testing must be performed by a <strong>certified backflow tester</strong></li>
<li>Results must be <strong>reported to the city</strong> within the required timeframe</li>
<li>Failure to comply can result in <strong>fines and water shutoff</strong></li>
</ul>

<h2 id="who">Who Needs Backflow Testing?</h2>
<ul>
<li>All commercial properties with irrigation systems</li>
<li>Buildings with fire sprinkler systems</li>
<li>Properties with boilers or cooling towers</li>
<li>Buildings with dental/medical equipment</li>
<li>Properties with swimming pools connected to city water</li>
<li>Some residential properties with irrigation or pool connections</li>
</ul>

<p><strong>Need backflow testing?</strong> Call <a href="tel:8337586911">833-758-6911</a> for certified <a href="/chicago-il-plumbing/backflow-testing-installation/">backflow testing and installation</a>.</p>"""},

    {"slug": "best-time-replace-water-heater", "title": "When Is the Best Time to Replace Your Water Heater?",
     "categories": [{"slug": "tips", "name": "Tips"}],
     "seo": {"title": "Best Time to Replace Your Water Heater", "description": "Don't wait for a flood. Here's how to know when your water heater needs replacement, and the best time of year to do it."},
     "content": """<p>Most people replace their water heater after it fails — which often means a flooded basement and an emergency service call. Here's how to plan ahead.</p>

<h2 id="when">Replace Before It Fails: Warning Signs</h2>
<ul>
<li><strong>Age:</strong> Tank heaters last 8-12 years. Check the serial number for manufacture date</li>
<li><strong>Rust in hot water:</strong> Rust-colored hot water means the tank is corroding from inside</li>
<li><strong>Rumbling/popping:</strong> Sediment hardening on the bottom, reducing efficiency</li>
<li><strong>Leaking:</strong> Any water around the base means the tank is failing</li>
<li><strong>Not enough hot water:</strong> Reduced capacity as elements fail or sediment builds up</li>
<li><strong>Repair frequency:</strong> If you've repaired it twice in a year, replace instead</li>
</ul>

<h2 id="besttime">Best Time of Year</h2>
<p><strong>Late summer/early fall</strong> is ideal for Chicago homeowners:</p>
<ul>
<li>Before winter demand increases (water heaters work hardest in winter)</li>
<li>Before the holiday rush when plumbers are busiest</li>
<li>Weather is warm enough for comfortable basement work</li>
<li>You have time to compare options without emergency pressure</li>
</ul>

<h2 id="proactive">The Proactive Approach</h2>
<p>If your tank water heater is 8+ years old, start planning now. Get quotes, decide between <a href="/blog/electric-vs-gas-water-heater/">gas vs electric</a> or <a href="/blog/water-heater-replacement-cost-chicago/">tank vs tankless</a>, and schedule installation before an emergency forces your hand.</p>

<p><strong>Get a free water heater quote:</strong> Call <a href="tel:8337586911">833-758-6911</a>.</p>"""},

    {"slug": "kitchen-sink-not-draining-fixes", "title": "Kitchen Sink Not Draining? 5 Quick Fixes to Try First",
     "categories": [{"slug": "diy-tips", "name": "DIY Tips"}],
     "seo": {"title": "Kitchen Sink Not Draining? 5 Quick Fixes", "description": "Kitchen sink draining slowly or not at all? Try these 5 fixes before calling a plumber. Most work in under 10 minutes."},
     "content": """<p>A clogged kitchen sink is one of the most common plumbing complaints. Before calling a plumber, try these five fixes in order — they resolve most kitchen clogs.</p>

<h2 id="disposal">1. Check the Garbage Disposal</h2>
<p>If you have a disposal, run it for 15 seconds with cold water. A stuck disposal blocks drainage. If it hums but doesn't spin, press the red reset button on the bottom and try again. Use the hex wrench to free a jam.</p>

<h2 id="boiling">2. Boiling Water</h2>
<p>Boil a full kettle and pour it directly down the drain in 2-3 stages. This melts grease and dissolves soap scum — the two most common kitchen clog culprits. <strong>Only use on metal pipes</strong> (not PVC).</p>

<h2 id="baking">3. Baking Soda + Vinegar</h2>
<p>Pour 1/2 cup baking soda down the drain, then 1/2 cup white vinegar. Cover the drain and wait 30 minutes. The fizzing breaks down organic material. Flush with hot water.</p>

<h2 id="plunger">4. Plunger</h2>
<p>Use a flat-bottom cup plunger (not a toilet plunger). Fill the sink with enough water to cover the plunger cup. If you have a double sink, block the other drain with a wet cloth. Plunge vigorously 15-20 times.</p>

<h2 id="ptrap">5. Clean the P-Trap</h2>
<p>Place a bucket under the P-trap (the curved pipe under the sink). Unscrew both slip nuts by hand and remove the trap. Clean out any debris, rinse it, and reinstall. This catches clogs that plunging can't reach.</p>

<p><strong>Still clogged?</strong> Call <a href="tel:8337586911">833-758-6911</a> for professional <a href="/chicago-il-plumbing/drain-cleaning/">drain cleaning</a>.</p>"""},

    {"slug": "toilet-wont-flush-troubleshooting", "title": "Toilet Won't Flush? Complete Troubleshooting Guide",
     "categories": [{"slug": "diy-tips", "name": "DIY Tips"}],
     "seo": {"title": "Toilet Won't Flush? Troubleshooting Guide", "description": "Toilet not flushing properly? Diagnose the problem with this guide. Weak flush, phantom flush, double flush, and more."},
     "content": """<p>A toilet that won't flush properly has a limited number of possible causes. Here's how to diagnose and fix each one.</p>

<h2 id="wontflush">Toilet Won't Flush at All</h2>
<p><strong>Check the handle and chain:</strong> Lift the tank lid. The chain connecting the handle to the flapper may be disconnected, too long (no tension), or broken. Reconnect or shorten the chain so it has about 1/2 inch of slack.</p>

<h2 id="weak">Weak Flush (Water Rises Then Slowly Drains)</h2>
<p><strong>Clog in the trap:</strong> The toilet's internal trap is partially blocked. Use a toilet plunger (flange type with extended rubber lip) — 15-20 vigorous plunges. If that doesn't work, try a toilet auger ($15 at hardware stores).</p>

<h2 id="partial">Partial Flush (Bowl Doesn't Empty Completely)</h2>
<p><strong>Low water level in tank:</strong> Open the tank and check. Water should be about 1 inch below the overflow tube. Adjust the float to raise the water level. More water = more flush power.</p>

<h2 id="phantom">Phantom Flushing (Toilet Runs Randomly)</h2>
<p><strong>Leaking flapper:</strong> The flapper is slowly leaking water from tank to bowl. When the water drops enough, the fill valve triggers. Replace the flapper ($3-$8). <a href="/blog/fix-running-toilet-10-minutes/">See our running toilet fix guide</a>.</p>

<h2 id="double">Double Flush Required</h2>
<p><strong>Flapper closing too fast:</strong> The flapper drops before enough water leaves the tank. Adjust the chain length or replace with a slower-closing flapper. On some toilets, the water level is too low.</p>

<p><strong>Still having issues?</strong> Call <a href="tel:8337586911">833-758-6911</a> for <a href="/chicago-il-plumbing/toilet-install/">toilet service</a>.</p>"""},

    {"slug": "leaky-faucet-water-waste-cost", "title": "How Much Water Does a Leaky Faucet Waste? (The Numbers)",
     "categories": [{"slug": "tips", "name": "Tips"}],
     "seo": {"title": "How Much Water Does a Leaky Faucet Waste?", "description": "A dripping faucet wastes more than you think. Here's exactly how much water and money you're losing, and when to fix it."},
     "content": """<p>That drip-drip-drip might seem minor, but the numbers add up fast.</p>

<h2 id="numbers">The Math on a Leaky Faucet</h2>
<table>
<tr><th>Drip Rate</th><th>Gallons/Day</th><th>Gallons/Year</th><th>Annual Cost*</th></tr>
<tr><td>1 drip/second</td><td>5</td><td>1,825</td><td>~$18</td></tr>
<tr><td>2 drips/second</td><td>10</td><td>3,650</td><td>~$36</td></tr>
<tr><td>Steady stream</td><td>50-100+</td><td>18,000-36,000+</td><td>$180-$360+</td></tr>
</table>
<p><em>*Based on Chicago water rates (~$10 per 1,000 gallons)</em></p>

<p>A single leaky faucet at 1 drip per second wastes <strong>1,825 gallons per year</strong>. If you have 2-3 dripping faucets, you could be wasting 5,000+ gallons annually. And if it's a hot water faucet, you're also paying to heat that wasted water.</p>

<h2 id="beyond">Beyond Water Waste</h2>
<ul>
<li><strong>Staining:</strong> Constant dripping causes mineral stains in sinks and tubs</li>
<li><strong>Mold:</strong> Persistent moisture promotes mold growth under and around fixtures</li>
<li><strong>Worsening problem:</strong> A small drip becomes a bigger leak as the washer continues to deteriorate</li>
</ul>

<h2 id="fix">Fix or Replace?</h2>
<p>Most faucet leaks are caused by a worn washer, O-ring, or cartridge — a $5-$20 part. If the faucet is 15+ years old, replacement is usually the better investment. Professional <a href="/chicago-il-plumbing/faucet-repair/">faucet repair</a> typically costs $150-$300.</p>

<p><strong>Stop wasting water:</strong> Call <a href="tel:8337586911">833-758-6911</a>.</p>"""},

    {"slug": "plumbing-maintenance-schedule-by-season", "title": "Plumbing Maintenance Schedule by Season (Chicago Edition)",
     "categories": [{"slug": "seasonal-tips", "name": "Seasonal Tips"}],
     "seo": {"title": "Plumbing Maintenance Schedule by Season (Chicago)", "description": "Season-by-season plumbing maintenance for Chicago homeowners. What to check, when to service, and how to prevent problems year-round."},
     "content": """<p>Preventive maintenance is the best way to avoid plumbing emergencies. Here's your year-round schedule, tailored for Chicago's climate.</p>

<h2 id="spring">Spring (March - May)</h2>
<ul>
<li>Test sump pump — pour water into pit until it triggers</li>
<li>Check sump pump battery backup</li>
<li>Inspect outdoor faucets for winter damage</li>
<li>Reconnect garden hoses and check for leaks</li>
<li>Clear debris from floor drains and window wells</li>
<li>Schedule <a href="/chicago-il-plumbing/sewer-camera-inspection/">annual sewer camera inspection</a></li>
</ul>

<h2 id="summer">Summer (June - August)</h2>
<ul>
<li>Check sprinkler system for leaks</li>
<li>Monitor garbage disposal usage (cookout season)</li>
<li>Check toilet flappers for slow leaks (food coloring test)</li>
<li>Inspect visible pipes for condensation/dripping</li>
<li>Clean washing machine hoses and check for bulges</li>
</ul>

<h2 id="fall">Fall (September - November)</h2>
<ul>
<li><strong>Top priority:</strong> Winterize before first freeze</li>
<li>Disconnect garden hoses</li>
<li>Shut off outdoor faucets from inside</li>
<li>Insulate exposed pipes in garage, crawl space, exterior walls</li>
<li>Flush water heater tank (annual)</li>
<li>Test water pressure (should be 40-80 PSI)</li>
<li>Schedule <a href="/chicago-il-plumbing/water-heater-repair/">water heater maintenance</a></li>
</ul>

<h2 id="winter">Winter (December - February)</h2>
<ul>
<li>Keep heat at 55°F minimum, even when away</li>
<li>Open cabinet doors during extreme cold</li>
<li>Let faucets drip on exterior walls during sub-zero temps</li>
<li>Monitor sump pump discharge line for ice blockage</li>
<li>Know where your <a href="/blog/how-to-shut-off-water-emergency-chicago/">main shutoff valve</a> is</li>
</ul>

<p><strong>Schedule seasonal maintenance:</strong> Call <a href="tel:8337586911">833-758-6911</a>.</p>"""},

    {"slug": "what-is-sewer-cleanout-where-is-mine", "title": "What Is a Sewer Cleanout and Where Is Mine?",
     "categories": [{"slug": "guides", "name": "Guides"}],
     "seo": {"title": "What Is a Sewer Cleanout & Where to Find It", "description": "Your sewer cleanout provides critical access for drain cleaning. Here's what it is, where to find it in a Chicago home, and why it matters."},
     "content": """<p>A sewer cleanout is an access point to your main sewer line. It's one of the most important plumbing features in your home, and many homeowners don't even know they have one.</p>

<h2 id="what">What Is It?</h2>
<p>A sewer cleanout is a pipe with a removable cap that provides direct access to your sewer line. Plumbers use it to run drain cables, camera equipment, and hydro-jetting equipment to clear blockages and inspect the line.</p>

<h2 id="where">Where to Find It in a Chicago Home</h2>
<ul>
<li><strong>Basement floor:</strong> Most common in Chicago. Look for a round PVC or cast iron cap (3-4 inches) flush with or slightly above the floor, usually near the front wall</li>
<li><strong>Basement wall:</strong> Sometimes a pipe extends from the wall at floor level</li>
<li><strong>Outside:</strong> Look for a cap at ground level near the foundation, usually near the front of the house or near the property line</li>
<li><strong>Utility room:</strong> Near the water heater or laundry area</li>
</ul>

<h2 id="why">Why It Matters</h2>
<ul>
<li><strong>Faster service:</strong> With a cleanout, plumbers can access your sewer line immediately without going through fixtures</li>
<li><strong>Lower cost:</strong> Direct access means less labor time</li>
<li><strong>Better cleaning:</strong> The cleanout allows equipment to reach the full length of the sewer line</li>
<li><strong>Camera access:</strong> Sewer cameras are inserted through the cleanout</li>
</ul>

<h2 id="dont">Don't Have One?</h2>
<p>Many older Chicago homes lack a cleanout. Installing one costs $500-$1,500 and is a worthwhile investment if you ever need sewer service. <a href="/chicago-il-plumbing/sewer-cleanout-installation/">Learn about cleanout installation</a>.</p>

<p><strong>Need sewer service?</strong> Call <a href="tel:8337586911">833-758-6911</a>.</p>"""},

    # Items 111-115: Location combo pages
    {"slug": "emergency-plumber-naperville-il", "title": "Emergency Plumber in Naperville, IL — 24/7 Service",
     "categories": [{"slug": "service-areas", "name": "Service Areas"}],
     "seo": {"title": "Emergency Plumber Naperville IL | 24/7 | Plumbers 911", "description": "24/7 emergency plumber in Naperville, IL. Burst pipes, sewer backups, water heater failures. Fast response. Call 833-758-6911."},
     "content": """<p>Plumbing emergencies in <strong>Naperville, IL</strong> don't wait for business hours. Plumbers 911 provides <strong>24/7 emergency plumbing service</strong> to Naperville and surrounding DuPage County communities.</p>

<h2>Emergency Services in Naperville</h2>
<ul>
<li><a href="/chicago-il-plumbing/frozen-broken-pipe-repair/">Burst pipe repair</a> — Critical during Naperville's harsh winters</li>
<li>Sewer backup cleanup and repair</li>
<li><a href="/chicago-il-plumbing/water-heater-repair/">Water heater emergency repair</a></li>
<li><a href="/chicago-il-plumbing/water-leak-detection-repair/">Flood and water leak emergency</a></li>
<li><a href="/chicago-il-plumbing/gas-line-install-repair/">Gas leak response</a></li>
</ul>

<h2>Why Naperville Trusts Plumbers 911</h2>
<ul>
<li>30-60 minute response time to Naperville</li>
<li>Licensed, bonded, and insured Illinois plumbers</li>
<li>Upfront pricing — no surprise charges</li>
<li>We know Naperville's plumbing infrastructure (1960s-2000s construction mix)</li>
</ul>

<p><strong>Naperville emergency plumber:</strong> <a href="tel:8337586911">833-758-6911</a>. Available now.</p>"""},

    {"slug": "water-heater-repair-joliet-il", "title": "Water Heater Repair in Joliet, IL — Same Day Service",
     "categories": [{"slug": "service-areas", "name": "Service Areas"}],
     "seo": {"title": "Water Heater Repair Joliet IL | Same Day | Plumbers 911", "description": "Water heater repair in Joliet, IL. Tank and tankless. Same day service available. All major brands. Call 833-758-6911."},
     "content": """<p>No hot water in your <strong>Joliet, IL</strong> home? Plumbers 911 provides same-day <a href="/chicago-il-plumbing/water-heater-repair/">water heater repair</a> service to Joliet and surrounding Will County communities.</p>

<h2>Water Heater Services in Joliet</h2>
<ul>
<li>Tank water heater repair (all brands: Rheem, A.O. Smith, Bradford White)</li>
<li><a href="/chicago-il-plumbing/tankless-water-heater-repair/">Tankless water heater repair</a> (Rinnai, Navien, Noritz)</li>
<li><a href="/chicago-il-plumbing/water-heater-installation/">Water heater replacement</a> — tank and tankless options</li>
<li>Annual maintenance and flushing</li>
<li>Anode rod inspection and replacement</li>
</ul>

<h2>Common Joliet Water Heater Issues</h2>
<p>Joliet's water is harder than Chicago's, which means faster sediment buildup in tanks. We recommend annual flushing for Joliet homes and more frequent anode rod checks.</p>

<p><strong>Joliet water heater service:</strong> <a href="tel:8337586911">833-758-6911</a>.</p>"""},

    {"slug": "drain-cleaning-schaumburg-il", "title": "Drain Cleaning in Schaumburg, IL — Fast & Affordable",
     "categories": [{"slug": "service-areas", "name": "Service Areas"}],
     "seo": {"title": "Drain Cleaning Schaumburg IL | Same Day | Plumbers 911", "description": "Professional drain cleaning in Schaumburg, IL. Kitchen, bathroom, main line. Snaking and hydro jetting. Call 833-758-6911."},
     "content": """<p>Clogged drains in <strong>Schaumburg, IL</strong>? Plumbers 911 provides fast, professional <a href="/chicago-il-plumbing/drain-cleaning/">drain cleaning</a> throughout Schaumburg and the surrounding northwest suburbs.</p>

<h2>Drain Cleaning Services</h2>
<ul>
<li>Kitchen drain cleaning (grease and food buildup)</li>
<li>Bathroom drain cleaning (hair and soap scum)</li>
<li>Main sewer line cleaning</li>
<li>Floor drain cleaning</li>
<li><a href="/blog/hydro-jetting-vs-snaking-drain-cleaning/">Hydro jetting for stubborn clogs</a></li>
<li><a href="/chicago-il-plumbing/sewer-camera-inspection/">Sewer camera inspection</a></li>
</ul>

<p><strong>Schaumburg drain cleaning:</strong> <a href="tel:8337586911">833-758-6911</a>. Same-day service available.</p>"""},

    # Items 116-118: County hub pages
    {"slug": "lake-county-plumbing-services", "title": "Plumbing Services in Lake County, IL",
     "categories": [{"slug": "service-areas", "name": "Service Areas"}],
     "seo": {"title": "Lake County IL Plumbing Services | Plumbers 911", "description": "Licensed plumbing services throughout Lake County, IL. Waukegan, Highland Park, Lake Forest, and more. 24/7 emergency. Call 833-758-6911."},
     "content": """<p>Plumbers 911 provides comprehensive plumbing services throughout <strong>Lake County, Illinois</strong>. From Waukegan to Highland Park, our licensed plumbers serve homeowners and businesses across all Lake County communities.</p>

<h2>Cities We Serve in Lake County</h2>
<ul>
<li>Waukegan</li>
<li>Highland Park</li>
<li>Lake Forest</li>
<li>Libertyville</li>
<li>Mundelein</li>
<li>Grayslake</li>
<li><a href="/service-area/">View full service area</a></li>
</ul>

<p><strong>Call <a href="tel:8337586911">833-758-6911</a></strong> for Lake County plumbing service.</p>"""},

    {"slug": "kane-county-plumbing-services", "title": "Plumbing Services in Kane County, IL",
     "categories": [{"slug": "service-areas", "name": "Service Areas"}],
     "seo": {"title": "Kane County IL Plumbing Services | Plumbers 911", "description": "Licensed plumbing in Kane County, IL. Aurora, Elgin, Geneva, St. Charles. 24/7 emergency service. Call 833-758-6911."},
     "content": """<p>Plumbers 911 serves homeowners and businesses throughout <strong>Kane County, Illinois</strong>. From Aurora to Elgin, our licensed plumbers provide the full range of residential and commercial plumbing services.</p>

<h2>Cities We Serve in Kane County</h2>
<ul>
<li><a href="/aurora-il-plumbing/">Aurora</a></li>
<li><a href="/elgin-il-plumbing/">Elgin</a></li>
<li>Geneva</li>
<li>St. Charles</li>
<li>Batavia</li>
<li><a href="/service-area/">View full service area</a></li>
</ul>

<p><strong>Call <a href="tel:8337586911">833-758-6911</a></strong> for Kane County plumbing service.</p>"""},

    {"slug": "mchenry-county-plumbing-services", "title": "Plumbing Services in McHenry County, IL",
     "categories": [{"slug": "service-areas", "name": "Service Areas"}],
     "seo": {"title": "McHenry County IL Plumbing Services | Plumbers 911", "description": "Licensed plumbing in McHenry County, IL. Crystal Lake, McHenry, Woodstock. 24/7 emergency. Call 833-758-6911."},
     "content": """<p>Plumbers 911 provides expert plumbing services throughout <strong>McHenry County, Illinois</strong>. Our licensed plumbers serve homes and businesses from Crystal Lake to Woodstock.</p>

<h2>Cities We Serve in McHenry County</h2>
<ul>
<li>Crystal Lake</li>
<li>McHenry</li>
<li>Woodstock</li>
<li>Algonquin (McHenry County portion)</li>
<li>Cary</li>
<li><a href="/service-area/">View full service area</a></li>
</ul>

<p><strong>Call <a href="tel:8337586911">833-758-6911</a></strong> for McHenry County plumbing service.</p>"""},

    # Items 121-125: Landing pages
    {"slug": "plumbing-near-me-chicago", "title": "Plumbing Near Me in Chicago — Find a Licensed Plumber Now",
     "categories": [{"slug": "service-areas", "name": "Service Areas"}],
     "seo": {"title": "Plumbing Near Me Chicago | Licensed Plumber | Plumbers 911", "description": "Looking for a plumber near you in Chicago? Plumbers 911 serves 188+ cities. Licensed, bonded, insured. 24/7 emergency service. Call 833-758-6911."},
     "content": """<p>Searching for a <strong>plumber near you</strong> in the Chicago area? Plumbers 911 Chicago has licensed plumbers dispatched from locations throughout the metro area, ensuring fast response times wherever you are.</p>

<h2>Why Choose Plumbers 911?</h2>
<ul>
<li><strong>30-60 minute response</strong> for emergencies</li>
<li><strong>188+ cities served</strong> across 10 counties</li>
<li><strong>Licensed, bonded, insured</strong> — verified Illinois plumbing licenses</li>
<li><strong>Upfront pricing</strong> — written estimates before work begins</li>
<li><strong>24/7 availability</strong> — nights, weekends, holidays</li>
<li><strong>Satisfaction guaranteed</strong></li>
</ul>

<h2>Areas We Serve</h2>
<ul>
<li><a href="/blog/cook-county-plumbing-services/">Cook County</a> (Chicago and suburbs)</li>
<li><a href="/blog/dupage-county-plumbing-services/">DuPage County</a> (Naperville, Elmhurst, Lombard)</li>
<li><a href="/blog/will-county-plumbing-services/">Will County</a> (Joliet, Lockport, Homer Glen)</li>
<li><a href="/blog/lake-county-plumbing-services/">Lake County</a> (Waukegan, Highland Park)</li>
<li><a href="/blog/kane-county-plumbing-services/">Kane County</a> (Aurora, Elgin)</li>
<li><a href="/blog/mchenry-county-plumbing-services/">McHenry County</a> (Crystal Lake, Woodstock)</li>
</ul>

<p><strong>Find a plumber near you now:</strong> <a href="tel:8337586911">833-758-6911</a></p>"""},

    {"slug": "24-hour-plumber-chicago", "title": "24 Hour Plumber in Chicago — Available Right Now",
     "categories": [{"slug": "service-areas", "name": "Service Areas"}],
     "seo": {"title": "24 Hour Plumber Chicago | Available Now | Plumbers 911", "description": "Need a plumber at 2 AM? Plumbers 911 Chicago is available 24 hours, 7 days a week. No extra charge for nights. Call 833-758-6911."},
     "content": """<p>Plumbing emergencies happen at the worst possible times — 2 AM on a Sunday, during a holiday dinner, in the middle of a Chicago blizzard. <strong>Plumbers 911 is available 24 hours a day, 7 days a week, 365 days a year.</strong></p>

<h2>What We Handle After Hours</h2>
<ul>
<li>Burst pipes and water leaks</li>
<li>Sewer backups and overflows</li>
<li>Water heater failures (no hot water)</li>
<li>Frozen pipe thawing and repair</li>
<li>Gas leak response</li>
<li>Overflowing toilets</li>
<li>Sump pump failures during storms</li>
</ul>

<h2>How Fast Can We Get There?</h2>
<p>We typically dispatch a licensed plumber within <strong>30-60 minutes</strong> in the Chicago metro area. Our plumbers are positioned throughout Cook, DuPage, Will, Lake, and Kane counties for maximum coverage.</p>

<p><strong>Call now — we're available:</strong> <a href="tel:8337586911">833-758-6911</a></p>"""},
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
            "id": str(15000 + added), "title": post["title"], "slug": post["slug"],
            "url_path": "/blog/" + post["slug"], "date": "2026-02-23 14:00:00",
            "modified": "2026-02-23 14:00:00", "author": "Plumbers 911 Chicago",
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
