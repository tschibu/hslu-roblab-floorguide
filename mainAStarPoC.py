from astar.astar import Astar
from roblib.map import Map
import numpy as np

def main():


    map = Map()
    map.load_json()
    pepper_matrix = np.ones((map.map_size_x, map.map_size_y), dtype=int)

    for n in map.nodes.itervalues():
        pepper_matrix[n.x][n.y] = 0

    print("finished")

    start = (27, 19)
    end = (33, 1)
    a = Astar()

    path = a.astar(pepper_matrix, start, end)
    print(path)


if __name__ == "__main__":
    main()