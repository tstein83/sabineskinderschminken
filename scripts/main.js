// Sabines Kinderschminken - Main JavaScript

// ============================================
// Mobile Navigation
// ============================================
const navToggle = document.getElementById('navToggle');
const navMenu = document.getElementById('navMenu');
const navLinks = document.querySelectorAll('.nav-link');

navToggle.addEventListener('click', () => {
    navMenu.classList.toggle('active');
});

// Close mobile menu when clicking a link
navLinks.forEach(link => {
    link.addEventListener('click', () => {
        navMenu.classList.remove('active');
    });
});

// ============================================
// Header Scroll Effect
// ============================================
const header = document.getElementById('header');

window.addEventListener('scroll', () => {
    if (window.scrollY > 100) {
        header.classList.add('scrolled');
    } else {
        header.classList.remove('scrolled');
    }
});

// ============================================
// Active Navigation Link on Scroll
// ============================================
const sections = document.querySelectorAll('section[id]');

function highlightNavigation() {
    const scrollY = window.pageYOffset;

    sections.forEach(section => {
        const sectionHeight = section.offsetHeight;
        const sectionTop = section.offsetTop - 100;
        const sectionId = section.getAttribute('id');
        const navLink = document.querySelector(`.nav-link[href="#${sectionId}"]`);

        if (navLink && scrollY > sectionTop && scrollY <= sectionTop + sectionHeight) {
            navLinks.forEach(link => link.classList.remove('active'));
            navLink.classList.add('active');
        }
    });
}

window.addEventListener('scroll', highlightNavigation);

// ============================================
// Gallery
// ============================================
const galleryImages = [
    // Kinderschminken
    { src: 'public/images/gallery/kinderschminken_beispiel_1.jpg', category: 'kinderschminken', alt: 'Kinderschminken Beispiel 1' },
    { src: 'public/images/gallery/kinderschminken_beispiel_2.jpg', category: 'kinderschminken', alt: 'Kinderschminken Beispiel 2' },
    { src: 'public/images/gallery/galerie_1.jpg', category: 'kinderschminken', alt: 'Kinderschminken' },
    { src: 'public/images/gallery/galerie_2.jpg', category: 'kinderschminken', alt: 'Facepainting' },
    { src: 'public/images/services/kinderschminken_1.jpg', category: 'kinderschminken', alt: 'Kinderschminken Service' },
    { src: 'public/images/services/kinderschminken_2.jpg', category: 'kinderschminken', alt: 'Kinderschminken Event' },

    // Ballons
    { src: 'public/images/services/ballons_1.jpg', category: 'ballons', alt: 'Ballon-Figuren' },
    { src: 'public/images/services/ballons_2.jpg', category: 'ballons', alt: 'Ballonkunst' },
    { src: 'public/images/services/ballons_3.jpg', category: 'ballons', alt: 'Ballontiere' },
    { src: 'public/images/services/ballons_4.jpg', category: 'ballons', alt: 'Ballondekoration' },

    // Events
    { src: 'public/images/gallery/galerie_3.jpg', category: 'events', alt: 'Event 1' },
    { src: 'public/images/gallery/galerie_4.jpg', category: 'events', alt: 'Event 2' },
    { src: 'public/images/services/facepainting_1.jpg', category: 'events', alt: 'Facepainting Event' },
    { src: 'public/images/services/halloween_1.jpg', category: 'events', alt: 'Halloween Event' },
];

const galleryGrid = document.getElementById('galleryGrid');
const filterButtons = document.querySelectorAll('.filter-btn');

// Render gallery
function renderGallery(filter = 'all') {
    galleryGrid.innerHTML = '';

    const filteredImages = filter === 'all'
        ? galleryImages
        : galleryImages.filter(img => img.category === filter);

    filteredImages.forEach((image, index) => {
        const galleryItem = document.createElement('div');
        galleryItem.className = 'gallery-item';
        galleryItem.dataset.index = index;
        galleryItem.innerHTML = `
            <img src="${image.src}" alt="${image.alt}" loading="lazy">
        `;
        galleryGrid.appendChild(galleryItem);
    });

    // Add click handlers for lightbox
    const galleryItems = document.querySelectorAll('.gallery-item');
    galleryItems.forEach(item => {
        item.addEventListener('click', () => {
            const index = parseInt(item.dataset.index);
            openLightbox(filteredImages, index);
        });
    });
}

// Gallery filter
filterButtons.forEach(button => {
    button.addEventListener('click', () => {
        // Update active button
        filterButtons.forEach(btn => btn.classList.remove('active'));
        button.classList.add('active');

        // Filter gallery
        const filter = button.dataset.filter;
        renderGallery(filter);
    });
});

// Initial gallery render
renderGallery();

// ============================================
// Lightbox
// ============================================
const lightbox = document.getElementById('lightbox');
const lightboxImg = document.getElementById('lightboxImg');
const lightboxClose = document.getElementById('lightboxClose');
const lightboxPrev = document.getElementById('lightboxPrev');
const lightboxNext = document.getElementById('lightboxNext');

let currentImages = [];
let currentIndex = 0;

function openLightbox(images, index) {
    currentImages = images;
    currentIndex = index;
    updateLightboxImage();
    lightbox.classList.add('active');
    document.body.style.overflow = 'hidden';
}

function closeLightbox() {
    lightbox.classList.remove('active');
    document.body.style.overflow = '';
}

function updateLightboxImage() {
    if (currentImages.length > 0) {
        lightboxImg.src = currentImages[currentIndex].src;
        lightboxImg.alt = currentImages[currentIndex].alt;
    }
}

function showPrevImage() {
    currentIndex = (currentIndex - 1 + currentImages.length) % currentImages.length;
    updateLightboxImage();
}

function showNextImage() {
    currentIndex = (currentIndex + 1) % currentImages.length;
    updateLightboxImage();
}

// Lightbox event listeners
lightboxClose.addEventListener('click', closeLightbox);
lightboxPrev.addEventListener('click', showPrevImage);
lightboxNext.addEventListener('click', showNextImage);

// Close lightbox on background click
lightbox.addEventListener('click', (e) => {
    if (e.target === lightbox) {
        closeLightbox();
    }
});

// Keyboard navigation
document.addEventListener('keydown', (e) => {
    if (!lightbox.classList.contains('active')) return;

    if (e.key === 'Escape') closeLightbox();
    if (e.key === 'ArrowLeft') showPrevImage();
    if (e.key === 'ArrowRight') showNextImage();
});

// ============================================
// Contact Form
// ============================================
const contactForm = document.getElementById('contactForm');

contactForm.addEventListener('submit', (e) => {
    e.preventDefault();

    // Get form data
    const formData = new FormData(contactForm);
    const data = Object.fromEntries(formData);

    console.log('Form data:', data);

    // In production, send to backend
    // For now, show success message
    alert('Vielen Dank für Ihre Nachricht! Wir melden uns bald bei Ihnen.');
    contactForm.reset();

    // TODO: Implement actual form submission
    // fetch('/api/contact', {
    //     method: 'POST',
    //     headers: { 'Content-Type': 'application/json' },
    //     body: JSON.stringify(data)
    // });
});

// ============================================
// Smooth Scroll
// ============================================
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        const href = this.getAttribute('href');

        // Skip if href is just "#"
        if (href === '#') {
            e.preventDefault();
            return;
        }

        const target = document.querySelector(href);
        if (target) {
            e.preventDefault();
            const headerOffset = 80;
            const elementPosition = target.getBoundingClientRect().top;
            const offsetPosition = elementPosition + window.pageYOffset - headerOffset;

            window.scrollTo({
                top: offsetPosition,
                behavior: 'smooth'
            });
        }
    });
});

// ============================================
// Scroll Animations (AOS - Animate On Scroll)
// ============================================
const observerOptions = {
    threshold: 0.1,
    rootMargin: '0px 0px -50px 0px'
};

const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.classList.add('aos-animate');
        }
    });
}, observerOptions);

// Observe all elements with data-aos attribute
document.querySelectorAll('[data-aos]').forEach(el => {
    observer.observe(el);
});

// ============================================
// Loading State
// ============================================
window.addEventListener('load', () => {
    document.body.classList.add('loaded');
});

// ============================================
// Performance: Lazy Loading Images
// ============================================
if ('loading' in HTMLImageElement.prototype) {
    // Browser supports native lazy loading
    const images = document.querySelectorAll('img[loading="lazy"]');
    images.forEach(img => {
        img.src = img.src;
    });
} else {
    // Fallback for browsers that don't support lazy loading
    const script = document.createElement('script');
    script.src = 'https://cdnjs.cloudflare.com/ajax/libs/lazysizes/5.3.2/lazysizes.min.js';
    document.body.appendChild(script);
}

// ============================================
// Console Message
// ============================================
console.log('%c✨ Sabines Kinderschminken ✨', 'font-size: 20px; color: #FF6B9D; font-weight: bold;');
console.log('%cWebsite entwickelt mit ❤️', 'font-size: 12px; color: #4ECDC4;');
