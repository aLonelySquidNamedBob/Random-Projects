import maze_generator_import as maze
import random
import pygame
import math
import time
from perlin_noise import PerlinNoise


def drawMap(map):
    for y in range(len(map)):
        for x in range(len(map)):
            if map[y][x].state == 'closed':
                pygame.draw.rect(screen, (255, 0, 0), (x * multiplier, y * multiplier, multiplier, multiplier), 0)
            elif map[y][x].state == 'open':
                pygame.draw.rect(screen, (0, 255, 0), (x * multiplier, y * multiplier, multiplier, multiplier), 0)
            elif map[y][x].state == 'path':
                pygame.draw.rect(screen, (0, 0, 255), (x * multiplier, y * multiplier, multiplier, multiplier), 0)
            elif map[y][x].type == 'wall':
                pygame.draw.rect(screen, (0, 0, 0), (x * multiplier, y * multiplier, multiplier, multiplier), 0)
            elif map[y][x].type is None:
                pygame.draw.rect(screen, (255, 255, 255), (x * multiplier, y * multiplier, multiplier, multiplier), 0)
            elif map[y][x].type == 'start':
                pygame.draw.rect(screen, (255, 0, 255), (x * multiplier, y * multiplier, multiplier, multiplier), 0)
            elif map[y][x].type == 'end':
                pygame.draw.rect(screen, (255, 0, 255), (x * multiplier, y * multiplier, multiplier, multiplier), 0)

    pygame.display.update()


def drawBinaryMap(map):
    for y in range(len(map)):
        for x in range(len(map)):
            if map[y][x] == 1:
                pygame.draw.rect(screen, (255, 255, 255), (x * multiplier, y * multiplier, multiplier, multiplier), 0)

    pygame.display.update()


class Node:
    def __init__(self, x, y):
        self.x = x
        self.y = y

        self.type = None
        self.state = None
        self.parent = None

        self.g_cost = math.inf
        self.h_cost = math.inf
        self.f_cost = self.g_cost + self.h_cost


def drawNodeFromBinary(binaryMap):
    mazeMap = []
    for y in range(len(binaryMap)):
        mazeMap.append([])
        for x in range(len(binaryMap)):
            mazeMap[y].append(Node(x, y))
            if binaryMap[y][x] == 1:
                mazeMap[y][x].type = 'wall'
    return mazeMap


def generateMaze(size):
    binaryMap = maze.generateMap(size, "binary")
    maze.saveMap(binaryMap)
    nodeMap = drawNodeFromBinary(binaryMap)
    return nodeMap


def generateRadomTerrain(size):
    map = []
    noise = PerlinNoise(octaves=int(0.4 * size))
    for y in range(size):
        map.append([])
        for x in range(size):
            noise_value = round(noise([x / size, y / size]) + 0.46, 0)
            map[y].append(noise_value)

    return map


def findNeighbours(node, map):
    neighbours = []
    for x in range(-1, 2):
        for y in range(-1, 2):
            if x == 0 and y == 0:
                continue

            checkX = node.x + x
            checkY = node.y + y

            if 0 <= checkX < len(map):
                if 0 <= checkY < len(map):
                    if map[checkY][checkX].type is None or map[checkY][checkX].type == 'end':
                        neighbours.append(map[checkY][checkX])
    return neighbours


def evaluateDistance(nodeA, nodeB):
    distanceX = abs(nodeA.x - nodeB.x)
    distanceY = abs(nodeA.y - nodeB.y)
    if distanceX > distanceY:
        return 16 * distanceY + 10 * (distanceX - distanceY)
    else:
        return 16 * distanceX + 10 * (distanceY - distanceX)


def retraceSteps(start_node, end_node):
    path = []
    current = end_node
    while current != start_node:
        path.append(current)
        current.state = 'path'
        current = current.parent

    path.reverse()


def A_Star(start_node, end_node, map):
    open_nodes = []
    closed_nodes = []
    open_nodes.append(start_node)
    frame = 0

    while len(open_nodes) > 0:
        frame += 1
        current = open_nodes[0]
        for node in open_nodes:
            if node.f_cost < current.f_cost or node.f_cost == current.f_cost and node.h_cost < current.h_cost:
                current = node

        open_nodes.remove(current)
        closed_nodes.append(current)
        current.state = "closed"

        if current.type == 'end':
            retraceSteps(start_node, end_node)
            break

        neighbours = findNeighbours(current, map)

        for neighbour in neighbours:
            if neighbour in closed_nodes:
                continue

            new_move_cost = current.g_cost + evaluateDistance(current, neighbour)
            if new_move_cost < neighbour.g_cost or neighbour not in open_nodes:
                neighbour.g_cost = new_move_cost
                neighbour.h_cost = evaluateDistance(neighbour, end_node)
                neighbour.parent = current
                if neighbour not in open_nodes:
                    open_nodes.append(neighbour)
                    neighbour.state = "open"

        if frame % 50 == 0:
            drawMap(map)


def setStartNodes(nodeMap):
    start_node = None
    end_node = None
    mouse_coords = None
    clicked = False
    next_node = False

    while end_node is None:
        pygame.event.get()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RETURN]:
            start_node = nodeMap[random.randint(0, len(nodeMap)-1)][random.randint(0, len(nodeMap)-1)]
            start_node.type = 'start'
            end_node = nodeMap[random.randint(0, len(nodeMap)-1)][random.randint(0, len(nodeMap)-1)]
            end_node.type = 'end'
            return start_node, end_node
        elif pygame.mouse.get_pressed(3)[0]:
            clicked = True
            mouse_coords = pygame.mouse.get_pos()
            if next_node:
                end_node = nodeMap[mouse_coords[1] // multiplier][mouse_coords[0] // multiplier]
                end_node.type = 'end'
            else:
                start_node = nodeMap[mouse_coords[1] // multiplier][mouse_coords[0] // multiplier]
                start_node.type = 'start'
        elif clicked:
            next_node = True
            mouse_coords = None

        drawMap(nodeMap)

    return start_node, end_node


def editMap(nodeMap):
    node = nodeMap[0][0]
    type = node.type
    node.type = 'wall'

    while True:
        pygame.event.get()

        mouse_coords = pygame.mouse.get_pos()
        map_coords = [mouse_coords[0] // multiplier, mouse_coords[1] // multiplier]

        if not pygame.mouse.get_pressed(3)[0] and not pygame.mouse.get_pressed(3)[2]:
            old_node = node
            node = nodeMap[map_coords[1]][map_coords[0]]
            if node != old_node:
                old_node.type = type
                type = node.type
                node.type = 'wall'

        keys = pygame.key.get_pressed()
        if keys[pygame.K_RETURN]:
            node.type = type
            return nodeMap

        if pygame.mouse.get_pressed(3)[0]:
            node = nodeMap[mouse_coords[1] // multiplier][mouse_coords[0] // multiplier]
            node.type = 'wall'
            type = "wall"

        if pygame.mouse.get_pressed(3)[2]:
            mouse_coords = pygame.mouse.get_pos()
            node = nodeMap[mouse_coords[1] // multiplier][mouse_coords[0] // multiplier]
            node.type = None
            type = None

        #drawMap(nodeMap)


def main():
    global screen, multiplier
    size = 200
    multiplier = int(1000 / size)

    screen = pygame.display.set_mode((size * multiplier, size * multiplier))
    screen.fill((255, 255, 255))

    # map = maze.generateMapRecursive(size)
    # map = maze.generateMapIterative(size)
    # nodeMap = drawNodeFromBinary(map)
    map = generateRadomTerrain(size)
    nodeMap = drawNodeFromBinary(map)
    drawMap(nodeMap)

    while True:
        for row in nodeMap:
            for node in row:
                if node.type != 'wall' and node.type != 'end' and node.type != 'start':
                    node.type = None
                node.state = None

        drawMap(nodeMap)
        time.sleep(1)
        nodeMap = editMap(nodeMap)
        time.sleep(1)
        start_node, end_node = setStartNodes(nodeMap)
        start_node_coords = [start_node.x, start_node.y]
        end_node_coords = [end_node.x, end_node.y]

        start_time = time.time()
        A_Star(start_node, end_node, nodeMap)
        elapsed_time = time.time() - start_time
        print(elapsed_time)
        drawMap(nodeMap)
        pygame.image.save(screen, "mazeMap1.jpg")

        for row in nodeMap:
            for node in row:
                if node.type != 'wall':
                    node.type = None
                node.state = None

        end_node = nodeMap[start_node_coords[1]][start_node_coords[0]]
        start_node = nodeMap[end_node_coords[1]][end_node_coords[0]]

        end_node.type = 'end'
        start_node.type = 'start'

        drawMap(nodeMap)

        start_time = time.time()
        A_Star(start_node, end_node, nodeMap)
        elapsed_time = time.time() - start_time
        print(elapsed_time)
        drawMap(nodeMap)
        pygame.image.save(screen, "mazeMap2.jpg")

        time.sleep(1)

        while True:
            pygame.event.get()
            keys = pygame.key.get_pressed()
            if keys[pygame.K_RETURN]:
                break


if __name__ == '__main__':
    main()
