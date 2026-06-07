import os
import re
import json

base_dir = r"c:\Users\hsini\Desktop\website manga projects\Classroom-of-the-Elite"
manga_dir = os.path.join(base_dir, "manga")

def natural_sort_key(s):
    return [int(text) if text.isdigit() else text.lower() for text in re.split('([0-9]+)', s)]

def get_chapter_data(year):
    path = os.path.join(manga_dir, year)
    if not os.path.exists(path):
        return []
    
    chapters = []
    folders = [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))]
    folders.sort(key=natural_sort_key)
    
    for folder in folders:
        folder_path = os.path.join(path, folder)
        images = [f for f in os.listdir(folder_path) if f.lower().endswith(('.png', '.webp', '.jpg', '.jpeg'))]
        images.sort(key=natural_sort_key)
        
        # Look for cover-colored.png
        cover = next((f for f in images if 'cover-colored' in f.lower()), None)
        if not cover and images:
            cover = images[0] # Fallback to first image
            
        chapter_num = folder.replace('Chapter-', '')
        # Simple name extraction (if any) - for now just the num
        chapter_name = f"Chapter {chapter_num}"
        
        chapters.append({
            "id": folder,
            "num": chapter_num,
            "name": chapter_name,
            "cover": f"manga/{year}/{folder}/{cover}" if cover else None
        })
        
    return chapters

y1_data = get_chapter_data("year-1")
y2_data = get_chapter_data("year-2")

js_content = f"const CHAPTERS_Y1_META = {json.dumps(y1_data, indent=2)};\nconst CHAPTERS_Y2_META = {json.dumps(y2_data, indent=2)};"

with open(os.path.join(base_dir, "chapters_metadata.js"), "w", encoding="utf-8") as f:
    f.write(js_content)

print(f"Generated metadata for {len(y1_data)} Y1 chapters and {len(y2_data)} Y2 chapters.")
