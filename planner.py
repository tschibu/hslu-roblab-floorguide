
from roblib.datastructures import MoveCommand
from roblib.datastructures import Coordinate

class Planner():
    def __init__(self):
        pass

    def getMoveCommands(self, map, current_pos, destination_pos):
        mcs = []
        diffrence_x = self.calculate_distance(destination_pos.getX(),current_pos.getX())
        diffrence_y = self.calculate_distance(destination_pos.getY(),current_pos.getY())
        print("INFO: X=" + str(diffrence_x) + " / Y=" + str(diffrence_y))

        if (diffrence_x >= 0):
            mcs.append(MoveCommand(0,0,self.calculate_rotation(current_pos.getDegrees(), 90)))

        mcs.append(MoveCommand(10, 10, 0))
        return mcs

    def calculate_move(self):
        pass

    def calculate_rotation(self, current_view, goal_view):
        if (current_view == goal_view):
            return 0
        else:
            return (current_view - goal_view)

    def calculate_distance(self, position_from, position_to):
        return (position_to - position_from)