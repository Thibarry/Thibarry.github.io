import os
import re

projectsDir = os.path.join('assets', '_projects')
htmlFile = 'projects.html'

def parseMarkdownFile(filePath):
    with open(filePath, 'r', encoding='utf-8') as fileObj:
        fileContent = fileObj.read()

    frontmatterMatch = re.match(r'^---\n(.*?)\n---', fileContent, re.DOTALL)
    if not frontmatterMatch:
        return None

    yamlBlock = frontmatterMatch.group(1)
    
    parsedData = {}
    for rawLine in yamlBlock.split('\n'):
        if ':' in rawLine:
            rawKey, rawVal = rawLine.split(':', 1)
            cleanKey = rawKey.strip()
            cleanVal = rawVal.strip().strip('"').strip("'")
            
            if cleanKey == 'tech_stack':
                techItems = re.findall(r'"([^"]*)"|\'([^\']*)\'', cleanVal)
                cleanVal = [item for sublist in techItems for item in sublist if item]
            
            parsedData[cleanKey] = cleanVal
            
    return parsedData

def generateVisualDiagram(projectTitle):
    titleLower = projectTitle.lower()
    
    if "pipeline" in titleLower or "données" in titleLower:
        return '''
            <div class="w-full h-full bg-[#0a1128] relative overflow-hidden flex items-center justify-center p-4">
                <div class="absolute inset-0 bg-[radial-gradient(#a855f7_1px,transparent_1px)] [background-size:16px_16px] opacity-20"></div>
                <svg class="w-full h-full max-h-36" viewBox="0 0 320 120" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <path d="M 30 60 L 100 60 L 160 30 L 220 30 L 290 60" stroke="#c084fc" stroke-width="2" stroke-dasharray="4 4" class="animate-pulse" />
                    <path d="M 100 60 L 160 90 L 220 90 L 250 60" stroke="#f43f5e" stroke-width="1.5" stroke-dasharray="3 3" />
                    <path d="M 220 90 C 180 115, 120 115, 100 65" stroke="#10b981" stroke-width="2" stroke-linecap="round" />
                    
                    <circle cx="30" cy="60" r="14" fill="#1e293b" stroke="#c084fc" stroke-width="2" />
                    <text x="30" y="63" font-size="8" fill="#e9d5ff" font-family="monospace" text-anchor="middle">INGEST</text>
                    
                    <rect x="80" y="42" width="40" height="36" rx="8" fill="#1e1b4b" stroke="#a855f7" stroke-width="2" />
                    <circle cx="100" cy="55" r="4" fill="#d8b4fe" />
                    <text x="100" y="71" font-size="7" fill="#f3e8ff" font-family="monospace" text-anchor="middle">DÉTECTEUR</text>
                    
                    <rect x="175" y="16" width="46" height="28" rx="6" fill="#064e3b" stroke="#10b981" stroke-width="1.5" />
                    <text x="198" y="33" font-size="7" fill="#6ee7b7" font-family="monospace" text-anchor="middle">ETL SAIN</text>
                    
                    <rect x="175" y="76" width="46" height="28" rx="6" fill="#881337" stroke="#f43f5e" stroke-width="1.5" />
                    <text x="198" y="93" font-size="7" fill="#fda4af" font-family="monospace" text-anchor="middle">AUTO-HEAL</text>
                    
                    <circle cx="290" cy="60" r="15" fill="#0f172a" stroke="#10b981" stroke-width="2" />
                    <text x="290" y="63" font-size="8" fill="#34d399" font-family="monospace" text-anchor="middle">DATALAKE</text>
                    
                    <rect x="130" y="5" width="60" height="14" rx="4" fill="#1e293b" stroke="#475569" stroke-width="1" />
                    <text x="160" y="14" font-size="7" fill="#c084fc" font-family="monospace" text-anchor="middle">ÉTAT: ACTIF</text>
                </svg>
            </div>
        '''
    elif "omniagent" in titleLower:
        return '''
            <div class="w-full h-full bg-[#030712] relative overflow-hidden flex items-center justify-center p-4">
                <div class="absolute inset-0 bg-[radial-gradient(#6366f1_1px,transparent_1px)] [background-size:16px_16px] opacity-20"></div>
                <svg class="w-full h-full max-h-36" viewBox="0 0 320 120" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <line x1="160" y1="35" x2="60" y2="90" stroke="#6366f1" stroke-width="1.5" stroke-dasharray="4 2" />
                    <line x1="160" y1="35" x2="125" y2="90" stroke="#6366f1" stroke-width="1.5" stroke-dasharray="4 2" />
                    <line x1="160" y1="35" x2="195" y2="90" stroke="#6366f1" stroke-width="1.5" stroke-dasharray="4 2" />
                    <line x1="160" y1="35" x2="260" y2="90" stroke="#6366f1" stroke-width="1.5" stroke-dasharray="4 2" />
                    <path d="M 60 90 Q 160 115 260 90" stroke="#a855f7" stroke-width="1" stroke-dasharray="2 2" />
                    
                    <circle cx="160" cy="32" r="18" fill="#1e1b4b" stroke="#818cf8" stroke-width="2" />
                    <circle cx="160" cy="32" r="6" fill="#6366f1" class="animate-ping" opacity="0.7" />
                    <text x="160" y="35" font-size="7" fill="#e0e7ff" font-family="monospace" text-anchor="middle" font-weight="bold">SUPERVISEUR</text>
                    
                    <circle cx="60" cy="90" r="13" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5" />
                    <text x="60" y="93" font-size="7" fill="#7dd3fc" font-family="monospace" text-anchor="middle">ROUTER</text>
                    
                    <circle cx="125" cy="90" r="13" fill="#0f172a" stroke="#a855f7" stroke-width="1.5" />
                    <text x="125" y="93" font-size="7" fill="#d8b4fe" font-family="monospace" text-anchor="middle">RAG</text>
                    
                    <circle cx="195" cy="90" r="13" fill="#0f172a" stroke="#ec4899" stroke-width="1.5" />
                    <text x="195" y="93" font-size="7" fill="#f472b6" font-family="monospace" text-anchor="middle">CRITIC</text>
                    
                    <circle cx="260" cy="90" r="13" fill="#0f172a" stroke="#10b981" stroke-width="1.5" />
                    <text x="260" y="93" font-size="7" fill="#6ee7b7" font-family="monospace" text-anchor="middle">FINOPS</text>
                    
                    <rect x="15" y="10" width="85" height="14" rx="4" fill="#111827" stroke="#374151" stroke-width="1" />
                    <text x="57" y="19" font-size="7" fill="#818cf8" font-family="monospace" text-anchor="middle">SWARM: 4 AGENTS</text>
                </svg>
            </div>
        '''
    elif "rag" in titleLower:
        return '''
            <div class="w-full h-full bg-[#051329] relative overflow-hidden flex items-center justify-center p-4">
                <div class="absolute inset-0 bg-[radial-gradient(#0284c7_1px,transparent_1px)] [background-size:16px_16px] opacity-20"></div>
                <svg class="w-full h-full max-h-36" viewBox="0 0 320 120" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <line x1="45" y1="60" x2="110" y2="60" stroke="#0ea5e9" stroke-width="2" />
                    <line x1="110" y1="60" x2="180" y2="35" stroke="#38bdf8" stroke-width="1.5" stroke-dasharray="3 3" />
                    <line x1="110" y1="60" x2="180" y2="85" stroke="#38bdf8" stroke-width="1.5" stroke-dasharray="3 3" />
                    <line x1="180" y1="35" x2="250" y2="60" stroke="#10b981" stroke-width="2" />
                    <line x1="180" y1="85" x2="250" y2="60" stroke="#10b981" stroke-width="2" />
                    
                    <rect x="20" y="46" width="50" height="28" rx="6" fill="#0f294a" stroke="#38bdf8" stroke-width="1.5" />
                    <text x="45" y="63" font-size="7" fill="#e0f2fe" font-family="monospace" text-anchor="middle">REQUÊTE</text>
                    
                    <circle cx="110" cy="60" r="16" fill="#0c4a6e" stroke="#0284c7" stroke-width="2" />
                    <text x="110" y="63" font-size="7" fill="#7dd3fc" font-family="monospace" text-anchor="middle">HYBRIDE</text>
                    
                    <rect x="155" y="20" width="55" height="28" rx="6" fill="#1e293b" stroke="#818cf8" stroke-width="1.5" />
                    <text x="182" y="37" font-size="7" fill="#c7d2fe" font-family="monospace" text-anchor="middle">PGVECTOR</text>
                    
                    <rect x="155" y="72" width="55" height="28" rx="6" fill="#1e293b" stroke="#f59e0b" stroke-width="1.5" />
                    <text x="182" y="89" font-size="7" fill="#fde68a" font-family="monospace" text-anchor="middle">GRAPH DB</text>
                    
                    <rect x="240" y="44" width="60" height="32" rx="8" fill="#064e3b" stroke="#34d399" stroke-width="2" />
                    <text x="270" y="58" font-size="7" fill="#a7f3d0" font-family="monospace" text-anchor="middle">RE-RANKER</text>
                    <text x="270" y="68" font-size="6" fill="#6ee7b7" font-family="monospace" text-anchor="middle">TOP-K CONTEXTE</text>
                </svg>
            </div>
        '''
    elif "quality" in titleLower or "observabilité" in titleLower or "gates" in titleLower:
        return '''
            <div class="w-full h-full bg-[#0b132b] relative overflow-hidden flex items-center justify-center p-4">
                <div class="absolute inset-0 bg-[radial-gradient(#10b981_1px,transparent_1px)] [background-size:16px_16px] opacity-20"></div>
                <svg class="w-full h-full max-h-36" viewBox="0 0 320 120" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <line x1="40" y1="60" x2="95" y2="60" stroke="#34d399" stroke-width="2" />
                    <line x1="95" y1="60" x2="160" y2="60" stroke="#38bdf8" stroke-width="2" />
                    <line x1="160" y1="60" x2="225" y2="60" stroke="#818cf8" stroke-width="2" />
                    <line x1="225" y1="60" x2="280" y2="60" stroke="#10b981" stroke-width="2" />
                    
                    <circle cx="40" cy="60" r="14" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5" />
                    <text x="40" y="63" font-size="7" fill="#7dd3fc" font-family="monospace" text-anchor="middle">PROMPT</text>
                    
                    <rect x="80" y="44" width="48" height="32" rx="6" fill="#132e35" stroke="#2dd4bf" stroke-width="1.5" />
                    <text x="104" y="57" font-size="6" fill="#5eead4" font-family="monospace" text-anchor="middle">GUARDRAIL</text>
                    <text x="104" y="67" font-size="6" fill="#99f6e4" font-family="monospace" text-anchor="middle">SCHEMA OK</text>
                    
                    <rect x="145" y="42" width="55" height="36" rx="8" fill="#1e1b4b" stroke="#818cf8" stroke-width="2" />
                    <text x="172" y="55" font-size="6" fill="#c7d2fe" font-family="monospace" text-anchor="middle">EVAL MATRIX</text>
                    <text x="172" y="66" font-size="6" fill="#a5b4fc" font-family="monospace" text-anchor="middle">SCORE: 99.4%</text>
                    
                    <circle cx="230" cy="60" r="14" fill="#064e3b" stroke="#10b981" stroke-width="2" />
                    <path d="M 224 60 L 228 64 L 236 56" stroke="#34d399" stroke-width="2" stroke-linecap="round" />
                    
                    <rect x="265" y="46" width="45" height="28" rx="6" fill="#0f172a" stroke="#10b981" stroke-width="1.5" />
                    <text x="287" y="63" font-size="7" fill="#6ee7b7" font-family="monospace" text-anchor="middle">PROD DEPLOY</text>
                    
                    <rect x="15" y="10" width="95" height="14" rx="4" fill="#111827" stroke="#374151" stroke-width="1" />
                    <text x="62" y="19" font-size="7" fill="#34d399" font-family="monospace" text-anchor="middle">CI/CD: QUALITY GATE</text>
                </svg>
            </div>
        '''
    elif "lakehouse" in titleLower or "feature" in titleLower:
        return '''
            <div class="w-full h-full bg-[#110e20] relative overflow-hidden flex items-center justify-center p-4">
                <div class="absolute inset-0 bg-[radial-gradient(#a855f7_1px,transparent_1px)] [background-size:16px_16px] opacity-20"></div>
                <svg class="w-full h-full max-h-36" viewBox="0 0 320 120" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <path d="M 40 60 L 100 60" stroke="#a855f7" stroke-width="2" />
                    <path d="M 140 45 L 200 30" stroke="#c084fc" stroke-width="1.5" />
                    <path d="M 140 75 L 200 90" stroke="#38bdf8" stroke-width="1.5" />
                    <path d="M 255 30 L 290 50" stroke="#34d399" stroke-width="2" />
                    <path d="M 255 90 L 290 70" stroke="#34d399" stroke-width="2" />
                    
                    <circle cx="40" cy="60" r="14" fill="#1e1b4b" stroke="#a855f7" stroke-width="1.5" />
                    <text x="40" y="63" font-size="7" fill="#e9d5ff" font-family="monospace" text-anchor="middle">STREAM</text>
                    
                    <rect x="95" y="44" width="50" height="32" rx="6" fill="#2e1065" stroke="#c084fc" stroke-width="1.5" />
                    <text x="120" y="57" font-size="6" fill="#f3e8ff" font-family="monospace" text-anchor="middle">VECTORIZED</text>
                    <text x="120" y="67" font-size="6" fill="#e9d5ff" font-family="monospace" text-anchor="middle">DUCKDB</text>
                    
                    <rect x="200" y="16" width="55" height="28" rx="6" fill="#0f172a" stroke="#818cf8" stroke-width="1.5" />
                    <text x="227" y="33" font-size="6" fill="#c7d2fe" font-family="monospace" text-anchor="middle">PARQUET LAKE</text>
                    
                    <rect x="200" y="76" width="55" height="28" rx="6" fill="#0c4a6e" stroke="#38bdf8" stroke-width="1.5" />
                    <text x="227" y="93" font-size="6" fill="#7dd3fc" font-family="monospace" text-anchor="middle">FEATURE STORE</text>
                    
                    <circle cx="295" cy="60" r="15" fill="#064e3b" stroke="#10b981" stroke-width="2" />
                    <text x="295" y="63" font-size="7" fill="#6ee7b7" font-family="monospace" text-anchor="middle">&lt;1ms</text>
                    
                    <rect x="15" y="10" width="85" height="14" rx="4" fill="#1e1b4b" stroke="#4c1d95" stroke-width="1" />
                    <text x="57" y="19" font-size="7" fill="#d8b4fe" font-family="monospace" text-anchor="middle">LAKEHOUSE ML</text>
                </svg>
            </div>
        '''
    else:
        return '''
            <div class="w-full h-full bg-[#0d1117] relative overflow-hidden flex items-center justify-center p-4">
                <div class="absolute inset-0 bg-[radial-gradient(#10b981_1px,transparent_1px)] [background-size:16px_16px] opacity-20"></div>
                <svg class="w-full h-full max-h-36" viewBox="0 0 320 120" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <path d="M 90 60 L 150 25 L 230 25" stroke="#10b981" stroke-width="2" />
                    <path d="M 90 60 L 150 60 L 230 60" stroke="#38bdf8" stroke-width="1.5" stroke-dasharray="3 3" />
                    <path d="M 90 60 L 150 95 L 230 95" stroke="#f59e0b" stroke-width="1.5" stroke-dasharray="3 3" />
                    
                    <rect x="15" y="46" width="50" height="28" rx="6" fill="#161b22" stroke="#484f58" stroke-width="1.5" />
                    <text x="40" y="63" font-size="7" fill="#c9d1d9" font-family="monospace" text-anchor="middle">API REQ</text>
                    
                    <circle cx="90" cy="60" r="16" fill="#064e3b" stroke="#10b981" stroke-width="2" />
                    <text x="90" y="63" font-size="7" fill="#6ee7b7" font-family="monospace" text-anchor="middle">ROUTER</text>
                    
                    <rect x="230" y="12" width="75" height="24" rx="5" fill="#042f2e" stroke="#14b8a6" stroke-width="1.5" />
                    <text x="267" y="27" font-size="7" fill="#5eead4" font-family="monospace" text-anchor="middle">EDGE (8B) · $0.00</text>
                    
                    <rect x="230" y="48" width="75" height="24" rx="5" fill="#0c2d48" stroke="#0284c7" stroke-width="1.5" />
                    <text x="267" y="63" font-size="7" fill="#7dd3fc" font-family="monospace" text-anchor="middle">SONNET / GPT · $</text>
                    
                    <rect x="230" y="84" width="75" height="24" rx="5" fill="#422006" stroke="#d97706" stroke-width="1.5" />
                    <text x="267" y="99" font-size="7" fill="#fcd34d" font-family="monospace" text-anchor="middle">OPUS / O1 · $$$</text>
                    
                    <rect x="135" y="103" width="75" height="12" rx="3" fill="#111827" stroke="#374151" stroke-width="1" />
                    <text x="172" y="111" font-size="6" fill="#10b981" font-family="monospace" text-anchor="middle">RÉDUCTION COÛT: -72%</text>
                </svg>
            </div>
        '''

def buildProjects():
    print("Project architecture is managed declaratively in projects.html.")

if __name__ == "__main__":
    buildProjects()
