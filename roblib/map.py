from logger import Logger
from roblib.node import Node, Room
import json

NODES = "nodes"
ROOM = "room"
NAME = "name"
DEGREE = "deg"


class Map:
    def __init__(self):
        self.size_x = 0
        self.size_y = 0
        self.nodes = {}

    def generate_map(self):
        pass

    def load_json(self):
        with open("webapp/json/map.json") as json_file:
            data = json.load(json_file)

            size = data["square"]
            self.size_x = size["x"]
            self.size_y = size["y"]

            self.alg()

            for n in data[NODES]:
                if (len(n[ROOM]) == 2):
                    r = Room("", n[ROOM][NAME], n[ROOM][DEGREE])
                    Logger.debug("Map.load_json", "add_room", str(n[ROOM][NAME]) + " "+ str(n[ROOM][DEGREE]))
                else:
                    r = None;
                n = Node(n["x"], n["y"], r)

    def alg(self):
        pass

    def log(self):
        pass
