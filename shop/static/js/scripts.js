
function updatePrice(selectElement) {
    const prices = {
        "25 ml": 24.00,
        "50 ml": 36.00,
        "75 ml": 60.00
    };
    document.getElementById("price").innerText = "£" + prices[selectElement.value].toFixed(2);
}

document.addEventListener('DOMContentLoaded', function () {
    const cartItems = document.querySelectorAll('.cart-item');
    const finalisePurchaseDiv = document.getElementById('make-purchase');
    if (cartItems.length === 0) {
        finalisePurchaseDiv.classList.add('hide')
    } else {
        finalisePurchaseDiv.classList.remove('hide');
    }
});