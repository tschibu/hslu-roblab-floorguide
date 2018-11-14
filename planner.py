
from typing import List
from roblib.datastructures import MoveCommand
from roblib.datastructures import Coordinate
Vector = List[float]

class Planner():
    def __init__(self):
        pass

    def getMoveCommands(currentPos: Coordinate, destinationPos: Coordinate) -> List[MoveCommand]:
        mcs = []
        mcs.append(MoveCommand(1, 1, 90))
        return mcs
