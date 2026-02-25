"""Build county-to-city mapping for the SVG map component."""
import json

# All 248 cities mapped to their Illinois county
COUNTY_MAP = {
    "Cook": [
        "Alsip", "Arlington Heights", "Barrington", "Bedford Park", "Bellwood",
        "Berkeley", "Berwyn", "Blue Island", "Bridgeview", "Broadview",
        "Brookfield", "Buffalo Grove", "Burbank", "Burnham", "Burr Ridge",
        "Calumet City", "Chicago", "Chicago Heights", "Chicago Ridge", "Cicero",
        "Country Club Hills", "Countryside", "Crestwood", "Crete", "Des Plaines",
        "Dolton", "Elk Grove Village", "Elmwood Park", "Evanston", "Evergreen Park",
        "Flossmoor", "Forest Park", "Fort Sheridan", "Franklin Park", "Glencoe",
        "Glenview", "Glenwood", "Harwood Heights", "Harvey", "Hazel Crest",
        "Hickory Hills", "Hillside", "Hines", "Hinsdale", "Hodgkins",
        "Hoffman Estates", "Hometown", "Homewood", "Indian Head Park", "Justice",
        "Kenilworth", "La Grange", "La Grange Park", "Lansing", "Lemont",
        "Lincolnwood", "Lyons", "Markham", "Matteson", "Maywood",
        "McCook", "Melrose Park", "Merrionette Park", "Midlothian", "Morton Grove",
        "Mount Prospect", "Niles", "Norridge", "North Riverside", "Northbrook",
        "Northlake", "Oak Brook", "Oak Forest", "Oak Lawn", "Oak Park",
        "Olympia Fields", "Orland Hills", "Orland Park", "Palatine", "Palos Heights",
        "Palos Hills", "Palos Park", "Park Forest", "Park Ridge", "Posen",
        "Prospect Heights", "Richton Park", "River Forest", "River Grove",
        "Riverdale", "Riverside", "Robbins", "Rolling Meadows", "Roselle",
        "Rosemont", "Sauk Village", "Schaumburg", "Schiller Park", "Skokie",
        "South Holland", "Steger", "Stickney", "Stone Park", "Streamwood",
        "Summit", "Summit Argo", "Thornton", "Thorton", "Tinley Park",
        "Western Springs", "Westchester", "Westmont", "Wheeling", "Wilmette",
        "Willow Springs", "Winnetka", "Worth"
    ],
    "DuPage": [
        "Addison", "Bartlett", "Bensenville", "Bloomingdale", "Bolingbrook",
        "Carol Stream", "Clarendon Hills", "Darien", "Downers Grove", "Elmhurst",
        "Glen Ellyn", "Glendale Heights", "Hanover Park", "Itasca", "Lisle",
        "Lombard", "Medinah", "Naperville", "Roselle", "Villa Park", "Warrenville",
        "Wayne", "West Chicago", "Westmont", "Wheaton", "Willowbrook", "Winfield",
        "Wood Dale", "Woodridge"
    ],
    "Will": [
        "Beecher", "Bolingbrook", "Braidwood", "Channahon", "Crest Hill",
        "Elwood", "Frankfort", "Homer Glen", "Joliet", "Lockport",
        "Manhattan", "Mokena", "Monee", "New Lenox", "Orland Park",
        "Peotone", "Plainfield", "Romeoville", "Shorewood", "Tinley Park",
        "University Park", "Wilmington"
    ],
    "Lake": [
        "Antioch", "Buffalo Grove", "Deerfield", "Fox Lake", "Fort Sheridan",
        "Grayslake", "Gurnee", "Hawthorn Woods", "Highland Park", "Highwood",
        "Ingleside", "Lake Bluff", "Lake Forest", "Lake Villa", "Lake Zurich",
        "Libertyville", "Lincolnshire", "Lindenhurst", "Long Grove", "Mundelein",
        "North Chicago", "Round Lake", "Round Lake Beach", "Russell",
        "Vernon Hills", "Wadsworth", "Waukegan", "Wauconda", "Winthrop Harbor",
        "Zion"
    ],
    "Kane": [
        "Aurora", "Batavia", "Big Rock", "Burlington", "Carpentersville",
        "Dundee", "East Dundee", "Elburn", "Elgin", "Geneva",
        "Gilberts", "Hampshire", "Kaneville", "Maple Park", "Mooseheart",
        "North Aurora", "St Charles", "St. Charles", "South Elgin",
        "Sugar Grove", "Wasco", "West Dundee"
    ],
    "McHenry": [
        "Algonquin", "Cary", "Crystal Lake", "Fox River Grove", "Garden Prairie",
        "Harvard", "Hebron", "Huntley", "Island Lake", "Kingston",
        "Lake In The Hills", "Lake in the Hills", "Marengo", "Mchenry", "McHenry",
        "Richmond", "Ringwood", "Spring Grove", "Union", "Wonder Lake", "Woodstock"
    ],
    "Kendall": [
        "Bristol", "Montgomery", "Oswego", "Plano", "Yorkville"
    ],
    "Grundy": [
        "Braceville", "Coal City", "Diamond", "Dwight", "Mazon",
        "Minooka", "Morris"
    ],
    "Kankakee": [
        "Bourbonnais", "Bradley", "Kankakee", "Manteno"
    ],
    "DeKalb": [
        "Cortland", "DeKalb", "Dekalb", "Genoa", "Hinckley",
        "Kingston", "Kirkland", "Malta", "Sandwich", "Shabbona", "Sycamore"
    ],
    "Boone": [
        "Belvidere", "Garden Prairie"
    ],
    "LaSalle": [
        "Grand Ridge", "La Salle", "Lostant", "Marseilles", "Mendota",
        "Oglesby", "Ottawa", "Peru", "Seneca", "Spring Valley",
        "Streator", "Tonica"
    ],
    "Livingston": [
        "Blackstone", "Dwight", "Long Point", "Minonk", "Pontiac"
    ],
    "Winnebago": [
        "Rockford"
    ],
    "Marshall": [
        "Long Point", "Rutland"
    ],
    "Bureau": [
        "Dana", "Grand Ridge", "La Fox"
    ],
    "Lee": [
        "Big Rock", "Fox Valley", "Salem"
    ]
}

# Load actual city list from location_index.json
cities = json.load(open("data/location_index.json", "r", encoding="utf-8"))
city_names = {c["city_name"] for c in cities}
city_slugs = {c["city_name"]: c["city_slug"] for c in cities}
city_urls = {c["city_name"]: c["url_path"] for c in cities}

# Check coverage
mapped = set()
for county, city_list in COUNTY_MAP.items():
    for c in city_list:
        mapped.add(c)

unmapped = city_names - mapped
print(f"Total cities: {len(city_names)}")
print(f"Mapped to counties: {len(mapped & city_names)}")
print(f"Unmapped: {len(unmapped)}")
if unmapped:
    for c in sorted(unmapped):
        print(f"  {c}")

# Save county map as JSON for the build
output = {}
for county, city_list in COUNTY_MAP.items():
    output[county] = []
    for c in sorted(city_list):
        if c in city_names:
            output[county].append({
                "name": c,
                "slug": city_slugs.get(c, ""),
                "url": city_urls.get(c, ""),
                "has_page": True
            })
    # Also note count
    print(f"{county}: {len(output[county])} cities matched")

with open("data/county_map.json", "w", encoding="utf-8") as f:
    json.dump(output, f, indent=2)
print("\nSaved data/county_map.json")
