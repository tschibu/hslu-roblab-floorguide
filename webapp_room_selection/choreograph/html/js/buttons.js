var session; //Store session of pepper
try {
    QiSession(function (s) {
        session = s;
        alert("QiSession connected!");
    }, function () {
        alert("QiSession connection Failed!");
    });
} catch (err) {
    alert("QiSession not Found! Error: " + err);
}

var requestURL = 'json/map.json';
var request = new XMLHttpRequest();

request.open('GET', requestURL);
request.responseType = 'json';
request.send();

request.onload = function () {
    var data = request.response;
    drawButtons(data);
}

function isEmpty(obj) {
    for (var prop in obj) {
        if (obj.hasOwnProperty(prop)) { return false; }
    }
    return JSON.stringify(obj) === JSON.stringify({});
}

function drawButtons(data) {
    var count = 0;
    var maxPerRow = 4;

    roomNodes = data.nodes.filter(function (n) { return !isEmpty(n.room); });

    selection = document.getElementById("selection");
    var table = document.createElement('table');
    table.setAttribute('id', 'buttons');
    var row = document.createElement('tr');
    for (var i = 0; i < roomNodes.length; i++ , count++) {
        if (count >= maxPerRow) {
            //new row
            table.appendChild(row);
            row = document.createElement('tr');
            count = 0;
        }
        var el = document.createElement('td');
        var button = document.createElement('button');
        button.innerHTML = roomNodes[i].room.name;
        button.setAttribute("id", roomNodes[i].room.name);
        button.onclick = onButtonClick;
        el.appendChild(button);
        row.appendChild(el);
    }
    table.appendChild(row);
    selection.appendChild(table);
}

function onButtonClick(event) {
    alert("you pressed on: " + event.path[0].id);

    triggerEvent(event.path[0].id);
}

function triggerEvent(roomNumber) {
    session.service('ALTextToSpeech').then(function (tts) {
        var txt = 'Hey Roblab Looser! I bring you to Room ' + roomNumber;
        alert(txt);
        tts.say(txt);
        //tts.say(txt);
    }, function (error) {
        alert(error);
    })
}
