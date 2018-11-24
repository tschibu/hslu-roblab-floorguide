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

function drawMap(initMap) {

    const x = initMap['square']['x'];
    console.log(x);
    const y = initMap['square']['y'];
    console.log(y);
    const nodes = initMap['nodes'];
    console.log(nodes);

    // var floor = [1, 2, 16, 17, 31, 32, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 
    //             58, 59, 60, 61, 69, 70, 75, 76, 84, 85, 90, 91, 99, 100, 105, 106, 114, 
    //             115, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 
    //             133, 134, 135, 149, 150, 164, 165, 179, 180];

    // var rooms = [51, 52, 58, 59, 60, 61, 121, 122, 126, 127, 133, 135];


    var t = '<table cellspacing="0" border="1" cellpadding="0" class="grid"><tr>';

    for (var i = 0; i <= (x * y); i++) {

        t += '<td id="field-' + i + '"></td>';

        if (i != (x * y)) {

            t += ((i % (x - 1) === 0 && i != 0) ? '</tr><tr>' : '');

        } else {

            t += '</tr>';

        }

    }

    t += '</table>';

    $("#map-canvas").html(t);

}