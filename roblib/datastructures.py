class MoveCommand():
    def __init__(self, x, y, degrees, isCalibrationCmd=False, naoMarkId=0):
        self.x = x
        self.y = y
        self.degrees = degrees
        self.isCalibrationCmd = isCalibrationCmd
        self.naoMarkId = naoMarkId

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def getDegrees(self):
        return self.degrees

    def getText(self):
        return str(self.x)

    def get_isCalibrationCmd(self):
        return self.isCalibrationCmd

    def getNaoMarkId(self):
        return self.naoMarkId

Coordinate = MoveCommand
