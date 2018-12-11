function drawPosition(position) {

    // get rid of position classes
    var positionElements = Array.from(document.querySelectorAll('.position'));
    positionElements.forEach(function (e) {
        e.classList.remove("position");
    });

    // add new position class to element
    var id = position['x'] + '-' + position['y'];
    var deg = position['deg'];
    var e = document.getElementById(id);
    e.className += " position";
    e.className += " deg-" + deg;

}

function updatePosition() {

    var requestURL = 'json/position.json';
    var request = new XMLHttpRequest();

    request.open('GET', requestURL+ ((/\?/).test(requestURL) ? "&" : "?") + (new Date()).getTime());
    request.responseType = 'json';
    request.send();

    request.onload = function () {

        var jsonObj = request.response;
        var position = jsonObj['position'];

        drawPosition(position);
    }

}
