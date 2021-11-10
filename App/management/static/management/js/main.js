window.addEventListener("scroll", function(event) {
    document.getElementById("showScroll").innerHTML = window.pageYOffset + "px";
});

function print_collected_data(data) {

    // Collect Table Body:
    let tbody = document.getElementById("logger-div-tbody");

    // Fill Body Heder:
    var logger_list = data.results;
    for(let i=0; i<logger_list.length; i++) {
        let log_values = Object.values(logger_list[i]);

        // Create TR and add to Table Body:
        let tr = document.createElement("tr");

        log_values.forEach(function(element, index, array) {
            if (index === 0) {
                var row = document.createElement("th");
                row.setAttribute("scope", "col")
            } else {
                var row = document.createElement("td");
            }
            
            row.innerText = element;
            tr.appendChild(row);
        });

        tbody.appendChild(tr);
    }

}

function collect_data(request) {
    
    fetch(request).then( resp => {
        if(!resp.ok) {
            return {}
        } else {
            return resp.json();
        }
    }).then( rest_object => {

        //console.log(rest_object.count);
        //console.log(rest_object.next);
        //console.log(rest_object.previous); ?page=2

        print_collected_data(rest_object)

    });

}

var api_request_url = 'http://127.0.0.1:8000/api/loggerdata/last'

collect_data(api_request_url)
collect_data(api_request_url)
collect_data(api_request_url)
collect_data(api_request_url)

console.log(api_request_url)