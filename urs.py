from pynaoqi_mate import Robot
from configuration import PepperConfiguration
import time

class Urs():

    def __init__(self):
        self.config = PepperConfiguration('Amber')
        robot = Robot(self.config)
        self.tts = robot.ALTextToSpeech
        self.audio = robot.ALAudioPlayer
        self.touch = robot.ALTouch
        self.tts.setLanguage('German')
        self.tts.setParameter('speed', 80)

    def annoyUrs(self):
        while (True):
            self.tts.say('Urs!')

    def playMusic(self):
        self.audio.playFile('/data/home/nao/recordings/mp3/Wartemusik.mp3')

    def reactToTouch(self):
        self.touch.getStatus()

if __name__ == '__main__':
    urs = Urs()
    while True:
        print(urs.reactToTouch())
        time.sleep(0.5)
