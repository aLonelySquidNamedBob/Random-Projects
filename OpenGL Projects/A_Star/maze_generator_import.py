import random


class Node:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.visited = 0
        self.wall = 1


def createEmptyMap(range_x, range_y):
    map = []
    for y in range(range_y):
        map.append([])
        for x in range(range_x):
            node = Node(x, y)
            map[y].append(node)
    return map


def createWalls(map):
    for y in range(len(map)):
        for x in range(len(map)):
            if y % 2 == 0:
                if x % 2 == 0:
                    map[y][x].wall = 0
    return map


def findNeighbours(map, x, y):
    neighbours = [None, None, None, None]

    if x > 0:
        neighbours[0] = map[y][x - 2]
    if x < len(map) - 2:
        neighbours[1] = map[y][x + 2]
    if y > 0:
        neighbours[2] = map[y - 2][x]
    if y < len(map) - 2:
        neighbours[3] = map[y + 2][x]

    possibleNeighbours = []
    for neighbour in neighbours:
        if neighbour is not None:
            if not neighbour.visited:
                possibleNeighbours.append(neighbour)

    return possibleNeighbours


def chooseNeighbour(possibleNeighbours):
    if len(possibleNeighbours) > 0:
        randomIndex = random.randint(0, len(possibleNeighbours) - 1)
        chosenNeighbour = possibleNeighbours[randomIndex]
        return chosenNeighbour
    else:
        return None


def generateBranchRecursive(x, y):
    mazeMap[y][x].visited = 1

    while True:
        neighbours = findNeighbours(mazeMap, x, y)
        if len(neighbours) > 0:
            chosenNeighbour = chooseNeighbour(neighbours)

            if chosenNeighbour is not None:
                wallX = int((x + chosenNeighbour.x)/2)
                wallY = int((y + chosenNeighbour.y)/2)

                mazeMap[wallY][wallX].wall = 0

                generateBranchRecursive(chosenNeighbour.x, chosenNeighbour.y)
        else:
            break


def generateBranchIterative():
    stack = []
    initial = mazeMap[0][0]
    initial.visited = 1
    stack.append(initial)

    while len(stack) > 0:
        current = random.choice(stack)
        stack.remove(current)

        neighbours = findNeighbours(mazeMap, current.x, current.y)
        if len(neighbours) > 0:
            stack.append(current)
            chosenNeighbour = chooseNeighbour(neighbours)

            wallX = int((current.x + chosenNeighbour.x) / 2)
            wallY = int((current.y + chosenNeighbour.y) / 2)
            mazeMap[wallY][wallX].wall = 0

            chosenNeighbour.visited = 1
            stack.append(chosenNeighbour)


def nodeToBinary(map):
    binaryMap = []
    for y in range(len(map)):
        binaryMap.append([])
        for x in range(len(map)):
            binaryMap[y].append(map[y][x].wall)
    return binaryMap


def saveMap(map):
    with open("maze_coords.txt", "w") as f:
        for line in map:
            f.write(str(line) + ",\n")
        f.close()


def generateMapRecursive(size, output="binary"):
    global mazeMap

    mazeMap = createEmptyMap(size, size)
    mazeMap = createWalls(mazeMap)

    generateBranchRecursive(0, 0)

    if output == 'binary':
        binaryMap = nodeToBinary(mazeMap)
        return binaryMap

    elif output == 'node':
        return mazeMap

    else:
        raise AttributeError("Output must be either 'node' or 'binary'")


def generateMapIterative(size, output="binary"):
    global mazeMap

    mazeMap = createEmptyMap(size, size)
    mazeMap = createWalls(mazeMap)

    generateBranchIterative()

    if output == 'binary':
        binaryMap = nodeToBinary(mazeMap)
        return binaryMap

    elif output == 'node':
        return mazeMap

    else:
        raise AttributeError("Output must be either 'node' or 'binary'")

