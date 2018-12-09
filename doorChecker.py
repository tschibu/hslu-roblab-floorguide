import io
import os
from google.cloud import vision_v1p3beta1 as vision
import time

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
            _DOOR_CHECKER.takePicture(_PEPPER_PATH, _FILENAME)
            os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "../res/Pepper-4fd1ecb47687.json"

            # Google Vision API
            client = vision.ImageAnnotatorClient()

            time.sleep(2)
            with io.open(_PEPPER_PATH + "/" + _FILENAME, 'rb') as image_file:
                content = image_file.read()

            image = vision.types.Image(content=content)

            # Language hint codes for handwritten OCR:
            # en-t-i0-handwrit, mul-Latn-t-i0-handwrit
            # Note: Use only one language hint code per request for handwritten OCR.
            image_context = vision.types.ImageContext(language_hints=['en-t-i0-handwrit'])

            response = client.document_text_detection(image=image,image_context=image_context)

            print(response.full_text_annotation.text.strip())
            return True
        return False