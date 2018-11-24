function drawPosition(position) {

    var id = position['x'] + '-' + position['y'];
    var e = document.getElementById(id);
    e.className += " position";

}

function drawPath(path) {

    path.forEach(node => {
        
        var id = node['x'] + '-' + node['y'];
        var e = document.getElementById(id);
        e.className += " path";

    });

}

function updateMap() {

    console.log('function called.');

    var requestURL = 'https://picks.ciaran.ch/json/position.json';
    var request = new XMLHttpRequest();

    request.open('GET', requestURL);
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