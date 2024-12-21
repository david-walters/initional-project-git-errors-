
function updatePrice(selectElement) {
    const prices = {
        "25 ml": 24.00,
        "50 ml": 36.00,
        "75 ml": 60.00
    };
    document.getElementById("price").innerText = "£" + prices[selectElement.value].toFixed(2);
}