import sys
import time
from logger import Logger
from pynaoqi_mate import Robot
from configuration import PepperConfiguration
from roblib.datastructures import Coordinate
from planner import Planner
from movement import Movement
from speech import Speech
from positionCalibrator import PositionCalibrator
from tracer import Tracer


roboterName = "Porter"
initPosition = "StandZero" # StandInit, StandZero, Crouch
current_pos = Coordinate(3, 2, 90)
destination_pos = Coordinate(4, 18, 180)

#Main entry point for the Planner & Movement Proof-of-Concept
def _main():
    # init Robot
    config = PepperConfiguration(roboterName)
    #if(not config.isAvailable()):
    #    Logger.err("Main", "checkAvailability", "name: " + config.Name + ", ip: " + config.Ip + " not reachable!")
    #    sys.exit(1)

    robot = Robot(config)

    #lifeService = robot.session.service("ALAutonomousLife")
    #lifeService.setAutonomousAbilityEnabled("AutonomousBlinking", False)
    #lifeService.setAutonomousAbilityEnabled("BackgroundMovement", False)
    #lifeService.setAutonomousAbilityEnabled("BasicAwareness", False)
    #lifeService.setAutonomousAbilityEnabled("ListeningMovement", False)
    #lifeService.setAutonomousAbilityEnabled("SpeakingMovement", False)

    #robot.ALRobotPosture.goToPosture(initPosition, 1)
    #time.sleep(3)

    # create Components
    Speech(robot)
    planner = Planner()
    movement = Movement(robot)
    poscalibrator = PositionCalibrator(robot)
    coord_list = planner.get_coord_list(current_pos, destination_pos)
    move_cmds = []
    # info to the audience

    for i in range(len(coord_list)):
        move_cmds.append(planner.get_move_cmd_from_coord(current_pos, coord_list[i]))


    Logger.info("mainPlanMove2.py", "_main", "I have %d movements to do." % len(coord_list))
    #for cmd in moveCmds:
    #    Logger.info("mainPlanMove2.py", "_main", "Execute move command with " + cmd.getText() + " units ")
    #    print("MoveCommand({}, {}, {})".format(cmd.getX(), cmd.getY(), cmd.getDegrees()))
    #    if cmd.get_isCalibrationCmd() == True:
    #        movement.move(cmd)
    #        poscalibrator.calibratePosition(cmd.getNaoMarkId())
    #    else:
    #        movement.move(cmd)

if __name__ == "__main__":
    _main()