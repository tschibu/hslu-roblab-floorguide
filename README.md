_Cognitive Robotics Lab HS2018 - Team 10_

# FloorGuide

## Frameworks
### pynaoqi_mate
Der Code basiert auf das pynaoqi_mate-Framework
https://github.com/uts-magic-lab/pynaoqi_mate
und wurde auf die Pepper Roboer `amber` und `porter` der HSLU optimiert.

### Google Vision API
#### Install package for Google Vision API
```
pip install --upgrade google-cloud-vision
pip install --upgrade pillow
```
Check if you have set de API-Access Key:
```
export GOOGLE_APPLICATION_CREDENTIALS="[PATH]"
```
The key is in the `res`-folder.

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
- [ ] Prio01 : Sensoren Limits heruntersetzen
- [ ] Prio02 : Was passiwert wenn der Kopf schräg ist und Pepper sich nicht Kalibrieren kann?
- [ ] Prio03 : Tür erkennen aus Bild ausschneiden
- [ ] Prio04 : Was passiert wenn wir ein Hindernis haben auf dem Weg? / Ausgangsposition
- [ ] Prio05 : Was passiert wenn jemand vor Pepper steht nachdem er den Raum ausgewählt hat? (Lösung: Kopfsensor betätigen, wenn man dahinter steht.)
- [ ] Prio06 : Statemachine / Controlflow
- [ ] Prio08 : Tracer Auswertung
- [ ] Prio09 : Path Updaten
- [ ] Prio10 : Position Updaten


#  Naming Conventions
Type | Conventions 
--- | --- 
Packages | `lower_case_with_underscores`|
Modules | `lower_case_with_underscores`
Classes | `CapitalizedWords`
Exceptions | `CapitalizedWords` 
Functions | `lower_case_with_underscores()`
Constants | `_UPPERCASE`
Local Variables | `lower_case_with_underscores`


