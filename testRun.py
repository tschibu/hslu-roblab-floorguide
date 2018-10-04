from pynaoqi_mate import Mate
from configuration import PepperConfiguration

config = PepperConfiguration('Amber')
pepper = Mate(config)

pepper.ALTextToSpeech.setLanguage('English')
pepper.ALAnimatedSpeech.say('hello')
lang = pepper.ALTextToSpeech.getAvailableLanguages()

pepper.ALTextToSpeech.setLanguage('German')
pepper.ALTextToSpeech.say('hallo')



