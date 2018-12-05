import sys
import time
from logger import Logger
from pynaoqi_mate import Robot
from configuration import PepperConfiguration
from roblib.datastructures import Coordinate
from planner import Planner
from movement import Movement
from roblib.map import Map
from tracer import Tracer

roboterName = "Amber"
initPosition = "StandZero" # StandInit, StandZero, Crouch
current_pos = Coordinate(27, 19, 270)
destination_pos = Coordinate(33, 1, 90)

#Main entry point for the Planner & Movement Proof-of-Concept
def _main():
    #init Robot
    config = PepperConfiguration(roboterName)
    if(not config.isAvailable()):
        Logger.err("Main", "checkAvailability", "name: " + config.Name + ", ip: " + config.Ip + " not reachable!")
        sys.exit(1)

    robot = Robot(config)
    robot.ALRobotPosture.goToPosture(initPosition, 1)
    time.sleep(3)

    #create Components
    planner = Planner()
    movement = Movement(robot)
    map = Map()
    map.load_json()

    moveCmds = planner.getMoveCommands(map, current_pos, destination_pos)

    for mcmd in moveCmds:
        print("INFO: move!")
        #movement.move(mcmd)

    #movement.moveFromTo(current_pos, destination_pos)

if __name__ == "__main__":
    _main()