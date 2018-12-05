import math
from roblib.datastructures import Coordinate
from logger import Logger

FACTOR = 0.6

class Movement():
    def __init__(self, session):
        self.session = session
        self.motion = session.ALMotion
        self.navigation = session.ALNavigation
        self.memory = session.ALMemory
        self.subscriberOnMoveFailed = self.memory.subscriber("MoveFailed")
        self.subscriberOnMoveFailed.signal.connect(self.onMoveFailed)

    def onMoveFailed(eventName, value, subscriberIdentifier):
        Logger.err("Movement", "onMoveFailed", "eventName: " + eventName + ", value: " + value + ", subscriberIdentifier: " + subscriberIdentifier)

    def move(self, moveCmd):
        return self._moveIntern(moveCmd.getX(), moveCmd.getY(), moveCmd.getDegrees())

    def moveFromTo(self, currentPos, destinationPos):
        x = destinationPos.getX() - currentPos.getX()
        y = destinationPos.getY() - currentPos.getY()
        degrees = destinationPos.getDegrees() - currentPos.getDegrees()
        return self._moveIntern(x, y, degrees)

    def _moveIntern(self, x, y, degrees):
        status = True
        if x != 0 or y != 0:
            status = self.log(self.navigation.navigateTo(x*FACTOR, y*FACTOR), x*FACTOR, y*FACTOR, degrees)
        if degrees != 0:
            self.motion.moveTo(0, 0 , math.radians(-degrees))
        return status

    def log(self, value, x, y, degrees):
        if value:
            Logger.info("Movement", "navigateTo", "successful move with x: " + str(x) + " y: " + str(y) + " degrees: " + str(degrees))
        else:
            Logger.err("Movement", "navigateTo", "failed move with x: " + str(x) + " y: " + str(y) + " degrees: " + str(degrees))
        return value
