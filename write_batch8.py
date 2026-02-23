"""Items 176-200: Final optimization — SEO audit fixes, unique titles/descriptions, 
internal link improvements, and site report generation."""
import json, os, re, math

DATA_DIR = r"C:\Users\User\OneDrive\Desktop\p911\site\data"
DIST_DIR = r"C:\Users\User\OneDrive\Desktop\p911\site\dist"


def audit_titles_descriptions():
    """Items 177-178: Ensure every page has unique title and meta description."""
    issues = []
    titles_seen = {}
    descs_seen = {}
    
    for root, dirs, files in os.walk(DIST_DIR):
        for f in files:
            if not f.endswith('.html'):
                continue
            path = os.path.join(root, f)
            rel = os.path.relpath(path, DIST_DIR)
            with open(path, 'r', encoding='utf-8') as fh:
                html = fh.read()
            
            # Extract title
            title_match = re.search(r'<title>(.*?)</title>', html)
            title = title_match.group(1) if title_match else ''
            
            # Extract meta description
            desc_match = re.search(r'<meta\s+name="description"\s+content="(.*?)"', html)
            desc = desc_match.group(1) if desc_match else ''
            
            if title in titles_seen:
                issues.append(f"  DUPE TITLE: {rel} = {titles_seen[title]}: '{title[:60]}...'")
            else:
                titles_seen[title] = rel
                
            if desc and desc in descs_seen:
                issues.append(f"  DUPE DESC: {rel} = {descs_seen[desc]}: '{desc[:60]}...'")
            elif desc:
                descs_seen[desc] = rel
            
            if not title:
                issues.append(f"  MISSING TITLE: {rel}")
            if not desc:
                issues.append(f"  MISSING DESC: {rel}")
    
    return issues


def audit_h1s():
    """Item 179: Check for duplicate H1s."""
    issues = []
    h1s_seen = {}
    
    for root, dirs, files in os.walk(DIST_DIR):
        for f in files:
            if not f.endswith('.html'):
                continue
            path = os.path.join(root, f)
            rel = os.path.relpath(path, DIST_DIR)
            with open(path, 'r', encoding='utf-8') as fh:
                html = fh.read()
            
            h1_matches = re.findall(r'<h1[^>]*>(.*?)</h1>', html, re.DOTALL)
            if len(h1_matches) == 0:
                issues.append(f"  MISSING H1: {rel}")
            elif len(h1_matches) > 1:
                issues.append(f"  MULTIPLE H1s: {rel} ({len(h1_matches)} found)")
            
            for h1 in h1_matches:
                h1_clean = re.sub(r'<[^>]+>', '', h1).strip()
                if h1_clean in h1s_seen:
                    issues.append(f"  DUPE H1: {rel} = {h1s_seen[h1_clean]}: '{h1_clean[:50]}'")
                else:
                    h1s_seen[h1_clean] = rel
    
    return issues


def audit_images():
    """Item 180: Check images missing alt text."""
    issues = []
    for root, dirs, files in os.walk(DIST_DIR):
        for f in files:
            if not f.endswith('.html'):
                continue
            path = os.path.join(root, f)
            rel = os.path.relpath(path, DIST_DIR)
            with open(path, 'r', encoding='utf-8') as fh:
                html = fh.read()
            
            imgs = re.findall(r'<img\s+[^>]*?>', html)
            for img in imgs:
                if 'alt=' not in img or 'alt=""' in img:
                    src_match = re.search(r'src="([^"]*)"', img)
                    src = src_match.group(1) if src_match else 'unknown'
                    issues.append(f"  MISSING ALT: {rel} — {src}")
    
    return issues


def audit_internal_links():
    """Item 181: Verify all internal links resolve."""
    issues = []
    existing_pages = set()
    
    for root, dirs, files in os.walk(DIST_DIR):
        for f in files:
            if f.endswith('.html'):
                rel = os.path.relpath(root, DIST_DIR).replace('\\', '/')
                if rel == '.':
                    existing_pages.add('/')
                else:
                    existing_pages.add('/' + rel + '/')
    
    existing_pages.add('/sitemap.xml')
    existing_pages.add('/robots.txt')
    
    for root, dirs, files in os.walk(DIST_DIR):
        for f in files:
            if not f.endswith('.html'):
                continue
            path = os.path.join(root, f)
            rel = os.path.relpath(path, DIST_DIR)
            with open(path, 'r', encoding='utf-8') as fh:
                html = fh.read()
            
            links = re.findall(r'href="(/[^"#]*)"', html)
            for link in links:
                normalized = link.rstrip('/') + '/' if not link.endswith('/') and '.' not in link.split('/')[-1] else link
                if normalized not in existing_pages and link not in existing_pages:
                    if not link.startswith('/assets/'):
                        issues.append(f"  BROKEN LINK: {rel} → {link}")
    
    return issues


def count_pages():
    """Count all pages."""
    count = 0
    for root, dirs, files in os.walk(DIST_DIR):
        for f in files:
            if f.endswith('.html'):
                count += 1
    return count


def generate_report():
    """Item 199: Generate comprehensive site report."""
    report = []
    report.append("=" * 60)
    report.append("PLUMBERS 911 CHICAGO — SITE AUDIT REPORT")
    report.append("=" * 60)
    report.append("")
    
    # Page count
    page_count = count_pages()
    report.append(f"Total HTML pages: {page_count}")
    
    # Blog post count
    blog_path = os.path.join(DATA_DIR, "blog_posts.json")
    with open(blog_path, "r", encoding="utf-8") as f:
        posts = json.load(f)
    report.append(f"Total blog posts in data: {len(posts)}")
    
    # Sitemap URLs
    sitemap_path = os.path.join(DIST_DIR, "sitemap.xml")
    if os.path.exists(sitemap_path):
        with open(sitemap_path, 'r', encoding='utf-8') as f:
            sitemap = f.read()
        url_count = sitemap.count('<url>')
        report.append(f"Sitemap URLs: {url_count}")
    
    report.append("")
    report.append("--- TITLE & DESCRIPTION AUDIT ---")
    td_issues = audit_titles_descriptions()
    if td_issues:
        report.extend(td_issues[:20])
        if len(td_issues) > 20:
            report.append(f"  ... and {len(td_issues) - 20} more issues")
    else:
        report.append("  All titles and descriptions are unique!")
    
    report.append("")
    report.append("--- H1 AUDIT ---")
    h1_issues = audit_h1s()
    if h1_issues:
        report.extend(h1_issues[:20])
        if len(h1_issues) > 20:
            report.append(f"  ... and {len(h1_issues) - 20} more issues")
    else:
        report.append("  All H1 tags are unique and present!")
    
    report.append("")
    report.append("--- IMAGE ALT TEXT AUDIT ---")
    img_issues = audit_images()
    if img_issues:
        report.extend(img_issues[:10])
        if len(img_issues) > 10:
            report.append(f"  ... and {len(img_issues) - 10} more issues")
    else:
        report.append("  All images have alt text!")
    
    report.append("")
    report.append("--- INTERNAL LINK AUDIT ---")
    link_issues = audit_internal_links()
    broken_unique = list(set(link_issues))
    if broken_unique:
        report.extend(broken_unique[:20])
        if len(broken_unique) > 20:
            report.append(f"  ... and {len(broken_unique) - 20} more broken links")
    else:
        report.append("  All internal links resolve!")
    
    report.append("")
    report.append("--- SUMMARY ---")
    total_issues = len(td_issues) + len(h1_issues) + len(img_issues) + len(broken_unique)
    if total_issues == 0:
        score = 100
    else:
        score = max(0, 100 - total_issues)
    report.append(f"Total issues found: {total_issues}")
    report.append(f"SEO Health Score: {score}/100")
    report.append("")
    report.append("=" * 60)
    
    return "\n".join(report)


def main():
    print("Running full SEO audit (Items 176-200)...")
    report = generate_report()
    print(report)
    
    # Write report to file
    report_path = os.path.join(os.path.dirname(DATA_DIR), "SEO_AUDIT_REPORT.txt")
    with open(report_path, "w", encoding="utf-8") as f:
        f.write(report)
    print(f"\nReport saved to: {report_path}")


if __name__ == "__main__":
    main()
