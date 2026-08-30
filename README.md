# 🏛️ Architect.ai - Lead AI R&D Architect Portfolio

![Build Status](https://img.shields.io/badge/build-passing-brightgreen)
![Python Version](https://img.shields.io/badge/python-3.10%2B-blue)
![Tailwind CSS](https://img.shields.io/badge/Tailwind_CSS-3.4-38B2AC?logo=tailwind-css)
![Vanilla JS](https://img.shields.io/badge/Vanilla_JS-ES6-F7DF1E?logo=javascript)

Dépôt officiel du portfolio web de **Thierno Barry**, Lead AI R&D Architect & GenAIOps. 

Ce projet n'utilise pas de frameworks front-end lourds (comme React ou Next.js). Il s'agit d'une architecture **Static Site Generator (SSG) "Home-made"** conçue pour la performance brute : les contenus (Projets, Blog, Podcast) sont rédigés en `Markdown / YAML` et compilés en HTML statique via des scripts Python natifs, le tout stylisé dynamiquement avec Tailwind CSS via CDN.

🔗 **[Visiter le site en production](https://thierno-ai.com)** *(Lien à mettre à jour)*

---

## 🧠 Architecture du Projet

L'écosystème est divisé en deux couches :
1. **La couche UI (Front-End) :** Fichiers HTML statiques, injectés avec Tailwind CSS via le script `tailwind-config.js` et animés par `main.js` (DOM manipulations, filtres clients, scroll reveal).
2. **La couche Data (SSG Python) :** Fichiers sources Markdown situés dans le dossier `assets/` et compilés par les scripts `build_*.py`.

```text
ai-architect-portfolio/
├── *.html                  # Pages statiques finales (index, about, projects, blog...)
├── build_*.py              # Scripts de compilation Python (Générateurs HTML)
├── test_filters.py         # Tests E2E Playwright pour la logique de filtrage
└── assets/
    ├── _projects/          # Fichiers sources Markdown des projets R&D
    ├── _blog/              # Fichiers sources Markdown des articles
    ├── _podcast/           # Fichiers sources Markdown des épisodes
    ├── css/                # Styles globaux
    ├── img/                # Médias et logos
    └── js/                 # Logique client (main.js) et config Tailwind
```

## ⚙️ Stack Technologique

- **Data Injection & SSG** : Python 3 (Regex, OS, IO)
- **Tests E2E** : Playwright (Async Python)
- **Front-End** : HTML5, Vanilla JavaScript (ES6)
- **Design System** : Tailwind CSS (via script CDN en développement/production)
- **Hébergement cible** : Vercel / GitHub Pages / Netlify

---

## 🚀 Installation & Build Local

Pour cloner le projet, recompiler le HTML à partir des fichiers Markdown et tester localement, suivez ces étapes :

### 1. Cloner le dépôt
```bash
git clone https://github.com/votre-nom/ai-architect-portfolio.git
cd ai-architect-portfolio
```

### 2. (Optionnel) Environnement Python pour les tests
Si vous souhaitez exécuter les tests Playwright (`test_filters.py`), créez un environnement virtuel :

```bash
python -m venv .venv
source .venv/bin/activate  # Sur Windows: .venv\Scripts\activate
pip install playwright
playwright install chromium
```

### 3. Compilation des contenus (SSG Python)
Les contenus dynamiques (Blog, Projets, Podcasts) sont générés à partir des fichiers Markdown. Exécutez les scripts de build pour injecter le HTML :

```bash
# Générer les articles de blog
python build_blog.py

# Générer les cartes projets
python build_projects.py

# Générer les épisodes de podcast
python build_podcast.py
```
*(Le terminal vous confirmera le nombre de fichiers injectés avec succès).*

### 4. Lancer le serveur de développement local
Comme il s'agit de HTML statique pur, n'importe quel serveur HTTP suffit.

```bash
python -m http.server 8000
```
Ouvrez votre navigateur sur `http://localhost:8000`.

---

## 🧪 Tests
Le projet inclut une vérification des filtres de la page Projets basée sur Playwright.

```bash
python test_filters.py
```

---

## 🖋️ Ajouter du contenu (Workflow Markdown)
Pour ajouter un nouveau projet, créez simplement un fichier `.md` dans `assets/_projects/` en respectant ce format YAML (Frontmatter) :

```yaml
---
title: "Nom de la nouvelle architecture"
date: 2026-10-01
theme: "AgentOps"
type: "Production"
tech_stack: ["Python", "LangGraph", "vLLM"]
image: ""
excerpt: "Description ultra-concise et orientée impact/FinOps."
---
# Description approfondie (Markdown)
...
```

Puis, exécutez `python build_projects.py` pour mettre à jour `projects.html`.

---

## ⚖️ Licence
Créé par Thierno Barry.  
L'utilisation de ce code source est autorisée pour des besoins personnels, sous réserve de modification des données, de l'identité et du design system.

---

> *Architecting deterministic systems. Securing the future.*
