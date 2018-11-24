from logger import Logger
from roblib.node import Node, Room
import json

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

            for n in data["nodes"]:
                if (len(n["room"]) == 2):
                    r = Room("", n["room"]["name"], n["room"]["degree"])
                    Logger.debug("Map.load_json","add_room", str(n["room"]["name"]) + " "+ str(n["room"]["degree"]))
                else:
                    r = None;
                n = Node(n["x"], n["y"], r)

    def alg(self):
        pass

    def log(self):
        pass
