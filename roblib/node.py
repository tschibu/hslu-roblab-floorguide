from logger import Logger
from roblib.datastructures import Coordinate

class Node:
    def __init__(self, x, y, passable, room, naomark):
        self.x = x
        self.y = y
        self.room = room
        self.right_node = None
        self.left_node = None
        self.up_node = None
        self.down_node = None
        self.passable = passable
        self.naomark = naomark

    def set_right(self, node):
        self.right_node = node

    def set_left(self, node):
        self.left_node = node

    def set_up(self, node):
        self.up_node = node

    def set_down(self, node):
        self.down_node = node

    def set_passable(self, passable):
        self.passable = passable

    def set_naomark(self, naomark):
        self.naomark = naomark

    def get_naomark(self):
        return self.naomark

    def is_passable(self):
        if (self.passable == 1):
            return True
        else:
            return False

    def get_room(self):
        return self.room

    def get_coordinate(self):
        return Coordinate(self.x, self.y, self.get_room().get_degree())

class Room:
    def __init__(self, number, name, degree):
        self.number = number
        self.name = name
        self.degree = degree

    def get_name(self):
        return self.name

    def get_degree(self):
        return self.degree

class Naomark:
    def __init__(self, id, degree):
        self.id = id
        self.degree = degree

    def get_degree(self):
        return self.degree

    def get_id(self):
        return self.id