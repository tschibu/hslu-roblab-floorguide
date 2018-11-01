from pynaoqi_mate import Robot
from configuration import PepperConfiguration
from movement import Movement

roboterName = "Amber"

def _main():
    config = PepperConfiguration(roboterName)
    robot = Robot(config)
    robot.ALRobotPosture.goToPosture("StandInit", 1)

    mov = Movement(robot)
    mov.moveSquare(1)

if __name__ == '__main__':
    _main()