import os
import re

# natural sort for chapter folders
def natural_sort_key(s):
    return [int(text) if text.isdigit() else text.lower() for text in re.split('([0-9]+)', s)]

base_dir = r"c:\Users\hsini\Desktop\website manga projects\Classroom-of-the-Elite"
manga_dir = os.path.join(base_dir, "manga")
google_tag_id = "G-0NVX5DV7CE"

template = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} - Classroom Elite Online</title>
    <link rel="icon" type="image/x-icon" href="../../../favicon.png">
    <meta name="description" content="Read {title} manga online at Classroom Elite Online. High-resolution images, fast loading, and expert psychological analysis of Ayanokouji's tactics. Full chapter archive available.">
    <meta name="keywords" content="Read {title} Manga Online, Classroom of the Elite Chapter Analysis, COTE Manga HQ, Ayanokouji Kiyotaka Genius Tactics, White Room Secrets">
    
    <!-- GEO/Local SEO -->
    <meta name="geo.region" content="US-NY" />
    <meta name="geo.placename" content="New York" />
    <meta name="geo.position" content="40.7128;-74.0060" />
    <meta name="ICBM" content="40.7128, -74.0060" />

    <!-- Open Graph / Meta -->
    <meta property="og:title" content="{title} - Classroom Elite Online" />
    <meta property="og:type" content="article" />
    <meta property="og:url" content="https://classroomelite.online/manga/{year_id}/{chapter_id}/" />
    <meta property="og:image" content="https://classroomelite.online/manga/{year_id}/{chapter_id}/1.jpg" />
    <meta property="og:description" content="Official data terminal for {title}. Elite reading experience with high-tech pedagogical analysis." />
    
    <!-- JSON-LD Structured Data -->
    <script type="application/ld+json">
    {{
      "@context": "https://schema.org",
      "@type": "Article",
      "mainEntityOfPage": {{
        "@type": "WebPage",
        "@id": "https://classroomelite.online/manga/{year_id}/{chapter_id}/"
      }},
      "headline": "{title} - Strategy & Analysis",
      "description": "Read {title} manga online with deep psychological analysis and strategic breakdowns. Classroom Elite Online Terminal.",
      "image": "https://classroomelite.online/manga/{year_id}/{chapter_id}/1.jpg",
      "author": {{
        "@type": "Organization",
        "name": "Classroom Elite Online"
      }},
      "publisher": {{
        "@type": "Organization",
        "name": "Classroom Elite Online",
        "logo": {{
          "@type": "ImageObject",
          "url": "https://classroomelite.online/favicon.png"
        }}
      }},
      "datePublished": "2026-04-06",
      "dateModified": "2024-04-06",
      "genre": "Psychological Thriller",
      "keywords": "manga, strategy, school life, anime"
    }}
    </script>
    <script type="application/ld+json">
    {{
      "@context": "https://schema.org",
      "@type": "BreadcrumbList",
      "itemListElement": [{{
        "@type": "ListItem",
        "position": 1,
        "name": "Home",
        "item": "https://classroomelite.online/"
      }},{{
        "@type": "ListItem",
        "position": 2,
        "name": "{year_id}",
        "item": "https://classroomelite.online/manga/{year_id}/"
      }},{{
        "@type": "ListItem",
        "position": 3,
        "name": "{chapter_id}",
        "item": "https://classroomelite.online/manga/{year_id}/{chapter_id}/"
      }}]
    }}
    </script>

    <script src="https://cdn.tailwindcss.com"></script>
    <script>
        tailwind.config = {{
            theme: {{
                extend: {{
                    colors: {{
                        primary: '{primary_color}',
                        secondary: '#0d1117',
                        darkBg: '#050505',
                        accent: '{accent_color}',
                    }}
                }}
            }}
        }}
    </script>
    <style type="text/tailwindcss">
        @layer base {{
            body {{
                @apply bg-darkBg text-gray-300 font-sans;
            }}
        }}
        .header-wrap {{
            @apply fixed top-0 left-0 w-full z-[1000] bg-secondary/80 backdrop-blur-xl border-b border-white/5 transition-transform duration-500;
        }}
        .nav-btn {{
            @apply bg-white/5 border border-white/10 text-white font-black text-[10px] px-6 py-2 rounded uppercase italic tracking-widest hover:bg-primary hover:border-transparent transition-all duration-300;
        }}
        .manga-image {{
            @apply w-full max-w-5xl mx-auto block shadow-2xl;
        }}
        .academic-terminal::before {{
            content: ""; position: fixed; top: 0; left: 0; width: 100%; height: 100%;
            background: linear-gradient(rgba(18, 16, 16, 0) 50%, rgba(0, 0, 0, 0.1) 50%), 
                        linear-gradient(90deg, rgba(255, 0, 0, 0.02), rgba(0, 255, 0, 0.01), rgba(0, 0, 255, 0.02));
            background-size: 100% 3px, 3px 100%; pointer-events: none; z-index: 500; opacity: 0.1;
        }}
        select {{
            @apply bg-black/60 border border-white/10 text-white text-[10px] font-black uppercase tracking-widest px-4 py-2 rounded focus:border-primary transition-colors cursor-pointer outline-none appearance-none;
        }}
    </style>
    <!-- Google Tag Manager (gtag.js) -->
    <script async src="https://www.googletagmanager.com/gtag/js?id={tag_id}"></script>
    <script>
      window.dataLayer = window.dataLayer || [];
      function gtag(){{dataLayer.push(arguments);}}
      gtag('js', new Date());
      gtag('config', '{tag_id}');
    </script>
</head>
<body class="academic-terminal pt-20">
    <div id="progress-bar" class="fixed top-0 left-0 h-1 bg-primary z-[1100] transition-all duration-300 shadow-[0_0_15px_rgba(139,0,0,0.5)]"></div>

    <header id="main-header" class="header-wrap px-6 py-4">
        <div class="max-w-7xl mx-auto flex items-center justify-between gap-6">
            <a href="/" class="flex items-center gap-3 group">
                <div class="w-8 h-8 bg-primary/20 border border-primary/40 rounded flex items-center justify-center text-primary font-black text-xs">C</div>
                <div class="hidden md:block">
                    <span class="block text-white font-black text-[10px] leading-none uppercase italic tracking-tighter">Classroom Elite</span>
                    <span class="block text-white/30 text-[8px] font-mono tracking-widest uppercase mt-1">Terminal Access</span>
                </div>
            </a>
            
            <div class="flex-grow max-w-sm relative">
                <select onchange="window.location.href=this.value" class="w-full pr-10">
                    <option value="" disabled selected>JUMP_TO_CHAPTER</option>
                    {chapter_options}
                </select>
                <div class="absolute right-4 top-1/2 -translate-y-1/2 pointer-events-none text-white/20">
                    <svg class="w-3 h-3" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path d="M19 9l-7 7-7-7" stroke-width="4" stroke="currentColor"></path></svg>
                </div>
            </div>

            <div class="flex items-center gap-2">
                {prev_link}
                <a href="/" class="nav-btn !bg-accent/20 !border-accent/40 !text-accent hover:!bg-accent hover:!text-white border">Home</a>
                {next_link}
            </div>
        </div>
    </header>

    <main class="w-full pb-20 relative z-10">
        <div class="flex flex-col items-center bg-black">
            {images}
        </div>

        <div class="flex justify-center items-center gap-4 py-20 border-t border-white/5 bg-darkBg">
            {prev_link}
            <a href="/" class="nav-btn !bg-accent/20 !border-accent/40 !text-accent">TERMINAL_HOME</a>
            {next_link}
        </div>

        <!-- Read Info Section for SEO -->
        <div class="max-w-4xl mx-auto px-6">
            <details class="group bg-secondary/30 border border-white/5 rounded-xl overflow-hidden hover:border-primary/20 transition-all duration-300">
                <summary class="flex items-center justify-between px-8 py-6 cursor-pointer list-none">
                    <div class="flex items-center gap-4 text-primary">
                        <svg class="w-6 h-6 animate-pulse" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z"></path></svg>
                        <span class="font-heading font-black tracking-widest uppercase italic">READ INFO: STRATEGIC_ANALYSIS</span>
                    </div>
                    <svg class="w-5 h-5 text-primary group-open:rotate-180 transition-transform duration-300" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"></path></svg>
                </summary>
                <div class="px-8 pb-10 prose prose-invert prose-red max-w-none border-t border-white/5 pt-8">
                    <h3 class="text-primary italic uppercase font-black">Data Fragment: Psychological Deep-Dive</h3>
                    <p class="text-white/50 italic text-sm">Initializing analysis for {title}... Tactical overview and character evolution data will be populated by the academic terminal.</p>

                    <div class="mt-8 p-6 bg-white/5 border border-white/10 rounded-xl flex flex-col md:flex-row items-center justify-between gap-6">
                        <div class="text-[10px] text-white/30 font-mono italic uppercase tracking-widest">Compiling Full Strategy Breakdown...</div>
                        <a href="../../../article_content.html" class="px-6 py-3 bg-primary text-white font-black text-[10px] italic tracking-widest uppercase hover:opacity-80 transition-all no-underline rounded">Core Hub Analysis</a>
                    </div>
                </div>
            </details>
        </div>
    </main>

    <footer class="bg-black border-t border-white/5 py-20 text-center px-6">
        <nav class="flex flex-wrap justify-center gap-8 mb-12 text-[10px] font-black tracking-widest uppercase italic text-white/20">
            <a href="../../../privacy.html" class="hover:text-primary transition-colors">Privacy</a>
            <a href="../../../dmca.html" class="hover:text-primary transition-colors">DMCA</a>
            <a href="../../../terms.html" class="hover:text-primary transition-colors">Terms</a>
            <a href="../../../cookies.html" class="hover:text-primary transition-colors">Cookies</a>
            <a href="../../../disclaimer.html" class="hover:text-primary transition-colors">Disclaimer</a>
            <a href="../../../about.html" class="hover:text-primary transition-colors">About</a>
            <a href="../../../contact.html" class="hover:text-primary transition-colors">Contact</a>
        </nav>
        <div class="text-white/10 text-[9px] uppercase tracking-[0.5em] italic">Classroom Elite Online // Managed by AI Antigravity Terminal</div>
    </footer>

    <script>
        // Track reading progress
        const chapterId = "{chapter_id}";
        const yearId = "{year_id}";
        const storageKey = `read_${{yearId}}_${{chapterId}}`;
        localStorage.setItem(storageKey, 'true');

        // Scroll to top on load
        window.scrollTo(0, 0);

        // Header Show/Hide Logic & Progress Bar
        let lastScrollTop = 0;
        const header = document.getElementById('main-header');
        const progressBar = document.getElementById('progress-bar');

        window.addEventListener('scroll', () => {{
            let scrollTop = window.pageYOffset || document.documentElement.scrollTop;
            
            // Header Logic: Hide on scroll down, show on scroll up
            if (scrollTop > lastScrollTop && scrollTop > 100) {{
                header.style.transform = 'translateY(-100%)';
            }} else {{
                header.style.transform = 'translateY(0)';
            }}
            lastScrollTop = scrollTop;

            // Progress Logic
            const height = document.documentElement.scrollHeight - document.documentElement.clientHeight;
            const scrolled = (scrollTop / height) * 100;
            progressBar.style.width = scrolled + "%";
        }});
    </script>
</body>
</html>
"""

def generate():
    years = ["year-1", "year-2"]
    for year in years:
        year_path = os.path.join(manga_dir, year)
        if not os.path.exists(year_path):
            continue
        
        chapters = [d for d in os.listdir(year_path) if os.path.isdir(os.path.join(year_path, d))]
        chapters.sort(key=natural_sort_key)
        
        # Generate common chapter options once per year
        options_html = ""
        for ch_opt in chapters:
            display_name = ch_opt.replace('-', ' ').upper()
            options_html += f'<option value="../{ch_opt}/">{display_name}</option>\n'
        
        for i, chapter in enumerate(chapters):
            chapter_path = os.path.join(year_path, chapter)
            images_list = [f for f in os.listdir(chapter_path) if f.lower().endswith(('.jpg', '.jpeg', '.png', '.webp'))]
            images_list.sort(key=natural_sort_key)
            
            img_tags = ""
            for img in images_list:
                img_tags += f'<img src="./{img}" class="manga-image" alt="{chapter} Page" loading="lazy">\n'
            
            prev_link = ""
            if i > 0:
                prev_link = f'<a href="../{chapters[i-1]}/" class="nav-btn">PREV</a>'
            
            next_link = ""
            if i < len(chapters) - 1:
                next_link = f'<a href="../{chapters[i+1]}/" class="nav-btn">NEXT</a>'
            
            display_title = f"{'1st Year' if year == 'year-1' else '2nd Year'} - {chapter.replace('-', ' ')}"
            
            primary_color = "#3b82f6" if year == "year-1" else "#8b0000"
            accent_color = "#60a5fa" if year == "year-1" else "#d4af37"

            html_content = template.format(
                title=display_title,
                tag_id=google_tag_id,
                prev_link=prev_link,
                next_link=next_link,
                images=img_tags,
                chapter_id=chapter,
                year_id=year,
                chapter_options=options_html,
                primary_color=primary_color,
                accent_color=accent_color
            )
            
            with open(os.path.join(chapter_path, "index.html"), "w", encoding="utf-8") as f:
                f.write(html_content)
            
            print(f"Generated {year}/{chapter}/index.html")

if __name__ == "__main__":
    generate()
