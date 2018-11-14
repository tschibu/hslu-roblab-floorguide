from roblib.datastructures import Coordinate
from planner import Planner
from movement import Movement

testCurrentPos = Coordinate(0, 0, 0)
testDestinationPos = Coordinate(2, 5, 0)


#Main entry point for the Planner & Movement Proof-of-Concept
def _main():
    #init Robot
    config = PepperConfiguration(roboterName)
    robot = Robot(config)
    robot.ALRobotPosture.goToPosture("StandInit", 1)

    #create Components
    planner = Planner()
    movement = Movement(robot)

    moveCmds = planner.getMoveCommands(testCurrentPos, testDestinationPos)

    for mcmd in moveCmds:
        movement.move(mcmd)

if __name__ == "__main__":
    _main()