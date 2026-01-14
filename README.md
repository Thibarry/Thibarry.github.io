# Thibarry.github.io
# ⚡ Modern Portfolio | Industrial Edition

![Deployment Status](https://img.shields.io/github/deployments/votre-username/votre-repo/github-pages?label=Deployment&style=flat-square)
![Lighthouse Score](https://img.shields.io/badge/Lighthouse-100%2F100-success?style=flat-square&logo=lighthouse)
![Design System](https://img.shields.io/badge/Design-Dark%20%26%20Gold-orange?style=flat-square)

> A high-performance, responsive portfolio website reimagined with a 'Dark/Gold' industrial aesthetic. Built with semantic HTML5, modern CSS3 (Glassmorphism), and vanilla JavaScript for maximum speed and zero dependencies.

🔗 **[Live Demo](https://votre-username.github.io/votre-repo/)**

---

## 🎨 Design Philosophy: "Industrial Art"

This project moves away from generic templates to establish a strong personal brand. The UI focuses on hierarchy, contrast, and subtle motion.

* **Void Black & Industrial Gold:** A high-contrast palette optimized for readability and visual impact.
* **Glassmorphism:** Navigation and cards use backdrop-filters to create depth and hierarchy without clutter.
* **Responsive Grid:** A fluid layout that adapts seamlessly from 4K desktops to mobile devices.
* **Micro-Interactions:** Hover states, scroll-triggered fade-ins, and typewriter effects enhance user engagement.

## 🛠 Tech Stack

* **Core:** Semantic HTML5, CSS3 (Variables, Flexbox, Grid), ES6+ JavaScript.
* **Performance:** Zero external frameworks (No Bootstrap, No jQuery). Optimized critical rendering path.
* **Logic:** `IntersectionObserver` API for scroll animations, DOM manipulation for dynamic UI.
* **DevOps:** GitHub Actions for automated CI/CD deployment to GitHub Pages.

## 🚀 Key Features

### 1. Performance-First Architecture
Achieves near-perfect Lighthouse scores by eliminating render-blocking resources and using vanilla JavaScript.

### 2. Modern CSS Architecture
* **CSS Variables (`:root`)**: Centralized color and spacing management for easy theming.
* **Merged Media Queries**: Mobile-first approach integrated directly into the main stylesheet for maintainability.
* **Animations**: Hardware-accelerated CSS transitions for smooth 60fps performance.

### 3. Automated Deployment (CI/CD)
This repository includes a GitHub Actions workflow (`.github/workflows/deploy.yml`) that automatically builds and deploys changes to the live site upon pushing to the `main` branch.

## 📂 Project Structure

```bash
/
├── .github/
│   └── workflows/
│       └── deploy.yml   # CI/CD Pipeline configuration
├── assets/              # Optimized images and icons
├── index.html           # Semantic Markup
├── style.css            # Unified Design System & Responsive Rules
├── script.js            # UI Logic & Observer API
└── README.md            # Documentation
