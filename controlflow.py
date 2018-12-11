import sys
import time
from logger import Logger
from pynaoqi_mate import Robot
from configuration import PepperConfiguration
from roblib.datastructures import Coordinate
from planner import Planner
from movement import Movement
from speech import Speech
#from doorChecker import DoorChecker
from positionCalibrator import PositionCalibrator
from tracer import Tracer
from sensorHandler import SensorHandler
from tabletHandler import TabletHandler

# Robot to use
_ROBOT_NAME = "Porter"
# Default Posture
_INIT_POSTURE = "StandInit" # StandInit, StandZero, Crouch
# Start Coordiante
_START_COORDINATE = Coordinate(1, 4, 360)
# Global flag which indicates that App should run
_RUN = True

class ControlFlow():
    def __init__(self):
        self.config = PepperConfiguration(_ROBOT_NAME)
        if(not self.config.isAvailable()):
            Logger.err("ControlFlow", "checkAvailability", "name: " + self.config.Name + ", ip: " + self.config.Ip + " not reachable!")
            sys.exit(1) #Abort since robot is not available...
        self.robot = Robot(self.config)
        Speech(self.robot) #Initialize Speech (static class, no reference needed)
        #DoorChecker(self.robot) #Initialize DoorChecker (static class, no reference needed)
        TabletHandler(self.robot) #Initialize TabletHandler (static class, no reference needed)
        self.sensorhandler = SensorHandler(self.robot)
        self.planner = Planner()
        self.movement = Movement(self.robot)
        self.poscalib = PositionCalibrator(self.robot)

    def init(self):
        self.robot.ALRobotPosture.goToPosture(_INIT_POSTURE, 1)
        #self.sensorhandler.write_operation_modes(1.0) #Laser and Obstacle Detection Off
        return True

    def run(self):
         #show Room Selection and register call back
        TabletHandler.startApp(TabletHandler.getRoomSelectionApp())
        sub = self.robot.ALMemory.subscriber("FGButtonClicked")
        sub.signal.connect(self.on_room_selected)

        while _RUN:
            pass

    def on_room_selected(self, value):
        TabletHandler.startApp(TabletHandler.getMapApp())
        print(value)
        coordinate = self.planner.get_coor_by_room_name(value)
        if coordinate != None:
            Logger.info("ControlFlow", "onRoomSelected", "I will bring you to the room now. Go out of my way please!")
            time.sleep(3)
            self.move_to_room(coordinate)
        else:
            Logger.err("ControlFlow", "onRoomSelected", "could not find specified room - abort behavior")
            self.init()

    def move_to_room(self, coordinate):
        end_coordinate = self.move_to_location(_START_COORDINATE, coordinate)

        #self.announce_destination()
        self.go_to_start_coordinate(end_coordinate)

    def move_to_location(self, start_coordinate, end_coordinate):
        moveCmds = self.planner.getMoveCommands(start_coordinate, end_coordinate)
        Logger.info("ControlFlow", "moveToLocation", "I have %d movements to do." % len(moveCmds))

        for cmd in moveCmds:
            Logger.info("ControlFlow", "moveToLocation", "Execute move command with " + cmd.getText() + " units ")
            if cmd.get_isCalibrationCmd():
                if not self.movement.move(cmd):
                    Logger.err("ControlFlow", "moveToLocation", "Could not move to the given Position. Is something in my way?")
                self.robot.ALRobotPosture.goToPosture(_INIT_POSTURE, 1)
                self.poscalib.calibratePosition(cmd.getNaoMarkId())
            else:
                if not self.movement.move(cmd):
                    Logger.err("ControlFlow", "moveToLocation", "Could not move to the given Position. Is something in my way?")

        return end_coordinate #TODO return real end position!

    def announce_destination(self, door_name):
        #DoorChecker.check_door(door_name)
        Logger.info("ControlFlow", "announceDestination", "I found the correct room, it's directly in front of me")
        time.sleep(5)

    def go_to_start_coordinate(self, end_coordinate):
        Logger.info("ControlFlow", "goToStartCoordinate", "Moving back to my initial position")
        self.move_to_location(end_coordinate, _START_COORDINATE)
        global _RUN
        _RUN = False
        TabletHandler.startApp(TabletHandler.getRoomSelectionApp())

#Main entry point for the Floor Guide
def _main():
    cf = ControlFlow()
    if cf.init() == True:
        cf.run()

if __name__ == "__main__":
    _main()