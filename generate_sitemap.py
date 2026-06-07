import os
import re
import datetime

BASE_URL = "https://classroomelite.online"
JS_FILE = "chapters_metadata.js"
OUTPUT_FILE = "sitemap.xml"

def extract_chapters(content, var_name):
    pattern = rf"const {var_name} = \[(.*?)\];"
    match = re.search(pattern, content, re.DOTALL)
    if not match:
        return []
    
    # Simple extraction of IDs
    chapter_ids = re.findall(r'"id":\s*"(.*?)"', match.group(1))
    return chapter_ids

def generate_sitemap():
    if not os.path.exists(JS_FILE):
        print(f"Error: {JS_FILE} not found.")
        return

    with open(JS_FILE, "r", encoding="utf-8") as f:
        content = f.read()

    y1_chapters = extract_chapters(content, "CHAPTERS_Y1_META")
    y2_chapters = extract_chapters(content, "CHAPTERS_Y2_META")

    today = datetime.date.today().isoformat()

    sitemap_content = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">',
        '  <url>',
        f'    <loc>{BASE_URL}/</loc>',
        f'    <lastmod>{today}</lastmod>',
        '    <changefreq>daily</changefreq>',
        '    <priority>1.0</priority>',
        '  </url>',
        '  <url>',
        f'    <loc>{BASE_URL}/article_content.html</loc>',
        f'    <lastmod>{today}</lastmod>',
        '    <changefreq>weekly</changefreq>',
        '    <priority>0.8</priority>',
        '  </url>'
    ]

    # Add Legal Pages
    legal_pages = ["privacy.html", "dmca.html", "terms.html", "cookies.html", "disclaimer.html", "about.html", "contact.html"]
    for page in legal_pages:
        sitemap_content.extend([
            '  <url>',
            f'    <loc>{BASE_URL}/{page}</loc>',
            f'    <lastmod>{today}</lastmod>',
            '    <changefreq>monthly</changefreq>',
            '    <priority>0.3</priority>',
            '  </url>'
        ])

    # Add Year 1 Chapters
    for cid in y1_chapters:
        sitemap_content.extend([
            '  <url>',
            f'    <loc>{BASE_URL}/manga/year-1/{cid}/index.html</loc>',
            f'    <lastmod>{today}</lastmod>',
            '    <changefreq>weekly</changefreq>',
            '    <priority>0.7</priority>',
            '  </url>'
        ])

    # Add Year 2 Chapters
    for cid in y2_chapters:
        sitemap_content.extend([
            '  <url>',
            f'    <loc>{BASE_URL}/manga/year-2/{cid}/index.html</loc>',
            f'    <lastmod>{today}</lastmod>',
            '    <changefreq>weekly</changefreq>',
            '    <priority>0.7</priority>',
            '  </url>'
        ])

    sitemap_content.append('</urlset>')

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write("\n".join(sitemap_content))

    print(f"Successfully generated {OUTPUT_FILE} with {len(y1_chapters) + len(y2_chapters) + 9} URLs.")

if __name__ == "__main__":
    generate_sitemap()
