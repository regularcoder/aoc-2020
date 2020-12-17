# To run: python 33.py < input_17.txt
import sys
import copy
import itertools

lines = [l.rstrip('\n') for l in sys.stdin]

def printGameDict(dict, width):
    for i in range(0, width):
        print
        for j in range(0, width):
            print dict[i, j, 0],

gameDict = {}
for i, l in enumerate(lines):
    for j, c in enumerate(l):
        gameDict[i, j, 0] = c

def findNeighboursRecursive(position, index):
    # vary position at index
    indexPosition = position[index]

    if index == 2:
        return [(indexPosition,), (indexPosition+1,), (indexPosition-1,)]
    else:
        nextIndex = findNeighboursRecursive(position, index + 1)

        results = []
        for next in nextIndex:
            results.append((indexPosition+1,) + next)
            results.append((indexPosition,) + next)
            results.append((indexPosition-1,) + next)

        return results

def findNeighbours(position):
    neighbours = findNeighboursRecursive(position, 0)
    neighbours.remove(position)

    return neighbours


def runCycle(dict1):
    dict2 = {}

    runThrough = dict1.items()
    print runThrough
    while(len(runThrough) > 0):
        currentPos, posValue = runThrough.pop()
        neighbours = findNeighbours(currentPos)

        activeNeighbours = len(filter(bool, [dict1.get(pos, "") == "#" for pos in neighbours]))

        print("finding neigbours for", currentPos, activeNeighbours)

        
        if posValue == "#":
            # also add missing neighbours
            for neighbour in neighbours:
                if neighbour not in dict1:
                    runThrough.append((neighbour, ".",))
                    dict1[neighbour] = "."
                    dict2[neighbour] = "."

            if activeNeighbours == 2 or activeNeighbours == 3:
                dict2[currentPos] = "#"
            else:
                dict2[currentPos] = "."
        else:
            if activeNeighbours == 3:
                dict2[currentPos] = "#"
            else:
                dict2[currentPos] = "."
    
    return dict2

def countActive(dict1):
    activeCount = 0
    for currentPos, posValue in dict1.items():
        if posValue == "#":
            activeCount = activeCount + 1
    
    return activeCount


for i in range(6):
    gameDict = runCycle(gameDict)
    print countActive(gameDict)