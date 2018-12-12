import json
from astar.astar import Astar
from roblib.map import Map
import numpy as np
from roblib.datastructures import MoveCommand
from roblib.datastructures import Coordinate
from filetransfer import Filetransfer

# Path JSON
_PATH_LOCAL = "./path.json"
_PATH_REMOTE = "/home/nao/.local/share/PackageManager/apps/FloorGuide_Map/html/json/path.json"


class Planner():
    def __init__(self):
        self.map = Map()
        self.map.load_json()
        self.pepper_matrix = np.ones((self.map.map_size_x, self.map.map_size_y), dtype=int)
        for n in self.map.nodes.itervalues():
            if (n.is_passable()):
                self.pepper_matrix[n.x][n.y] = 0

    def get_coord_list(self, current_pos, destination_pos):
        a = Astar()
        start = (current_pos.getX(), current_pos.getY())
        end = (destination_pos.getX(), destination_pos.getY())
        path = a.astar(self.pepper_matrix, start, end)
        self._write_json_path(path)
        simplified_path = self._simplifyPath(path)
        coord_list = []
        for p in simplified_path:
            coord_list.append(Coordinate(p[0], p[1]))
        coord_list[len(coord_list) - 1].degrees = destination_pos.degrees
        return coord_list

    def _simplifyPath(self, path):
        path_comp = []
        start_node = path[0]
        prev_node = path[0]
        for node in path:
            if (start_node[0] != node[0] and start_node[1] != node[1]):
                path_comp.append(prev_node)
                start_node = prev_node
            prev_node = node
        path_comp.append(prev_node)
        return path_comp

    def get_move_cmd_from_coord(self, currentpos, targetpos):
        move_list = []
        current_direction = currentpos.getDegrees()
        direction = (targetpos.x - currentpos.x, targetpos.y - currentpos.y)
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

        distance = abs(direction[0] + direction[1])
        turn = self._getTurnDegrees(current_direction, new_direction)

        if turn != 0:
            move_list.append(MoveCommand(0, 0, turn))
        if distance != 0:
            move_list.append(MoveCommand(distance, 0, 0))

        node = self.map.nodes['%d:%d' % (targetpos.x, targetpos.y)]
        if node.get_naomark() != None:
            naoMarkDegree = node.get_naomark().get_degree()
            degrees = self._getTurnDegrees(new_direction, naoMarkDegree)
            move_list.append(MoveCommand(0, 0, degrees, True, node.get_naomark().get_id()))
            if degrees != 0:
                move_list.append(MoveCommand(0, 0, -degrees))

        if targetpos.getDegrees() != None:
            move_list.append(MoveCommand(0, 0, self._getTurnDegrees(new_direction, targetpos.getDegrees())))



        currentpos.x = targetpos.x
        currentpos.y = targetpos.y
        currentpos.degrees = new_direction
        return move_list

    def _getTurnDegrees(self, currentDirection, newDirection):
        turn = newDirection - currentDirection
        if turn > 180:
            turn -= 360
        if turn < -180:
            turn += 360
        return turn

    def _write_json_path(self, path):
        path_obj = {}
        array = []
        for p in path:
            obj = {}
            obj['x'] = p[0]
            obj['y'] = p[1]
            array.append(obj)
        path_obj['path'] = array
        with open(_PATH_LOCAL, 'w') as pathfile:
            json.dump(path_obj, pathfile)
        Filetransfer.transfer_file_from_local_to_pepper(_PATH_LOCAL, _PATH_REMOTE)

    def get_coor_by_room_name(self, room_name):
        for n in self.map.nodes.itervalues():
            if n.get_room() != None:
                if room_name in n.get_room().get_name():
                    return n.get_coordinate()
        return None
