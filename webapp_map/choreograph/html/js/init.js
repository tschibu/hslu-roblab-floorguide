var requestURL = 'json/map.json';
var request = new XMLHttpRequest();

request.open('GET', requestURL);
request.responseType = 'json';
request.send();

request.onload = function() {
  var initMap = request.response;
  drawMap(initMap);
}

function drawGrid(x, y) {

  var t = '<table cellspacing="0" border="1" cellpadding="0" class="grid">';

  for (var i = 0; i < y; i++) {

    t += '<tr>';

    for (var j = 0; j < x; j++) {

      t += '<td id="' + j + '-' + i + '">';

    }

    t += '</tr>';

  }

  t += '</table>';

  return t;
}

function drawNodes(nodes) {

  nodes.forEach(function(element) {

    var id = element['x'] + '-' + element['y'];
    var e = document.getElementById(id);
    e.className = "floor";

    var room = element['room'];

    if (!jQuery.isEmptyObject(room)) {

      e.textContent += room['name'].substring(0, 3);
      e.className += " room";

    }

  });

}

function drawMap(initMap) {

  var x = initMap['square']['x'];
  var y = initMap['square']['y'];

  var nodes = initMap['nodes'];

  $("#map-canvas").html(drawGrid(x, y));

  drawNodes(nodes);
  window.setInterval(calcPath, 2000);

}
