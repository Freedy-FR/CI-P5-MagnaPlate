
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