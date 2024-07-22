document.addEventListener('DOMContentLoaded', () => {
    const incrementButtons = document.querySelectorAll('.increment-qty');
    const decrementButtons = document.querySelectorAll('.decrement-qty');
    const qtyInputs = document.querySelectorAll('.qty_input');

    // Function to handle increment
    function handleIncrement(e) {
        const itemId = e.currentTarget.dataset.item_id;
        const itemSize = e.currentTarget.dataset.item_size;
        const qtyInput = document.getElementById(`id_qty_${itemId}_${itemSize}`);
        if (qtyInput) {
            let currentValue = parseInt(qtyInput.value);
            if (currentValue < 99) {
                qtyInput.value = currentValue + 1;
                qtyInput.dispatchEvent(new Event('change'));
            }
        }
    }

    // Function to handle decrement
    function handleDecrement(e) {
        const itemId = e.currentTarget.dataset.item_id;
        const itemSize = e.currentTarget.dataset.item_size;
        const qtyInput = document.getElementById(`id_qty_${itemId}_${itemSize}`);
        if (qtyInput) {
            let currentValue = parseInt(qtyInput.value);
            if (currentValue > 1) {
                qtyInput.value = currentValue - 1;
                qtyInput.dispatchEvent(new Event('change'));
            }
        }
    }

    // Add event listeners to increment buttons
    incrementButtons.forEach(button => {
        button.addEventListener('click', handleIncrement);
    });

    // Add event listeners to decrement buttons
    decrementButtons.forEach(button => {
        button.addEventListener('click', handleDecrement);
    });
});
