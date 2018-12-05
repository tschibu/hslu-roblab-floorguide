def simplifyPath(self, path):
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


def getMoveList(self, currentPos, destinationPos, path):
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
        turn = getTurnDegrees(None, current_direction, new_direction)

        if turn != 0:
            moveList.append(MoveCommand(0, 0, turn))
        current_direction = new_direction

        # drive command
        distance = abs(direction[0] + direction[1])
        moveList.append(MoveCommand(distance, 0, 0))
        print(direction)
        prev_waypoint = waypoint

    turn = destinationPos.getDegrees() - current_direction
    moveList.append(MoveCommand(0, 0, turn))
    for move in moveList:
        print("MoveCommand({}, {}, {})".format(move.getX(), move.getY(), move.getDegrees()))
    return moveList

def getTurnDegrees(self, currentDirection, newDirection):
    turn = newDirection - currentDirection
    if turn > 180:
        turn -= 360
    if turn < -180:
        turn += 360
    return turn



path_comp = simplifyPath(None, pepper_path)
getMoveList(None, current_pos, destination_pos, path_comp)