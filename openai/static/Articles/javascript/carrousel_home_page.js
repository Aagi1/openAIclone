/************Fonctionnement du carousel principal le hero*/
// Tableau contenant les données du carrousel

const slides = [
    {
        backgroundImage: "url('/static/Articles/images/building-an-early-warning-system-for-llm-aided-biological-threat-creation.avif')",
        h2: "Apple & ChatGPT",
        p: "OpenAI and Apple announce partnership to integrate ChatGPT into Apple experiences."
    },
    {
        backgroundImage: "url('/static/Articles/images/1.webp')",
        h2: "OpenAI Model Preview",
        p: "A new series of AI models designed to spend more time thinking before they respond."
    },
    {
        backgroundImage: "url('/static/Articles/images/2.avif')",
        h2: "Sora: AI Integration",
        p: "Sora is now integrating AI models to enhance user experience."
    }
];

// Variable pour garder la trace de l'index actuel du carrousel
let currentSlide = 0;

// Fonction pour mettre à jour le carrousel
function updateCarousel() {
    const carrouselItem = document.querySelector('.carrousel-item');
    const h2 = document.querySelector(".carrousel-item > .carrousel-text h2");
    const p = document.querySelector(".carrousel-item > .carrousel-text p");
    const carrouselNavLeft = document.querySelector('.carrousel-nav-left');
    const carrouselNavRight = document.querySelector('.carrousel-nav-right');

    // Mise à jour de l'image de fond, du titre et du texte
    carrouselItem.style.backgroundImage = slides[currentSlide].backgroundImage;
    h2.textContent = slides[currentSlide].h2;
    p.textContent = slides[currentSlide].p;

    // Mise à jour des flèches de navigation
    if (currentSlide === 0) {
        carrouselNavLeft.style.visibility = 'hidden'; // Cacher la flèche gauche si on est sur le premier slide
    } else {
        carrouselNavLeft.style.visibility = 'visible'; // Afficher la flèche gauche et mettre l'image du slide précédent
        carrouselNavLeft.style.backgroundImage = slides[currentSlide - 1].backgroundImage;
    }

    if (currentSlide === slides.length - 1) {
        carrouselNavRight.style.visibility = 'hidden'; // Cacher la flèche droite si on est sur le dernier slide
    } else {
        carrouselNavRight.style.visibility = 'visible'; // Afficher la flèche droite et mettre l'image du slide suivant
        carrouselNavRight.style.backgroundImage = slides[currentSlide + 1].backgroundImage;
    }

    // Mise à jour des indicateurs
    updateIndicators();
}

// Fonction pour passer à la diapositive précédente
function previousSlide() {
    if (currentSlide > 0) {
        currentSlide = (currentSlide - 1) % slides.length; // Reculer d'une diapositive
        updateCarousel();
    }
}

// Fonction pour passer à la diapositive suivante
function nextSlide() {
    if (currentSlide < slides.length - 1) {
        currentSlide = (currentSlide + 1) % slides.length; // Avancer d'une diapositive
        updateCarousel();
    }
}

function updateIndicators() {
    const indicators = document.querySelectorAll('.carrousel-indicators li');
    indicators.forEach((indicator, index) => {
        indicator.classList.toggle('active', index === currentSlide);
    });
}

// Fonction pour aller à une diapositive spécifique
function goToSlide(index) {
    currentSlide = index;
    updateCarousel();
}


// Initialiser le carrousel
updateCarousel();