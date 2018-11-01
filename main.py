from pynaoqi_mate import Robot
from configuration import PepperConfiguration
from tracer import Tracer
from movement import Movement
from dialog import Dialog

roboterName = "Amber"

def _main():
    config = PepperConfiguration(roboterName)
    robot = Robot(config)
    robot.ALRobotPosture.goToPosture("StandInit", 1)

<<<<<<< HEAD
    dia = Dialog(robot)
    dia.talk()

    #mov = Movement(robot)
    #mov.moveSquare(1)#
=======
    tracer = Tracer(robot)
    tracer.start()

    mov = Movement(robot)
    mov.moveSquare2(1)

    tracer.stop()
>>>>>>> origin/master

if __name__ == '__main__':
    _main()