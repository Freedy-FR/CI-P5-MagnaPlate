// Select the carousel element by its ID
const myCarouselElement = document.querySelector('#myCarousel');

// Initialize the Bootstrap carousel with specific options
const carousel = new bootstrap.Carousel(myCarouselElement, {
    interval: 2000, // Set the interval between slides to 2000 milliseconds (2 seconds)
    touch: false    // Disable touch interactions for the carousel
});
