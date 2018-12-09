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


roboterName = "Amber"
initPosition = "StandZero" # StandInit, StandZero, Crouch
current_pos = Coordinate(8, 2, 270)
destination_pos = Coordinate(4, 18, 180)

#Main entry point for the Planner & Movement Proof-of-Concept
def _main():
    # init Robot
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

    # create Components
    Speech(robot)
    planner = Planner()
    movement = Movement(robot)
    poscalibrator = PositionCalibrator(robot)
    moveCmds = planner.getMoveCommands(current_pos, destination_pos)

    # info to the audience
    Logger.info("mainPlanMove2.py", "_main", "I have %d movements to do." % len(moveCmds))

    for cmd in moveCmds:
        Logger.info("mainPlanMove2.py", "_main", "Execute move command with " + cmd.getText() + " units ")
        print("MoveCommand({}, {}, {})".format(cmd.getX(), cmd.getY(), cmd.getDegrees()))
        if cmd.get_isCalibrationCmd() == True:
            movement.move(cmd)
            poscalibrator.calibratePosition(cmd.getNaoMarkId())
        else:
            movement.move(cmd)

if __name__ == "__main__":
    _main()