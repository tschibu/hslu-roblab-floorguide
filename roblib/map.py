from logger import Logger
from roblib.node import Node, Room
import json

NODES = "nodes"
ROOM = "room"
NAME = "name"
DEGREE = "deg"
SQUARE = "square"
X = "x"
Y = "y"


class Map:
    def __init__(self):
        self.map_size_x = 0
        self.map_size_y = 0
        self.nodes = {}

    def load_json(self):
        with open("webapp/html/json/map.json") as json_file:
            data = json.load(json_file)

            size = data[SQUARE]
            self.map_size_x = size[X]
            self.map_size_y = size[Y]

            for n in data[NODES]:
                if (len(n[ROOM]) == 2):
                    r = Room("", n[ROOM][NAME], n[ROOM][DEGREE])
                else:
                    r = None;
                node = Node(n["x"], n["y"], r)
                self.nodes[str(n["x"]) + ":" + str(n["y"])] = node
            self.neighbor_alg()

    def neighbor_alg(self):
        Logger.info("Map.neighbor_alg", "state_neighbor_calc", "start")
        for n in self.nodes.itervalues():
            right_node = str((n.x + 1)) + ":" + str(n.y)
            left_node = str((n.x - 1)) + ":" + str(n.y)
            down_node = str(n.x) + ":" + str((n.y + 1))
            up_node = str(n.x) + ":" + str((n.y - 1))

            if(self.nodes.get(right_node) is not None):
                n.set_right(self.nodes[right_node])

            if(self.nodes.get(left_node) is not None):
                n.set_left(self.nodes[left_node])

            if(self.nodes.get(down_node) is not None):
                n.set_down(self.nodes[down_node])

            if(self.nodes.get(up_node) is not None):
                n.set_up(self.nodes[up_node])
        Logger.info("Map.neighbor", "state_neighbor_calc", "finished")