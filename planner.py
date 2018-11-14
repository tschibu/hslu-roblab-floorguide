
from roblib.datastructures import MoveCommand
from roblib.datastructures import Coordinate

class Planner():
    def __init__(self):
        pass

    def getMoveCommands(currentPos, destinationPos):
        mcs = []
        mcs.append(MoveCommand(1, 1, 90))
        return mcs
