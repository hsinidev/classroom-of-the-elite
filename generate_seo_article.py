import requests
import json
import time

URL = "https://ollama.com/api/generate"
MODEL = "gpt-oss:120b"

import os
# API keys are loaded from environment variables for security
env_keys = os.environ.get("BIGMODEL_API_KEY", "")
API_KEYS = [k.strip() for k in env_keys.split(",") if k.strip()] if env_keys else []

sections = [
    "Introduction to Classroom of the Elite: The genius of Ayanokouji Kiyotaka and the Advanced Nurturing High School rules.",
    "Year 1 Foundation: The Class D struggle, the S-System revealed, and the first Island Special Exam.",
    "Year 1 Midterm: The Sports Festival, Paper Shuffle, and the tactical battle against Ryuen Kakeru.",
    "Year 1 Climax: The final exam of the 1st year and the confrontation on the rooftop. Why Ayanokouji is the ultimate mastermind.",
    "Transition to 2nd Year: How the school rules evolved. The introduction of the OAA system and student evaluations.",
    "2nd Year New Rivals: The White Room enforcers arrive. Amasawa Ichika, Nanase Tsubasa, and Houzen Kazuomi.",
    "The 2nd Year Island Survival: Comparing Y1 vs Y2 survival exams. Higher stakes and more complex alliances.",
    "Nagumo Miyabi vs Manabu Horikita: The clash of student council presidents and how it shapes the school's future.",
    "Ayanokouji vs The World: His growth in Year 2, his relationship with Kei, and his tactical shift towards Class A.",
    "Character Deep Dive: Horikita Suzune, Kushida Kikyo, and Karuizawa Kei's development across two years.",
    "The White Room Mystery: Exploring the shadows of Ayanokouji's past and the Professor's influence.",
    "Conclusion and Future Outlook: What to expect from COTE Year 2 all chapters. Why it remains the top psychological manga."
]

target_keywords = [
    "Classroom of the Elite 2nd Year manga online",
    "COTE Year 2 all chapters",
    "Ayanokouji Year 2 vs Year 1"
]

def generate_section(section_topic, key, index):
    prompt = f"""
    Write a detailed, high-quality SEO-optimized section for a manga website about 'Classroom of the Elite'.
    Topic: {section_topic}
    Target Keywords: {', '.join(target_keywords)}
    Requirements:
    - Use semantic HTML (h2, h3, p, strong, ul, li).
    - Maintain a 'High-Tech Academic Terminal' tone: analytical, psychological, dualistic, and elite.
    - Aim for approximately 1000 words for this section.
    - Focus on the psychological depth and tactical brilliance of the series.
    - Ensure it flows well as Part {index+1} of a comprehensive 12,000-word guide.
    - Do not use generic filler. Provide actual plot analysis and character insights.
    """
    
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {key}"
    }
    
    # Note: Ollama standard generate prompt
    data = {
        "model": MODEL,
        "prompt": prompt,
        "stream": False
    }
    
    try:
        response = requests.post(URL, headers=headers, json=data, timeout=120)
        if response.status_code == 200:
            return response.json().get('response', '')
        else:
            print(f"Error {response.status_code}: {response.text}")
            return None
    except Exception as e:
        print(f"Exception: {e}")
        return None

def main():
    full_article = ""
    key_index = 0
    
    for i, topic in enumerate(sections):
        print(f"Generating section {i+1}/{len(sections)}: {topic[:50]}...", flush=True)
        
        # Try keys until one works
        success = False
        attempts = 0
        while not success and attempts < len(API_KEYS):
            key = API_KEYS[key_index % len(API_KEYS)]
            content = generate_section(topic, key, i)
            if content:
                full_article += f"\n<section id='section-{i+1}'>\n{content}\n</section>\n"
                success = True
                print(f"Successfully generated section {i+1}", flush=True)
            else:
                print(f"Key {key_index} failed, trying next key...")
                key_index += 1
                attempts += 1
                time.sleep(1)
        
        if not success:
            print(f"Failed to generate section {i+1} after trying all keys.")
            
        key_index += 1 # Cycle keys anyway
        
    if full_article:
        with open("article_content.html", "w", encoding="utf-8") as f:
            f.write(full_article)
        print("Article saved to article_content.html")
        
        # Inject into index.html
        with open("index.html", "r", encoding="utf-8") as f:
            html = f.read()
            
        placeholder = '<div id="article-body">'
        if placeholder in html:
            parts = html.split(placeholder)
            end_parts = parts[1].split('</div>', 1)
            new_html = parts[0] + placeholder + "\n" + full_article + "\n</div>" + end_parts[1]
            
            with open("index.html", "w", encoding="utf-8") as f:
                f.write(new_html)
            print("Injected article into index.html")

if __name__ == "__main__":
    main()
