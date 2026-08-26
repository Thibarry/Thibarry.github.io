# État des lieux du projet : AI Architect Portfolio

Ce document présente l'inventaire du projet, le rôle de chaque fichier ainsi que l'organisation des dépendances et de la chaîne de compilation.

## 📂 1. Inventaire des Répertoires et Fichiers

```text
ai-architect-portfolio/
│
├── index.html                  # Page d'accueil du portfolio
├── about.html                  # Page de présentation ("À propos")
├── projects.html               # Page listant les projets (générée ou modifiée par script)
├── blog.html                   # Page du blog (générée ou modifiée par script)
├── podcast.html                # Page du podcast (générée ou modifiée par script)
│
├── build_projects.py           # Script Python compilant les projets markdown en HTML
├── build_blog.py               # Script Python compilant les articles de blog markdown en HTML
├── build_podcast.py            # Script Python compilant les épisodes de podcast markdown en HTML
├── test_filters.py             # Script Python de tests unitaires sur les filtres
│
└── assets/
    ├── _projects/              # Sources Markdown des projets (avec métadonnées YAML)
    │   ├── agentic-data-pipeline.md
    │   ├── llm-routing-proxy.md
    │   ├── omniagent-framework.md
    │   └── semantic-rag-engine.md
    │
    ├── _blog/                  # Sources Markdown des articles de blog (avec métadonnées YAML)
    │   ├── agentic-ai-os.md
    │   ├── evolution-semantic-rag.md
    │   ├── scaling-multi-agent.md
    │   └── why-prompt-engineering.md
    │
    ├── _podcast/               # Sources Markdown des épisodes de podcast
    │   └── ep1-agentic-workflows.md
    │
    ├── css/                    # Styles CSS (styles globaux et configurations)
    ├── img/                    # Images et illustrations statiques
    └── js/
        ├── main.js             # Fichier JS principal (interactivité, scroll, filtres client)
        └── tailwind-config.js  # Configuration à la volée du framework Tailwind CSS
```

---

## ⚙️ 2. Rôle de chaque Fichier

### A. Pages HTML (Présentation)
Ces pages constituent l'interface utilisateur finale. Elles chargent Tailwind CSS dynamiquement et appliquent la configuration de thème locale.
*   [`index.html`](file:///c:/Users/thibarry/Documents/Personnel/Agentic/Antigravity/ai-architect-portfolio/index.html) : Hub principal présentant l'identité, les compétences phares et des extraits de projets/blog.
*   [`about.html`](file:///c:/Users/thibarry/Documents/Personnel/Agentic/Antigravity/ai-architect-portfolio/about.html) : Détail du parcours professionnel, des compétences techniques et méthodologiques.
*   [`projects.html`](file:///c:/Users/thibarry/Documents/Personnel/Agentic/Antigravity/ai-architect-portfolio/projects.html) : Galerie de réalisations avec système de filtrage interactif.
*   [`blog.html`](file:///c:/Users/thibarry/Documents/Personnel/Agentic/Antigravity/ai-architect-portfolio/blog.html) : Espace de partage d'articles techniques.
*   [`podcast.html`](file:///c:/Users/thibarry/Documents/Personnel/Agentic/Antigravity/ai-architect-portfolio/podcast.html) : Page dédiée aux publications audio/vidéo.

### B. Scripts de Build (Python)
Ces scripts automatisent l'insertion des contenus rédigés en Markdown directement au sein des pages HTML cibles, jouant le rôle de générateur de site statique simplifié.
*   [`build_projects.py`](file:///c:/Users/thibarry/Documents/Personnel/Agentic/Antigravity/ai-architect-portfolio/build_projects.py) : Analyse les fichiers de [`assets/_projects/`](file:///c:/Users/thibarry/Documents/Personnel/Agentic/Antigravity/ai-architect-portfolio/assets/_projects) et génère/injecte les cartes HTML associées dans [`projects.html`](file:///c:/Users/thibarry/Documents/Personnel/Agentic/Antigravity/ai-architect-portfolio/projects.html).
*   [`build_blog.py`](file:///c:/Users/thibarry/Documents/Personnel/Agentic/Antigravity/ai-architect-portfolio/build_blog.py) : Analyse les fichiers de [`assets/_blog/`](file:///c:/Users/thibarry/Documents/Personnel/Agentic/Antigravity/ai-architect-portfolio/assets/_blog) et injecte les cartes HTML associées dans [`blog.html`](file:///c:/Users/thibarry/Documents/Personnel/Agentic/Antigravity/ai-architect-portfolio/blog.html).
*   [`build_podcast.py`](file:///c:/Users/thibarry/Documents/Personnel/Agentic/Antigravity/ai-architect-portfolio/build_podcast.py) : Analyse les fichiers de [`assets/_podcast/`](file:///c:/Users/thibarry/Documents/Personnel/Agentic/Antigravity/ai-architect-portfolio/assets/_podcast) et injecte les cartes HTML dans [`podcast.html`](file:///c:/Users/thibarry/Documents/Personnel/Agentic/Antigravity/ai-architect-portfolio/podcast.html).
*   [`test_filters.py`](file:///c:/Users/thibarry/Documents/Personnel/Agentic/Antigravity/ai-architect-portfolio/test_filters.py) : Script utilitaire pour valider l'intégrité de la logique ou des filtres.

### C. Contenus Sources (Markdown)
Chaque fichier Markdown contient un bloc de métadonnées YAML (Frontmatter) décrivant l'élément (titre, sous-titre, tags, date, etc.) suivi d'une courte description.
*   **Projets** : Situés dans `assets/_projects/`.
*   **Blog** : Situés dans `assets/_blog/`.
*   **Podcast** : Situés dans `assets/_podcast/`.

### D. Ressources Statiques & Scripts Front-End
*   [`assets/js/main.js`](file:///c:/Users/thibarry/Documents/Personnel/Agentic/Antigravity/ai-architect-portfolio/assets/js/main.js) : Gère :
    1.  L'apparition fluide des éléments au défilement (classe `.reveal`).
    2.  L'adaptation visuelle de la barre de navigation au scroll.
    3.  Le filtrage et le tri côté client des projets, articles et podcasts en fonction des choix de l'utilisateur (inputs, sélecteurs, cases à cocher).
*   [`assets/js/tailwind-config.js`](file:///c:/Users/thibarry/Documents/Personnel/Agentic/Antigravity/ai-architect-portfolio/assets/js/tailwind-config.js) : Configure les jetons de design Tailwind à la volée (ex: polices personnalisées et couleurs de marque comme `brand-blue`).

---

## 🔗 3. Liens et Flux de Dépendances

### Flux de Compilation
```text
[Fichiers Markdown]  ──(Scripts Python de build)──>  [Pages HTML correspondantes]
 (Données YAML)                                         (Injection dans les grid)
```

### Fonctionnement Dynamique Front-End
1.  **Style** : Les pages HTML chargent Tailwind CSS qui interprète [`tailwind-config.js`](file:///c:/Users/thibarry/Documents/Personnel/Agentic/Antigravity/ai-architect-portfolio/assets/js/tailwind-config.js).
2.  **Interactivity** : [`main.js`](file:///c:/Users/thibarry/Documents/Personnel/Agentic/Antigravity/ai-architect-portfolio/assets/js/main.js) s'initialise à la fin du chargement du DOM, attache les écouteurs d'événements sur les contrôles de filtrage, et ajuste la visibilité des cartes générées par le build Python.
