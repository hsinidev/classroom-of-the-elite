import os
import re

def natural_sort_key(s):
    return [int(text) if text.isdigit() else text.lower() for text in re.split('([0-9]+)', s)]

base_dir = r"c:\Users\hsini\Desktop\website manga projects\Classroom-of-the-Elite"
manga_dir = os.path.join(base_dir, "manga")

def get_chapters(year):
    path = os.path.join(manga_dir, year)
    if not os.path.exists(path):
        return []
    chapters = [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))]
    chapters.sort(key=natural_sort_key)
    # Check if index.html exists in each folder
    valid_chapters = []
    for c in chapters:
        if os.path.exists(os.path.join(path, c, "index.html")):
            valid_chapters.append(c)
    return valid_chapters

y1 = get_chapters("year-1")
y2 = get_chapters("year-2")

js_content = f'const CHAPTERS_Y1 = {y1};\\nconst CHAPTERS_Y2 = {y2};'

with open(os.path.join(base_dir, "chapters.js"), "w") as f:
    f.write(js_content)

print(f"Updated chapters.js with {len(y1)} Y1 chapters and {len(y2)} Y2 chapters.")
