import math

class Movement():
    def __init__(self, session):
        self.session = session
        self.motion = session.ALMotion

    def moveSquare(self, meters):
        self.motion.moveTo(meters, 0, 0)
        self.motion.moveTo(0, 0 , math.pi/2)
        self.motion.moveTo(meters, 0, 0)
        self.motion.moveTo(0, 0 , math.pi/2)
        self.motion.moveTo(meters, 0, 0)
        self.motion.moveTo(0, 0 , math.pi/2)
        self.motion.moveTo(meters, 0, 0)
        self.motion.moveTo(0, 0 , math.pi/2)
