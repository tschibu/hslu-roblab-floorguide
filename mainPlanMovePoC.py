import sys
from logger import Logger
from pynaoqi_mate import Robot
from configuration import PepperConfiguration
from roblib.datastructures import Coordinate
from planner import Planner
from movement import Movement

roboterName = "Amber"
testCurrentPos = Coordinate(0, 0, 0)
testDestinationPos = Coordinate(1, 1, 90)

#Main entry point for the Planner & Movement Proof-of-Concept
def _main():
    #init Robot
    config = PepperConfiguration(roboterName)
    if(not config.isAvailable()):
        Logger.err("Main", "checkAvailability", "name: " + config.Name + ", ip: " + config.Ip + " not reachable!")
        sys.exit(1)

    robot = Robot(config)
    robot.ALRobotPosture.goToPosture("StandInit", 1)

    #create Components
    planner = Planner()
    movement = Movement(robot)

    moveCmds = planner.getMoveCommands(testCurrentPos, testDestinationPos)

    for mcmd in moveCmds:
        movement.move(mcmd)

    #movement.move(testCurrentPos, testDestinationPos)

if __name__ == "__main__":
    _main()