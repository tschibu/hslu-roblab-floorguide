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
    var room = event.path[0].id;
    var txt = "Should I bring you to room " + room + "?";
    buttonDisabled(true);
    say(txt);
    //need to wait until say is done...
    setTimeout(function () { confirmRoom(room, txt); }, 2000);
}

function confirmRoom(room, txt) {
    var r = confirm(txt);
    if (r == true) {
        triggerEvent(room);
    } else {
        say("Please select another room")
        buttonDisabled(false);
    }
}

function say(text) {
    session.service('ALTextToSpeech').then(function (tts) {
        tts.say(text);
    }, function (error) {
        alert(error);
    });
}

function triggerEvent(roomNumber) {
    say("Alright! I bring you to room " + roomNumber);
    session.service('ALMemory').then(function (m) {
        m.raiseEvent("FGButtonClicked", roomNumber);
    }, function (error) {
        alert(error);
    });
}

function buttonDisabled(state) {
    $('button').prop('disabled', state);
}
