var requestURL = 'https://picks.ciaran.ch/json/j.json';
var request = new XMLHttpRequest();

request.open('GET', requestURL);
request.responseType = 'json';
request.send();

request.onload = function() {
    var jsonObj = request.response;
    drawGrid(jsonObj);
}

function calcPath(jsonPath) {

    var pathArr = new Array(jsonPath.length);

    for (var i = 0; i < jsonPath.length; i++) {

        pathArr[i] = (jsonPath[i]['x'] + ((jsonPath[i]['y'] - 1) * 15));

    }

    return pathArr;
}

function drawGrid(jsonObj) {

    var jsonPath = jsonObj['path'];
    var jsonPosition = jsonObj['position'];

    var position = jsonPosition['x'] + ((jsonPosition['y'] - 1) * 15);
    var path = calcPath(jsonPath);
    console.log(path);

    var floor = [1, 2, 16, 17, 31, 32, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 
                58, 59, 60, 61, 69, 70, 75, 76, 84, 85, 90, 91, 99, 100, 105, 106, 114, 
                115, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 
                133, 134, 135, 149, 150, 164, 165, 179, 180];

    var rooms = [51, 52, 58, 59, 60, 61, 121, 122, 126, 127, 133, 135];

    var x = 15;
    var y = 12;

    var t = '<table cellspacing="0" border="1" cellpadding="0" class="grid">';

    for (var i = 1; i <= (x * y); i++) {

        t += (i == 1 ? '<tr>' : '');

        if (floor.includes(i)) {

            if (i == position) {

                t += '<td id="field-' + i + '" class="floor position">'
                
            } else if (path.includes(i)) {

                t += '<td id="field-' + i + '" class="floor path">'
                
            } else {
                t += '<td id="field-' + i + '" class="floor">'
            }

                if (rooms.includes(i)) {      

                    switch(i) {

                        case 51:
                            t += '307';
                            break;
                        case 52:
                            t += '308';
                            break;
                        case 58:
                            t += '309';
                            break;
                        case 59:
                            t += '310';
                            break;
                        case 60:
                            t += '311';
                            break;
                        case 61:
                            t += '305';
                            break;
                        case 121:
                            t += '304';
                            break;
                        case 122:
                            t += '303';
                            break;
                        case 126:
                            t += '302';
                            break;
                        case 127:
                            t += '301';
                            break;
                        case 133:
                            t += '301';
                            break;
                        case 135:
                            t += '312';
                            break;
                        default:
                            t += '';
                    }

                t += '</td>';

            } else {
                t += '</td>';
            }
            

        } else {

            t += '<td id="field-' + i + '"></td>';

        }

        

        if (i != (x * y)) {

            t += (i % 15 === 0 ? '</tr><tr>' : '');

        } else {

            t += '</tr>';

        }

    }

    t += '</table>';

    $("#map-canvas").html(t);

}