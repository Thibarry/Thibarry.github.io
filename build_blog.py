import os
import re

BLOG_DIR = os.path.join('assets', '_blog')
HTML_FILE = 'blog.html'

def parse_markdown_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    frontmatter_match = re.match(r'^---\n(.*?)\n---', content, re.DOTALL)
    if not frontmatter_match:
        return None

    yaml_block = frontmatter_match.group(1)
    
    data = {}
    for line in yaml_block.split('\n'):
        if ':' in line:
            key, val = line.split(':', 1)
            key = key.strip()
            val = val.strip().strip('"').strip("'")
            data[key] = val
            
    return data

def generate_blog_card_html(post, delay_ms=0):
    title = post.get('title', 'Unknown Post')
    category = post.get('category', 'Uncategorized')
    date = post.get('date', '2026-01-01')
    excerpt = post.get('excerpt', '')
    image = post.get('image', '')
    
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    try:
        y, m, d = str(date).split('-')
        date_formatted = f"{months[int(m)-1]} {int(d)}, {y}"
    except:
        date_formatted = str(date)
        
    if image and image.strip() != "":
        visual_html = f'<img src="{image}" alt="{title}" class="w-full h-full object-cover">'
    else:
        # Fallback SVG based on category
        svg_content = ''
        if category.lower() == 'research':
            svg_content = '<path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M19 20H5a2 2 0 01-2-2V6a2 2 0 012-2h10a2 2 0 012 2v1m2 13a2 2 0 01-2-2V7m2 13a2 2 0 002-2V9.5a2.5 2.5 0 00-2.5-2.5H15"></path>'
        elif category.lower() == 'engineering':
            svg_content = '<path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M9.75 17L9 20l-1 1h8l-1-1-.75-3M3 13h18M5 17h14a2 2 0 002-2V5a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z"></path>'
        else: # Opinion or default
            svg_content = '<path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M13 10V3L4 14h7v7l9-11h-7z"></path>'
            
        visual_html = f'<svg class="w-12 h-12 text-slate-300" fill="none" stroke="currentColor" viewBox="0 0 24 24">{svg_content}</svg>'

    delay_style = f' style="transition-delay: {delay_ms}ms;"' if delay_ms > 0 else ''

    html = f'''                    <!-- Blog Post -->
                    <a href="#" class="blog-card group block reveal"{delay_style} data-title="{title.lower()}" data-theme="{category}" data-type="Article" data-date="{date}">
                        <div class="rounded-2xl overflow-hidden mb-6 card-panel aspect-video flex items-center justify-center bg-slate-50 group-hover:border-blue-300 transition-colors">
                            {visual_html}
                        </div>
                        <div class="flex items-center gap-3 text-sm text-slate-500 mb-3">
                            <span class="text-brand-blue font-medium">{category}</span>
                            <span>&bull;</span>
                            <span>{date_formatted}</span>
                        </div>
                        <h3 class="text-xl font-bold text-slate-900 mb-3 group-hover:text-brand-blue transition-colors">
                            {title}</h3>
                        <p class="text-slate-600 text-sm line-clamp-3">{excerpt}</p>
                    </a>
'''
    return html

def main():
    if not os.path.exists(BLOG_DIR):
        print(f"Directory {BLOG_DIR} not found.")
        return

    posts = []
    for filename in os.listdir(BLOG_DIR):
        if filename.endswith('.md'):
            filepath = os.path.join(BLOG_DIR, filename)
            post_data = parse_markdown_file(filepath)
            if post_data:
                posts.append(post_data)
                
    # Sort posts by date descending
    posts.sort(key=lambda x: str(x.get('date', '')), reverse=True)
    
    html_cards = []
    for idx, post in enumerate(posts):
        delay = (idx % 3) * 100 
        html_cards.append(generate_blog_card_html(post, delay))
        
    all_cards_html = "".join(html_cards)
    
    # Inject into HTML
    with open(HTML_FILE, 'r', encoding='utf-8') as f:
        html_content = f.read()
        
    start_marker = "<!-- BLOG_START -->"
    end_marker = "<!-- BLOG_END -->"
    
    start_idx = html_content.find(start_marker)
    end_idx = html_content.find(end_marker)
    
    if start_idx == -1 or end_idx == -1:
        print("Markers not found in HTML file!")
        return
        
    new_html = html_content[:start_idx + len(start_marker)] + "\n" + all_cards_html + "                    " + html_content[end_idx:]
    
    with open(HTML_FILE, 'w', encoding='utf-8') as f:
        f.write(new_html)
        
    print(f"Successfully built {len(posts)} blog posts into {HTML_FILE}!")

if __name__ == "__main__":
    main()
