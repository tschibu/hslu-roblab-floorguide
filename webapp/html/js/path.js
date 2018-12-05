function drawPosition(position) {

    // get rid of position classes
    var positionElements = Array.from(document.querySelectorAll('.position'));
    positionElements.forEach(function (e) {
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
    var pathElements = Array.from(document.querySelectorAll('.path'));
    pathElements.forEach(function (e) {
        e.classList.remove("path");
    });

    path.forEach(function (node) {        
        var id = node['x'] + '-' + node['y'];
        var e = document.getElementById(id);
        e.className += " path";
    });

}

function updateMap() {

    var requestURL = '/json/position.json';
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