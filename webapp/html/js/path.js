function drawPosition(position) {

    // get rid of position classes 
    let positionElements = Array.from(document.querySelectorAll('.position'));
    positionElements.forEach(e =>{
        e.className = "floor";
    });

    // add new position class to element
    var id = position['x'] + '-' + position['y'];
    var deg = position['deg'];
    var e = document.getElementById(id);
    e.className += " position";
    e.className += " deg-" + deg;

}

function drawPath(path) {

    // get rid of path classes
    let pathElements = Array.from(document.querySelectorAll('.path'));
    pathElements.forEach(e => {
        e.classList.remove("path");
    });

    path.forEach(node => {        
        var id = node['x'] + '-' + node['y'];
        var e = document.getElementById(id);
        e.className += " path";
    });

}

function updateMap() {

    var requestURL = 'https://picks.ciaran.ch/json/position.json';
    var request = new XMLHttpRequest();

    request.open('GET', requestURL+ ((/\?/).test(requestURL) ? "&" : "?") + (new Date()).getTime());
    request.responseType = 'json';
    request.send();

    request.onload = function () {

        var jsonObj = request.response;
    
        var position = jsonObj['position'];
        var path = jsonObj['path'];
    
        drawPosition(position);
        drawPath(path);

    } 

}