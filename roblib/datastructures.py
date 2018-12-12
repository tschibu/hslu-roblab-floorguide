class MoveCommand():
    def __init__(self, x, y, degrees=None, isCalibrationCmd=False, naoMarkId=0):
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
        if self.x > 0:
            return "Moving " + str(self.x) + " units."
        elif self.degrees != 0:
            return "Turning " + str(self.degrees) + " degrees."
        else:
            return ""

    def get_isCalibrationCmd(self):
        return self.isCalibrationCmd

    def getNaoMarkId(self):
        return self.naoMarkId

Coordinate = MoveCommand
