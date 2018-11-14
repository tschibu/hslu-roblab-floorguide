import math

class Movement():
    def __init__(self, session):
        self.session = session
        self.motion = session.ALMotion
        self.navigation = session.ALNavigation

    def log(self, text, value):
        if value:
            print("Successful: " + str(text))
        else:
            print("Failed: " + str(text))

    def moveSquare(self, meters):
        self.log("Move Straight", self.motion.moveTo(meters, 0, 0))
        self.log("Turn Left", self.motion.moveTo(0, 0 , math.pi/2))
        self.log("Move Straight", self.motion.moveTo(meters, 0, 0))
        self.log("Turn Left", self.motion.moveTo(0, 0 , math.pi/2))
        self.log("Move Straight", self.motion.moveTo(meters, 0, 0))
        self.log("Turn Left", self.motion.moveTo(0, 0 , math.pi/2))
        self.log("Move Straight", self.motion.moveTo(meters, 0, 0))
        self.log("Turn Left", self.motion.moveTo(0, 0 , math.pi/2))

    def moveSquare2(self, meters):
        self.log("Move Straight", self.navigation.navigateTo(meters, 0))
        self.log("Turn Left", self.motion.moveTo(0, 0 , math.pi))
        self.log("Move Straight", self.navigation.navigateTo(meters, 0))
        self.log("Turn Left", self.motion.moveTo(0, 0 , math.pi))
        self.log("Move Straight", self.navigation.navigateTo(meters, 0))
        self.log("Turn Left", self.motion.moveTo(0, 0 , math.pi))
        self.log("Move Straight", self.navigation.navigateTo(meters, 0))
        self.log("Turn Left", self.motion.moveTo(0, 0 , math.pi))
