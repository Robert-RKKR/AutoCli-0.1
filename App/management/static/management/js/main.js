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

// 
fetch('http://127.0.0.1:8000/api/device/all').then( resp => {
    if(!resp.ok) {
        return {}
    } else {
        return resp.json();
    }
}).then( obj => {
    console.log(obj)
});

function collectDeviceSshData(device_id) {
    fetch('http://127.0.0.1:8000/api/device/ssh/'+device_id).then( resp => {
        if(!resp.ok) {
            return {}
        } else {
            return resp.json();
        }
    }).then( obj => {
        console.log(obj)
    });
}

var moreButtons = document.getElementsByClassName("more-button");

for(let i=0; i<moreButtons.length; i++) {
    let moreButton = moreButtons[i]

    moreButton.addEventListener("click", function(event) {
        collectDeviceSshData(moreButton.id)
    });
}


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
    });
}

task_status()



function apiListTasks() {
    return fetch('http://127.0.0.1:8000/api/device/all').then(
        function(resp) {
            if(!resp.ok) {
                alert('Wystąpił błąd! Otwórz devtools i zakładkę Sieć/Network, i poszukaj przyczyny');
            }
            return resp.json();
        }
    )
}
  
apiListTasks().then(
    function(response) {
        console.log('Odpowiedź z serwera to:', response);
    }
);
  


function task_status(task_type) {
    const response_output = JSON.parse(document.getElementById("response_output").textContent);
    var socket = new WebSocket("ws://127.0.0.1:8000/ws/collect/");

    socket.onmessage = function(event) {
        var collect = event.data;
        document.querySelector("#collect-device-status").innerText = collect;
    }

    console.log(response_output)
}