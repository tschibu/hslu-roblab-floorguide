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

function calcPath() {

    var requestURL = 'json/path.json';
    var request = new XMLHttpRequest();

    request.open('GET', requestURL+ ((/\?/).test(requestURL) ? "&" : "?") + (new Date()).getTime());
    request.responseType = 'json';
    request.send();

    request.onload = function () {

        var jsonObj = request.response;
        var path = jsonObj['path'];

        drawPath(path);

    }

}
