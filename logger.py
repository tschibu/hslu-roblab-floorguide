import os
import datetime
from speech import Speech

_DEBUG = True
_SPEECH = True
_FILESTREAM = open("team10_room_guide.log", "a")
_LINEENDING = os.linesep

def writeLogMsg(t, className, topic, message):
    ts = datetime.datetime.utcnow()
    txt = t + ": " + str(ts) + ", " + className + "." + topic + " -> '" + message + "'"
    print(txt)
    _FILESTREAM.write(txt+_LINEENDING)
    if _SPEECH:
        Speech.sayText(t)
        Speech.sayText(message)

class Logger():
    @staticmethod
    def setDebug(isOn):
        global _DEBUG
        _DEBUG = isOn

    @staticmethod
    def setSpeech(isOn):
        global _SPEECH
        _SPEECH = isOn

    @staticmethod
    def info(className, topic, message):
        writeLogMsg("INFO", className, topic, message)

    @staticmethod
    def err(className, topic, message):
        writeLogMsg("ERROR", className, topic, message)

    @staticmethod
    def debug(className, topic, message):
        if _DEBUG == True:
            writeLogMsg("DEBUG", className, topic, message)
