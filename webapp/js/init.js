var requestURL = 'https://picks.ciaran.ch/json/map.json';
var request = new XMLHttpRequest();

request.open('GET', requestURL);
request.responseType = 'json';
request.send();

request.onload = function () {
    var initMap = request.response;
    drawMap(initMap);
}

// function calcPath(jsonPath) {

//     var pathArr = new Array(jsonPath.length);

//     for (var i = 0; i < jsonPath.length; i++) {

//         pathArr[i] = (jsonPath[i]['x'] + ((jsonPath[i]['y'] - 1) * 15));

//     }

//     return pathArr;
// }

function calcNodes(nodesObj, x) {

    var nodesArr = new Array(nodesObj.length);
    console.log(nodesObj);

    for (var i = 0; i < nodesObj.length; i++) {

        nodesArr[i] = (nodesObj[i]['x'] + ((nodesObj[i]['y']) * x + 1));

    }

    return nodesArr;
}

function drawMap(initMap) {

    const x = initMap['square']['x'];
    const y = initMap['square']['y'];

    var nodesObj = initMap['nodes'];
    const nodes = calcNodes(nodesObj, x);

    var t = '<table cellspacing="0" border="1" cellpadding="0" class="grid"><tr>';

    for (var i = 1; i <= (x * y); i++) {

        if (nodes.includes(i)) {

            t += '<td id="field-' + i + '" class="floor">';

        } else {

            t += '<td id="field-' + i + '"></td>';

        }

        if (i != (x * y)) {

            t += ((i % x === 0) ? '</tr><tr>' : '');

        } else {

            t += '</tr>';

        }
    }

    t += '</table>';

    $("#map-canvas").html(t);

}