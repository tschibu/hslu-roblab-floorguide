import sys
import time
from logger import Logger
from pynaoqi_mate import Robot
from configuration import PepperConfiguration
from roblib.datastructures import Coordinate
from planner import Planner
from movement import Movement
from speech import Speech
from doorChecker import DoorChecker
from positionCalibrator import PositionCalibrator
from tracer import Tracer
from sensorHandler import SensorHandler
from tabletHandler import TabletHandler

# Robot to use
_ROBOT_NAME = "Amber"
# Default Posture
_INIT_POSTURE = "StandZero" # StandInit, StandZero, Crouch
# Start Coordiante
_START_COORDINATE = Coordinate(8, 2, 270)

class ControlFlow():
    def __init__(self):
        self.config = PepperConfiguration(_ROBOT_NAME)
        if(not self.config.isAvailable()):
            Logger.err("ControlFlow", "checkAvailability", "name: " + self.config.Name + ", ip: " + self.config.Ip + " not reachable!")
            sys.exit(1) #Abort since robot is not available...
        self.robot = Robot(self.config)
        Speech(self.robot) #Initialize Speech (static class, no reference needed)
        DoorChecker(self.robot) #Initialize DoorChecker (static class, no reference needed)
        TabletHandler(self.robot) #Initialize TabletHandler (static class, no reference needed)
        self.sensorhandler = SensorHandler()
        self.planner = Planner()
        self.movement = Movement(self.robot)
        self.poscalib = PositionCalibrator()

    def init(self):
        self.robot.ALRobotPosture.goToPosture(_INIT_POSTURE, 1)
        self.sensorhandler.write_operation_modes(0.0) #Laser and Obstacle Detection Off
        return True

    def run(self):
         #show Room Selection and register call back
        TabletHandler.startApp(TabletHandler.getRoomSelectionApp())
        sub = self.robot.ALMemory.subscriber("FGButtonClicked")
        sub.signal.connect(self.on_room_selected)

    def on_room_selected(self, value):
        TabletHandler.startApp(TabletHandler.getMapApp())
        coordinate = self.planner.get_coor_by_room_name(value)
        if coordinate != None:
            self.move_to_room(coordinate)
        else:
            Logger.err("ControlFlow", "onRoomSelected", "could not find specified room - abort behavior")
            self.init()

    def move_to_room(self, coordinate):
        moveCmds = self.planner.getMoveCommands(_START_COORDINATE, coordinate)
        Logger.info("ControlFlow", "bringToRoom", "I have %d movements to do." % len(moveCmds))

        for cmd in moveCmds:
            Logger.info("ControlFlow", "bringToRoom", "Execute move command with " + cmd.getText() + " units ")
            if cmd.get_isCalibrationCmd() == True:
                self.movement.move(cmd) #TODO check if movement is ok
                self.poscalibrator.calibratePosition(cmd.getNaoMarkId())
            else:
                self.movement.move(cmd) #TODO check if movement is ok

        self.announce_destination()
        self.go_to_start_coordinate()

    def announce_destination(self, door_name):
        DoorChecker.check_door(door_name)

    def go_to_start_coordiante(self):
        pass

#Main entry point for the Floor Guide
def _main():
    cf = ControlFlow()
    if cf.init() == True:
        cf.run()

if __name__ == "__main__":
    _main()