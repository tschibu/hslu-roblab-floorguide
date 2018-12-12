import sys
import time
import json
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
from filetransfer import Filetransfer

# Robot to use
_ROBOT_NAME = "Amber"
# Default Posture
_INIT_POSTURE = "StandInit" # StandInit, StandZero, Crouch
# Start Coordiante
_START_COORDINATE = Coordinate(8, 2, 90)
# Global flag which indicates that App should run
_RUN = True
# Position JSON
_POSITION_LOCAL = "./position.json"
_POSITION_REMOTE = "/home/nao/.local/share/PackageManager/apps/FloorGuide_Map/html/json/position.json"

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
        Filetransfer(self.config) #Initialize Filetransfer (static class, no reference needed)
        #self.tracer = Tracer(self.robot) # enable to gather sensor data
        self.sensorhandler = SensorHandler(self.robot)
        self.planner = Planner()
        self.movement = Movement(self.robot)
        self.poscalib = PositionCalibrator(self.robot)
        self.currentpos = _START_COORDINATE

    def init(self):
        global _RUN
        _RUN = True
        self.robot.ALRobotPosture.goToPosture(_INIT_POSTURE, 1)
        self._write_actual_position(self.currentpos)
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
        coordinate = self.planner.get_coor_by_room_name(value)
        if coordinate != None:
            Logger.info("ControlFlow", "onRoomSelected", "I will bring you to the room now. Please stand aside.")
            time.sleep(3)
            self.move_to_room(coordinate, value)
        else:
            Logger.err("ControlFlow", "onRoomSelected", "could not find specified room - abort behavior")
            self.init()

    def move_to_room(self, coordinate, room_name):
        move_success = self.move_to_location(_START_COORDINATE, coordinate)
        if move_success:
            self.announce_destination(room_name)
            self.go_to_start_coordinate()

    def move_to_location(self, start_coordinate, end_coordinate):
        coord_list = self.planner.get_coord_list(start_coordinate, end_coordinate)
        Logger.debug("ControlFlow", "moveToLocation", "I have %d waypoints." % len(coord_list))

        for i in range(len(coord_list)):
            for cmd in self.planner.get_move_cmd_from_coord(self.currentpos, coord_list[i]):

                Logger.info("ControlFlow", "moveToLocation", cmd.getText())
                if not self.movement.move(cmd):
                    Logger.err("ControlFlow", "moveToLocation", "Could not move to the given Position. Is something in my way?")
                    return False
                if cmd.get_isCalibrationCmd():
                    self.robot.ALRobotPosture.goToPosture(_INIT_POSTURE, 1)
                    self.poscalib.calibratePosition()
            self._write_actual_position(self.currentpos)

        return True

    def announce_destination(self, door_name):
        self.robot.ALRobotPosture.goToPosture(_INIT_POSTURE, 1)
        DoorChecker.check_door(door_name)
        Logger.info("ControlFlow", "announceDestination", "I found the correct room, it's directly in front of me")
        time.sleep(5)

    def go_to_start_coordinate(self):
        Logger.info("ControlFlow", "goToStartCoordinate", "Moving back to my initial position")
        self.move_to_location(self.currentpos, _START_COORDINATE)
        global _RUN
        _RUN = False
        self.init()

    def _write_actual_position(self, coordinate):
        pos_obj = {}
        obj = {}
        obj['x'] = coordinate.getX()
        obj['y'] = coordinate.getY()
        obj['degrees'] = coordinate.getDegrees()
        pos_obj['position'] = obj
        with open(_POSITION_LOCAL, 'w') as posfile:
            json.dump(pos_obj, posfile)
        Filetransfer.transfer_file_from_local_to_pepper(_POSITION_LOCAL, _POSITION_REMOTE)

#Main entry point for the Floor Guide
def _main():
    cf = ControlFlow()
    if cf.init() == True:
        cf.run()

if __name__ == "__main__":
    _main()