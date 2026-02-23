"""
Phases 123-134, 140: SEO audit scripts + build pipeline improvements.
Runs checks on the built site and generates a report.
"""
import os
import re
import json
from html.parser import HTMLParser

DIST_DIR = r"C:\Users\User\OneDrive\Desktop\p911\site\dist"

class PageAuditor(HTMLParser):
    def __init__(self):
        super().__init__()
        self.title = ""
        self.meta_desc = ""
        self.h1_count = 0
        self.h1_text = ""
        self.has_canonical = False
        self.has_robots = False
        self.has_og_title = False
        self.has_og_desc = False
        self.images_without_alt = 0
        self.images_without_dims = 0
        self.total_images = 0
        self.internal_links = 0
        self.external_links = 0
        self.has_schema = False
        self._in_title = False
        self._in_h1 = False

    def handle_starttag(self, tag, attrs):
        d = dict(attrs)
        if tag == "title":
            self._in_title = True
        elif tag == "h1":
            self.h1_count += 1
            self._in_h1 = True
        elif tag == "meta":
            if d.get("name") == "description":
                self.meta_desc = d.get("content", "")
            if d.get("name") == "robots":
                self.has_robots = True
            if d.get("property") == "og:title":
                self.has_og_title = True
            if d.get("property") == "og:description":
                self.has_og_desc = True
        elif tag == "link" and d.get("rel") == "canonical":
            self.has_canonical = True
        elif tag == "img":
            self.total_images += 1
            if not d.get("alt"):
                self.images_without_alt += 1
            if not d.get("width") or not d.get("height"):
                self.images_without_dims += 1
        elif tag == "a":
            href = d.get("href", "")
            if href.startswith("http") and "plumbers911chicago" not in href:
                self.external_links += 1
            elif href.startswith("/") or href.startswith("#"):
                self.internal_links += 1
        elif tag == "script" and d.get("type") == "application/ld+json":
            self.has_schema = True

    def handle_data(self, data):
        if self._in_title:
            self.title += data
        if self._in_h1:
            self.h1_text += data

    def handle_endtag(self, tag):
        if tag == "title":
            self._in_title = False
        if tag == "h1":
            self._in_h1 = False


def audit_page(filepath):
    with open(filepath, "r", encoding="utf-8", errors="replace") as f:
        html = f.read()
    auditor = PageAuditor()
    try:
        auditor.feed(html)
    except:
        pass
    word_count = len(re.sub(r'<[^>]+>', '', html).split())
    return {
        "title": auditor.title.strip(),
        "title_len": len(auditor.title.strip()),
        "meta_desc": auditor.meta_desc[:80] + "..." if len(auditor.meta_desc) > 80 else auditor.meta_desc,
        "meta_desc_len": len(auditor.meta_desc),
        "h1_count": auditor.h1_count,
        "has_canonical": auditor.has_canonical,
        "has_robots": auditor.has_robots,
        "has_og": auditor.has_og_title and auditor.has_og_desc,
        "has_schema": auditor.has_schema,
        "imgs_no_alt": auditor.images_without_alt,
        "imgs_no_dims": auditor.images_without_dims,
        "total_images": auditor.total_images,
        "internal_links": auditor.internal_links,
        "external_links": auditor.external_links,
        "word_count": word_count,
        "file_size": os.path.getsize(filepath),
    }


def main():
    print("=" * 60)
    print("PLUMBERS 911 CHICAGO — SEO AUDIT REPORT")
    print("=" * 60)

    issues = []
    stats = {"total": 0, "with_schema": 0, "with_og": 0, "with_canonical": 0, "thin": 0}
    total_words = 0
    total_size = 0

    for root, dirs, files in os.walk(DIST_DIR):
        for f in files:
            if not f.endswith(".html"):
                continue
            filepath = os.path.join(root, f)
            rel = filepath.replace(DIST_DIR, "").replace("\\", "/").replace("/index.html", "/") or "/"
            result = audit_page(filepath)
            stats["total"] += 1
            total_words += result["word_count"]
            total_size += result["file_size"]

            if result["has_schema"]: stats["with_schema"] += 1
            if result["has_og"]: stats["with_og"] += 1
            if result["has_canonical"]: stats["with_canonical"] += 1

            # Check for issues
            if result["title_len"] > 65:
                issues.append(f"TITLE TOO LONG ({result['title_len']} chars): {rel}")
            if result["title_len"] < 20:
                issues.append(f"TITLE TOO SHORT ({result['title_len']} chars): {rel}")
            if result["meta_desc_len"] > 165:
                issues.append(f"META DESC TOO LONG ({result['meta_desc_len']} chars): {rel}")
            if result["meta_desc_len"] < 50:
                issues.append(f"META DESC TOO SHORT ({result['meta_desc_len']} chars): {rel}")
            if result["h1_count"] != 1:
                issues.append(f"H1 COUNT = {result['h1_count']} (should be 1): {rel}")
            if not result["has_canonical"]:
                issues.append(f"MISSING CANONICAL: {rel}")
            if not result["has_robots"]:
                issues.append(f"MISSING ROBOTS META: {rel}")
            if result["imgs_no_alt"] > 0:
                issues.append(f"{result['imgs_no_alt']} IMAGES WITHOUT ALT: {rel}")
            if result["word_count"] < 200:
                issues.append(f"THIN CONTENT ({result['word_count']} words): {rel}")
                stats["thin"] += 1
            if result["internal_links"] < 2:
                issues.append(f"LOW INTERNAL LINKS ({result['internal_links']}): {rel}")

    print(f"\n--- SUMMARY ---")
    print(f"Total HTML pages: {stats['total']}")
    print(f"Total word count: {total_words:,}")
    print(f"Total HTML size: {total_size/1024/1024:.1f} MB")
    print(f"Avg words/page: {total_words//stats['total']}")
    print(f"Pages with schema: {stats['with_schema']}/{stats['total']}")
    print(f"Pages with OG tags: {stats['with_og']}/{stats['total']}")
    print(f"Pages with canonical: {stats['with_canonical']}/{stats['total']}")
    print(f"Thin pages (<200 words): {stats['thin']}")

    print(f"\n--- ISSUES ({len(issues)}) ---")
    for issue in sorted(issues)[:50]:
        print(f"  {issue}")
    if len(issues) > 50:
        print(f"  ... and {len(issues)-50} more issues")

    print(f"\n--- HEALTH SCORE ---")
    score = 100
    score -= min(20, len([i for i in issues if "MISSING" in i]) * 2)
    score -= min(15, len([i for i in issues if "THIN" in i]) * 3)
    score -= min(10, len([i for i in issues if "TOO LONG" in i or "TOO SHORT" in i]))
    score -= min(10, len([i for i in issues if "H1 COUNT" in i]) * 2)
    score -= min(5, len([i for i in issues if "ALT" in i]))
    print(f"SEO Health Score: {max(0,score)}/100")
    print("=" * 60)


if __name__ == "__main__":
    main()
