import os
import re

PROJECTS_DIR = os.path.join('assets', '_projects')
HTML_FILE = 'projects.html'

def parse_markdown_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Simple YAML frontmatter parser
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
            
            # Handle tech_stack array
            if key == 'tech_stack':
                # Parse ["Python", "FastAPI"] to list
                items = re.findall(r'"([^"]*)"|\'([^\']*)\'', val)
                # flatten list of tuples and remove empty strings
                val = [item for sublist in items for item in sublist if item]
            
            data[key] = val
            
    return data

def generate_card_html(project, delay_ms=0):
    title = project.get('title', 'Unknown Project')
    title_lower = title.lower()
    theme = project.get('theme', 'Autre')
    type_ = project.get('type', 'Autre')
    date = project.get('date', '2026-01-01')
    excerpt = project.get('excerpt', '')
    tech_stack = project.get('tech_stack', [])
    image = project.get('image', '')
    
    # Format date to Month YYYY (simple mapping for French)
    months = ["Janvier", "Février", "Mars", "Avril", "Mai", "Juin", "Juillet", "Août", "Septembre", "Octobre", "Novembre", "Décembre"]
    try:
        y, m, d = date.split('-')
        date_formatted = f"{months[int(m)-1]} {y}"
    except:
        date_formatted = date
    
    tech_stack_html = '\n'.join([
        f'<span class="text-[10px] font-medium text-slate-500 bg-slate-100 px-2 py-1 rounded">{tech}</span>'
        for tech in tech_stack
    ])
    
    # Visual area: Use image if exists, else fallback code block
    if image and image.strip() != "":
        visual_html = f'<img src="{image}" alt="{title}" class="w-full h-full object-cover opacity-80 group-hover:opacity-100 transition-opacity">'
    else:
        visual_html = f'''
                                <div class="font-mono text-slate-300 text-xs p-6 w-full h-full text-left scale-90 origin-left">
                                    <span class="text-purple-400">async def</span> <span class="text-blue-400">run</span>():<br />
                                    &nbsp;&nbsp;<span class="text-slate-500"># {title}</span><br />
                                    &nbsp;&nbsp;<span class="text-purple-400">await</span> system.init()<br />
                                    &nbsp;&nbsp;<span class="text-purple-400">return</span> system.execute()
                                </div>
        '''

    html = f'''
                        <!-- Project Card -->
                        <a href="#"
                            class="project-card group flex flex-col bg-white border border-slate-200 rounded-2xl overflow-hidden hover:border-blue-400 hover:shadow-xl hover:shadow-brand-blue/5 transition-all card-panel reveal"
                            data-title="{title_lower}" data-theme="{theme}" data-type="{type_}"
                            data-date="{date}" style="transition-delay: {delay_ms}ms;">
                            <!-- Image/Visual Area -->
                            <div class="h-48 bg-slate-900 relative overflow-hidden flex flex-col items-center justify-center border-b border-slate-200 w-full">
                                {visual_html.strip()}
                            </div>
                            <!-- Content Area -->
                            <div class="p-8 flex-1 flex flex-col">
                                <div class="mb-4">
                                    <span class="inline-block px-3 py-1 bg-blue-50 text-brand-blue text-xs font-semibold rounded-full border border-blue-100 group-hover:bg-brand-blue group-hover:text-white transition-colors">{theme}</span>
                                </div>
                                <h3 class="text-xl font-bold text-slate-900 mb-3 group-hover:text-brand-blue transition-colors font-serif">
                                    {title}
                                </h3>
                                <p class="text-slate-600 text-sm mb-6 flex-1 leading-relaxed">
                                    {excerpt}
                                </p>
                                <div class="flex flex-wrap gap-2 mb-4">
                                    {tech_stack_html}
                                </div>
                                <div class="flex items-center justify-between mt-auto pt-4 border-t border-slate-100">
                                    <span class="text-xs font-medium text-slate-400 uppercase tracking-widest">{date_formatted}</span>
                                    <svg class="w-5 h-5 text-brand-blue transform group-hover:translate-x-1 transition-transform" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14 5l7 7m0 0l-7 7m7-7H3"></path></svg>
                                </div>
                            </div>
                        </a>
'''
    return html

def main():
    if not os.path.exists(PROJECTS_DIR):
        print(f"Directory {PROJECTS_DIR} not found.")
        return

    projects = []
    for filename in os.listdir(PROJECTS_DIR):
        if filename.endswith('.md'):
            filepath = os.path.join(PROJECTS_DIR, filename)
            project_data = parse_markdown_file(filepath)
            if project_data:
                projects.append(project_data)
                
    # Sort projects by date descending
    projects.sort(key=lambda x: x.get('date', ''), reverse=True)
    
    html_cards = []
    for idx, project in enumerate(projects):
        delay = (idx % 3) * 100 # Add a small cascade animation delay for the first cards
        html_cards.append(generate_card_html(project, delay))
        
    all_cards_html = "".join(html_cards)
    
    # Inject into HTML
    with open(HTML_FILE, 'r', encoding='utf-8') as f:
        html_content = f.read()
        
    start_marker = "<!-- PROJECTS_START -->"
    end_marker = "<!-- PROJECTS_END -->"
    
    start_idx = html_content.find(start_marker)
    end_idx = html_content.find(end_marker)
    
    if start_idx == -1 or end_idx == -1:
        print("Markers not found in HTML file!")
        return
        
    new_html = html_content[:start_idx + len(start_marker)] + "\n" + all_cards_html + "                        " + html_content[end_idx:]
    
    with open(HTML_FILE, 'w', encoding='utf-8') as f:
        f.write(new_html)
        
    print(f"Successfully built {len(projects)} projects into {HTML_FILE}!")

if __name__ == "__main__":
    main()
