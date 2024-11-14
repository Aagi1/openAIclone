


/*********defilement menu hamburger mobile********/
const navLinks = document.querySelector('#navbarNav')
const iconSearch = document.querySelector('#iconSearch');

function onToggleMenu(e) {
    e.name = e.name === 'menu' ? 'close' : 'menu'

    // Alterner l'affichage de l'icône de recherche
    iconSearch.style.display = iconSearch.style.display === 'none' ? 'block' : 'none';

    navLinks.classList.toggle('top-[54px]')
}


/*******Scroll horizontal des carrousel des differentes sections*/
document.addEventListener("DOMContentLoaded", function () {
    const carrouselContainers = document.querySelectorAll(".carrouselContainer");
    const btnLefts = document.querySelectorAll(".carrousel-button-left");
    const btnRights = document.querySelectorAll(".carrousel-button-right");

    carrouselContainers.forEach((container, index) => {
        // Sélectionne les boutons gauche et droite pour le carrousel actuel
        const btnLeft = btnLefts[index];
        const btnRight = btnRights[index];

        // Remet le carrousel à la position de départ
        container.scrollLeft = 0;

        // Fonction pour vérifier la position du carrousel et ajuster les boutons
        function checkButtons() {
            btnLeft.style.opacity = container.scrollLeft === 0 ? "0.5" : "1";
            btnRight.style.opacity = container.scrollLeft + container.clientWidth >= container.scrollWidth ? "0.5" : "1";
        }

        // Fonction pour défiler à droite
        btnRight.addEventListener("click", function () {
            const scrollAmount = container.clientWidth;
            container.scrollBy({ left: scrollAmount, behavior: "smooth" });
        });

        // Fonction pour défiler à gauche
        btnLeft.addEventListener("click", function () {
            const scrollAmount = container.clientWidth;
            container.scrollBy({ left: -scrollAmount, behavior: "smooth" });
        });

        // Vérifie la position initiale du carrousel
        checkButtons();

        // Écoute les événements de défilement pour ajuster les boutons
        container.addEventListener("scroll", checkButtons);
    });
});


/*****************menu dropdown **********/

// Sélectionner tous les éléments de type dropdown et leurs éléments de déclenchement
const dropdowns = [
    { trigger: document.querySelector('#research-nav'), menu: document.getElementById('dropdown-research') },
    { trigger: document.querySelector('#products-nav'), menu: document.getElementById('dropdown-products') },
    { trigger: document.querySelector('#company-nav'), menu: document.getElementById('dropdown-company') }
];

let hideTimeout;

// Fonction générique pour afficher un dropdown
function showDropdown(dropdownMenu) {
    clearTimeout(hideTimeout); // Annuler le masquage s'il est prévu
    dropdownMenu.classList.remove('hidden');
    dropdownMenu.classList.add('flex');
}

// Fonction générique pour masquer un dropdown
function hideDropdown(dropdownMenu) {
    hideTimeout = setTimeout(() => {
        dropdownMenu.classList.remove('flex');
        dropdownMenu.classList.add('hidden');
    }, 200); // 200ms pour donner le temps de passer entre les éléments
}

// Ajouter les événements pour chaque dropdown
dropdowns.forEach(({ trigger, menu }) => {
    trigger.addEventListener('mouseover', () => showDropdown(menu)); // Afficher lors du survol du trigger
    trigger.addEventListener('mouseleave', () => hideDropdown(menu)); // Masquer lors du départ de la souris du trigger
    menu.addEventListener('mouseover', () => showDropdown(menu)); // Rester visible lors du survol du menu
    menu.addEventListener('mouseleave', () => hideDropdown(menu)); // Masquer lors du départ de la souris du menu
});

/**********afficher ou cacher le header en fonction du scroll */
window.onload = function () {
    let lastScrollY = window.scrollY;
    const header = document.querySelector('header');

    window.addEventListener('scroll', function () {
        const currentScrollY = window.scrollY;

        // Si on défile vers le bas
        if (currentScrollY > lastScrollY) {
            header.classList.add('-translate-y-full'); // Cache le header
        } else {
            header.classList.remove('-translate-y-full'); // Affiche le header
            header.classList.add('bg-opacity-80'); // Rendre le header transparent
        }

        // Si on est tout en haut, rétablir la transparence
        if (currentScrollY === 0) {
            header.classList.remove('bg-opacity-50');
        }

        lastScrollY = currentScrollY;
    })

};
