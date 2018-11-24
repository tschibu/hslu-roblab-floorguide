import math
from roblib.datastructures import Coordinate
from logger import Logger

class Movement():
    def __init__(self, session):
        self.session = session
        self.motion = session.ALMotion
        self.navigation = session.ALNavigation

    def move(currentPos, destinationPos):
        x = destinationPos.getX() - currentPos.getX()
        y = destinationPos.getY() - currentPos.getY()
        degrees = destinationPos.getDegrees() - currentPos.getDegrees()
        return log(self.motion.navigateTo(x, y), x, y, degrees)

    def log(self, value, x, y, degrees):
        if value:
            Logger.info("Movement", "navigateTo", "successful move with x: " + str(x) + " y: " + str(y) + " degrees: " + str(degrees))
        else:
            Logger.err("Movement", "navigateTo", "failed move with x: " + str(x) + " y: " + str(y) + " degrees: " + str(degrees))
        return value
