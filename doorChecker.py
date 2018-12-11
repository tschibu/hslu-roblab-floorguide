import io
import os
from google.cloud import vision_v1p3beta1 as vision
from logger import Logger
import time
import datetime

_DOOR_CHECKER = None
_PEPPER_PATH = "/home/nao/recordings/cameras"
_FILENAME = "DoorChecker.jpg"

class DoorChecker():
    def __init__(self, session):
        global _DOOR_CHECKER
        self.session = session
        self.camera = session.ALPhotoCapture
        _DOOR_CHECKER = self.camera

    @staticmethod
    def check_door(door_name):
        global _DOOR_CHECKER
        if _DOOR_CHECKER:
            try:
                # Set image attribute
                _DOOR_CHECKER.setResolution(0) # Image of 160*120px
                _DOOR_CHECKER.setPictureFormat("jpg")

                # Save top picture
                _DOOR_CHECKER.setCameraID(0) # Top camera
                _DOOR_CHECKER.takePicture2(_PEPPER_PATH, _FILENAME, True)
            except Exception, e:
                Logger.err("doorChecker.py", "check_door", "Photocapture exeption " + str(e))
            os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "../res/Pepper-4fd1ecb47687.json"

            # Google Vision API
            client = vision.ImageAnnotatorClient()

            with io.open(_PEPPER_PATH + "/" + _FILENAME, 'rb') as image_file:
                content = image_file.read()

            image = vision.types.Image(content=content)

            # Language hint codes for handwritten OCR:
            # en-t-i0-handwrit, mul-Latn-t-i0-handwrit
            # Note: Use only one language hint code per request for handwritten OCR.
            image_context = vision.types.ImageContext(language_hints=['en-t-i0-handwrit'])

            response = client.document_text_detection(image=image, image_context=image_context)
            google_api_text_response = response.full_text_annotation.text.strip()

            response_to_check = "".join(google_api_text_response.split())
            if door_name in response_to_check:
                # trying to split room name from response
                speech_room_name = google_api_text_response.replace(door_name, "").replace("\n", "").strip()
                if not speech_room_name:
                    Logger.info("doorChecker.py", "check_door", "Here is your requested room " + door_name + " " + speech_room_name)

            #Houskeeping FS
            os.remove(_PEPPER_PATH + "/" + _FILENAME)
            return True
        else:
            return False