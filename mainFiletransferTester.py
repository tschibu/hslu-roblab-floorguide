import sys
import time
from logger import Logger
from pynaoqi_mate import Robot
from configuration import PepperConfiguration
from roblib.datastructures import Coordinate
from planner import Planner
from movement import Movement
from positionCalibrator import PositionCalibrator
from tracer import Tracer
from filetransfer import Filetransfer
from doorChecker import DoorChecker
from speech import Speech
import os

roboterName = "Amber"
initPosition = "StandZero" # StandInit, StandZero, Crouch

#Main entry point for the Planner & Movement Proof-of-Concept
def _main():
    # init Robot
    config = PepperConfiguration(roboterName)
    if(not config.isAvailable()):
        Logger.err("Main", "checkAvailability", "name: " + config.Name + ", ip: " + config.Ip + " not reachable!")
        sys.exit(1)

    robot = Robot(config)

    robot.ALRobotPosture.goToPosture(initPosition, 1)
    time.sleep(3)

    ft = Filetransfer(config, robot)
    ft.transfer_file_from_pepper_to_local("/home/nao/recordings/cameras/test_jmm_1.jpg", "/tmp/test.jpg")
    os.rename("/tmp/test.jpg", "/tmp/test_ready2upload.jpg")
    ft.transfer_file_from_local_to_pepper("/tmp/test_ready2upload.jpg","/home/nao/recordings/cameras/test_NEUNEU.jpg")

if __name__ == "__main__":
    _main()