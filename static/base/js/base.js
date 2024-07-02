
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



// Cursor position logic
document.querySelectorAll('.pagination-link').forEach(function(link) {
    link.addEventListener('click', function() {
        // Store the scroll position
        localStorage.setItem('scrollPosition', window.scrollY);
    });
});


document.addEventListener('DOMContentLoaded', function() {


    // Cursor position logic

    // Retrieve the scroll position if it exists
    const scrollPosition = localStorage.getItem('scrollPosition');
    if (scrollPosition) {
        window.scrollTo(0, parseInt(scrollPosition));
        localStorage.removeItem('scrollPosition'); // Clear the stored position
    }

    
});


