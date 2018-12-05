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

#Main entry point for the Planner & Movement Proof-of-Concept
def _main():
    #init Robot
    config = PepperConfiguration(roboterName)
    if(not config.isAvailable()):
        Logger.err("Main", "checkAvailability", "name: " + config.Name + ", ip: " + config.Ip + " not reachable!")
        sys.exit(1)

    robot = Robot(config)
    #lifeService = robot.session.service("ALAutonomousLife")
    #lifeService.setAutonomousAbilityEnabled("AutonomousBlinking", False)
    #lifeService.setAutonomousAbilityEnabled("BackgroundMovement", False)
    #lifeService.setAutonomousAbilityEnabled("BasicAwareness", False)
    #lifeService.setAutonomousAbilityEnabled("ListeningMovement", False)
    #lifeService.setAutonomousAbilityEnabled("SpeakingMovement", False)
    #robot.ALRobotPosture.goToPosture(initPosition, 1)
    #time.sleep(3)

    sub = robot.ALMemory.subscriber("FGButtonClicked")
    sub.signal.connect(buttonClicked)

    sub2 = robot.ALMemory.subscriber("SBR/Test/Tablet/FastTouch")
    sub2.signal.connect(buttonClicked)

    sub3 = robot.ALMemory.subscriber("SBR/Test/Tablet/SlowTouch")
    sub3.signal.connect(buttonClicked)

    while True:
        pass

def buttonClicked(value):
    print(value)

if __name__ == "__main__":
    _main()