"""Location FAQs batch 1: Chicago through Oak Brook (10 cities)."""

def register(F):

    F["chicago"] = [
        {"question": "Does Chicago require a plumbing permit for water heater replacement?",
         "answer": "Yes. The City of Chicago requires a plumbing permit for water heater replacement. Your plumber must hold a Chicago Plumbing License in addition to the Illinois state license. We handle the permit and schedule the inspection."},
        {"question": "How do I get my lead service line replaced in Chicago?",
         "answer": "Chicago has an ongoing Lead Service Line Replacement Program. Homeowners can apply through the city's Department of Water Management. We work with homeowners to replace the private-side lead line from the property line to the home. Costs typically run $3,000–$8,000 for the homeowner's portion."},
        {"question": "Why does my basement flood during heavy rain in Chicago?",
         "answer": "Chicago uses a combined sewer system that handles both stormwater and sanitary sewage. During heavy rain, the system can back up into homes through floor drains. A backwater valve (overhead sewer conversion) prevents this. The city offers a cost-sharing program to help with installation."},
        {"question": "What areas of Chicago do you serve?",
         "answer": "We serve all 77 community areas across Chicago — from Rogers Park and Edgewater on the North Side to Beverly and Mount Greenwood on the South Side, and everywhere in between including the Loop, Lincoln Park, Lakeview, Logan Square, Pilsen, Bridgeport, and Hyde Park."},
        {"question": "How quickly can a plumber get to my Chicago home in an emergency?",
         "answer": "Most emergency calls within Chicago city limits are responded to within 30–60 minutes. Response times depend on your location, traffic, and current demand. We dispatch the nearest available licensed plumber to your address."}
    ]

    F["park-ridge"] = [
        {"question": "Does Park Ridge have different plumbing codes than Chicago?",
         "answer": "Yes. Park Ridge follows the Illinois State Plumbing Code rather than Chicago's municipal code. Permit requirements and inspection processes differ. We're familiar with Park Ridge's building department and handle permits for all plumbing work that requires them."},
        {"question": "Why is my water pressure low in Park Ridge?",
         "answer": "Park Ridge gets its water from the City of Chicago's system via an intergovernmental agreement. Low pressure can be caused by corroded galvanized supply lines inside your home, a partially closed main shutoff, or a failing pressure regulator. We diagnose and fix all of these."},
        {"question": "How old are the sewer lines in most Park Ridge homes?",
         "answer": "Many Park Ridge homes were built in the 1950s–1960s, meaning their original clay sewer lines are 60–70+ years old. These clay pipes are prone to root intrusion and joint failure. A camera inspection can assess their condition before problems arise."},
        {"question": "Do you offer emergency plumbing service in Park Ridge?",
         "answer": "Yes, 24/7. Park Ridge is a priority service area for us. Most emergency calls in Park Ridge are responded to within 30–45 minutes."},
        {"question": "Can you help with sump pump issues in Park Ridge?",
         "answer": "Absolutely. Park Ridge's high water table means sump pumps work hard, especially during spring thaws and heavy rains. We install, repair, and replace sump pumps and battery backup systems to keep your basement dry year-round."}
    ]

    F["joliet"] = [
        {"question": "Does Joliet have hard water?",
         "answer": "Yes. Joliet's water comes from underground wells and is notably hard — typically 20–25 grains per gallon. This causes significant mineral buildup in water heaters, pipes, and fixtures. A water softener is strongly recommended for Joliet homes."},
        {"question": "What's different about plumbing in Joliet versus Chicago?",
         "answer": "Joliet follows Will County and Illinois state plumbing codes, which differ from Chicago's municipal code. Joliet also has harder well water, different soil conditions (more limestone), and its own permit and inspection process. We know Joliet's requirements and work with the local building department regularly."},
        {"question": "How much does a water softener cost in Joliet?",
         "answer": "A standard water softener installation in Joliet runs $1,200–$3,000 including the unit and labor. Given Joliet's extremely hard water, a softener pays for itself in extended appliance life, reduced soap usage, and fewer plumbing repairs from scale buildup."},
        {"question": "Do you serve all of Joliet and surrounding Will County areas?",
         "answer": "Yes. We cover all of Joliet plus surrounding Will County communities including Plainfield, Romeoville, Lockport, Shorewood, Crest Hill, and New Lenox."},
        {"question": "Can you replace a sewer line in Joliet?",
         "answer": "Yes. We replace sewer lines in Joliet using both traditional excavation and trenchless methods. Joliet's limestone bedrock can make excavation more challenging in some areas, which is why trenchless options like pipe bursting or lining are popular here. We assess your specific situation and recommend the best approach."}
    ]

    F["arlington-heights"] = [
        {"question": "What plumbing permits does Arlington Heights require?",
         "answer": "Arlington Heights requires permits for most plumbing work beyond basic repairs — water heater replacements, fixture additions, sewer work, and remodeling. Permits are obtained through the Village's Community Development Department. We pull permits and schedule inspections as part of the job."},
        {"question": "Is Arlington Heights water hard?",
         "answer": "Moderately. Arlington Heights purchases Lake Michigan water through the Northwest Suburban Municipal Joint Action Water Agency. It's softer than well water but harder than Chicago city water. Some homeowners still benefit from a water softener or conditioning system."},
        {"question": "Do you handle sump pump installation in Arlington Heights?",
         "answer": "Yes. Many Arlington Heights homes, particularly those in flood-prone areas near Salt Creek, rely heavily on sump pumps. We install primary pumps, battery backup systems, and can upgrade undersized pumps to handle heavy water flow during spring storms."},
        {"question": "How fast can you respond to a plumbing emergency in Arlington Heights?",
         "answer": "We typically respond to Arlington Heights emergency calls within 30–60 minutes. We have plumbers in the northwest suburban area available 24/7 for burst pipes, sewer backups, and other emergencies."},
        {"question": "Can you repipe an older Arlington Heights home?",
         "answer": "Yes. Many homes in Arlington Heights built in the 1950s–1970s still have original galvanized steel supply lines that are corroding and restricting water flow. We repipe with copper or PEX, restoring full pressure to every fixture. Most repipes take 2–3 days."}
    ]

    F["park-forest"] = [
        {"question": "What plumbing issues are common in Park Forest homes?",
         "answer": "Park Forest was built primarily in the late 1940s–1950s as one of America's first planned communities. The original plumbing — galvanized supply lines and cast iron drains — is now 70+ years old. Common issues include low water pressure from corroded galvanized pipes, sewer line root intrusion, and aging water heaters."},
        {"question": "Does Park Forest have a lead pipe problem?",
         "answer": "Some Park Forest homes may have lead service lines connecting to the water main. The Village has been working on identification and replacement. If you're unsure about your service line material, we can inspect and advise on replacement options."},
        {"question": "How much does a whole-house repipe cost in Park Forest?",
         "answer": "For a typical Park Forest ranch or split-level home, whole-house repiping runs $4,000–$8,000 depending on the number of fixtures, pipe material chosen (copper vs. PEX), and accessibility. Given the age of Park Forest's housing stock, this is one of the most common jobs we do there."},
        {"question": "Do you service Park Forest and surrounding south suburbs?",
         "answer": "Yes. We serve Park Forest and all surrounding south Cook County communities including Matteson, Olympia Fields, Richton Park, University Park, Chicago Heights, and Flossmoor."},
        {"question": "Can you help with basement flooding in Park Forest?",
         "answer": "Yes. Basement flooding is common in Park Forest due to aging storm and sanitary sewers. We install and repair sump pumps, battery backups, and backwater valves. For recurring sewer backups, we camera-inspect the line and recommend cleaning or replacement as needed."}
    ]

    F["cicero"] = [
        {"question": "Does Cicero follow Chicago plumbing codes?",
         "answer": "No. Cicero is an independent municipality with its own building department and follows the Illinois State Plumbing Code. Permit requirements and inspection processes differ from Chicago. We're familiar with Cicero's codes and handle all permit work."},
        {"question": "What are common plumbing problems in Cicero homes?",
         "answer": "Cicero has a mix of older brick two-flats and single-family homes built from the 1920s–1960s. Common issues include corroded galvanized water lines, deteriorating cast iron sewer stacks, lead service lines, and aging water heaters. The dense housing stock also means sewer line access can be challenging."},
        {"question": "How much does a plumber charge for a service call in Cicero?",
         "answer": "A standard service call in Cicero runs $150–$300 including diagnosis and the first hour of labor. Emergency and after-hours calls are higher. We provide upfront pricing before starting any work beyond the initial assessment."},
        {"question": "Do you handle commercial plumbing in Cicero?",
         "answer": "Yes. Cicero has a large commercial and industrial corridor along Cicero Avenue and Cermak Road. We serve restaurants, retail spaces, warehouses, and multi-unit residential buildings with full commercial plumbing services including drain maintenance, backflow testing, and emergency response."},
        {"question": "Can you replace a sewer line in Cicero's tight lots?",
         "answer": "Yes. Cicero's narrow lots and gangways make traditional sewer excavation challenging. Trenchless methods like pipe bursting and lining are often the best option here — less digging, less disruption to your property and your neighbors. We assess access and recommend the most practical method."}
    ]

    F["bartlett"] = [
        {"question": "Where does Bartlett get its water?",
         "answer": "Bartlett purchases Lake Michigan water through the DuPage Water Commission. The water quality is good but moderately hard. Some Bartlett homeowners choose to install water softeners to reduce mineral buildup on fixtures and in appliances."},
        {"question": "Do you need a permit for plumbing work in Bartlett?",
         "answer": "Yes. The Village of Bartlett requires permits for water heater replacements, fixture additions, sewer repairs, and remodeling plumbing. We handle the permit application and inspection scheduling through Bartlett's Building Division."},
        {"question": "What plumbing issues are common in Bartlett?",
         "answer": "Bartlett has a mix of 1970s–1990s subdivisions and newer developments. Common issues include water heater failures (10–15 year old units), sump pump problems during heavy rains, and polybutylene pipe failures in some 1980s-era homes. Newer homes sometimes have builder-grade fixtures that fail prematurely."},
        {"question": "How fast can you get a plumber to Bartlett?",
         "answer": "Most emergency calls in Bartlett are responded to within 30–60 minutes. We have plumbers in the western suburban DuPage County area available around the clock."},
        {"question": "Do you install sump pumps in Bartlett?",
         "answer": "Yes. Bartlett's clay soil and relatively high water table make sump pumps essential for most homes. We install primary pumps, battery backup systems, and can add a second pump for redundancy. Annual sump pump testing before spring is recommended."}
    ]

    F["hickory-hills"] = [
        {"question": "What plumbing problems are common in Hickory Hills?",
         "answer": "Hickory Hills homes were largely built in the 1950s–1970s. Common issues include galvanized pipe corrosion causing low water pressure, cast iron drain stack deterioration, tree root intrusion in clay sewer lines, and aging water heaters. The area's clay soil also contributes to foundation settling that can stress drain lines."},
        {"question": "Does Hickory Hills use well water or city water?",
         "answer": "Hickory Hills receives Lake Michigan water through the Southwest Suburban Water Commission. The water is treated and relatively soft compared to well water, but mineral buildup can still affect fixtures and water heaters over time."},
        {"question": "How much does drain cleaning cost in Hickory Hills?",
         "answer": "A standard drain cleaning in Hickory Hills runs $100–$250 for a single fixture drain and $200–$500 for a main sewer line. Hydro jetting for thorough cleaning costs $400–$900. Emergency after-hours service adds a premium."},
        {"question": "Do you serve Hickory Hills and nearby southwest suburbs?",
         "answer": "Yes. We serve Hickory Hills and all surrounding communities including Palos Heights, Palos Hills, Worth, Chicago Ridge, Oak Lawn, Bridgeview, and Justice."},
        {"question": "Can you install a backwater valve in Hickory Hills?",
         "answer": "Yes. A backwater valve prevents sewer backups from entering your home during heavy rain — a common problem in southwest suburban communities. Installation runs $1,500–$3,500 depending on access. It's one of the best investments for basement flood prevention."}
    ]

    F["chicago-heights"] = [
        {"question": "What makes plumbing in Chicago Heights different?",
         "answer": "Chicago Heights has some of the oldest housing stock in the south suburbs, with many homes dating to the early 1900s. Original plumbing in these homes includes lead service lines, galvanized supply pipes, and clay sewer lines — all of which are past their useful life. The city's industrial history also means some areas have unique soil and water conditions."},
        {"question": "Does Chicago Heights have hard water?",
         "answer": "Chicago Heights gets its water from a deep well system, and it is notably hard. Hard water causes scale buildup in water heaters, white deposits on fixtures, and reduced soap efficiency. A water softener is highly recommended for Chicago Heights homes."},
        {"question": "How much does a water heater replacement cost in Chicago Heights?",
         "answer": "A standard 40–50 gallon gas water heater replacement in Chicago Heights runs $800–$1,800 including the unit, installation, and disposal of the old one. Given the hard water, we recommend periodic tank flushing to extend the new heater's life."},
        {"question": "Do you handle sewer line work in Chicago Heights?",
         "answer": "Yes. Sewer line cleaning, camera inspection, and replacement are among our most requested services in Chicago Heights. Many homes still have original clay sewer lines that are 80–100+ years old. We use camera inspections to assess condition before recommending cleaning or replacement."},
        {"question": "Is emergency plumbing service available in Chicago Heights?",
         "answer": "Yes, 24/7. We respond to emergency calls in Chicago Heights and surrounding south Cook County communities including Park Forest, Steger, South Chicago Heights, Sauk Village, and Lynwood."}
    ]

    F["oak-brook"] = [
        {"question": "What plumbing services do Oak Brook homes typically need?",
         "answer": "Oak Brook is an affluent community with larger homes that have more complex plumbing systems — multiple bathrooms, high-end fixtures, hydronic heating, and elaborate landscaping with irrigation. Common needs include water heater upgrades, bathroom remodel plumbing, backflow testing for irrigation systems, and sewer line maintenance."},
        {"question": "Does Oak Brook require backflow testing?",
         "answer": "Yes. If you have an irrigation system, fire suppression system, or any cross-connection, Oak Brook (through DuPage County Health Department) requires annual backflow preventer testing. We test, certify, and file the paperwork."},
        {"question": "How much does bathroom remodeling plumbing cost in Oak Brook?",
         "answer": "Given Oak Brook's larger homes and higher-end finishes, bathroom remodeling plumbing typically runs $2,000–$8,000+ depending on scope — from a basic fixture swap to a full master bath gut-and-rebuild with relocated drains and supply lines."},
        {"question": "Do you work on commercial properties in Oak Brook?",
         "answer": "Yes. Oak Brook has a significant commercial district including Oakbrook Center and surrounding office complexes. We provide commercial plumbing services including tenant buildouts, drain maintenance, backflow testing, and emergency response."},
        {"question": "Can you install a tankless water heater in Oak Brook?",
         "answer": "Yes. Tankless water heaters are popular in Oak Brook due to larger homes with higher hot water demand. We install Rinnai, Navien, and other premium brands. For larger homes, we may recommend multiple units or a recirculation system to eliminate wait times at distant fixtures."}
    ]
