from logger import Logger

class Node:
    def __init__(self, x, y, Room):
        self.x = x
        self.y = y
        self.Room = Room
        self.right_node = None
        self.left_node = None
        self.up_node = None
        self.down_node = None

    def set_right(self, node):
        self.right_node = node

    def set_left(self, node):
        self.left_node = node

    def set_up(self, node):
        self.up_node = node

    def set_down(self, node):
        self.down_node = node

class Room:
    def __init__(self, number, name, degree):
        self.number = number
        self.name = name
        self.degree = degree