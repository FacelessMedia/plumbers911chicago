"""Items 126-150: Glossary, tools pages, resource pages, more content."""
import json, os, math

DATA_DIR = r"C:\Users\User\OneDrive\Desktop\p911\site\data"

POSTS = [
    # Item 131: Cost estimator page
    {"slug": "plumbing-cost-estimator", "title": "Plumbing Cost Estimator — Get a Rough Estimate",
     "categories": [{"slug": "tools", "name": "Tools"}],
     "seo": {"title": "Plumbing Cost Estimator | Plumbers 911 Chicago", "description": "Estimate plumbing costs for common services in Chicago. Select your service type and get a rough price range instantly."},
     "content": """<p>Use this guide to get a rough idea of what common plumbing services cost in the Chicago area. <strong>These are estimates only</strong> — actual costs depend on your specific situation. Call <a href="tel:8337586911">833-758-6911</a> for a free, accurate quote.</p>

<h2 id="emergency">Emergency Services</h2>
<table>
<tr><th>Service</th><th>Estimated Cost</th></tr>
<tr><td>Emergency service call (diagnosis)</td><td>$150 - $300</td></tr>
<tr><td>Burst pipe repair</td><td>$200 - $1,000+</td></tr>
<tr><td>Frozen pipe thaw + repair</td><td>$200 - $800</td></tr>
<tr><td>Emergency sewer backup</td><td>$300 - $800</td></tr>
<tr><td>Emergency water heater repair</td><td>$200 - $800</td></tr>
</table>

<h2 id="drains">Drain & Sewer Services</h2>
<table>
<tr><th>Service</th><th>Estimated Cost</th></tr>
<tr><td>Single drain cleaning (snake)</td><td>$150 - $300</td></tr>
<tr><td>Main line cleaning</td><td>$250 - $500</td></tr>
<tr><td>Hydro jetting</td><td>$400 - $900</td></tr>
<tr><td>Sewer camera inspection</td><td>$200 - $500</td></tr>
<tr><td>Sewer line repair (spot)</td><td>$1,500 - $5,000</td></tr>
<tr><td>Sewer line replacement (full)</td><td>$3,000 - $25,000+</td></tr>
<tr><td>Trenchless sewer lining</td><td>$4,000 - $15,000</td></tr>
<tr><td>Sewer cleanout installation</td><td>$500 - $1,500</td></tr>
</table>

<h2 id="waterheater">Water Heater Services</h2>
<table>
<tr><th>Service</th><th>Estimated Cost</th></tr>
<tr><td>Water heater repair</td><td>$150 - $800</td></tr>
<tr><td>Tank water heater replacement (40-50 gal)</td><td>$1,500 - $3,500</td></tr>
<tr><td>Tankless water heater installation</td><td>$2,500 - $5,500</td></tr>
<tr><td>Water heater flush (maintenance)</td><td>$100 - $250</td></tr>
<tr><td>Anode rod replacement</td><td>$150 - $300</td></tr>
</table>

<h2 id="fixtures">Fixture Services</h2>
<table>
<tr><th>Service</th><th>Estimated Cost</th></tr>
<tr><td>Faucet repair</td><td>$150 - $300</td></tr>
<tr><td>Faucet replacement (with fixture)</td><td>$200 - $600</td></tr>
<tr><td>Toilet replacement (with toilet)</td><td>$250 - $500</td></tr>
<tr><td>Garbage disposal installation</td><td>$200 - $500</td></tr>
<tr><td>Dishwasher installation</td><td>$200 - $500</td></tr>
</table>

<h2 id="major">Major Projects</h2>
<table>
<tr><th>Service</th><th>Estimated Cost</th></tr>
<tr><td>Whole house repiping (copper)</td><td>$8,000 - $15,000+</td></tr>
<tr><td>Whole house repiping (PEX)</td><td>$4,000 - $10,000</td></tr>
<tr><td>Bathroom remodel (plumbing only)</td><td>$2,000 - $10,000</td></tr>
<tr><td>Kitchen remodel (plumbing only)</td><td>$1,500 - $5,000</td></tr>
<tr><td>Sump pump installation</td><td>$500 - $1,500</td></tr>
<tr><td>Sump pump battery backup</td><td>$300 - $600</td></tr>
<tr><td>Backwater valve installation</td><td>$1,000 - $3,000</td></tr>
</table>

<p><em>Prices are estimates for the Chicago metro area as of 2026. Actual costs vary based on complexity, access, materials, and urgency. Emergency and after-hours rates may be higher.</em></p>

<p><strong>Get an exact quote:</strong> Call <a href="tel:8337586911">833-758-6911</a> for a free estimate. No obligation.</p>"""},

    # Item 132: Pipe material identifier
    {"slug": "pipe-material-identifier-guide", "title": "How to Identify Your Pipe Material: Visual Guide",
     "categories": [{"slug": "guides", "name": "Guides"}],
     "seo": {"title": "How to Identify Your Pipe Material (Visual Guide)", "description": "Copper, galvanized, PVC, PEX, cast iron, or lead? How to identify what type of pipes are in your home and what it means."},
     "content": """<p>Knowing what type of pipes you have helps you understand potential problems, plan for replacements, and communicate effectively with plumbers. Here's how to identify each type.</p>

<h2 id="supply">Supply Line Materials (Water Pipes)</h2>

<h3>Copper</h3>
<ul>
<li><strong>Color:</strong> Reddish-brown (new) or greenish patina (old)</li>
<li><strong>Sound:</strong> Rings when tapped with a coin</li>
<li><strong>Joints:</strong> Soldered (smooth silver joints)</li>
<li><strong>Status:</strong> Good. Standard since 1960s. Lasts 50-70 years</li>
</ul>

<h3>Galvanized Steel</h3>
<ul>
<li><strong>Color:</strong> Gray, often with rust spots or flaking</li>
<li><strong>Sound:</strong> Dull thud when tapped</li>
<li><strong>Magnet test:</strong> Magnetic (sticks to a magnet)</li>
<li><strong>Status:</strong> REPLACE. Common in pre-1960 Chicago homes. Corrodes internally, reduces water pressure</li>
</ul>

<h3>PEX (Cross-Linked Polyethylene)</h3>
<ul>
<li><strong>Color:</strong> Red (hot), blue (cold), or white</li>
<li><strong>Texture:</strong> Flexible plastic, can bend</li>
<li><strong>Joints:</strong> Crimp rings or push-fit fittings</li>
<li><strong>Status:</strong> Good. Modern standard. Freeze-resistant</li>
</ul>

<h3>Lead</h3>
<ul>
<li><strong>Color:</strong> Dark gray, soft</li>
<li><strong>Scratch test:</strong> Scratch with a coin — shows shiny silver underneath</li>
<li><strong>Bend test:</strong> Slightly flexible</li>
<li><strong>Status:</strong> HEALTH HAZARD. Common as Chicago service lines. <a href="/blog/chicago-lead-pipe-replacement-program/">Check replacement program</a></li>
</ul>

<h2 id="drain">Drain/Sewer Materials</h2>

<h3>Cast Iron</h3>
<ul>
<li><strong>Color:</strong> Black or dark gray</li>
<li><strong>Sound:</strong> Dull thud</li>
<li><strong>Appearance:</strong> Heavy, thick-walled, often with hub-and-spigot joints</li>
<li><strong>Status:</strong> OK if under 75 years. Check for corrosion, cracks</li>
</ul>

<h3>PVC (Polyvinyl Chloride)</h3>
<ul>
<li><strong>Color:</strong> White or cream</li>
<li><strong>Appearance:</strong> Plastic, lightweight, smooth</li>
<li><strong>Joints:</strong> Cemented (glued)</li>
<li><strong>Status:</strong> Good. Modern standard for drains. Very long lifespan</li>
</ul>

<h3>ABS (Acrylonitrile Butadiene Styrene)</h3>
<ul>
<li><strong>Color:</strong> Black plastic</li>
<li><strong>Appearance:</strong> Similar to PVC but black</li>
<li><strong>Status:</strong> Good. Common in some areas, less common than PVC in Chicago</li>
</ul>

<h3>Clay (Vitrified Clay)</h3>
<ul>
<li><strong>Color:</strong> Reddish-brown (like terra cotta)</li>
<li><strong>Location:</strong> Underground sewer lines only</li>
<li><strong>Status:</strong> REPLACE if 50+ years old. Prone to root intrusion and cracking</li>
</ul>

<p><strong>Need pipe assessment?</strong> Call <a href="tel:8337586911">833-758-6911</a> for a professional plumbing inspection.</p>"""},

    # Item 133: Water heater sizing
    {"slug": "water-heater-sizing-guide", "title": "What Size Water Heater Do I Need? Sizing Guide",
     "categories": [{"slug": "guides", "name": "Guides"}],
     "seo": {"title": "What Size Water Heater Do I Need? Sizing Guide", "description": "How to choose the right water heater size for your household. Tank size guide based on family size, usage habits, and fixture count."},
     "content": """<p>An undersized water heater runs out of hot water. An oversized one wastes energy. Here's how to find the right size.</p>

<h2 id="tank">Tank Water Heater Sizing</h2>
<table>
<tr><th>Household Size</th><th>Recommended Tank Size</th></tr>
<tr><td>1-2 people</td><td>30-40 gallons</td></tr>
<tr><td>2-3 people</td><td>40-50 gallons</td></tr>
<tr><td>3-4 people</td><td>50-60 gallons</td></tr>
<tr><td>5+ people</td><td>60-80 gallons (or tankless)</td></tr>
</table>

<h2 id="peak">Peak Hour Demand Method</h2>
<p>For a more accurate sizing, calculate your peak hour demand:</p>
<table>
<tr><th>Activity</th><th>Gallons of Hot Water</th></tr>
<tr><td>Shower (per person)</td><td>10-15</td></tr>
<tr><td>Bath</td><td>20</td></tr>
<tr><td>Dishwasher cycle</td><td>6-10</td></tr>
<tr><td>Washing machine (hot)</td><td>20-30</td></tr>
<tr><td>Hand washing/shaving</td><td>2-4</td></tr>
</table>
<p>Add up the hot water used during your busiest hour. Your tank's <strong>first hour rating (FHR)</strong> should meet or exceed this number. FHR is listed on the water heater's yellow EnergyGuide label.</p>

<h2 id="tankless">Tankless Sizing</h2>
<p>Tankless heaters are sized by <strong>flow rate (GPM)</strong> and <strong>temperature rise</strong>. In Chicago, incoming water temperature drops to ~40°F in winter, requiring a 70°F rise to reach 110°F at the faucet.</p>
<ul>
<li><strong>1 shower:</strong> 2-3 GPM → Small tankless unit</li>
<li><strong>2 showers simultaneously:</strong> 4-6 GPM → Medium unit</li>
<li><strong>Whole house:</strong> 7-10 GPM → Large unit or multiple units</li>
</ul>

<p><strong>Need help sizing?</strong> Call <a href="tel:8337586911">833-758-6911</a> for a free in-home assessment.</p>"""},

    # Item 161: Glossary
    {"slug": "plumbing-glossary", "title": "Plumbing Glossary: 50+ Terms Every Homeowner Should Know",
     "categories": [{"slug": "guides", "name": "Guides"}],
     "seo": {"title": "Plumbing Glossary: 50+ Terms Explained", "description": "Complete plumbing glossary. Definitions of common plumbing terms from anode rod to water hammer. Understand what your plumber is talking about."},
     "content": """<p>Understanding plumbing terminology helps you communicate with plumbers and make informed decisions. Here are the most important terms every homeowner should know.</p>

<h2 id="a">A</h2>
<dl>
<dt><strong>Anode Rod</strong></dt><dd>A sacrificial metal rod inside a water heater tank that corrodes instead of the tank itself. Needs replacement every 3-5 years. <a href="/blog/water-heater-anode-rod-guide/">Learn more</a></dd>
<dt><strong>Auger</strong></dt><dd>A flexible cable tool used to clear drain clogs. Also called a drain snake</dd>
</dl>

<h2 id="b">B</h2>
<dl>
<dt><strong>Backflow</strong></dt><dd>Water flowing backward in the plumbing system, potentially contaminating the clean supply. Prevented by backflow prevention devices</dd>
<dt><strong>Backwater Valve</strong></dt><dd>A valve that prevents sewer water from flowing back into your home during heavy rain or sewer overflows</dd>
<dt><strong>Ball Valve</strong></dt><dd>A shutoff valve with a lever handle. Quarter-turn to close. More reliable than gate valves</dd>
</dl>

<h2 id="c">C</h2>
<dl>
<dt><strong>Cleanout</strong></dt><dd>An access point with a removable cap that provides entry to the sewer line for cleaning and inspection. <a href="/blog/what-is-sewer-cleanout-where-is-mine/">Find yours</a></dd>
<dt><strong>CIPP</strong></dt><dd>Cured-In-Place Pipe. A trenchless sewer repair method where a resin-coated liner is inserted and hardened inside the existing pipe</dd>
<dt><strong>Combined Sewer</strong></dt><dd>A sewer system that carries both sewage and stormwater in the same pipes. Chicago uses this system, which can cause backups during heavy rain</dd>
<dt><strong>Copper Piping</strong></dt><dd>Metal supply pipe standard since the 1960s. Lasts 50-70 years. Can develop pinhole leaks</dd>
</dl>

<h2 id="d">D</h2>
<dl>
<dt><strong>Drain Tile</strong></dt><dd>A perforated pipe system around a foundation that collects groundwater and directs it to a sump pit</dd>
<dt><strong>DWV</strong></dt><dd>Drain-Waste-Vent. The system of pipes that carries wastewater out and allows air in for proper drainage</dd>
</dl>

<h2 id="f">F</h2>
<dl>
<dt><strong>Flapper</strong></dt><dd>The rubber seal at the bottom of a toilet tank that lifts when you flush. The most common cause of running toilets</dd>
<dt><strong>Float</strong></dt><dd>The mechanism in a toilet tank that controls water level. When it reaches the set height, it stops the fill valve</dd>
<dt><strong>FHR (First Hour Rating)</strong></dt><dd>The number of gallons of hot water a tank water heater can deliver in the first hour of use</dd>
</dl>

<h2 id="g">G</h2>
<dl>
<dt><strong>Galvanized Steel</strong></dt><dd>Steel pipe coated with zinc. Used in homes before 1960. Corrodes internally over time, reducing water pressure. Should be replaced</dd>
<dt><strong>Gate Valve</strong></dt><dd>A shutoff valve with a round wheel handle. Multiple turns to close. Less reliable than ball valves</dd>
<dt><strong>GPM</strong></dt><dd>Gallons Per Minute. Used to measure water flow rate, especially for tankless water heater sizing</dd>
</dl>

<h2 id="h">H</h2>
<dl>
<dt><strong>Hydro Jetting</strong></dt><dd>Using high-pressure water (3,000-4,000 PSI) to clean the inside of drain and sewer pipes. More thorough than snaking</dd>
<dt><strong>Hydrostatic Pressure</strong></dt><dd>Water pressure in the soil around a foundation. Can force water through cracks in basement walls</dd>
</dl>

<h2 id="p">P</h2>
<dl>
<dt><strong>P-Trap</strong></dt><dd>The P-shaped curved pipe under sinks. Holds water to block sewer gases from entering the home</dd>
<dt><strong>PEX</strong></dt><dd>Cross-linked polyethylene. A flexible plastic pipe used for water supply. Color-coded red (hot) and blue (cold)</dd>
<dt><strong>PRV (Pressure Reducing Valve)</strong></dt><dd>A valve that reduces water pressure from the main to a safe level (40-80 PSI) for your home</dd>
<dt><strong>PSI</strong></dt><dd>Pounds Per Square Inch. Used to measure water pressure. Residential should be 40-80 PSI</dd>
<dt><strong>PVC</strong></dt><dd>Polyvinyl Chloride. White plastic pipe used for drain, waste, and vent lines. Very durable, long lifespan</dd>
</dl>

<h2 id="r">R</h2>
<dl>
<dt><strong>Rough-In</strong></dt><dd>The installation of plumbing pipes before walls and floors are finished. Critical during new construction or remodeling</dd>
<dt><strong>Rough-In Distance</strong></dt><dd>The distance from the wall to the center of the toilet drain. Standard is 12 inches</dd>
</dl>

<h2 id="s">S</h2>
<dl>
<dt><strong>Service Line</strong></dt><dd>The pipe connecting the city water main to your home. In Chicago, many are still lead</dd>
<dt><strong>Sewer Lateral</strong></dt><dd>The pipe connecting your home's plumbing to the city sewer main. Homeowner's responsibility to maintain</dd>
<dt><strong>Sump Pump</strong></dt><dd>A pump in a pit (sump) that removes water collecting under the foundation and discharges it away from the home</dd>
<dt><strong>Supply Line</strong></dt><dd>Pipes that bring clean water to fixtures. Separate from drain lines</dd>
</dl>

<h2 id="t">T</h2>
<dl>
<dt><strong>Tankless Water Heater</strong></dt><dd>A water heater that heats water on demand without storing it in a tank. Also called on-demand or instantaneous</dd>
<dt><strong>T&P Valve (Temperature & Pressure Relief)</strong></dt><dd>A safety valve on a water heater that opens if temperature or pressure exceeds safe levels. Essential safety device — never cap or remove it</dd>
<dt><strong>Trap</strong></dt><dd>A curved section of pipe that holds water to prevent sewer gases from entering the home. Every drain has one</dd>
</dl>

<h2 id="v">V</h2>
<dl>
<dt><strong>Vent Pipe</strong></dt><dd>A pipe that allows air into the drain system for proper flow and releases sewer gases above the roof</dd>
</dl>

<h2 id="w">W</h2>
<dl>
<dt><strong>Water Hammer</strong></dt><dd>A loud banging noise in pipes when water flow is suddenly stopped. Caused by pressure shock waves. Fixed with hammer arrestors</dd>
<dt><strong>Wax Ring</strong></dt><dd>A wax seal between the toilet base and the floor flange. Creates a watertight, gas-tight seal</dd>
</dl>

<p><strong>Have a plumbing question?</strong> Call <a href="tel:8337586911">833-758-6911</a> — we're happy to explain anything in plain English.</p>"""},

    # Item 166: Careers page
    {"slug": "careers-plumbing-jobs-chicago", "title": "Plumbing Jobs in Chicago — Careers at Plumbers 911",
     "categories": [{"slug": "about", "name": "About"}],
     "seo": {"title": "Plumbing Jobs Chicago | Careers at Plumbers 911", "description": "Join our team of licensed plumbers in Chicago. Competitive pay, benefits, steady work. We're hiring experienced plumbers and apprentices."},
     "content": """<p>Plumbers 911 Chicago is always looking for talented, licensed plumbers to join our growing team. We serve 188+ cities across the Chicago metro area, and we need reliable professionals to help our customers.</p>

<h2 id="positions">Open Positions</h2>
<h3>Licensed Plumber</h3>
<ul>
<li>Valid Illinois plumbing license required</li>
<li>3+ years residential plumbing experience</li>
<li>Experience with drain cleaning, water heaters, repiping, and sewer work</li>
<li>Clean driving record</li>
<li>Professional attitude and strong customer service skills</li>
</ul>

<h3>Plumbing Apprentice</h3>
<ul>
<li>Enrolled in or willing to enter an apprenticeship program</li>
<li>Basic mechanical aptitude</li>
<li>Reliable transportation</li>
<li>Willingness to learn and work hard</li>
</ul>

<h2 id="benefits">Why Work With Us</h2>
<ul>
<li><strong>Competitive pay</strong> — Above-market rates for licensed plumbers</li>
<li><strong>Steady work</strong> — We have more calls than we can handle</li>
<li><strong>No cold calling</strong> — All leads are inbound from our marketing</li>
<li><strong>Company vehicle</strong> for service calls</li>
<li><strong>Tools provided</strong></li>
<li><strong>Flexible scheduling</strong></li>
<li><strong>Growth opportunity</strong> — We're expanding rapidly</li>
</ul>

<h2 id="apply">How to Apply</h2>
<p>Call <a href="tel:8337586911">833-758-6911</a> and ask about career opportunities, or email your resume to our office. We respond to all qualified applicants within 48 hours.</p>"""},

    # Item 167: Financing page
    {"slug": "plumbing-financing-payment-options", "title": "Plumbing Financing & Payment Options",
     "categories": [{"slug": "about", "name": "About"}],
     "seo": {"title": "Plumbing Financing & Payment Options | Plumbers 911", "description": "Affordable plumbing service with flexible payment options. We accept all major payment methods. Ask about financing for major projects."},
     "content": """<p>We believe that everyone deserves access to quality plumbing service, regardless of budget. Here are the payment and financing options available to our customers.</p>

<h2 id="payment">Payment Methods Accepted</h2>
<ul>
<li>Cash</li>
<li>Check</li>
<li>All major credit cards (Visa, Mastercard, Amex, Discover)</li>
<li>Debit cards</li>
</ul>

<h2 id="financing">Financing for Major Projects</h2>
<p>For larger projects like sewer replacement, whole-house repiping, or water heater installation, ask about our financing options. We can help you find a payment plan that fits your budget.</p>

<h2 id="estimates">Free Estimates</h2>
<p>We provide free, written estimates for all non-emergency work. You'll know exactly what the job costs before we start. No surprises, no hidden fees.</p>

<h2 id="guarantee">Our Pricing Guarantee</h2>
<ul>
<li><strong>Upfront pricing</strong> — We quote before we work</li>
<li><strong>No overtime charges</strong> for standard after-hours calls</li>
<li><strong>No trip fees</strong> if we do the work</li>
<li><strong>Written estimates</strong> for all major work</li>
</ul>

<p><strong>Questions about cost?</strong> Call <a href="tel:8337586911">833-758-6911</a> for a free estimate.</p>"""},

    # Item 168: Warranties page
    {"slug": "plumbing-warranties-guarantees", "title": "Plumbing Warranties & Service Guarantees",
     "categories": [{"slug": "about", "name": "About"}],
     "seo": {"title": "Plumbing Warranties & Guarantees | Plumbers 911", "description": "Plumbers 911 stands behind our work. Learn about our labor warranties, manufacturer warranties, and satisfaction guarantee."},
     "content": """<p>When you hire Plumbers 911 Chicago, you're getting more than a repair — you're getting peace of mind. We stand behind every job we do.</p>

<h2 id="labor">Labor Warranty</h2>
<p>All labor performed by Plumbers 911 is warranted. If something we installed or repaired fails due to our workmanship, we'll fix it at no additional charge.</p>

<h2 id="manufacturer">Manufacturer Warranties</h2>
<p>All parts and equipment we install come with the manufacturer's warranty. We use only quality, brand-name products from trusted manufacturers including:</p>
<ul>
<li><strong>Water heaters:</strong> Rheem, A.O. Smith, Bradford White (6-12 year tank warranties)</li>
<li><strong>Tankless heaters:</strong> Rinnai, Navien, Noritz (5-15 year warranties)</li>
<li><strong>Fixtures:</strong> Moen, Delta, Kohler, American Standard</li>
<li><strong>Pipe materials:</strong> All PEX and copper from certified manufacturers</li>
</ul>

<h2 id="satisfaction">Satisfaction Guarantee</h2>
<p>We're not done until you're satisfied. If you're not happy with our work, tell us — we'll make it right.</p>

<h2 id="license">Licensed, Bonded & Insured</h2>
<p>Every Plumbers 911 technician holds a valid Illinois plumbing license. We carry comprehensive liability insurance and are fully bonded, protecting you and your property.</p>

<p><strong>Questions?</strong> Call <a href="tel:8337586911">833-758-6911</a>.</p>"""},

    # Item 169: Our Process page
    {"slug": "our-plumbing-service-process", "title": "Our Process: How Plumbers 911 Works",
     "categories": [{"slug": "about", "name": "About"}],
     "seo": {"title": "How Our Plumbing Service Works | Plumbers 911", "description": "Here's what to expect when you call Plumbers 911 Chicago. From first call to job completion, our process is transparent and hassle-free."},
     "content": """<p>From the moment you call to the moment we leave, here's exactly what to expect.</p>

<h2 id="step1">Step 1: Call Us</h2>
<p>Call <a href="tel:8337586911">833-758-6911</a>. A real person answers — no phone trees, no waiting. Tell us what's going on and we'll assess the urgency. For emergencies, we dispatch immediately. For non-urgent work, we schedule a convenient appointment.</p>

<h2 id="step2">Step 2: Diagnosis</h2>
<p>A licensed plumber arrives at your home, introduces themselves, and puts on shoe covers (we respect your home). They examine the problem, explain what they find in plain English, and answer your questions.</p>

<h2 id="step3">Step 3: Written Quote</h2>
<p>Before any paid work begins, you receive a written quote with the full cost. No surprises. You approve the price before we start. If you want a second opinion, no hard feelings.</p>

<h2 id="step4">Step 4: The Work</h2>
<p>Our plumber completes the repair or installation professionally. We protect your home with drop cloths, work efficiently, and clean up after ourselves. We handle all necessary permits.</p>

<h2 id="step5">Step 5: Walkthrough & Payment</h2>
<p>We walk you through what was done, show you the completed work, answer any questions, and explain maintenance tips to prevent future issues. Payment is collected only after you're satisfied.</p>

<h2 id="step6">Step 6: Follow-Up</h2>
<p>For major work, we follow up to make sure everything is working properly. Our warranty covers the work we performed, so if anything isn't right, we come back and fix it.</p>

<p><strong>Ready to get started?</strong> Call <a href="tel:8337586911">833-758-6911</a>.</p>"""},

    # Item 170: Coupons page
    {"slug": "plumbing-coupons-specials-chicago", "title": "Plumbing Coupons & Specials — Chicago Area",
     "categories": [{"slug": "about", "name": "About"}],
     "seo": {"title": "Plumbing Coupons & Specials Chicago | Plumbers 911", "description": "Save on plumbing services in Chicago. Current coupons, seasonal specials, and discounts for new customers. Call 833-758-6911."},
     "content": """<p>We want to make professional plumbing service affordable. Check out our current offers:</p>

<h2 id="current">Current Offers</h2>

<div class="testimonial-grid">
<div class="testimonial-card" style="text-align:center;">
<div style="font-size:2rem;font-weight:800;color:var(--red);">$50 OFF</div>
<p><strong>Any Plumbing Service Over $300</strong></p>
<p>First-time customers only. Mention this offer when booking.</p>
</div>

<div class="testimonial-card" style="text-align:center;">
<div style="font-size:2rem;font-weight:800;color:var(--red);">FREE</div>
<p><strong>Sewer Camera Inspection</strong></p>
<p>With any sewer cleaning service. A $200-$500 value.</p>
</div>

<div class="testimonial-card" style="text-align:center;">
<div style="font-size:2rem;font-weight:800;color:var(--red);">$100 OFF</div>
<p><strong>Water Heater Installation</strong></p>
<p>Tank or tankless. Includes removal of old unit.</p>
</div>
</div>

<h2 id="redeem">How to Redeem</h2>
<p>Mention the coupon when you call <a href="tel:8337586911">833-758-6911</a> to schedule service. Coupons cannot be combined with other offers. Subject to availability.</p>

<h2 id="seniors">Senior & Military Discounts</h2>
<p>We offer additional discounts for seniors (65+) and active military / veterans. Ask when you call.</p>"""},
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
            "id": str(16000 + added), "title": post["title"], "slug": post["slug"],
            "url_path": "/blog/" + post["slug"], "date": "2026-02-23 15:00:00",
            "modified": "2026-02-23 15:00:00", "author": "Plumbers 911 Chicago",
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
