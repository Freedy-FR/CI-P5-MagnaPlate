document.addEventListener('DOMContentLoaded', function() {
    // Get all quantity input elements
    var allQtyInputs = document.getElementsByClassName('qty_input');

    // Initialize button states based on current values
    for (var i = 0; i < allQtyInputs.length; i++) {
        var itemId = allQtyInputs[i].getAttribute('data-item_id');
        buttonEnableDisable(itemId);
    }

    /**
     * Enable or disable increment and decrement buttons based on quantity value
     * @param {string} itemId - The ID of the item
     */
    function buttonEnableDisable(itemId) {
        var currentValue = parseInt(document.getElementById(`id_qty_${itemId}`).value);
        var minusDisabled = currentValue < 2;
        var plusDisabled = currentValue > 98;
        document.getElementById(`decrement-qty_${itemId}`).disabled = minusDisabled;
        document.getElementById(`increment-qty_${itemId}`).disabled = plusDisabled;
    }

    /**
     * Increment the quantity of the item
     * @param {string} itemId - The ID of the item
     */
    function incrementQuantity(itemId) {
        var currentValue = parseInt(document.getElementById(`id_qty_${itemId}`).value);
        var newValue = currentValue + 1;
        document.getElementById(`id_qty_${itemId}`).value = newValue;
        buttonEnableDisable(itemId);
    }

    /**
     * Decrement the quantity of the item
     * @param {string} itemId - The ID of the item
     */
    function decrementQuantity(itemId) {
        var currentValue = parseInt(document.getElementById(`id_qty_${itemId}`).value);
        var newValue = currentValue - 1;
        document.getElementById(`id_qty_${itemId}`).value = newValue;
        buttonEnableDisable(itemId);
    }

    // Get all increment and decrement buttons
    var incrementButtons = document.getElementsByClassName('increment-qty');
    var decrementButtons = document.getElementsByClassName('decrement-qty');

    // Add click event listeners to increment buttons
    for (var i = 0; i < incrementButtons.length; i++) {
        incrementButtons[i].addEventListener('click', function(e) {
            e.preventDefault();
            var itemId = e.target.closest('.input-group').querySelector('.qty_input').getAttribute('data-item_id');
            incrementQuantity(itemId);
        });
    }

    // Add click event listeners to decrement buttons
    for (var i = 0; i < decrementButtons.length; i++) {
        decrementButtons[i].addEventListener('click', function(e) {
            e.preventDefault();
            var itemId = e.target.closest('.input-group').querySelector('.qty_input').getAttribute('data-item_id');
            decrementQuantity(itemId);
        });
    }
});
