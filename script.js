// ========================================
// 4 Mevsim Branda - Modern Awning Services Website
// ========================================

// ========================================
// Hero Image Slider
// ========================================

let currentSlide = 0;
const slides = document.querySelectorAll('.hero-slide');
const dots = document.querySelectorAll('.dot');
let slideInterval;

function showSlide(index) {
    // Remove active class from all slides and dots
    slides.forEach(slide => slide.classList.remove('active'));
    dots.forEach(dot => dot.classList.remove('active'));

    // Add active class to current slide and dot
    if (slides[index]) {
        slides[index].classList.add('active');
    }
    if (dots[index]) {
        dots[index].classList.add('active');
    }

    currentSlide = index;
}

function nextSlide() {
    let next = (currentSlide + 1) % slides.length;
    showSlide(next);
}

function prevSlide() {
    let prev = (currentSlide - 1 + slides.length) % slides.length;
    showSlide(prev);
}

function startAutoSlide() {
    slideInterval = setInterval(nextSlide, 5000); // Change slide every 5 seconds
}

function stopAutoSlide() {
    clearInterval(slideInterval);
}

// Initialize slider
if (slides.length > 0) {
    showSlide(0);
    startAutoSlide();

    // Pause on hover
    const heroSlider = document.querySelector('.hero-slider');
    if (heroSlider) {
        heroSlider.addEventListener('mouseenter', stopAutoSlide);
        heroSlider.addEventListener('mouseleave', startAutoSlide);
    }
}

// Counter Animation for Stats
function animateCounters() {
    const counters = document.querySelectorAll('.counter-number');

    counters.forEach(counter => {
        const target = parseInt(counter.getAttribute('data-target'));
        const duration = 2000; // 2 seconds
        const increment = target / (duration / 16); // 60fps

        let current = 0;
        const timer = setInterval(() => {
            current += increment;
            const suffix = counter.getAttribute('data-suffix') || '';
            if (current >= target) {
                counter.textContent = target.toLocaleString('tr-TR') + suffix;
                clearInterval(timer);
            } else {
                counter.textContent = Math.floor(current).toLocaleString('tr-TR') + suffix;
            }
        }, 16);
    });
}

// Intersection Observer for Counter Animation
const statsSection = document.querySelector('.stats-section');
if (statsSection) {
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                animateCounters();
                observer.unobserve(entry.target);
            }
        });
    }, { threshold: 0.1 });

    observer.observe(statsSection);
}

// ========================================
// Navigation
// ========================================

const navToggle = document.getElementById('navToggle');
const navLinks = document.getElementById('navLinks');
const navbar = document.getElementById('navbar');

// Mobile menu toggle
if (navToggle) {
    navToggle.addEventListener('click', () => {
        navLinks.classList.toggle('active');
    });
}

// Mobile Dropdown Toggle
const dropdowns = document.querySelectorAll('.dropdown');
dropdowns.forEach(dropdown => {
    const dropbtn = dropdown.querySelector('.dropbtn');
    if (dropbtn) {
        dropbtn.addEventListener('click', (e) => {
            // Only apply toggle logic on mobile (screens < 768px)
            if (window.innerWidth <= 768) {
                e.preventDefault(); // Prevent jump to #services
                dropdown.classList.toggle('active');
            }
        });
    }
});

// Navbar scroll effect
window.addEventListener('scroll', () => {
    if (window.scrollY > 100) {
        navbar.classList.add('scrolled');
    } else {
        navbar.classList.remove('scrolled');
    }
});

// ========================================
// Smooth Scroll
// ========================================

document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        const href = this.getAttribute('href');
        if (href !== '#' && href.startsWith('#')) {
            e.preventDefault();
            const target = document.querySelector(href);
            if (target) {
                const navbarHeight = navbar.offsetHeight;
                const targetPosition = target.offsetPosition - navbarHeight;

                window.scrollTo({
                    top: targetPosition,
                    behavior: 'smooth'
                });

                // Close mobile menu if open
                navLinks.classList.remove('active');
            }
        }
    });
});

// ========================================
// Scroll Reveal Animation (Sequence & Stagger)
// ========================================

const observerOptions = {
    threshold: 0.1,
    rootMargin: '0px 0px -50px 0px'
};

const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.classList.add('visible');
            entry.target.style.opacity = '1';
            entry.target.style.transform = 'translateY(0)';
        }
    });
}, observerOptions);

// Observe elements with staggered delay
const revealElements = document.querySelectorAll('.service-card, .counter-card, .card, .section-title, .section-subtitle, .hero-content > *');

revealElements.forEach((el, index) => {
    el.style.opacity = '0';
    el.style.transform = 'translateY(30px)';
    el.style.transition = 'all 0.8s cubic-bezier(0.2, 0.8, 0.2, 1)';

    observer.observe(el);
});

// ========================================
// Service Cards Interactions
// ========================================

document.querySelectorAll('.btn-details').forEach(button => {
    button.addEventListener('click', (e) => {
        e.preventDefault();
        const serviceTitle = button.closest('.service-card').querySelector('.service-title').textContent;

        // Show inquiry modal or redirect to contact
        alert(`${serviceTitle} hakkında daha fazla bilgi almak için 0 551 421 87 05 numaralı telefonu arayabilir veya WhatsApp ile iletişime geçebilirsiniz.`);
    });
});

console.log('4 Mevsim Branda website loaded successfully!');

// ========================================
// Gallery Carousel & Tabs
// ========================================

document.addEventListener('DOMContentLoaded', () => {
    console.log('Gallery script initializing...');

    const tabs = document.querySelectorAll('.gallery-tab');
    const carousels = document.querySelectorAll('.carousel-container');
    const carouselInstances = {};

    // --- Carousel Class ---
    class Carousel {
        constructor(element) {
            this.element = element;
            this.track = element.querySelector('.carousel-track');
            this.slides = Array.from(this.track.children);
            this.nextButton = element.querySelector('.carousel-btn.next');
            this.prevButton = element.querySelector('.carousel-btn.prev');
            this.dotsNav = element.querySelector('.carousel-nav');
            this.dots = Array.from(this.dotsNav.children);

            // Initial Setup
            // Ensure first slide is set if not already
            if (!this.track.querySelector('.current-slide')) {
                this.slides[0]?.classList.add('current-slide');
                this.dots[0]?.classList.add('current-slide');
            }

            // Event Listeners
            if (this.nextButton) {
                this.nextButton.addEventListener('click', (e) => {
                    e.preventDefault();
                    this.moveSlide('next');
                });
            }
            if (this.prevButton) {
                this.prevButton.addEventListener('click', (e) => {
                    e.preventDefault();
                    this.moveSlide('prev');
                });
            }

            this.dots.forEach((dot, index) => {
                dot.addEventListener('click', (e) => {
                    e.preventDefault();
                    this.moveToSlide(index);
                });
            });

            // Handle Resize - just ensuring nothing breaks, but percentage logic handles fluid width
            window.addEventListener('resize', () => {
                // No-op for now as percentages handle layout
            });
        }

        moveToSlide(targetIndex, transition = true) {
            if (targetIndex < 0 || targetIndex >= this.slides.length) return;

            const currentSlide = this.track.querySelector('.current-slide');
            const targetSlide = this.slides[targetIndex];
            const currentDot = this.dotsNav.querySelector('.current-slide');
            const targetDot = this.dots[targetIndex];

            // Setup Transition
            if (!transition) {
                this.track.style.transition = 'none';
            } else {
                this.track.style.transition = 'transform 0.5s ease-in-out';
            }

            // Move track to negative percentage based on index
            // 0 -> 0%, 1 -> -100%, 2 -> -200%
            this.track.style.transform = `translateX(-${targetIndex * 100}%)`;

            if (!transition) {
                // Force reflow
                void this.track.offsetWidth; // Flush CSS changes
                this.track.style.transition = 'transform 0.5s ease-in-out';
            }

            // Update Classes
            if (currentSlide) currentSlide.classList.remove('current-slide');
            if (targetSlide) targetSlide.classList.add('current-slide');

            if (currentDot) currentDot.classList.remove('current-slide');
            if (targetDot) targetDot.classList.add('current-slide');
        }

        moveSlide(direction) {
            const currentSlide = this.track.querySelector('.current-slide');
            const currentIndex = currentSlide ? this.slides.findIndex(slide => slide === currentSlide) : 0;
            let nextIndex;

            if (direction === 'next') {
                nextIndex = currentIndex + 1;
                if (nextIndex >= this.slides.length) nextIndex = 0; // Loop back
            } else {
                nextIndex = currentIndex - 1;
                if (nextIndex < 0) nextIndex = this.slides.length - 1; // Loop to end
            }

            this.moveToSlide(nextIndex);
        }
    }

    // Initialize carousels
    carousels.forEach(carouselEl => {
        carouselInstances[carouselEl.id] = new Carousel(carouselEl);
    });

    // --- Tab Switching ---
    tabs.forEach(tab => {
        tab.addEventListener('click', (e) => {
            e.preventDefault();

            // Update Tab UI
            tabs.forEach(t => t.classList.remove('active'));
            tab.classList.add('active');

            // Switch Carousel visibility
            carousels.forEach(c => c.classList.remove('active'));
            const targetId = `${tab.dataset.tab}-carousel`;
            const targetCarousel = document.getElementById(targetId);

            if (targetCarousel) {
                targetCarousel.classList.add('active');

                // Ensure instance is synced with correct slide position
                if (carouselInstances[targetId]) {
                    const instance = carouselInstances[targetId];
                    const currentSlide = targetCarousel.querySelector('.current-slide');
                    let index = 0;
                    if (currentSlide) {
                        index = instance.slides.indexOf(currentSlide);
                    } else {
                        instance.slides[0]?.classList.add('current-slide');
                        index = 0;
                    }

                    // Force slight delay to allow display:block to take effect if needed for reflow
                    // although percent transform should work regardless
                    requestAnimationFrame(() => {
                        instance.moveToSlide(index, false);
                    });
                }
            }
        });
    });



    // Window load fallback
    window.addEventListener('load', () => {
        window.dispatchEvent(new Event('resize'));
    });
});
