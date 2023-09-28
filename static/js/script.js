const closeButton1 = document.getElementById("close-button-1");
const closeButton2 = document.getElementById("close-button-2");
const panel = document.getElementById("panel");
function closePanel() {
    panel.style.display = "none";
}
closeButton1.addEventListener("click", closePanel);
closeButton2.addEventListener("click", closePanel);
