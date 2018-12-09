_Cognitive Robotics Lab HS2018 - Team 10_

# FloorGuide
## Aufbau Umgebung
Um die Applikation Floor Guide zu verwenden muss zuerst die Umgebung vorbereitet sein.

### Application Server
Wird mit Python entwickelt.

### Client
Um den Client zu entwickeln empfiehlt sich das Visual Studio Code.
```
xxxx
```
### Pepper Behaviour
Wird mit Choreograph entwickelt.

## Starten
### Application Server
Python Projekt starten mit dem Kommando
```
python xxxxx.py
```
### Client
xxxx

### Pepper Behaviour
xxxxx

### Important Infos
#### JavaScript libs on target
cd /opt/aldebaran/var/www/libs/

#### Webapp location on Robot
cd ~/.local/share/PackageManager/apps/roomselection_web/html

#### Markers
http://doc.aldebaran.com/2-5/naoqi/vision/allandmarkdetection.html#allandmarkdetection

### Open Todos
* Sensoren Limits heruntersetzen
* Was passiwert wenn der Kopf schräg ist und Pepper sich nicht Kalibrieren kann?
* Tür erkennen und Schlusswort sagen
* Was passiert wenn wir ein Hindernis haben auf dem Weg? / Ausgangsposition
* Was passiert wenn jemand vor Pepper steht nachdem er den Raum ausgewählt hat?
* Statemachine / Controlflow
* Tracer Auswertung
* Path Updaten
* Position Updaten


## Google Vision API
### Install package for Google Vision API
```
pip install --upgrade google-cloud-vision
pip install --upgrade pillow
```
Check if you have set de API-Access Key:
```
export GOOGLE_APPLICATION_CREDENTIALS="[PATH]"
```
The key is in the `res`-folder.



