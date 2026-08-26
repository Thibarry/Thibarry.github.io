import os
import re

POSTS_DIR = 'assets/_podcast'
OUTPUT_FILE = 'podcast.html'

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
        if category.lower() == 'interview':
            # Micro
            svg_content = '<path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M19 11a7 7 0 01-7 7m0 0a7 7 0 01-7-7m7 7v4m0 0H8m4 0h4m-4-8a3 3 0 01-3-3V5a3 3 0 116 0v6a3 3 0 01-3 3z"></path>'
        elif category.lower() == 'solo':
            # User/Solo
            svg_content = '<path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z"></path>'
        else: # Panel or default
            # Radio/Wave
            svg_content = '<path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M15.536 8.464a5 5 0 010 7.072m2.828-9.9a9 9 0 010 12.728M5.636 5.636a9 9 0 0112.728 0M12 14a2 2 0 100-4 2 2 0 000 4z"></path>'
            
        visual_html = f'<svg class="w-12 h-12 text-slate-300" fill="none" stroke="currentColor" viewBox="0 0 24 24">{svg_content}</svg>'

    delay_style = f' style="transition-delay: {delay_ms}ms;"' if delay_ms > 0 else ''

    html = f'''            <!-- Podcast Episode -->
            <a href="#" class="podcast-card group block reveal"{delay_style} data-title="{title.lower()}" data-theme="{category}" data-type="Episode" data-date="{date}">
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
    if not os.path.exists(POSTS_DIR):
        print(f"Directory {POSTS_DIR} not found.")
        return

    posts = []
    for filename in os.listdir(POSTS_DIR):
        if filename.endswith('.md'):
            filepath = os.path.join(POSTS_DIR, filename)
            post_data = parse_markdown_file(filepath)
            if post_data:
                posts.append(post_data)
                
    # Sort posts by date descending
    posts.sort(key=lambda x: str(x.get('date', '')), reverse=True)
    
    html_cards = []
    for idx, post in enumerate(posts):
        delay = (idx % 3) * 100 
        html_cards.append(generate_blog_card_html(post, delay))
        
    # Inject into HTML
    with open(OUTPUT_FILE, 'r', encoding='utf-8') as f:
        content = f.read()
        
    start_idx = content.find('<!-- PODCAST_START -->')
    end_idx = content.find('<!-- PODCAST_END -->')
    
    if start_idx != -1 and end_idx != -1:
        start_idx += len('<!-- PODCAST_START -->')
        
        new_content = content[:start_idx] + '\n' + '\n'.join(html_cards) + '\n' + '                            ' + content[end_idx:]
    
        with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        print(f"Successfully built {len(posts)} blog posts into {OUTPUT_FILE}!")

if __name__ == "__main__":
    main()
