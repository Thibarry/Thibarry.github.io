document.addEventListener('DOMContentLoaded', () => {
    // Reveal elements on scroll
    const revealElements = document.querySelectorAll('.reveal');

    const revealOnScroll = () => {
        const windowHeight = window.innerHeight;
        const revealPoint = 100;

        revealElements.forEach((el) => {
            const revealTop = el.getBoundingClientRect().top;
            if (revealTop < windowHeight - revealPoint) {
                el.classList.add('active');
            }
        });
    };

    // Initial check
    revealOnScroll();
    
    // Add scroll event listener
    window.addEventListener('scroll', () => {
        revealOnScroll();
        
        // Navbar styling on scroll
        const navbar = document.getElementById('navbar');
        if (window.scrollY > 50) {
            navbar.classList.add('glass-panel', 'border-b', 'border-white/5');
            navbar.classList.remove('py-4');
            navbar.classList.add('py-2');
        } else {
            navbar.classList.remove('glass-panel', 'border-b', 'border-white/5');
            navbar.classList.add('py-4');
            navbar.classList.remove('py-2');
        }
    });

    // Smooth scrolling for anchor links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const targetId = this.getAttribute('href');
            if (targetId === '#') return;
            
            const targetElement = document.querySelector(targetId);
            if (targetElement) {
                targetElement.scrollIntoView({
                    behavior: 'smooth'
                });
            }
        });
    });

    // Highlight active nav link and add animation classes
    const currentPath = window.location.pathname.split('/').pop() || 'index.html';
    const navLinks = document.querySelectorAll('#navbar a[href$=".html"], #mobile-menu a[href$=".html"]');
    
    navLinks.forEach(link => {
        link.classList.add('nav-link');
        const href = link.getAttribute('href');
        if (href === currentPath) {
            link.classList.add('active-nav-link');
        }
    });

    // Mobile Navigation Toggle
    const mobileMenuBtn = document.getElementById('mobile-menu-btn');
    const mobileMenu = document.getElementById('mobile-menu');
    const mobileMenuIconOpen = document.getElementById('mobile-menu-icon-open');
    const mobileMenuIconClose = document.getElementById('mobile-menu-icon-close');

    if (mobileMenuBtn && mobileMenu) {
        const toggleMobileMenu = () => {
            const isOpen = !mobileMenu.classList.contains('hidden');
            if (isOpen) {
                mobileMenu.classList.add('hidden');
                if (mobileMenuIconOpen) mobileMenuIconOpen.classList.remove('hidden');
                if (mobileMenuIconClose) mobileMenuIconClose.classList.add('hidden');
                document.body.classList.remove('overflow-hidden');
            } else {
                mobileMenu.classList.remove('hidden');
                if (mobileMenuIconOpen) mobileMenuIconOpen.classList.add('hidden');
                if (mobileMenuIconClose) mobileMenuIconClose.classList.remove('hidden');
                document.body.classList.add('overflow-hidden');
            }
        };

        mobileMenuBtn.addEventListener('click', toggleMobileMenu);

        // Close mobile menu when clicking on a link
        mobileMenu.querySelectorAll('a').forEach(link => {
            link.addEventListener('click', () => {
                mobileMenu.classList.add('hidden');
                if (mobileMenuIconOpen) mobileMenuIconOpen.classList.remove('hidden');
                if (mobileMenuIconClose) mobileMenuIconClose.classList.add('hidden');
                document.body.classList.remove('overflow-hidden');
            });
        });
    }
});

// --- Projects & Blog Page Filtering Logic ---
document.addEventListener('DOMContentLoaded', () => {
    const filterGrid = document.getElementById('projects-grid') || document.getElementById('blog-grid') || document.getElementById('podcast-grid');
    if (!filterGrid) return;
    
    // Select all project, blog, and podcast cards
    let filterCards = Array.from(document.querySelectorAll('.project-card, .blog-card, .podcast-card'));
    const filterSearch = document.getElementById('filter-search');
    const filterSort = document.getElementById('filter-sort');
    const filterTheme = document.getElementById('filter-theme');
    const filterTypeCheckboxes = document.querySelectorAll('.filter-type');
    const filterPeriodRadios = document.querySelectorAll('.filter-period');
    const btnReset = document.getElementById('btn-reset-filters');
    const noResultsMsg = document.getElementById('no-results');
    
    // Store all cards already defined above in filterCards
    
    // Store original order for 'relevance' sort fallback
    const originalOrder = [...filterCards];

    function applyFilters() {
        if (!filterGrid) return;
        
        const searchTerm = filterSearch ? filterSearch.value.toLowerCase() : '';
        const selectedTheme = filterTheme ? filterTheme.value : '';
        
        // Get active types
        const selectedTypes = Array.from(filterTypeCheckboxes)
            .filter(cb => cb.checked)
            .map(cb => cb.value);
            
        // Get active period
        const selectedPeriodRadio = document.querySelector('.filter-period:checked');
        const selectedPeriod = selectedPeriodRadio ? selectedPeriodRadio.value : null;

        let visibleCount = 0;
        const now = new Date();

        filterCards.forEach(card => {
            let isVisible = true;
            
            // Search filter (use textContent to read text even if element is hidden)
            if (searchTerm) {
                const title = card.getAttribute('data-title') || '';
                const excerpt = card.textContent.toLowerCase();
                if (!title.includes(searchTerm) && !excerpt.includes(searchTerm)) {
                    isVisible = false;
                }
            }
            
            // Theme filter
            if (isVisible && selectedTheme) {
                const theme = card.getAttribute('data-theme');
                if (theme !== selectedTheme) {
                    isVisible = false;
                }
            }
            
            // Type filter
            if (isVisible && selectedTypes.length > 0) {
                const type = card.getAttribute('data-type');
                if (!selectedTypes.includes(type)) {
                    isVisible = false;
                }
            }
            
            // Period filter
            if (isVisible && selectedPeriod) {
                const dateStr = card.getAttribute('data-date');
                if (dateStr) {
                    const cardDate = new Date(dateStr);
                    const diffTime = Math.abs(now - cardDate);
                    const diffDays = Math.ceil(diffTime / (1000 * 60 * 60 * 24));
                    
                    if (selectedPeriod === '1w' && diffDays > 7) isVisible = false;
                    else if (selectedPeriod === '1m' && diffDays > 31) isVisible = false;
                    else if (selectedPeriod === '1y' && diffDays > 365) isVisible = false;
                }
            }
            
            // Toggle visibility using inline style which overrides tailwind classes
            if (isVisible) {
                card.style.display = 'flex'; // Ensure cards stay flex/block as needed. We'll use style.display = '' to fallback to CSS class default
                card.style.display = '';
                // Since cards use `flex` or `block`, resetting it to empty string falls back to the CSS class definition.
                // Wait, project cards use flex, blog cards use block. Let's conditionally set it.
                if (card.classList.contains('flex')) {
                    card.style.display = 'flex';
                } else {
                    card.style.display = 'block';
                }
                
                visibleCount++;
            } else {
                card.style.display = 'none';
            }
        });
        
        // Handle 'no results' message
        if (noResultsMsg) {
            noResultsMsg.style.display = visibleCount === 0 ? 'block' : 'none';
        }
        
        applySorting();
    }

    function applySorting() {
        if (!filterSort || !filterGrid) return;
        const sortValue = filterSort.value;
        
        if (sortValue === 'rel') {
            // Restore original order
            originalOrder.forEach(card => filterGrid.appendChild(card));
        } else {
            // Sort by Date
            const sortedCards = [...filterCards].sort((a, b) => {
                const dateA = new Date(a.getAttribute('data-date') || 0);
                const dateB = new Date(b.getAttribute('data-date') || 0);
                return sortValue === 'desc' ? dateB - dateA : dateA - dateB;
            });
            sortedCards.forEach(card => filterGrid.appendChild(card));
        }
        
        // Ensure the no-results message stays at the very bottom of the grid
        if (noResultsMsg) {
            filterGrid.appendChild(noResultsMsg);
        }
    }

    // Attach Event Listeners safely
    if (filterSearch) filterSearch.addEventListener('input', applyFilters);
    if (filterTheme) filterTheme.addEventListener('change', applyFilters);
    if (filterSort) filterSort.addEventListener('change', applySorting); 
    
    if (filterTypeCheckboxes) {
        filterTypeCheckboxes.forEach(cb => cb.addEventListener('change', applyFilters));
    }
    
    if (filterPeriodRadios) {
        filterPeriodRadios.forEach(radio => radio.addEventListener('change', applyFilters));
    }
    
    if (btnReset) {
        btnReset.addEventListener('click', (e) => {
            e.preventDefault(); // Prevent any form submission just in case
            if (filterSearch) filterSearch.value = '';
            if (filterTheme) filterTheme.value = '';
            if (filterSort) filterSort.value = 'desc';
            if (filterTypeCheckboxes) filterTypeCheckboxes.forEach(cb => cb.checked = false);
            if (filterPeriodRadios) filterPeriodRadios.forEach(radio => radio.checked = false);
            applyFilters();
        });
    }
});
