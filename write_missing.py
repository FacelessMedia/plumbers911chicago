"""Write the 14 missing blog posts from PHASES_201_400 batches."""
import json, os, math

DATA_DIR = r"C:\Users\User\OneDrive\Desktop\p911\site\data"

POSTS = [
    # Batch 1 missing
    {"slug": "what-causes-sewer-gas-smell", "title": "What Causes Sewer Gas Smell in Your House?",
     "categories": [{"slug": "tips", "name": "Tips"}],
     "seo": {"title": "What Causes Sewer Gas Smell in Your House? | Plumbers 911", "description": "Rotten egg smell in your home? Learn the 7 most common causes of sewer gas smell and how to fix each one. Chicago plumbing experts explain."},
     "content": """<p>That rotten egg smell in your home isn't just unpleasant — sewer gas contains methane and hydrogen sulfide, which can be harmful in high concentrations. Here are the most common causes and how to fix them.</p>

<h2>1. Dry P-Trap</h2>
<p>The most common cause. Every drain has a P-trap — a U-shaped pipe that holds water to block sewer gases. If a drain isn't used for weeks, the water evaporates and gas seeps through.</p>
<p><strong>Fix:</strong> Run water in every drain for 30 seconds, especially guest bathrooms, basement drains, and laundry drains. Do this monthly for unused drains.</p>

<h2>2. Damaged or Missing Wax Ring</h2>
<p>The wax ring seals the base of your toilet to the floor flange. If it fails, sewer gas leaks around the toilet base. You might also notice water on the floor.</p>
<p><strong>Fix:</strong> Replace the wax ring. This requires removing the toilet — a job for a plumber if you're not comfortable.</p>

<h2>3. Cracked or Damaged Vent Pipe</h2>
<p>Vent pipes run from your drains up through the roof, allowing air in and sewer gas out. If a vent pipe cracks or gets blocked (leaves, bird nests, ice), gas backs up into the house.</p>
<p><strong>Fix:</strong> A plumber can inspect and repair vent pipes. Roof access is typically needed.</p>

<h2>4. Broken Sewer Line</h2>
<p>A cracked or collapsed sewer line can allow gas to seep up through the soil and into your home, especially through basement floor cracks.</p>
<p><strong>Fix:</strong> <a href="/chicago-il-plumbing/sewer-camera-inspection/">Sewer camera inspection</a> to locate the damage, followed by <a href="/chicago-il-plumbing/sewer-replacement/">sewer repair or replacement</a>.</p>

<h2>5. Loose or Missing Cleanout Cap</h2>
<p>Sewer cleanouts have caps that seal them. If a cap is loose, cracked, or missing, sewer gas escapes directly into your basement or crawl space.</p>
<p><strong>Fix:</strong> Replace the cleanout cap. Available at any hardware store for a few dollars.</p>

<h2>6. Failed Toilet Seal</h2>
<p>Loose toilet mounting bolts can break the seal between the toilet and the flange, allowing gas to escape even if the wax ring is intact.</p>
<p><strong>Fix:</strong> Tighten the mounting bolts. If the toilet rocks, the flange may need repair.</p>

<h2>7. Blocked Roof Vent</h2>
<p>In Chicago winters, ice can form on roof vents (called "frost closure"), blocking airflow and causing sewer gas to back up into the home. You may also hear gurgling drains.</p>
<p><strong>Fix:</strong> A plumber can clear the blockage. Some homes benefit from vent pipe insulation.</p>

<h2>When to Call a Professional</h2>
<p>If running water in drains doesn't solve the smell within a day, or if the smell is strong, call <a href="tel:8337586911">833-758-6911</a>. Persistent sewer gas can indicate a serious plumbing issue that needs professional diagnosis.</p>"""},

    {"slug": "how-to-prevent-basement-flooding-chicago", "title": "How to Prevent Basement Flooding in Chicago",
     "categories": [{"slug": "guides", "name": "Guides"}, {"slug": "seasonal-tips", "name": "Seasonal Tips"}],
     "seo": {"title": "How to Prevent Basement Flooding in Chicago | Plumbers 911", "description": "Chicago basements are prone to flooding. Learn 10 proven strategies to keep your basement dry, from sump pumps to backwater valves."},
     "content": """<p>Chicago's combined sewer system, heavy rains, and high water table make basement flooding a constant threat. Here are 10 proven strategies to protect your home.</p>

<h2>1. Install a Sump Pump</h2>
<p>If you don't have one, get one. If yours is over 7 years old, replace it. A quality sump pump is your first line of defense against groundwater. <a href="/chicago-il-plumbing/sump-pump-install-replacement/">Learn about sump pump installation</a>.</p>

<h2>2. Add a Battery Backup</h2>
<p>Power outages during storms are common in Chicago. A <a href="/chicago-il-plumbing/sump-pump-battery-backup-install/">battery backup sump pump</a> keeps your basement dry when the power goes out — exactly when you need it most.</p>

<h2>3. Install a Backwater Valve</h2>
<p>A backwater valve prevents city sewer water from flowing back into your home during heavy rain. Chicago's Department of Water Management offers rebates for backwater valve installation.</p>

<h2>4. Maintain Your Sewer Line</h2>
<p>Tree roots, grease, and debris can block your sewer lateral, causing backups into your basement. Schedule <a href="/chicago-il-plumbing/sewer-cleaning/">sewer cleaning</a> every 1-2 years as preventive maintenance.</p>

<h2>5. Grade Your Yard Away from the Foundation</h2>
<p>The ground around your home should slope away from the foundation at least 6 inches over the first 10 feet. This directs rainwater away from your basement walls.</p>

<h2>6. Extend Downspouts</h2>
<p>Gutter downspouts should discharge water at least 6 feet from your foundation. Use extensions or underground drain pipes to direct water away.</p>

<h2>7. Seal Foundation Cracks</h2>
<p>Even small cracks in basement walls or floors allow water entry. Hydraulic cement or epoxy injection can seal most cracks from the inside.</p>

<h2>8. Check Your Sump Pump Monthly</h2>
<p>Pour a bucket of water into the sump pit to verify the pump activates and discharges properly. Clean the pit of debris. Test the check valve.</p>

<h2>9. Clean Gutters Regularly</h2>
<p>Clogged gutters overflow and dump water directly along your foundation. Clean them at least twice a year — spring and fall.</p>

<h2>10. Consider Interior Drain Tile</h2>
<p>For chronic flooding, an interior drain tile system (French drain) along the basement perimeter collects water and routes it to the sump pit. This is the most effective long-term solution.</p>

<p><strong>Need help flood-proofing your basement?</strong> Call <a href="tel:8337586911">833-758-6911</a> for a free assessment.</p>"""},

    {"slug": "how-to-choose-right-toilet", "title": "How to Choose the Right Toilet for Your Bathroom",
     "categories": [{"slug": "guides", "name": "Guides"}],
     "seo": {"title": "How to Choose the Right Toilet | Buyer's Guide", "description": "Confused by toilet options? Learn about flush types, bowl shapes, height options, and water efficiency to choose the perfect toilet for your bathroom."},
     "content": """<p>A toilet is a 15-25 year investment, so choosing the right one matters. Here's what to consider before buying.</p>

<h2>Rough-In Distance</h2>
<p>Measure from the wall (not the baseboard) to the center of the floor bolts. Standard is 12 inches. Some older Chicago homes have 10" or 14" rough-ins. <strong>This is the most important measurement</strong> — a wrong rough-in means the toilet won't fit.</p>

<h2>Bowl Shape</h2>
<ul>
<li><strong>Round:</strong> Shorter front-to-back (~25.5"). Better for small bathrooms. Less expensive.</li>
<li><strong>Elongated:</strong> Longer (~31"). More comfortable for adults. Most popular for new installations.</li>
</ul>

<h2>Height</h2>
<ul>
<li><strong>Standard:</strong> 15" seat height. Standard for decades.</li>
<li><strong>Comfort/ADA:</strong> 17-19" seat height. Easier for adults and seniors to sit/stand. Increasingly popular.</li>
</ul>

<h2>Flush Type</h2>
<ul>
<li><strong>Gravity:</strong> Most common. Relies on water weight. Simple, reliable, quiet.</li>
<li><strong>Pressure-assist:</strong> Uses compressed air for powerful flush. Louder but clears waste better. Good for low-flow situations.</li>
<li><strong>Dual-flush:</strong> Two buttons — 0.8 GPF for liquids, 1.6 GPF for solids. Saves water.</li>
</ul>

<h2>Water Efficiency</h2>
<p>Federal standard is 1.6 GPF (gallons per flush). WaterSense-certified toilets use 1.28 GPF or less — saving ~13,000 gallons per year for a family of four. Look for the WaterSense label.</p>

<h2>One-Piece vs Two-Piece</h2>
<ul>
<li><strong>Two-piece:</strong> Separate tank and bowl. Less expensive. Easier to transport. More models available.</li>
<li><strong>One-piece:</strong> Tank and bowl molded together. Sleeker look. Easier to clean. Heavier.</li>
</ul>

<h2>Top Brands We Recommend</h2>
<ul>
<li><strong>TOTO:</strong> Best overall. Drake and UltraMax series are excellent.</li>
<li><strong>Kohler:</strong> Wide selection, great design. Cimarron is a top seller.</li>
<li><strong>American Standard:</strong> Reliable and affordable. Champion 4 has excellent flush power.</li>
</ul>

<p><strong>Need toilet installation?</strong> Call <a href="tel:8337586911">833-758-6911</a>. We'll install your new toilet and haul away the old one. <a href="/chicago-il-plumbing/toilet-install/">Learn more about our toilet services</a>.</p>"""},

    {"slug": "signs-sewer-line-needs-replacement", "title": "9 Signs Your Sewer Line Needs Replacement",
     "categories": [{"slug": "tips", "name": "Tips"}, {"slug": "sewer", "name": "Sewer"}],
     "seo": {"title": "9 Signs Your Sewer Line Needs Replacement | Plumbers 911", "description": "How do you know if your sewer line needs replacing? These 9 warning signs indicate serious sewer problems that may require a full replacement."},
     "content": """<p>Sewer line replacement is a major expense ($3,000-$25,000+), but ignoring a failing sewer line leads to sewage backups, property damage, and health hazards. Here are the signs to watch for.</p>

<h2>1. Recurring Backups</h2>
<p>One backup is usually a clog. Repeated backups — especially in the lowest drains — often indicate a structural problem with the sewer line itself.</p>

<h2>2. Multiple Slow Drains</h2>
<p>If multiple drains throughout the house are slow simultaneously, the problem is in the main sewer line, not individual drains.</p>

<h2>3. Sewage Smell in Yard</h2>
<p>A properly functioning sewer line is airtight. If you smell sewage outside, especially near the sewer line path, the pipe may be cracked or separated.</p>

<h2>4. Lush Green Patches in Yard</h2>
<p>Leaking sewage acts as fertilizer. Unusually green, lush grass in a strip across your yard likely follows the sewer line path.</p>

<h2>5. Sinkholes or Soft Spots</h2>
<p>A collapsed sewer line causes the soil above it to settle. You may notice dips, soft spots, or small sinkholes in your yard.</p>

<h2>6. Foundation Cracks</h2>
<p>A leaking sewer line near your foundation can wash away supporting soil, causing the foundation to settle and crack.</p>

<h2>7. Rodent or Insect Problems</h2>
<p>Rats and cockroaches can enter through cracks in sewer pipes. If you have a sudden pest problem, a broken sewer line could be the entry point.</p>

<h2>8. Age of Pipes</h2>
<p>Many Chicago homes have clay sewer lines from the 1920s-1960s. These have a 50-75 year lifespan and many are now failing. Cast iron lasts 75-100 years but corrodes from the inside.</p>

<h2>9. Camera Inspection Reveals Damage</h2>
<p>A <a href="/chicago-il-plumbing/sewer-camera-inspection/">sewer camera inspection</a> can reveal cracks, root intrusion, bellied (sagging) sections, and offset joints that indicate replacement is needed.</p>

<h2>What Are Your Options?</h2>
<ul>
<li><strong>Trenchless lining (CIPP):</strong> A resin liner is inserted inside the old pipe. No digging. Works for pipes with minor damage.</li>
<li><strong>Pipe bursting:</strong> A new pipe is pulled through the old one, breaking it apart. Minimal digging.</li>
<li><strong>Traditional replacement:</strong> Dig up and replace the entire line. Necessary for collapsed or severely damaged pipes.</li>
</ul>

<p><strong>Suspect sewer line problems?</strong> Call <a href="tel:8337586911">833-758-6911</a> for a <a href="/chicago-il-plumbing/sewer-camera-inspection/">camera inspection</a> — the first step to knowing exactly what's going on.</p>"""},

    {"slug": "chicago-water-quality-tap-water", "title": "Chicago Water Quality Report: What's in Your Tap Water?",
     "categories": [{"slug": "guides", "name": "Guides"}],
     "seo": {"title": "Chicago Water Quality: What's in Your Tap Water? | Plumbers 911", "description": "Is Chicago tap water safe? Learn about lead pipes, chlorine levels, and water quality. Plus what you can do to improve your home's water quality."},
     "content": """<p>Chicago's tap water comes from Lake Michigan and is treated at two of the world's largest water treatment plants. The water leaving the plant meets all federal standards — but what happens between the plant and your faucet matters.</p>

<h2>The Lead Pipe Problem</h2>
<p>Chicago has an estimated <strong>400,000 lead service lines</strong> — more than any other U.S. city. These are the pipes connecting the city water main to individual homes. If your home was built before 1986, you almost certainly have a lead service line.</p>
<p>The city adds phosphate to the water to create a coating inside lead pipes, reducing lead leaching. This works, but isn't perfect — disturbances like construction, water main breaks, or even running hot water through lead pipes can increase lead levels.</p>

<h2>What's in Chicago Tap Water?</h2>
<ul>
<li><strong>Chlorine/Chloramine:</strong> Added for disinfection. Safe but affects taste</li>
<li><strong>Fluoride:</strong> Added for dental health (~0.7 mg/L)</li>
<li><strong>Lead:</strong> Not in the source water, but can leach from service lines and plumbing</li>
<li><strong>Hardness:</strong> Chicago water is moderately hard (~8 grains per gallon)</li>
</ul>

<h2>How to Improve Your Water Quality</h2>

<h3>For Lead Concerns</h3>
<ul>
<li><strong>Run the tap for 5 minutes</strong> first thing in the morning before drinking/cooking</li>
<li><strong>Use cold water</strong> for cooking and drinking (hot water leaches more lead)</li>
<li><strong>Get a water test</strong> — free lead testing kits from the City of Chicago</li>
<li><strong>Install a certified water filter</strong> — NSF/ANSI 53 certified filters remove lead</li>
</ul>

<h3>For Taste and Chlorine</h3>
<ul>
<li>A simple carbon filter (Brita, PUR) removes chlorine taste</li>
<li>A <a href="/chicago-il-plumbing/water-filter-installation-replacement/">whole-house water filter</a> treats all water entering your home</li>
</ul>

<h3>For Hard Water</h3>
<ul>
<li>A <a href="/chicago-il-plumbing/water-softener-installation/">water softener</a> removes minerals that cause scale buildup, spots on dishes, and dry skin</li>
</ul>

<h2>Lead Service Line Replacement</h2>
<p>Chicago's Lead Service Line Replacement Program is replacing lead pipes across the city. Check if your address is eligible at chicago.gov. Until replaced, use a certified filter for drinking water.</p>

<p><strong>Want to improve your water quality?</strong> Call <a href="tel:8337586911">833-758-6911</a> for water filtration and softener installation.</p>"""},

    {"slug": "how-long-plumbing-fixtures-last-lifespan", "title": "How Long Do Plumbing Fixtures Last? Complete Lifespan Guide",
     "categories": [{"slug": "guides", "name": "Guides"}],
     "seo": {"title": "How Long Do Plumbing Fixtures Last? Lifespan Guide", "description": "When should you replace your water heater, faucets, toilet, and pipes? Complete plumbing fixture lifespan guide with replacement timelines."},
     "content": """<p>Knowing when plumbing fixtures and systems typically fail helps you plan ahead and avoid emergency replacements. Here's what to expect.</p>

<h2>Water Heaters</h2>
<table>
<tr><th>Type</th><th>Expected Lifespan</th></tr>
<tr><td>Tank water heater (gas)</td><td>8-12 years</td></tr>
<tr><td>Tank water heater (electric)</td><td>10-15 years</td></tr>
<tr><td>Tankless water heater</td><td>15-20+ years</td></tr>
</table>
<p><strong>Extend life:</strong> Annual flushing, anode rod replacement every 3-5 years. <a href="/chicago-il-plumbing/water-heater-repair/">Water heater services</a>.</p>

<h2>Pipes</h2>
<table>
<tr><th>Material</th><th>Expected Lifespan</th></tr>
<tr><td>Copper (supply)</td><td>50-70 years</td></tr>
<tr><td>Galvanized steel</td><td>20-50 years (replace ASAP)</td></tr>
<tr><td>PEX</td><td>40-50+ years</td></tr>
<tr><td>PVC/ABS (drain)</td><td>50-80+ years</td></tr>
<tr><td>Cast iron (drain)</td><td>75-100 years</td></tr>
<tr><td>Clay sewer line</td><td>50-75 years</td></tr>
</table>

<h2>Fixtures</h2>
<table>
<tr><th>Fixture</th><th>Expected Lifespan</th></tr>
<tr><td>Toilet</td><td>15-25+ years (internals: 5-10)</td></tr>
<tr><td>Faucet (quality)</td><td>15-20 years</td></tr>
<tr><td>Garbage disposal</td><td>8-12 years</td></tr>
<tr><td>Dishwasher</td><td>8-12 years</td></tr>
<tr><td>Sump pump</td><td>7-10 years</td></tr>
<tr><td>Water softener</td><td>10-15 years</td></tr>
</table>

<h2>When to Replace vs Repair</h2>
<ul>
<li><strong>Replace</strong> if the fixture is past 75% of its expected lifespan AND needs a repair costing more than 50% of replacement</li>
<li><strong>Replace</strong> if you're experiencing frequent repairs (more than 2 per year)</li>
<li><strong>Repair</strong> if the fixture is relatively new and the repair is straightforward</li>
</ul>

<p><strong>Not sure if it's time to replace?</strong> Call <a href="tel:8337586911">833-758-6911</a> for honest advice. We'll tell you if a repair makes more sense.</p>"""},

    {"slug": "how-to-winterize-vacant-chicago-property", "title": "How to Winterize a Vacant Chicago Property",
     "categories": [{"slug": "seasonal-tips", "name": "Seasonal Tips"}, {"slug": "guides", "name": "Guides"}],
     "seo": {"title": "How to Winterize a Vacant Chicago Property | Plumbers 911", "description": "Leaving a Chicago property vacant for winter? Follow this winterization guide to prevent frozen pipes, flooding, and costly water damage."},
     "content": """<p>A vacant property in a Chicago winter is a burst pipe waiting to happen. With temperatures regularly dropping below 0°F, proper winterization is essential. Here's the complete process.</p>

<h2>Option 1: Full Winterization (No Heat)</h2>
<p>If you're turning off the heat entirely:</p>

<h3>Step 1: Shut Off Water</h3>
<p>Turn off the main water supply valve. If the property has a meter in the basement, close the valve on the street side.</p>

<h3>Step 2: Drain All Pipes</h3>
<ol>
<li>Open all faucets (hot and cold) on every floor</li>
<li>Flush all toilets and hold the handle to drain tanks</li>
<li>Open drain valves at the lowest point of the plumbing system</li>
<li>Drain the water heater (connect a hose to the drain valve)</li>
<li>Run the dishwasher and washing machine briefly to drain lines</li>
</ol>

<h3>Step 3: Add Antifreeze</h3>
<p>Pour <strong>RV-grade (non-toxic) antifreeze</strong> into every drain trap, including:</p>
<ul>
<li>All sinks, tubs, and showers</li>
<li>Toilet bowls (after draining)</li>
<li>Floor drains</li>
<li>Washing machine drain</li>
</ul>
<p>This prevents the water in P-traps from freezing and cracking.</p>

<h3>Step 4: Disconnect Outdoor Fixtures</h3>
<ul>
<li>Disconnect and drain garden hoses</li>
<li>Close interior shut-off valves for outdoor faucets</li>
<li>Open outdoor faucets to drain remaining water</li>
</ul>

<h2>Option 2: Maintained Heat (Preferred)</h2>
<p>If possible, keep the heat running at a minimum of <strong>55°F</strong>. This is simpler and provides better protection.</p>
<ul>
<li>Keep all interior doors open for heat circulation</li>
<li>Open cabinet doors under sinks on exterior walls</li>
<li>Set faucets to drip during extreme cold (-10°F or below)</li>
<li>Have someone check the property weekly</li>
<li>Consider a <strong>smart thermostat with freeze alerts</strong></li>
</ul>

<h2>Additional Precautions</h2>
<ul>
<li>Insulate exposed pipes in unheated areas (basement, crawl space, garage)</li>
<li>Seal gaps around pipes where they enter exterior walls</li>
<li>Know where your main shutoff valve is in case of emergency</li>
<li>Leave a key with a neighbor or property manager for emergencies</li>
</ul>

<p><strong>Need professional winterization?</strong> Call <a href="tel:8337586911">833-758-6911</a>. We'll winterize your property correctly and give you peace of mind. See also: <a href="/chicago-il-plumbing/frozen-broken-pipe-repair/">Frozen pipe repair services</a>.</p>"""},

    # Batch 2 missing
    {"slug": "copper-vs-pex-vs-cpvc-piping", "title": "Copper vs PEX vs CPVC Piping: Complete Comparison",
     "categories": [{"slug": "guides", "name": "Guides"}],
     "seo": {"title": "Copper vs PEX vs CPVC Piping Comparison | Plumbers 911", "description": "Which pipe material is best for your home? Compare copper, PEX, and CPVC on cost, durability, installation, and performance for Chicago homes."},
     "content": """<p>Choosing the right pipe material for your home affects durability, water quality, cost, and maintenance. Here's an honest comparison of the three main options.</p>

<h2>Quick Comparison</h2>
<table>
<tr><th>Feature</th><th>Copper</th><th>PEX</th><th>CPVC</th></tr>
<tr><td>Cost (materials)</td><td>$$$</td><td>$</td><td>$$</td></tr>
<tr><td>Installation cost</td><td>$$$</td><td>$</td><td>$$</td></tr>
<tr><td>Lifespan</td><td>50-70 years</td><td>40-50+ years</td><td>50+ years</td></tr>
<tr><td>Freeze resistance</td><td>Poor</td><td>Good (expands)</td><td>Poor</td></tr>
<tr><td>Chicago winters</td><td>Risk of bursting</td><td>Best choice</td><td>Can crack</td></tr>
<tr><td>Taste/odor</td><td>None</td><td>Slight (fades)</td><td>None</td></tr>
<tr><td>UV resistance</td><td>Yes</td><td>No (indoor only)</td><td>Limited</td></tr>
</table>

<h2>Copper</h2>
<p><strong>Pros:</strong> Proven track record, biocidal (inhibits bacterial growth), recyclable, adds home value, UV resistant for outdoor use.</p>
<p><strong>Cons:</strong> Expensive (material + labor), can develop pinhole leaks (especially in Chicago's water), requires soldering (skilled labor), rigid (more fittings needed), bursts when frozen.</p>
<p><strong>Best for:</strong> Homeowners who want premium, proven materials and don't mind the cost.</p>

<h2>PEX (Cross-Linked Polyethylene)</h2>
<p><strong>Pros:</strong> Affordable, flexible (fewer fittings, easier installation), freeze-resistant (expands up to 3x), quiet (no water hammer), color-coded (red/blue), faster installation = lower labor cost.</p>
<p><strong>Cons:</strong> Can't be used outdoors (UV damage), slight taste initially (fades in weeks), not recyclable, newer track record (though used 30+ years in Europe).</p>
<p><strong>Best for:</strong> Most Chicago homes. Best freeze resistance, lowest cost, easiest installation.</p>

<h2>CPVC (Chlorinated PVC)</h2>
<p><strong>Pros:</strong> Cheaper than copper, handles hot water (up to 200°F), no metallic taste, fire resistant, doesn't corrode.</p>
<p><strong>Cons:</strong> Brittle in cold (can crack during Chicago winters), requires chemical cement joints, can't be used with some water treatments, limited flexibility.</p>
<p><strong>Best for:</strong> Budget-conscious projects in climate-controlled areas.</p>

<h2>Our Recommendation for Chicago</h2>
<p><strong>PEX is the best choice for most Chicago homes.</strong> Its freeze resistance alone makes it ideal for our harsh winters. Combined with lower cost and faster installation, it's what we install most often for <a href="/chicago-il-plumbing/whole-house-repiping/">whole-house repiping</a> projects.</p>

<p><strong>Need repiping?</strong> Call <a href="tel:8337586911">833-758-6911</a> for a free estimate.</p>"""},

    {"slug": "sump-pump-types-submersible-vs-pedestal", "title": "Sump Pump Types: Submersible vs Pedestal — Which Is Better?",
     "categories": [{"slug": "guides", "name": "Guides"}, {"slug": "sump-pump", "name": "Sump Pump"}],
     "seo": {"title": "Submersible vs Pedestal Sump Pump | Which Is Better?", "description": "Submersible or pedestal sump pump? Compare types, pros, cons, and costs to choose the best sump pump for your Chicago basement."},
     "content": """<p>Choosing between a submersible and pedestal sump pump? Here's what you need to know for your Chicago home.</p>

<h2>Submersible Sump Pumps</h2>
<p>The pump and motor sit inside the sump pit, below the water line. A sealed lid covers the pit.</p>
<p><strong>Pros:</strong></p>
<ul>
<li>Quieter — water and pit muffle the sound</li>
<li>More powerful — handles more water per hour</li>
<li>Out of sight — sealed pit is cleaner and safer</li>
<li>Handles solids better — less likely to clog</li>
<li>Longer lifespan if properly maintained (7-10 years)</li>
</ul>
<p><strong>Cons:</strong></p>
<ul>
<li>More expensive ($150-$400 for pump)</li>
<li>Harder to access for maintenance/repair</li>
<li>Motor is submerged — seal failure = replacement</li>
</ul>

<h2>Pedestal Sump Pumps</h2>
<p>The motor sits on top of a column above the pit. Only the impeller sits in the water.</p>
<p><strong>Pros:</strong></p>
<ul>
<li>Less expensive ($60-$200 for pump)</li>
<li>Easy to access for maintenance and repair</li>
<li>Motor stays dry — can last longer (15-25 years)</li>
<li>Works in narrow/shallow pits</li>
</ul>
<p><strong>Cons:</strong></p>
<ul>
<li>Much louder — motor is exposed</li>
<li>Less powerful — lower GPH capacity</li>
<li>Visible — takes up basement space</li>
<li>Can't handle solids as well</li>
</ul>

<h2>Which Is Better for Chicago?</h2>
<p><strong>Submersible pumps are recommended for most Chicago homes.</strong> Our heavy spring rains and high water table demand the higher pumping capacity. The quieter operation is a bonus, especially if you use your basement as living space.</p>
<p>Choose pedestal only if: your sump pit is unusually narrow, you want the lowest upfront cost, or you need easy motor access.</p>

<h2>Don't Forget Battery Backup</h2>
<p>Regardless of type, every Chicago home should have a <a href="/chicago-il-plumbing/sump-pump-battery-backup-install/">battery backup sump pump</a>. Spring storms knock out power exactly when you need your pump most.</p>

<p><strong>Need sump pump installation?</strong> Call <a href="tel:8337586911">833-758-6911</a>. <a href="/chicago-il-plumbing/sump-pump-install-replacement/">Learn more about our sump pump services</a>.</p>"""},

    # Batch 5 missing
    {"slug": "backflow-prevention-business", "title": "Backflow Prevention: Why Your Chicago Business Needs It",
     "categories": [{"slug": "commercial", "name": "Commercial"}, {"slug": "guides", "name": "Guides"}],
     "seo": {"title": "Backflow Prevention for Chicago Businesses | Plumbers 911", "description": "Chicago requires annual backflow testing for commercial properties. Learn about backflow prevention requirements, testing, and installation."},
     "content": """<p>If you own or manage a commercial property in Chicago, backflow prevention isn't optional — it's required by city ordinance. Here's what you need to know.</p>

<h2>What Is Backflow?</h2>
<p>Backflow occurs when water flows backward through the plumbing system, potentially contaminating the clean water supply with chemicals, waste, or other hazards. This can happen when water pressure drops (main break, fire hydrant use) or when downstream pressure exceeds supply pressure.</p>

<h2>Chicago Requirements</h2>
<ul>
<li>All commercial, industrial, and multi-unit residential buildings must have approved backflow prevention devices</li>
<li><strong>Annual testing is mandatory</strong> — results must be submitted to the City of Chicago</li>
<li>Only <strong>certified backflow testers</strong> can perform the annual test</li>
<li>Non-compliance can result in fines and water service disconnection</li>
</ul>

<h2>Who Needs Backflow Prevention?</h2>
<ul>
<li>Restaurants and food service</li>
<li>Medical and dental offices</li>
<li>Hotels and multi-unit buildings</li>
<li>Manufacturing and industrial facilities</li>
<li>Buildings with irrigation systems</li>
<li>Buildings with fire sprinkler systems</li>
<li>Car washes and laundromats</li>
<li>Any building with a boiler</li>
</ul>

<h2>Types of Backflow Prevention Devices</h2>
<ul>
<li><strong>RPZ (Reduced Pressure Zone):</strong> Highest protection. Required for high-hazard connections. Two check valves with a relief valve between them.</li>
<li><strong>DCVA (Double Check Valve Assembly):</strong> Medium protection. Two check valves in series. Common for low-hazard commercial use.</li>
<li><strong>PVB (Pressure Vacuum Breaker):</strong> For irrigation systems. Must be installed above the highest outlet.</li>
</ul>

<h2>What Annual Testing Involves</h2>
<p>A certified tester will:</p>
<ol>
<li>Inspect the device for physical damage</li>
<li>Test each check valve and relief valve</li>
<li>Verify proper operation at correct pressure differentials</li>
<li>Complete and submit the test report to the city</li>
</ol>

<p><strong>Need backflow testing or installation?</strong> Call <a href="tel:8337586911">833-758-6911</a>. Our certified testers handle everything, including city paperwork. <a href="/chicago-il-plumbing/backflow-testing-installation/">Learn more about our backflow services</a>.</p>"""},

    {"slug": "kitchen-sink-not-draining-quick-fixes", "title": "Kitchen Sink Not Draining? 5 Quick Fixes to Try First",
     "categories": [{"slug": "diy-tips", "name": "DIY Tips"}],
     "seo": {"title": "Kitchen Sink Not Draining? 5 Quick Fixes | Plumbers 911", "description": "Kitchen sink clogged or draining slowly? Try these 5 DIY fixes before calling a plumber. Step-by-step guide from Chicago plumbing experts."},
     "content": """<p>A slow or clogged kitchen sink is usually caused by grease, food particles, or soap buildup. Before calling a plumber, try these fixes in order.</p>

<h2>1. Boiling Water</h2>
<p><strong>Works for:</strong> Minor grease buildup</p>
<ol>
<li>Boil a full kettle of water</li>
<li>Pour it directly down the drain in 2-3 stages, waiting a few seconds between pours</li>
<li>The heat melts grease that's coating the pipe walls</li>
</ol>
<p><strong>Warning:</strong> Do NOT use boiling water if you have PVC drain pipes — it can soften the joints. Warm (not boiling) water is safe for all pipe types.</p>

<h2>2. Baking Soda + Vinegar</h2>
<p><strong>Works for:</strong> Moderate buildup</p>
<ol>
<li>Remove standing water from the sink</li>
<li>Pour 1/2 cup baking soda down the drain</li>
<li>Follow with 1/2 cup white vinegar</li>
<li>Cover the drain (a wet cloth works) and wait 15-30 minutes</li>
<li>Flush with hot water</li>
</ol>

<h2>3. Clean the P-Trap</h2>
<p><strong>Works for:</strong> Clogs from accumulated debris</p>
<ol>
<li>Place a bucket under the P-trap (the curved pipe under the sink)</li>
<li>Unscrew the slip nuts on both ends by hand</li>
<li>Remove the P-trap and clean out debris</li>
<li>Reassemble and hand-tighten</li>
</ol>

<h2>4. Plunge It</h2>
<p><strong>Works for:</strong> Clogs deeper in the line</p>
<ol>
<li>If you have a double sink, plug the other drain with a wet rag</li>
<li>Fill the clogged side with 3-4 inches of water</li>
<li>Use a flat-bottomed (sink) plunger — not a toilet plunger</li>
<li>Plunge vigorously 15-20 times</li>
</ol>

<h2>5. Check the Garbage Disposal</h2>
<p>If you have a disposal, the clog may be inside it:</p>
<ol>
<li>Turn off the disposal at the switch AND the breaker</li>
<li>Use the hex wrench (Allen key) on the bottom of the unit to manually rotate the blades</li>
<li>Press the reset button on the bottom</li>
<li>Run cold water and turn the disposal on</li>
</ol>

<h2>When to Call a Plumber</h2>
<ul>
<li>None of the above fixes work</li>
<li>Multiple drains are slow (indicates main line issue)</li>
<li>Water backs up into other fixtures when you run the kitchen sink</li>
<li>You hear gurgling sounds</li>
</ul>

<p><strong>Stubborn clog?</strong> Call <a href="tel:8337586911">833-758-6911</a>. Our <a href="/chicago-il-plumbing/drain-cleaning/">drain cleaning service</a> clears even the toughest blockages.</p>"""},

    {"slug": "leaky-faucet-water-waste", "title": "How Much Water Does a Leaky Faucet Waste?",
     "categories": [{"slug": "tips", "name": "Tips"}],
     "seo": {"title": "How Much Water Does a Leaky Faucet Waste? | Plumbers 911", "description": "A dripping faucet wastes more water than you think. See the numbers on water waste and cost, plus when to repair vs replace your faucet."},
     "content": """<p>That slow drip from your faucet might seem minor, but the numbers are surprising.</p>

<h2>The Math on Dripping Faucets</h2>
<table>
<tr><th>Drip Rate</th><th>Gallons/Day</th><th>Gallons/Year</th><th>Annual Cost*</th></tr>
<tr><td>1 drip/second</td><td>5.7</td><td>2,082</td><td>~$18</td></tr>
<tr><td>2 drips/second</td><td>11.4</td><td>4,164</td><td>~$36</td></tr>
<tr><td>Steady stream</td><td>50-100+</td><td>18,000+</td><td>~$155+</td></tr>
</table>
<p><em>*Based on Chicago average water/sewer rate of ~$8.60 per 1,000 gallons</em></p>

<h2>It's Not Just the Water Bill</h2>
<ul>
<li><strong>If it's the hot water faucet:</strong> You're also paying to heat that wasted water. A hot water drip can add $50-100+/year in energy costs.</li>
<li><strong>Staining:</strong> Constant dripping stains sinks, tubs, and countertops (especially from iron or minerals).</li>
<li><strong>Mold:</strong> Persistent moisture under a dripping faucet promotes mold growth.</li>
<li><strong>Worsening:</strong> A small drip always gets worse over time. A worn washer becomes a worn valve seat.</li>
</ul>

<h2>Common Causes of Faucet Drips</h2>
<ul>
<li><strong>Worn O-ring or washer</strong> — Most common. $1 part, 30-minute fix.</li>
<li><strong>Corroded valve seat</strong> — The seal between faucet and spout deteriorates.</li>
<li><strong>Worn cartridge</strong> — In single-handle faucets, the cartridge controls flow and temperature.</li>
<li><strong>High water pressure</strong> — Pressure above 80 PSI causes drips when fixtures are "off." Needs a pressure reducing valve.</li>
</ul>

<h2>Repair vs Replace</h2>
<ul>
<li><strong>Repair</strong> if the faucet is less than 8-10 years old and the repair is a simple washer/cartridge swap.</li>
<li><strong>Replace</strong> if the faucet is old, corroded, has multiple issues, or you want to upgrade. Modern faucets are more water-efficient.</li>
</ul>

<p><strong>Stop wasting water.</strong> Call <a href="tel:8337586911">833-758-6911</a> for fast <a href="/chicago-il-plumbing/faucet-repair/">faucet repair or replacement</a>.</p>"""},

    {"slug": "plumbing-maintenance-schedule-season", "title": "Plumbing Maintenance Schedule by Season",
     "categories": [{"slug": "seasonal-tips", "name": "Seasonal Tips"}, {"slug": "guides", "name": "Guides"}],
     "seo": {"title": "Plumbing Maintenance Schedule by Season | Plumbers 911", "description": "Keep your plumbing in top shape year-round with this seasonal maintenance checklist. Prevent emergencies with regular plumbing maintenance."},
     "content": """<p>Preventive plumbing maintenance prevents emergencies and extends the life of your fixtures and pipes. Follow this seasonal schedule for your Chicago home.</p>

<h2>Spring (March - May)</h2>
<ul>
<li><strong>Test sump pump</strong> — Pour water into the pit to verify it activates and discharges properly</li>
<li><strong>Inspect basement</strong> for signs of winter water damage or moisture</li>
<li><strong>Check outdoor faucets</strong> — Turn on and check for leaks from freeze damage</li>
<li><strong>Clean gutters</strong> — Prevent water pooling near foundation</li>
<li><strong>Schedule sewer line cleaning</strong> if not done in the past 2 years</li>
<li><strong>Check water heater</strong> — Look for leaks, rust, unusual noises</li>
</ul>

<h2>Summer (June - August)</h2>
<ul>
<li><strong>Check washing machine hoses</strong> — Replace rubber hoses with braided stainless steel</li>
<li><strong>Inspect toilets for leaks</strong> — Put food coloring in the tank; if it appears in the bowl without flushing, the flapper needs replacement</li>
<li><strong>Clean garbage disposal</strong> — Ice cubes + salt + lemon peels</li>
<li><strong>Check all faucets for drips</strong> — Repair before they worsen</li>
<li><strong>Inspect visible pipes</strong> for corrosion, leaks, or mineral buildup</li>
<li><strong>Test water pressure</strong> — Should be 40-80 PSI</li>
</ul>

<h2>Fall (September - November)</h2>
<ul>
<li><strong>Disconnect garden hoses</strong> — Leaving them connected can cause pipe freeze</li>
<li><strong>Close outdoor faucet shut-off valves</strong> and open outdoor faucets to drain</li>
<li><strong>Insulate exposed pipes</strong> in unheated areas (basement, crawl space, garage)</li>
<li><strong>Flush water heater</strong> — Drain sediment that reduces efficiency and lifespan</li>
<li><strong>Clean gutters again</strong> — Falling leaves clog quickly</li>
<li><strong>Test sump pump battery backup</strong></li>
<li><strong>Know your main shut-off valve location</strong> and verify it works</li>
</ul>

<h2>Winter (December - February)</h2>
<ul>
<li><strong>Keep heat above 55°F</strong> — Even when away</li>
<li><strong>Open cabinet doors</strong> under sinks on exterior walls during extreme cold</li>
<li><strong>Let faucets drip</strong> during sub-zero temperatures on exterior wall pipes</li>
<li><strong>Know the signs of frozen pipes</strong> — No water, bulging pipes, frost visible on pipes. <a href="/chicago-il-plumbing/frozen-broken-pipe-repair/">Call us immediately if you suspect frozen pipes</a>.</li>
<li><strong>Clear snow away from sump pump discharge pipe</strong></li>
<li><strong>Monitor water bill</strong> — A spike may indicate a hidden leak</li>
</ul>

<p><strong>Want a professional plumbing inspection?</strong> Call <a href="tel:8337586911">833-758-6911</a> to schedule a comprehensive plumbing checkup.</p>"""},

    {"slug": "sewer-replacement-oak-lawn-il", "title": "Sewer Replacement in Oak Lawn, IL — Expert Service",
     "categories": [{"slug": "service-areas", "name": "Service Areas"}, {"slug": "sewer", "name": "Sewer"}],
     "seo": {"title": "Sewer Replacement Oak Lawn IL | Plumbers 911 Chicago", "description": "Professional sewer replacement in Oak Lawn, IL. Trenchless and traditional options. Licensed, insured. Free estimates. Call 833-758-6911."},
     "content": """<p>Oak Lawn homeowners dealing with sewer line problems need fast, reliable service from plumbers who know the area. Plumbers 911 has been serving Oak Lawn and the surrounding south suburbs for years.</p>

<h2>Common Sewer Problems in Oak Lawn</h2>
<p>Many Oak Lawn homes were built in the 1950s-1970s, meaning sewer lines are 50-70+ years old. Common issues include:</p>
<ul>
<li><strong>Clay pipe deterioration</strong> — The original clay sewer lines crack and separate over time</li>
<li><strong>Tree root intrusion</strong> — Oak Lawn's mature trees send roots into cracked sewer lines</li>
<li><strong>Bellied (sagging) pipes</strong> — Soil settling causes low spots where waste accumulates</li>
<li><strong>Joint separation</strong> — Old connections pull apart, allowing infiltration and blockages</li>
</ul>

<h2>Our Sewer Replacement Options</h2>

<h3>Trenchless Sewer Lining (CIPP)</h3>
<p>A resin-coated liner is inserted into the existing pipe and cured in place, creating a new pipe within the old one. Minimal yard disruption.</p>
<ul><li>Best for: Pipes with cracks, root damage, or minor bellies</li><li>Timeline: Usually 1 day</li><li>Cost: $4,000 - $15,000</li></ul>

<h3>Pipe Bursting</h3>
<p>A new HDPE pipe is pulled through the old one, breaking the old pipe apart. Two small access holes needed.</p>
<ul><li>Best for: Fully deteriorated pipes</li><li>Timeline: 1-2 days</li><li>Cost: $5,000 - $15,000</li></ul>

<h3>Traditional Excavation</h3>
<p>Dig up and replace the entire sewer line. Necessary when the line has collapsed or shifted significantly.</p>
<ul><li>Best for: Collapsed pipes, major bellies, depth issues</li><li>Timeline: 2-5 days</li><li>Cost: $3,000 - $25,000+</li></ul>

<h2>Why Choose Plumbers 911 for Oak Lawn Sewer Work</h2>
<ul>
<li>Licensed and insured Illinois plumbers</li>
<li>Free sewer camera inspection with any replacement</li>
<li>We handle all Village of Oak Lawn permits</li>
<li>Clean, respectful work — we restore your yard</li>
<li>Written warranty on all sewer work</li>
</ul>

<p><strong>Suspect sewer problems?</strong> Call <a href="tel:8337586911">833-758-6911</a> for a free <a href="/chicago-il-plumbing/sewer-camera-inspection/">sewer camera inspection</a> and honest assessment.</p>"""},
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
            "url_path": "/blog/" + post["slug"], "date": "2026-02-23 19:00:00",
            "modified": "2026-02-23 19:00:00", "author": "Plumbers 911 Chicago",
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
    print(f"\nDone. {added} new posts. Total: {len(posts)}")


if __name__ == "__main__":
    main()
