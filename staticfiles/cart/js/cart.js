document.addEventListener('DOMContentLoaded', () => {
    // Get all increment and decrement buttons and quantity input fields
    const incrementButtons = document.querySelectorAll('.increment-qty');
    const decrementButtons = document.querySelectorAll('.decrement-qty');
    const qtyInputs = document.querySelectorAll('.qty_input');

    /**
     * Function to handle incrementing the quantity
     * @param {Event} e - The event object
     */
    function handleIncrement(e) {
        const itemId = e.currentTarget.dataset.item_id;
        const itemSize = e.currentTarget.dataset.item_size;
        const qtyInput = document.getElementById(`id_qty_${itemId}_${itemSize}`);
        
        if (qtyInput) {
            let currentValue = parseInt(qtyInput.value);
            if (currentValue < 99) { // Ensure the quantity doesn't exceed 99
                qtyInput.value = currentValue + 1;
                qtyInput.dispatchEvent(new Event('change')); // Trigger change event
            }
        }
    }

    /**
     * Function to handle decrementing the quantity
     * param {Event} e - The event object
     */
    function handleDecrement(e) {
        const itemId = e.currentTarget.dataset.item_id;
        const itemSize = e.currentTarget.dataset.item_size;
        const qtyInput = document.getElementById(`id_qty_${itemId}_${itemSize}`);
        
        if (qtyInput) {
            let currentValue = parseInt(qtyInput.value);
            if (currentValue > 1) { // Ensure the quantity doesn't go below 1
                qtyInput.value = currentValue - 1;
                qtyInput.dispatchEvent(new Event('change')); // Trigger change event
            }
        }
    }

    // Add click event listeners to increment buttons
    incrementButtons.forEach(button => {
        button.addEventListener('click', handleIncrement);
    });

    // Add click event listeners to decrement buttons
    decrementButtons.forEach(button => {
        button.addEventListener('click', handleDecrement);
    });
});
