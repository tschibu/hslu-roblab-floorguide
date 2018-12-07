class MoveCommand():
    def __init__(self, x, y, degrees, naoMarkDegree=None):
        self.x = x
        self.y = y
        self.degrees = degrees
        self.naoMarkDegree = naoMarkDegree

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def getDegrees(self):
        return self.degrees

    def getText(self):
        return str(self.x)

    def getNaoMarkDegree(self):
        return self.naoMarkDegree

Coordinate = MoveCommand
