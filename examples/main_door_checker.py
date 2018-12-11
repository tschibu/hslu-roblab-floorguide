from configuration import PepperConfiguration
from pynaoqi_mate import Robot
from doorChecker import DoorChecker
from logger import Logger
from filetransfer import Filetransfer
from speech import Speech
import sys

roboterName = "Porter"
initPosition = "StandZero" # StandInit, StandZero, Crouch

#Main entry point for the Planner & Movement Proof-of-Concept
def _main():
    #init Robot
    config = PepperConfiguration(roboterName)
    if(not config.isAvailable()):
        Logger.err("Main", "checkAvailability", "name: " + config.Name + ", ip: " + config.Ip + " not reachable!")
        sys.exit(1)

    robot = Robot(config)
    Speech(robot)
    Filetransfer(config)

    # init Door Checker
    DoorChecker(robot)
    robot.ALRobotPosture.goToPosture("StandInit", 1)
    DoorChecker.check_door("303")

    # Test
    #robot.ALPhotoCapture.

if __name__ == "__main__":
    _main()