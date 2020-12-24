# To run: python day24_2.py < input_24.txt
import sys
import re
import time

lines = [l.rstrip('\n') for l in sys.stdin]

def tokeniseLine(line):
    tokens = []
    prevToken = ""
    for i, c in enumerate(line):
        if c == "n" or c == "s":
            prevToken = c
        elif prevToken != "":
            if (c == "w" or c == "e"):
                prevToken += c
            tokens.append(prevToken)
            prevToken = ""
        else:
            tokens.append(c)

    return tokens

directionToXY = {
    "e": (2, 0),
    "se": (1, -1),
    "sw": (-1, -1),
    "w": (-2, 0),
    "nw": (-1, 1),
    "ne": (1, 1),
}

def add(position1, position2):
    return (position1[0] + position2[0], position1[1] + position2[1],)

def getCoordinates(tokens):
    position = (0, 0)

    for token in tokens:
        toApply = directionToXY[token]

        position = add(position, toApply)

    return position

def processInput(lines):
    tiles = {}

    for line in lines:
        tokens = tokeniseLine(line)

        tileXY = getCoordinates(tokens)

        # True: black side up
        if tileXY in tiles:
            tiles[tileXY] = not tiles[tileXY]
        else:
            tiles[tileXY] = True

    return tiles

def getNeighbourValues(tile, tiles):
    neighbours = []
    for key, direction in directionToXY.items():
        neighbour = add(tile, direction)

        neighbours.append(tiles.get(neighbour, False))
    
    return neighbours

def countBlack(tiles):
    counter = 0
    for tileKey, tileValue in tiles.items():
        if tileValue:
            counter += 1

    return counter

def applyRules(tiles):
    newTiles = {}

    # Add all neighbours
    for tileKey, tileValue in tiles.copy().items():
        for directionKey, directionValue in directionToXY.items():
            neighbour = add(tileKey, directionValue)

            if neighbour not in tiles:
                tiles[neighbour] = False

    for tileKey, tileValue in tiles.items():
        neighbours = getNeighbourValues(tileKey, tiles)
        blackCount = len([n for n in neighbours if n])
        
        if tileValue:
            if blackCount == 0 or blackCount > 2:
                newTiles[tileKey] = False
            else:
                newTiles[tileKey] = True
        else:
            if blackCount == 2:
                newTiles[tileKey] = True
            else:
                newTiles[tileKey] = False

    return newTiles

tiles = processInput(lines)
print(countBlack(tiles))

for i in range(1, 101):
    tiles = applyRules(tiles)
    print("Day %d: %d" % (i, countBlack(tiles)))