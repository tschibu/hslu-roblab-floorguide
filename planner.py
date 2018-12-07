from astar.astar import Astar
from roblib.map import Map
import numpy as np
from roblib.datastructures import MoveCommand
from roblib.datastructures import Coordinate

class Planner():
    def __init__(self):
        self.map = Map()
        self.map.load_json()
        self.pepper_matrix = np.ones((self.map.map_size_x, self.map.map_size_y), dtype=int)
        for n in self.map.nodes.itervalues():
            if (n.is_passable()):
                self.pepper_matrix[n.x][n.y] = 0

    def getMoveCommands(self, current_pos, destination_pos):
        a = Astar()
        start = (current_pos.getX(), current_pos.getY())
        end = (destination_pos.getX(), destination_pos.getY())
        path = a.astar(self.pepper_matrix, start, end)
        simplified_path = self._simplifyPath(path)

        mcs = self._getMoveList(current_pos, destination_pos, simplified_path)

        return mcs

    def _simplifyPath(self, path):
        path_comp = [path[0]]
        start_node = path[0]
        prev_node = path[0]
        for node in path:
            if (start_node[0] != node[0] and start_node[1] != node[1]):
                path_comp.append(prev_node)
                start_node = prev_node
            prev_node = node
        path_comp.append(prev_node)
        return path_comp

    def _getMoveList(self, currentPos, destinationPos, path):
        prev_waypoint = path[0]
        current_direction = currentPos.getDegrees()
        moveList = []
        for waypoint in path[1:]:
            direction = (waypoint[0] - prev_waypoint[0], waypoint[1] - prev_waypoint[1])
            # turn command
            new_direction = current_direction
            if direction[0] > 0:
                # go right
                new_direction = 90
            if direction[0] < 0:
                # go left
                new_direction = 270
            if direction[1] < 0:
                # go down
                new_direction = 0
            if direction[1] > 0:
                # go up
                new_direction = 180
            turn = self._getTurnDegrees(current_direction, new_direction)

            if turn != 0:
                moveList.append(MoveCommand(0, 0, turn))
            current_direction = new_direction

            node = self.map.nodes['%d:%d' % (waypoint[0], waypoint[1])]
            naoMarkDegree = None
            if node.get_naomark() != None:
                naoMarkDegree = node.get_naomark().get_degree()
            # drive command
            distance = abs(direction[0] + direction[1])
            moveList.append(MoveCommand(distance, 0, 0, naoMarkDegree))
            prev_waypoint = waypoint

        turn = destinationPos.getDegrees() - current_direction
        moveList.append(MoveCommand(0, 0, turn))
        return moveList

    def _getTurnDegrees(self, currentDirection, newDirection):
        turn = newDirection - currentDirection
        if turn > 180:
            turn -= 360
        if turn < -180:
            turn += 360
        return turn