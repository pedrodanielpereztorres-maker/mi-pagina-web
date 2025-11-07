document.addEventListener('DOMContentLoaded', () => {
    const observerOptions = {
        root: null, // Usar el viewport como contenedor
        rootMargin: '0px',
        threshold: 0.1 // El 10% del elemento debe ser visible para activar
    };

    const observer = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('is-visible');
                observer.unobserve(entry.target); // Dejar de observar una vez que es visible
            }
        });
    }, observerOptions);

    // Observar todos los elementos con la clase 'logo-appear'
    document.querySelectorAll('.logo-appear').forEach(logo => {
        observer.observe(logo);
    });
});