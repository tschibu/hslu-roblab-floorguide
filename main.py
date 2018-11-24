from pynaoqi_mate import Robot
from configuration import PepperConfiguration
from tracer import Tracer
from movement import Movement
from dialog import Dialog
from display import Tablet

roboterName = "Amber"

def _main():
    config = PepperConfiguration(roboterName)
    robot = Robot(config)
    robot.ALRobotPosture.goToPosture("StandInit", 1)



    tablet = Tablet(robot)
    tablet.onInput_onStart()

    #dia = Dialog(robot)
    #dia.talk()

    #mov = Movement(robot)
    #mov.moveSquare(1)

    #tracer = Tracer(robot)
    #tracer.start()

    #mov = Movement(robot)
    #mov.moveSquare2(1)

    #tracer.stop()#

if __name__ == '__main__':
    _main()
