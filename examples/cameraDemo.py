from pynaoqi_mate import Robot
from configuration import PepperConfiguration
import qi
import time


class TakePictureExample():
    def __init__(self):
        self.config = PepperConfiguration("Porter")
        robot = Robot(self.config)
        self.camera = robot.ALPhotoCapture
        self.tts = robot.ALTextToSpeech
        self.tts.setLanguage("English")
        self.audio = robot.ALAudioPlayer

    def takePicture(self):
        remote_folder_path = "/home/nao/recordings/cameras/"
        file_name = "myPicture.jpg"
        self.tts.say("say cheese!")
        qi.async(self.audio.playFile, "/home/nao/recordings/mp3/camera_shutter.mp3")
        time.sleep(3)
        self.camera.takePicture(remote_folder_path, file_name)


pepper = TakePictureExample()
pepper.takePicture()
