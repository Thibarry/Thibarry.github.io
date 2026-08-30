import os
import re

blogDirectory = os.path.join('assets', '_blog')
htmlFile = 'blog.html'

def parseMarkdownFile(filePath):
    with open(filePath, 'r', encoding='utf-8') as f:
        content = f.read()

    frontmatterMatch = re.match(r'^---\n(.*?)\n---', content, re.DOTALL)
    if not frontmatterMatch:
        return None

    yamlBlock = frontmatterMatch.group(1)
    
    data = {}
    for line in yamlBlock.split('\n'):
        if ':' in line:
            key, val = line.split(':', 1)
            key = key.strip()
            val = val.strip().strip('"').strip("'")
            data[key] = val
            
    return data

def formatFrenchDate(dateStr):
    months = [
        "janvier", "février", "mars", "avril", "mai", "juin",
        "juillet", "août", "septembre", "octobre", "novembre", "décembre"
    ]
    try:
        y, m, d = str(dateStr).split('-')
        dayNum = int(d)
        dayFormatted = "1er" if dayNum == 1 else str(dayNum)
        return f"{dayFormatted} {months[int(m)-1]} {y}"
    except Exception:
        return str(dateStr)

def generateBlogRowHtml(post):
    title = post.get('title', 'Publication IA')
    category = post.get('category', 'Architecture IA')
    date = post.get('date', '2026-01-01')
    excerpt = post.get('excerpt', '')
    dateFormatted = formatFrenchDate(date)

    readTimes = {
        "L'IA Agentique comme Nouveau Système d'Exploitation d'Entreprise": "7 min de lecture",
        "Orchestration Multi-Agents à l'Échelle des Workflows Industriels": "9 min de lecture",
        "L'Évolution des Moteurs RAG : Du Vector Search au GraphRAG Hybride": "8 min de lecture",
        "Pourquoi le Prompt Engineering Cède la Place à l'Ingénierie Déterministe": "6 min de lecture"
    }
    readTime = readTimes.get(title, "7 min de lecture")

    html = f'''                    <!-- Publication -->
                    <article class="py-6 group transition-all duration-300">
                        <div class="flex flex-wrap items-center gap-3 text-xs text-slate-500 mb-2">
                            <span class="font-semibold text-[#4376E6] bg-blue-50 px-2.5 py-0.5 rounded-md border border-blue-100/80">{category}</span>
                            <span class="text-slate-300">&bull;</span>
                            <span class="font-medium text-slate-500">{dateFormatted}</span>
                            <span class="text-slate-300">&bull;</span>
                            <span class="text-slate-400">{readTime}</span>
                        </div>
                        <h2 class="text-xl md:text-2xl font-bold font-serif text-slate-900 mb-2 group-hover:text-[#4376E6] transition-colors leading-snug">
                            <a href="#" class="inline-block">{title}</a>
                        </h2>
                        <p class="text-slate-600 text-sm md:text-base leading-relaxed mb-3">
                            {excerpt}
                        </p>
                        <div class="flex items-center gap-2 text-xs md:text-sm font-bold text-[#4376E6] group-hover:translate-x-1.5 transition-transform duration-200 inline-flex">
                            <span>Lire la publication</span>
                            <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14 5l7 7m0 0l-7 7m7-7H3" />
                            </svg>
                        </div>
                    </article>
'''
    return html

def buildBlog():
    if not os.path.exists(blogDirectory):
        print(f"Directory {blogDirectory} not found.")
        return

    posts = []
    for filename in os.listdir(blogDirectory):
        if filename.endswith('.md'):
            filePath = os.path.join(blogDirectory, filename)
            postData = parseMarkdownFile(filePath)
            if postData:
                posts.append(postData)
                
    # Sort posts by date descending
    posts.sort(key=lambda x: str(x.get('date', '')), reverse=True)
    
    htmlRows = []
    for post in posts:
        htmlRows.append(generateBlogRowHtml(post))
        
    allRowsHtml = "".join(htmlRows)
    
    # Inject into HTML
    with open(htmlFile, 'r', encoding='utf-8') as f:
        htmlContent = f.read()
        
    startMarker = "<!-- BLOG_START -->"
    endMarker = "<!-- BLOG_END -->"
    
    startIdx = htmlContent.find(startMarker)
    endIdx = htmlContent.find(endMarker)
    
    if startIdx == -1 or endIdx == -1:
        print("Markers not found in HTML file!")
        return
        
    newHtml = htmlContent[:startIdx + len(startMarker)] + "\n" + allRowsHtml + "                    " + htmlContent[endIdx:]
    
    with open(htmlFile, 'w', encoding='utf-8') as f:
        f.write(newHtml)
        
    print(f"Successfully built {len(posts)} blog posts into {htmlFile}!")

if __name__ == "__main__":
    buildBlog()
