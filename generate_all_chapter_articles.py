import os
import requests
import json
import random
import time
import re

# --- CONFIGURATION ---
OLLAMA_URL = "https://ollama.com/api/generate"
MODEL = "gpt-oss:120b"
BASE_DIR = r"c:\Users\hsini\Desktop\website manga projects\Classroom-of-the-Elite"
MANGA_DIR = os.path.join(BASE_DIR, "manga")

# Rotating API Keys for high-volume generation
import os
# API keys are loaded from environment variables for security
env_keys = os.environ.get("BIGMODEL_API_KEY", "")
API_KEYS = [k.strip() for k in env_keys.split(",") if k.strip()] if env_keys else []

# Author Personas for variety (avoids Google spam)
PERSONAS = [
    {"name": "The Analytical Strategist", "style": "Highly clinical, data-driven, focused on game theory and Ayanokouji's tactical moves."},
    {"name": "The Emotional Survivor", "style": "Passionate, focuses on character feelings, trauma, and personal growth. Uses evocative language."},
    {"name": "The Neutral Archivist", "style": "Objective, encyclopedic, focuses on world-building and school rules. Formal tone."},
    {"name": "The Cynical Critic", "style": "Sharp, witty, looks for flaws and deconstructs character motives. Skeptical tone."},
    {"name": "The Fan-Theory Specialist", "style": "Speculative, creative, links small details to the White Room and future arcs."},
    {"name": "The Literary Academic", "style": "Focuses on subtext, symbolism, and parallels to classic literature and behavioral psychology."},
    {"name": "The Classroom Gossip", "style": "Conversational, focuses on student relationships and social hierarchy. High-energy tone."},
    {"name": "The Tactical Analyst", "style": "Obsessed with the S-System and point-allocation strategies. Precise and technical."},
    {"name": "The Philosophical Debater", "style": "Discusses the ethics of the school, the concept of 'merit', and human nature."},
    {"name": "The Narrative Architect", "style": "Focuses on pacing, plot structure, and how the author builds tension in this specific chapter."}
]

# Shared Keywords for SEO
KEYWORDS = [
    "Classroom of the Elite Year 2 All Chapters",
    "Read COTE Manga Online",
    "Ayanokouji Kiyotaka Genius Tactics",
    "Classroom of the Elite Chapter Analysis",
    "White Room Mystery Explained"
]

def get_chapter_title(year, chapter):
    y_num = "1" if "year-1" in year else "2"
    c_num = chapter.replace("Chapter-", "")
    return f"Year {y_num} Chapter {c_num}"

def call_ollama(prompt, persona_name):
    # Rotate through API keys
    api_key = random.choice(API_KEYS)
    print(f"   [Cloud API] Using Key: {api_key[:8]}... | Persona: {persona_name}", flush=True)
    
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    
    data = {
        "model": MODEL,
        "prompt": prompt,
        "stream": False,
        "options": {
            "num_predict": 4096,
            "temperature": 0.8
        }
    }
    
    try:
        response = requests.post(OLLAMA_URL, json=data, headers=headers, timeout=300)
        if response.status_code == 200:
            content = response.json().get("response", "")
            return content
        else:
            print(f"   [Error] API Status: {response.status_code} | {response.text}")
            return None
    except Exception as e:
        print(f"   [Error] Exception during API call: {e}")
        return None

def generate_article(year, chapter):
    title = get_chapter_title(year, chapter)
    persona = random.choice(PERSONAS)
    
    prompt = f"""
    Write a definitive 3500-word SEO-optimized psychological analysis article for: {title} of the Classroom of the Elite manga.
    
    AUTHOR PERSONA: {persona['name']}
    WRITING STYLE: {persona['style']}
    
    SEO REQUIREMENTS:
    1. EXTREME LENGTH: Goal is 3500 words. Be incredibly comprehensive.
    2. HTML STRUCTURE: Use <h2>, <h3>, <p>, <strong>, <ul>, and <li> tags.
    3. CONTENT MODULES:
       - Strategic Plot Deconstruction (Scene-by-scene).
       - Tactical Mind-Game Analysis (The S-System & Points).
       - Character Psychological Profiles (X-Ray of motives).
       - The White Room Legacy (Secrets & Shadows).
       - Visual Narrative Tension (Paneling & Art Review).
       - Future Trajectory (The next 20 chapters).
    4. KEYWORDS: {', '.join(random.sample(KEYWORDS, 3))}.
    5. THEME: High-Tech Academic Terminal (Analytical, Dark, Elite).
    
    Target Title: {title}. Generate the full article now:
    """

    content = call_ollama(prompt, persona['name'])
    return content

def inject_into_index(file_path, article_content):
    if not article_content:
        return False
        
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            html = f.read()
            
        # Markers for insertion
        start_marker = '<div class="px-8 pb-10 prose prose-invert prose-red max-w-none border-t border-white/5 pt-8">'
        end_marker = '<div class="mt-8 p-6'
        
        if start_marker in html and end_marker in html:
            parts = html.split(start_marker)
            subparts = parts[1].split(end_marker, 1)
            
            # Clean article content (remove markdown markers and common AI prefixes)
            article_content = article_content.replace('```html', '').replace('```', '')
            article_content = re.sub(r'^Here is the analysis.*?:', '', article_content, flags=re.IGNORECASE)
            
            new_html = parts[0] + start_marker + "\n" + article_content + "\n" + end_marker + subparts[1]
            
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_html)
            return True
        else:
            print(f"   [Error] Could not find markers in {file_path}")
            return False
    except Exception as e:
        print(f"   [Error] Failed to inject into {file_path}: {e}")
        return False

def main():
    print(f"--- STARTING CLOUD-POWERED SEO ENGINE ---", flush=True)
    print(f"Model: {MODEL} | URL: {OLLAMA_URL}", flush=True)
    
    count = 0
    for year_folder in ["year-1", "year-2"]:
        year_path = os.path.join(MANGA_DIR, year_folder)
        if not os.path.exists(year_path): continue
            
        chapters = [d for d in os.listdir(year_path) if os.path.isdir(os.path.join(year_path, d))]
        chapters.sort(key=lambda s: [int(text) if text.isdigit() else text.lower() for text in re.split('([0-9]+)', s)])
        
        for ch in chapters:
            index_path = os.path.join(year_path, ch, "index.html")
            if os.path.exists(index_path):
                print(f"\n[{count+1}] Analyzing {year_folder}/{ch}...", flush=True)
                
                article = generate_article(year_folder, ch)
                if article:
                    if inject_into_index(index_path, article):
                        print(f"   [Success] Deep-analysis injected.")
                        count += 1
                    else:
                        print(f"   [Failed] Injection marker error.")
                else:
                    print(f"   [Failed] Cloud generation failure.")
                
                time.sleep(1) # Small pause
            
    print(f"\n--- TERMINAL TASK COMPLETED ---")
    print(f"Total Cloud-Generated Analysis: {count}")

if __name__ == "__main__":
    main()
