import requests
import json
import time

URL = "https://ollama.com/api/generate"
MODEL = "gpt-oss:120b"
import os
# API keys are loaded from environment variables for security
env_keys = os.environ.get("BIGMODEL_API_KEY", "")
API_KEYS = [k.strip() for k in env_keys.split(",") if k.strip()] if env_keys else []

PAGES = [
    {"name": "Privacy", "file": "privacy.html"},
    {"name": "DMCA", "file": "dmca.html"},
    {"name": "Terms", "file": "terms.html"},
    {"name": "Cookies", "file": "cookies.html"},
    {"name": "Disclaimer", "file": "disclaimer.html"},
    {"name": "About", "file": "about.html"},
    {"name": "Contact", "file": "contact.html"}
]

TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{page_name} - Classroom Elite Online</title>
    <script src="https://unpkg.com/@tailwindcss/browser@4"></script>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;700;900&display=swap" rel="stylesheet">
    <style>
        body {{ background: #050505; color: #d1d5db; font-family: 'Inter', sans-serif; line-height: 1.8; }}
        .academic-terminal::before {{
            content: ""; position: fixed; top: 0; left: 0; width: 100%; height: 100%;
            background: linear-gradient(rgba(18, 16, 16, 0) 50%, rgba(0, 0, 0, 0.25) 50%), linear-gradient(90deg, rgba(255, 0, 0, 0.03), rgba(0, 255, 0, 0.01), rgba(0, 0, 255, 0.03));
            background-size: 100% 4px, 3px 100%; pointer-events: none; z-index: 50; opacity: 0.1;
        }}
    </style>
</head>
<body class="academic-terminal min-h-screen flex flex-col">
    <header class="bg-black/80 backdrop-blur-xl border-b border-white/5 px-6 py-6 text-center">
        <a href="/" class="text-2xl font-black text-white italic tracking-tighter uppercase no-underline">
            Classroom Elite <span class="text-red-500">Online</span>
        </a>
    </header>

    <main class="flex-grow container mx-auto max-w-4xl px-6 py-16">
        <h1 class="text-4xl md:text-6xl font-black text-white mb-12 uppercase italic border-l-8 border-red-600 pl-8">{page_name}</h1>
        <div class="prose prose-invert prose-red max-w-none">
            {content}
        </div>
    </main>

    <footer class="bg-black py-12 border-t border-white/5 text-center px-6">
        <nav class="flex flex-wrap justify-center gap-6 mb-8 text-[10px] font-black tracking-widest uppercase">
            <a href="privacy.html" class="hover:text-red-500 transition-colors">Privacy</a>
            <a href="dmca.html" class="hover:text-red-500 transition-colors">DMCA</a>
            <a href="terms.html" class="hover:text-red-500 transition-colors">Terms</a>
            <a href="cookies.html" class="hover:text-red-500 transition-colors">Cookies</a>
            <a href="disclaimer.html" class="hover:text-red-500 transition-colors">Disclaimer</a>
            <a href="about.html" class="hover:text-red-500 transition-colors">About</a>
            <a href="contact.html" class="hover:text-red-500 transition-colors">Contact</a>
        </nav>
        <p class="text-white/20 text-[10px] uppercase tracking-widest leading-loose">&copy; 2026 Classroom Elite Online // Strategic Data Terminal</p>
    </footer>
</body>
</html>
"""

def generate_content(page_name, key):
    prompt = f"Write a professional, detailed, and legally sound {page_name} page for a manga reading website called 'Classroom of the Elite Online'. Use HTML tags like <h2>, <p>, and <ul>. Maintain a slightly technical, academic, and serious tone fitting the series' atmosphere. Focus on user safety, copyright (DMCA), and the strategic nature of the platform."
    headers = { "Authorization": f"Bearer {key}"}
    data = { "model": MODEL, "prompt": prompt, "stream": False }
    try:
        response = requests.post(URL, headers=headers, json=data, timeout=60)
        return response.json().get('response', '')
    except: return None

def main():
    key_idx = 0
    for pg in PAGES:
        print(f"Generating {pg['name']}...")
        content = None
        while not content and key_idx < len(API_KEYS):
            content = generate_content(pg['name'], API_KEYS[key_idx])
            if not content: key_idx += 1
        
        if content:
            final_html = TEMPLATE.format(page_name=pg['name'], content=content)
            with open(pg['file'], "w", encoding="utf-8") as f:
                f.write(final_html)
            print(f"Stored {pg['file']}")
        else:
            print(f"Failed to generate {pg['name']}")

if __name__ == "__main__":
    main()
