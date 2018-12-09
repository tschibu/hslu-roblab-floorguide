import os
import datetime
import qi
from movement import Movement
from logger import Logger
import time

class PositionCalibrator():
    def __init__(self, session):
        self.session = session
        self.landMarkDetection = session.ALLandMarkDetection
        self.memory = session.ALMemory
        self.movement = Movement(session)

    def checkForLM(self, id=None):
        landMark = self._getLandMark()
        return landMark and (id == None or id == landMark[1][0])

    def calibratePosition(self, id=None):
        for i in range(3):
            Logger.info("PositionCalibrator", "calibratePosition", "Looking for landmark")
            landMark = self._getLandMark()
            if landMark == None or (id != None and landMark[1][0] != id):
                Logger.info("PositionCalibrator", "calibratePosition", "Landmark not found")
                return False
            markShapeInfo = landMark[0]
            y = markShapeInfo[1]
            size = markShapeInfo[3]
            # size wanted: 0.131
            x = (0.131 - size) * 15
            if abs(y) < 0.1 and abs(x) < 0.1:
                Logger.info("PositionCalibrator", "calibratePosition", "Calibration complete")
                break
            Logger.info("PositionCalibrator", "calibratePosition", "Calibrating position")
            self.movement.moveCalibrate(x, y)
            landMark = self._getLandMark()
            y = markShapeInfo[1]
            size = markShapeInfo[3]
        return True

    def _getLandMark(self):
        #Logger.info("PositionCalibrator", "checkForLM", "Looking for Landmark")
        memValue = "LandmarkDetected"
        self.landMarkDetection.subscribe("Test_Landmark", 500, 0.0)
        for i in range(5):
            time.sleep(1.0)
            val = (self.memory).getData(memValue)
            if (val and isinstance(val, list) and len(val) >= 2):
                return val[1][0] # markInfo
        return None