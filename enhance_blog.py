"""
Phase 53: Enhance the performing blog post (hot water heater blankets)
Phase 52: Add reading time and Article schema to all kept blog posts
"""
import json, os, math

DATA_DIR = r"C:\Users\User\OneDrive\Desktop\p911\site\data"

# Blog post enhancements
BLOG_ENHANCEMENTS = {
    "do-hot-water-heater-blankets-work": {
        "faq": [
            ("Do water heater blankets really save money?", "Yes, water heater blankets can reduce standby heat loss by 25-45%, saving $30-$80 per year on energy bills. They're most effective on older, uninsulated tanks and tanks in unheated spaces like garages or basements."),
            ("What type of water heater blanket should I buy?", "Look for blankets with an R-value of at least R-8. Fiberglass blankets are most common and affordable ($20-$40). Foil-backed blankets are easier to install. Make sure to get the right size for your tank (40, 50, or 80 gallon)."),
            ("Can I put a blanket on a gas water heater?", "Yes, but with caution. Never cover the top of a gas water heater, the thermostat, or the burner access panel at the bottom. Keep the blanket at least 2 inches away from the flue pipe. Electric water heaters can be fully wrapped."),
            ("How do I know if my water heater needs a blanket?", "Touch the side of your water heater tank. If it feels warm to the touch, it's losing heat and would benefit from a blanket. Newer water heaters (made after 2015) typically have enough built-in insulation, but older units often don't."),
            ("Should I replace my water heater instead of insulating it?", "If your water heater is over 10-12 years old, replacement may be more cost-effective than insulation. A new energy-efficient model saves more long-term. For units under 10 years old, a blanket is a smart, low-cost improvement. Contact Plumbers 911 Chicago at 833-758-6911 for advice."),
        ],
    },
    "what-is-the-average-life-expectancy-of-a-water-heater": {
        "faq": [
            ("How long does a tank water heater last?", "Tank water heaters typically last 8-12 years with proper maintenance. In the Chicago area, hard water can reduce lifespan. Annual flushing and anode rod replacement every 3-5 years can extend life to 15+ years."),
            ("How long does a tankless water heater last?", "Tankless water heaters last 20+ years on average, roughly twice as long as tank models. However, they require annual descaling in Chicago due to moderate water hardness to maintain efficiency and longevity."),
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

def estimate_reading_time(html_content):
    """Estimate reading time from HTML content."""
    import re
    text = re.sub(r'<[^>]+>', '', html_content)
    words = len(text.split())
    minutes = max(1, math.ceil(words / 225))
    return minutes

def main():
    path = os.path.join(DATA_DIR, "blog_posts.json")
    with open(path, "r", encoding="utf-8") as f:
        posts = json.load(f)

    enhanced = 0
    for post in posts:
        slug = post.get("slug", "")

        # Add reading time to all posts
        content = post.get("content", "")
        reading_time = estimate_reading_time(content)
        post["reading_time"] = str(reading_time) + " min read"

        # Add FAQ enhancements to specific posts
        if slug in BLOG_ENHANCEMENTS and "Frequently Asked Questions" not in content:
            enh = BLOG_ENHANCEMENTS[slug]
            additions = build_faq_html(enh["faq"])
            additions += build_faq_schema(enh["faq"])
            additions += '\n<p><strong>Need water heater service?</strong> Call Plumbers 911 Chicago at <a href="tel:8337586911">833-758-6911</a>. Licensed, bonded, and insured. Available 24/7.</p>\n'
            post["content"] = content + additions
            enhanced += 1
            print(f"  ENHANCED: {slug} (+{len(additions)} chars, {reading_time} min read)")
        else:
            print(f"  Reading time added: {slug} ({reading_time} min read)")

    with open(path, "w", encoding="utf-8") as f:
        json.dump(posts, f, indent=2, ensure_ascii=False)
    print(f"\nDone. {enhanced} blog posts enhanced with FAQ. All posts have reading times.")

if __name__ == "__main__":
    main()
