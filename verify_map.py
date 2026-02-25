html = open("dist/service-area/index.html", "r", encoding="utf-8").read()
print("Has county-map SVG:", "county-map" in html)
print("Has countyData:", "countyData" in html)
print("Has Cook data:", '"Cook"' in html)
print("Has county-group:", "county-group" in html)
# Check JSON rendered
import re
m = re.search(r'var countyData = (\{.{50})', html)
if m:
    print("County data starts:", m.group(1)[:80])
else:
    print("WARNING: countyData not found or empty")
