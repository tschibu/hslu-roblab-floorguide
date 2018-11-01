from pynaoqi_mate import Robot
from configuration import PepperConfiguration
from tracer import Tracer
from movement import Movement

roboterName = "Amber"

def _main():
    config = PepperConfiguration(roboterName)
    robot = Robot(config)
    robot.ALRobotPosture.goToPosture("StandInit", 1)

    tracer = Tracer(robot)
    tracer.start()

    mov = Movement(robot)
    mov.moveSquare2(1)

    tracer.stop()

if __name__ == '__main__':
    _main()