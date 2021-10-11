import pygame, time, random, secrets


def drawMap(map, screen):
    for y in range(len(map)):
        for x in range(len(map)):
            if map[y][x].wall == 0:
                pygame.draw.rect(screen, (255, 255, 255), (x * multiplier, y * multiplier, multiplier, multiplier), 0)

    pygame.display.update()


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


def generateBranch(x, y):
    mazeMap[y][x].visited = 1

    while True:
        neighbours = findNeighbours(mazeMap, x, y)
        if len(neighbours) > 0:
            chosenNeighbour = chooseNeighbour(neighbours)

            if chosenNeighbour is not None:
                wallX = int((x + chosenNeighbour.x)/2)
                wallY = int((y + chosenNeighbour.y)/2)

                mazeMap[wallY][wallX].wall = 0

                drawMap(mazeMap, screen)
                generateBranch(chosenNeighbour.x, chosenNeighbour.y)
        else:
            break


def nodeToBinary(map):
    binaryMap = []
    for y in range(len(map)):
        binaryMap.append([])
        for x in range(len(map)):
            binaryMap[y].append(map[y][x].wall)
    return binaryMap


def saveMap(map):
    with open("maze_coords_2.txt", "w") as f:
        for line in map:
            f.write(str(line) + ",\n")
        f.close()


def main():
    global mazeMap, screen, multiplier

    size = 80
    multiplier = 7

    screen = pygame.display.set_mode((size * multiplier, size * multiplier))
    screen.fill((0, 0, 0))

    mazeMap = createEmptyMap(size, size)
    mazeMap = createWalls(mazeMap)

    generateBranch(0, 0)
    
    binaryMap = nodeToBinary(mazeMap)
    saveMap(binaryMap)
    pygame.image.save(screen, "mazeMap.jpg")


if __name__ == '__main__':
    main()