"""
Enhance bathtub-install and shower-install pages that ended up in pages_page.json
"""
import json, os

DATA_DIR = r"C:\Users\User\OneDrive\Desktop\p911\site\data"

ENHANCEMENTS = {
    "bathtub-install": {
        "cost": "$1,000-$5,000+ depending on type (standard replacement, tub-to-shower conversion, freestanding, whirlpool)",
        "faq": [
            ("Can you convert my bathtub to a walk-in shower?", "Yes, bathtub-to-shower conversions are one of our most popular services. We handle all plumbing modifications including drain relocation, supply line adjustments, and valve installation."),
            ("How long does bathtub installation take?", "A straightforward replacement typically takes 1-2 days for plumbing work. Conversions or new installations requiring pipe rerouting may take 2-3 days."),
            ("Do I need a permit for bathtub installation in Chicago?", "Yes, plumbing permits are typically required in Chicago for bathtub installations, especially if drain lines are being modified. We handle all permit applications and inspections."),
        ],
    },
    "shower-install": {
        "cost": "$1,500-$5,000+ depending on type (shower replacement, new shower installation, custom tile shower plumbing)",
        "faq": [
            ("Can you install a shower where there wasn't one before?", "Yes, we can install new showers by running supply and drain lines to the new location. This is common in basement finishes and bathroom additions. Permits are required in Chicago."),
            ("What's involved in shower valve replacement?", "Shower valve replacement involves accessing the valve behind the wall, removing the old valve, installing the new one, and testing for proper temperature mixing and pressure. Most replacements take 2-4 hours."),
            ("Do you install rain showerheads and body sprays?", "Yes, we install all types of shower fixtures including rain showerheads, body sprays, handheld showers, and multi-head systems. Some installations require upgraded water supply lines for adequate pressure."),
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

path = os.path.join(DATA_DIR, "pages_page.json")
with open(path, "r", encoding="utf-8") as f:
    pages = json.load(f)

enhanced = 0
for pg in pages:
    slug = pg.get("slug", "")
    if slug not in ENHANCEMENTS or "arlington" in pg.get("url_path", ""):
        continue
    if "Frequently Asked Questions" in pg.get("content", ""):
        print(f"  SKIP: {slug}")
        continue
    enh = ENHANCEMENTS[slug]
    name = pg.get("title", slug.replace("-", " ").title())
    additions = f'\n<h2>{name} Cost in Chicago</h2>\n<p>Typical cost: <strong>{enh["cost"]}</strong>. Call <a href="tel:8337586911">833-758-6911</a> for a free estimate.</p>\n'
    additions += build_faq_html(enh["faq"])
    additions += build_faq_schema(enh["faq"])
    additions += '\n<div style="background:#f5f5f5; border-left:4px solid #e52521; padding:1.25rem; margin:2rem 0; border-radius:4px;">\n<p style="margin:0; font-weight:700; font-size:1.05rem;">Call Plumbers 911 Chicago at <a href="tel:8337586911">833-758-6911</a> for a free estimate. Licensed, bonded, and insured. Available 24/7.</p>\n</div>\n'
    pg["content"] = pg.get("content", "") + additions
    enhanced += 1
    print(f"  ENHANCED: {slug} (+{len(additions)} chars)")

with open(path, "w", encoding="utf-8") as f:
    json.dump(pages, f, indent=2, ensure_ascii=False)
print(f"\nDone. {enhanced} pages enhanced.")
