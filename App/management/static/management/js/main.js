// CHECKBOX INDETERMINATE:
var checkboxes = document.getElementsByClassName("form-check-indeterminate");
for (let i =0; i < checkboxes.length; i++) {
    checkboxes[i].indeterminate = true;
    checkboxes[i].value = "indeterminate";
}

// SIDEBAR CLOSE ACTION:
var activeElement1 = document.getElementById("wrapper");
var toggleButton1 = document.getElementById("menu-toggle");

toggleButton1.onclick = function () {
    activeElement1.classList.toggle("toggled");
};