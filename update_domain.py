import os

old_domain = "classroomoftheeliteonline.com"
new_domain = "classroomelite.online"

files_to_update = [
    "index.html",
    "article_content.html",
    "privacy.html",
    "dmca.html",
    "terms.html",
    "cookies.html",
    "disclaimer.html",
    "about.html",
    "contact.html",
    "generate_chapter_pages.py",
    "generate_sitemap.py",
    "robots.txt"
]

def update_domain(file_path):
    if not os.path.exists(file_path):
        print(f"Skipping {file_path} (not found)")
        return
    
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    new_content = content.replace(old_domain, new_domain)
    
    if content != new_content:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"Updated {file_path}")
    else:
        print(f"No changes needed for {file_path}")

if __name__ == "__main__":
    for file in files_to_update:
        update_domain(file)
