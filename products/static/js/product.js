
document.addEventListener('DOMContentLoaded', function() {

    var allQtyInputs = document.getElementsByClassName('qty_input');

    for (var i = 0; i < allQtyInputs.length; i++) {
        var itemId = allQtyInputs[i].getAttribute('data-item_id');
        buttonEnableDisable(itemId);
    }

    function buttonEnableDisable(itemId) {
        var currentValue = parseInt(document.getElementById(`id_qty_${itemId}`).value);
        var minusDisabled = currentValue < 2;
        var plusDisabled = currentValue > 98;
        document.getElementById(`decrement-qty_${itemId}`).disabled = minusDisabled;
        document.getElementById(`increment-qty_${itemId}`).disabled = plusDisabled;
    }

    function incrementQuantity(itemId) {
        var currentValue = parseInt(document.getElementById(`id_qty_${itemId}`).value);
        var newValue = currentValue + 1;
        document.getElementById(`id_qty_${itemId}`).value = newValue;
        buttonEnableDisable(itemId);
    }

    function decrementQuantity(itemId) {
        var currentValue = parseInt(document.getElementById(`id_qty_${itemId}`).value);
        var newValue = currentValue - 1;
        document.getElementById(`id_qty_${itemId}`).value = newValue;
        buttonEnableDisable(itemId);
    }

    var incrementButtons = document.getElementsByClassName('increment-qty');
    var decrementButtons = document.getElementsByClassName('decrement-qty');

    for (var i = 0; i < incrementButtons.length; i++) {
        incrementButtons[i].addEventListener('click', function(e) {
            e.preventDefault();
            var itemId = e.target.closest('.input-group').querySelector('.qty_input').getAttribute('data-item_id');
            incrementQuantity(itemId);
        });
    }

    for (var i = 0; i < decrementButtons.length; i++) {
        decrementButtons[i].addEventListener('click', function(e) {
            e.preventDefault();
            var itemId = e.target.closest('.input-group').querySelector('.qty_input').getAttribute('data-item_id');
            decrementQuantity(itemId);
        });
    }
});


