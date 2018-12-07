from logger import Logger

class Node:
    def __init__(self, x, y, passable, Room):
        self.x = x
        self.y = y
        self.Room = Room
        self.right_node = None
        self.left_node = None
        self.up_node = None
        self.down_node = None
        self.passable = passable

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

    def is_passable(self):
        if (self.passable == 1):
            return True
        else:
            return False

class Room:
    def __init__(self, number, name, degree):
        self.number = number
        self.name = name
        self.degree = degree