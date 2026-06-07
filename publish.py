import os
import shutil

# --- CONFIGURATION ---
SOURCE_DIR = r"c:\Users\hsini\Desktop\website manga projects\Classroom-of-the-Elite"
OUT_DIR = os.path.join(SOURCE_DIR, "out")

# Essential production assets
ESSENTIAL_FILES = [
    "index.html",
    "article_content.html",
    "privacy.html",
    "dmca.html",
    "terms.html",
    "cookies.html",
    "disclaimer.html",
    "about.html",
    "contact.html",
    "sitemap.xml",
    "robots.txt",
    "favicon.png",
    "hero-y1.png",
    "hero-y2.png",
    "chapters.js",
    "chapters_metadata.js"
]

# Essential production directories
ESSENTIAL_DIRS = [
    "manga"
]

def publish():
    print(f"--- PREPARING PRODUCTION DEPLOYMENT ---")
    
    # 1. Clean previous build if exists
    if os.path.exists(OUT_DIR):
        print(f"   [Cleanup] Removing existing 'out/' folder...")
        shutil.rmtree(OUT_DIR)
    
    os.makedirs(OUT_DIR)
    print(f"   [System] Created fresh 'out/' directory.")

    # 2. Copy individual files
    for file in ESSENTIAL_FILES:
        src = os.path.join(SOURCE_DIR, file)
        dst = os.path.join(OUT_DIR, file)
        if os.path.exists(src):
            shutil.copy2(src, dst)
            print(f"   [Asset] Copied {file}")
        else:
            print(f"   [Warning] Missing essential file: {file}")

    # 3. Copy directories
    for directory in ESSENTIAL_DIRS:
        src = os.path.join(SOURCE_DIR, directory)
        dst = os.path.join(OUT_DIR, directory)
        if os.path.exists(src):
            print(f"   [System] Copying '{directory}' recursive... (This might take a moment)")
            shutil.copytree(src, dst)
            print(f"   [System] {directory} migration complete.")
        else:
            print(f"   [Error] Directory not found: {directory}")

    print(f"\n--- DEPLOYMENT READY ---")
    print(f"Location: {OUT_DIR}")
    print(f"Action Required: Upload the contents of 'out/' to your VPS /public_html directory.")

if __name__ == "__main__":
    publish()
