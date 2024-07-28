// Show all toasts when the page loads
$('.toast').toast('show');

// Add click event listeners to all pagination links
document.querySelectorAll('.pagination-link').forEach(function (link) {
    link.addEventListener('click', function () {
        // Store the current scroll position
        localStorage.setItem('scrollPosition', window.scrollY);

        // Find and store the nearest parent container with data-scroll-target="true"
        const scrollTargetElement = link.closest('[data-scroll-target="true"]');
        if (scrollTargetElement) {
            localStorage.setItem('scrollTarget', scrollTargetElement.id);
        }
    });
});

document.addEventListener('DOMContentLoaded', function () {
    // Retrieve the stored scroll position and target if they exist
    const scrollPosition = localStorage.getItem('scrollPosition');
    const scrollTarget = localStorage.getItem('scrollTarget');

    if (scrollTarget) {
        const scrollTargetElement = document.getElementById(scrollTarget);
        if (scrollTargetElement) {
            // Scroll to the stored target element
            scrollTargetElement.scrollIntoView();
        }
        // Clear the stored scroll target
        localStorage.removeItem('scrollTarget');
    } else if (scrollPosition) {
        // Scroll to the stored scroll position
        window.scrollTo(0, parseInt(scrollPosition));
        // Clear the stored scroll position
        localStorage.removeItem('scrollPosition');
    }
});
