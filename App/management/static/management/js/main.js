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


// SIDEBAR SUB MENU ACTION:
var toggleButton = document.getElementsByClassName("dropdown-action");

for(let i=0; i<toggleButton.length; i++) {
    let toggleButtonThis = toggleButton[i]
    let activeElement = toggleButton[i].nextElementSibling

    toggleButtonThis.addEventListener("click", function(event) {
        for(let i=0; i<toggleButton.length; i++) {
            let activeElementInside = toggleButton[i].nextElementSibling
            activeElementInside.classList.remove("dropdown-menu-block");
        }
        if(activeElement.classList.contains("dropdown-menu-block") === false) {
            activeElement.classList.add("dropdown-menu-block");
        } else {
            activeElementInside.classList.remove("dropdown-menu-block");
        }     
    })
}


function task_status(task_type) {
    const response_output = JSON.parse(document.getElementById("response_output").textContent);
    var socket = new WebSocket("ws://127.0.0.1:8000/ws/collect/");

    socket.onmessage = function(event) {
        var collect = event.data;
        document.querySelector("#collect-device-status").innerText = collect;
    }

    console.log(response_output)
}

task_status()