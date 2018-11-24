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

class Room:
    def __init__(self, number, name, degree):
        self.number = number
        self.name = name
        self.degree = degree