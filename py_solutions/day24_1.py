# To run: python day24_1.py < input_24.txt
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

def getCoordinates(tokens):
    position = (0, 0)

    print("\n%s" % (position,))
    for token in tokens:
        print("applying %s" % token)
        toApply = directionToXY[token]
        print("%s + %s = %s" % (position, toApply, (position[0] + toApply[0], position[1] + toApply[1],)))

        position = (position[0] + toApply[0], position[1] + toApply[1],)

    print("finally", position)
    return position

tiles = {}
def processInput(lines):
    for line in lines:
        tokens = tokeniseLine(line)

        tileXY = getCoordinates(tokens)

        if tileXY in tiles:
            tiles[tileXY] = not tiles[tileXY]
        else:
            tiles[tileXY] = True

    counter = 0
    for tileKey, tileValue in tiles.items():
        if tileValue:
            counter += 1

    return counter

print(processInput(lines))