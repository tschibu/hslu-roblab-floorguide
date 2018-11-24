import sys
import time
from logger import Logger
from pynaoqi_mate import Robot
from configuration import PepperConfiguration
from roblib.datastructures import Coordinate
from planner import Planner
from movement import Movement
from tracer import Tracer

roboterName = "Amber"
initPosition = "StandZero" # StandInit, StandZero, Crouch
testCurrentPos = Coordinate(0.0, 0.0, 0)
testDestinationPos = Coordinate(2.0, 0.0, 0)

#Main entry point for the Planner & Movement Proof-of-Concept
def _main():
    #init Robot
    config = PepperConfiguration(roboterName)
    if(not config.isAvailable()):
        Logger.err("Main", "checkAvailability", "name: " + config.Name + ", ip: " + config.Ip + " not reachable!")
        sys.exit(1)

    robot = Robot(config)
    robot.ALRobotPosture.goToPosture("StandZero", 1)
    time.sleep(3)

    #create Components
    planner = Planner()
    movement = Movement(robot)
    tracer = Tracer(robot)
    tracer.start() # start tracing

    #moveCmds = planner.getMoveCommands(testCurrentPos, testDestinationPos)

    #for mcmd in moveCmds:
    #    movement.move(mcmd)

    movement.moveFromTo(testCurrentPos, testDestinationPos)

    tracer.stop()

if __name__ == "__main__":
    _main()