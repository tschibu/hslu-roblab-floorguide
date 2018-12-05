import sys
import time
from logger import Logger
from speech import Speech
from pynaoqi_mate import Robot
from configuration import PepperConfiguration
from roblib.datastructures import Coordinate
from planner import Planner
from movement import Movement
from tracer import Tracer

roboterName = "Amber"
initPosition = "StandZero" # StandInit, StandZero, Crouch
testCurrentPos = Coordinate(0.0, 0.0, 0)
testDestinationPos = Coordinate(0.0, 0.0, 180)

#Main entry point for the Planner & Movement Proof-of-Concept
def _main():
    #init Robot
    config = PepperConfiguration(roboterName)
    if(not config.isAvailable()):
        Logger.err("Main", "checkAvailability", "name: " + config.Name + ", ip: " + config.Ip + " not reachable!")
        sys.exit(1)

    robot = Robot(config)
    lifeService = robot.session.service("ALAutonomousLife")
    lifeService.setAutonomousAbilityEnabled("AutonomousBlinking", False)
    lifeService.setAutonomousAbilityEnabled("BackgroundMovement", False)
    lifeService.setAutonomousAbilityEnabled("BasicAwareness", False)
    lifeService.setAutonomousAbilityEnabled("ListeningMovement", False)
    lifeService.setAutonomousAbilityEnabled("SpeakingMovement", False)
    robot.ALRobotPosture.goToPosture(initPosition, 1)
    time.sleep(3)

    #init Speech
    Speech(robot)

    Logger.info("Main", "testError", "we got an info message")
    Logger.err("Main", "testError", "we got an error message")
    Logger.debug("Main", "testError", "we got an debug message")

if __name__ == "__main__":
    _main()