import math
from roblib.datastructures import Coordinate
from logger import Logger

class Movement():
    def __init__(self, session):
        self.session = session
        self.motion = session.ALMotion
        self.navigation = session.ALNavigation

    def move(self, moveCmd):
        return self._moveIntern(moveCmd.getX(), moveCmd.getY(), moveCmd.getDegrees())

    def moveFromTo(self, currentPos, destinationPos):
        x = destinationPos.getX() - currentPos.getX()
        y = destinationPos.getY() - currentPos.getY()
        degrees = destinationPos.getDegrees() - currentPos.getDegrees()
        return self._moveIntern(x, y, degrees)

    def _moveIntern(self, x, y, degrees):
        status = self.log(self.navigation.navigateTo(x, y), x, y, degrees)
        self.motion.moveTo(0, 0 , math.radians(-degrees))
        return status

    def log(self, value, x, y, degrees):
        if value:
            Logger.info("Movement", "navigateTo", "successful move with x: " + str(x) + " y: " + str(y) + " degrees: " + str(degrees))
        else:
            Logger.err("Movement", "navigateTo", "failed move with x: " + str(x) + " y: " + str(y) + " degrees: " + str(degrees))
        return value
