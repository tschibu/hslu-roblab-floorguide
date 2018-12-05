_SPEECH = None

class Speech():
    def __init__(self, session):
        global _SPEECH
        self.session = session
        self.speech = session.ALTextToSpeech
        _SPEECH = self.speech

    @staticmethod
    def sayText(text):
        global _SPEECH
        if _SPEECH:
            _SPEECH.say(text)
