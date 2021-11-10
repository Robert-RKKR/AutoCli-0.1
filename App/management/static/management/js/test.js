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



window.addEventListener("scroll", function(event) {
    document.getElementById("showScroll").innerHTML = window.pageYOffset + "px";
});

// 

fetch('http://127.0.0.1:8000/api/loggerdata/last').then( resp => {
    if(!resp.ok) {
        return {}
    } else {
        return resp.json();
    }
}).then( rest_object => {
    
    var logger_div = document.getElementById("logger-div");
    var logger_list = rest_object.results;
    var logger_previous = rest_object.previous;
    var logger_next = rest_object.next;
    var logger_count = rest_object.count;

    for(let i=0; i<logger_list.length; i++) {
        let log = logger_list[i];
        
        let main_div = document.createElement('div');
        let log_id = document.createElement('h4');
        log_id.innerText = log.id;

        main_div.appendChild(log_id)

        logger_div.appendChild(main_div)
    };

});

var logger_div = document.getElementById("page-content-wrapper");
console.log(logger_div.scrollHeight)
var top = logger_div.scrollTop;
var bottom = logger_div.scrollHeight;

window.addEventListener("scroll", () => {

    console.log(logger_div.offsetHeight)
    console.log(logger_div.scrollTop)
    console.log(logger_div.scrollHeight)

    var offset = element.getBoundingClientRect().top - element.offsetParent.getBoundingClientRect().top;
    const top = window.pageYOffset + window.innerHeight - offset;

    if (top === element.scrollHeight) {
        console.log("bottom");
    }
}, { passive: false });

function scrolled(e) {
    if (logger_div.offsetHeight + logger_div.scrollTop >= logger_div.scrollHeight) {
        scrolledToBottom(e);
    }
}




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

function apiListTasks() {
    return fetch('http://127.0.0.1:8000/api/device/all').then(
        function(resp) {
            if(!resp.ok) {
                return {};
            }
            return resp.json();
        }
    )
}
  
apiListTasks().then(
    function(response) {
        console.log('Servers response:', response);
    }
);
  


function task_status(task_type) {
    const response_output = JSON.parse(document.getElementById("response_output").textContent);
    var socket = new WebSocket("ws://127.0.0.1:8000/ws/collect/");

    socket.onmessage = function(event) {
        var collect = event.data;
        console.log(collect)
        document.querySelector("#collect-device-status").innerText = collect;
    }

    console.log(response_output)
}

task_status()


