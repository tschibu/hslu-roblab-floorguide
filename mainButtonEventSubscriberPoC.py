import sys
import time
from logger import Logger
from speech import Speech
from pynaoqi_mate import Robot
from configuration import PepperConfiguration
from tabletHandler import TabletHandler

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
    TabletHandler(robot)

    #start RoomSelection Webapp
    TabletHandler.startApp(TabletHandler.getRoomSelectionApp())

    #register for events of RoomSelection Webapp
    sub = robot.ALMemory.subscriber("FGButtonClicked")
    sub.signal.connect(buttonClicked)

    while True:
        pass

def buttonClicked(value):
    print("ButtonClicked: " + value)
    TabletHandler.startApp(TabletHandler.getMapApp())

if __name__ == "__main__":
    _main()
