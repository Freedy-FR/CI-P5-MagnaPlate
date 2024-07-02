
// Initialize toasts
$('.toast').toast('show');

// Keep one popup open at each time
document.addEventListener('DOMContentLoaded', function () {
    document.querySelectorAll('.nav-item.dropdown').forEach(function (dropdown) {
        dropdown.addEventListener('show.bs.dropdown', function () {
            document.querySelectorAll('.nav-item.dropdown .dropdown-menu.show').forEach(function (openDropdown) {
                if (openDropdown !== dropdown.querySelector('.dropdown-menu')) {
                    bootstrap.Dropdown.getInstance(openDropdown.previousElementSibling).hide();
                }
            });
        });
    });
});

document.querySelectorAll('.pagination-link').forEach(function(link) {
    link.addEventListener('click', function() {
        // Store the scroll position
        localStorage.setItem('scrollPosition', window.scrollY);
        
        // Find the nearest parent container with data-scroll-target="true"
        const scrollTargetElement = link.closest('[data-scroll-target="true"]');
        if (scrollTargetElement) {
            localStorage.setItem('scrollTarget', scrollTargetElement.id);
        }
    });
});

document.addEventListener('DOMContentLoaded', function() {
    // Retrieve the scroll position if it exists
    const scrollPosition = localStorage.getItem('scrollPosition');
    const scrollTarget = localStorage.getItem('scrollTarget');
    
    if (scrollTarget) {
        const scrollTargetElement = document.getElementById(scrollTarget);
        if (scrollTargetElement) {
            scrollTargetElement.scrollIntoView();
        }
        localStorage.removeItem('scrollTarget'); // Clear the stored target
    } else if (scrollPosition) {
        window.scrollTo(0, parseInt(scrollPosition));
        localStorage.removeItem('scrollPosition'); // Clear the stored position
    }
});