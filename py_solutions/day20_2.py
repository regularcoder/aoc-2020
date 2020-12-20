# To run: python day20_2.py < input_20.txt
import sys
import re
import math

lines = [l.rstrip('\n') for l in sys.stdin]

# process input - basic
tiles = {}
currentTile = ''
for line in lines:
    if "Tile" in line:
        currentTile = int(re.search("\d+", line).group(0))
        tiles[currentTile] = []
    elif line != "":
        tiles[currentTile].append(line)

class Edge:
  def __init__(self, top, bottom, left, right):
    self.top = top
    self.bottom = bottom
    self.left = left
    self.right = right

def computeEdge(tile):
    topEdge = tile[0]
    bottomEdge = tile[-1]
    leftEdge = "".join([tileLine[0] for tileLine in tile])
    rightEdge = "".join([tileLine[-1] for tileLine in tile])

    return Edge(topEdge, bottomEdge, leftEdge, rightEdge)

# compute edges
tileEdges = {}
for key, tile in tiles.items():
    tileEdges[key] = computeEdge(tile)


# https://stackoverflow.com/questions/8421337/rotating-a-two-dimensional-array-in-
def rotate(tileToRotate):
    rotatedTuples = list(zip(*tileToRotate[::-1]))
    rotated = []
    for rotatedTuple in rotatedTuples:
        rotated.append("".join(rotatedTuple))

    return rotated

# https://www.codespeedy.com/how-to-reverse-two-dimensional-array-in-python/
def flipUpsideDown(tileName):
    tiles[tileName] = tiles[tileName][::-1]
    tileEdges[tileName] = computeEdge(tiles[tileName])

def flipLeftRight(tileName):
    tiles[tileName] = [tileLine[::-1] for tileLine in tiles[tileName]]
    tileEdges[tileName] = computeEdge(tiles[tileName])

def findMatchForEdge(edgeToLookFor, keyToExclude):
    for key, edge in tileEdges.items():
        if key != keyToExclude:
            if edgeToLookFor in [edge.top, edge.bottom, edge.left, edge.right]:
                return key

def findMatchForTile(tileName, tile, topEmpty = False, bottomEmpty = False, leftEmpty = False, rightEmpty = False):
    topMatch = findMatchForEdge(tile.top, tileName)  
    topMatchRev = findMatchForEdge(tile.top[::-1], tileName)  
    bottomMatch = findMatchForEdge(tile.bottom, tileName)  
    bottomMatchRev = findMatchForEdge(tile.bottom[::-1], tileName)  
    leftMatch = findMatchForEdge(tile.left, tileName)
    leftMatchRev = findMatchForEdge(tile.left[::-1], tileName)
    rightMatch = findMatchForEdge(tile.right, tileName)
    rightMatchRev = findMatchForEdge(tile.right[::-1], tileName)
    
    if (topEmpty and topMatch) or (bottomEmpty and bottomMatch):
        print "flipping upside down"
        flipUpsideDown(tileName)
    if (rightEmpty and rightMatchRev) or (leftEmpty and leftMatchRev):
        print "flipping left/right"
        flipLeftRight(tileName)

    matchingEdgesWithNone = [topMatch, topMatchRev, bottomMatch, bottomMatchRev, leftMatch, leftMatchRev, rightMatch, rightMatchRev]
    matchingEdges = [edge for edge in matchingEdgesWithNone if edge] 

    # if len(matchingEdges) == 2:
    #     print (tileName, matchingEdgesWithNone)

    return matchingEdges

def printTile(tileToPrint):
    for line in tileToPrint:
        print line

def findCorners():
    corners = []
    result = 1
    for key, edge in tileEdges.items():  
        matchingEdges = findMatchForTile(key, edge)

        if len(matchingEdges) == 2:
            corners.append(key)
            result = result * key

    print result

    return corners

bigSquareSide = int(math.sqrt(len(tiles)))
corners = findCorners()
bigSquare = {}
# bigSquare[0, 0] = corners.pop()
# bigSquare[0, bigSquareSide - 1] = corners.pop()
# bigSquare[bigSquareSide - 1, bigSquareSide - 1] = corners.pop()
# bigSquare[bigSquareSide - 1, 0] = corners.pop()

bigSquare[0, 0] = 1951
bigSquare[0, bigSquareSide - 1] = 3079
bigSquare[bigSquareSide - 1, bigSquareSide - 1] = 1171
bigSquare[bigSquareSide - 1, 0] = 2971

# findMatchForTile(bigSquare[0, 0], tileEdges[key], topEmpty=True, rightEmpty=True)
# print("0, 0")
# printTile(tiles[bigSquare[0, 0]])

findMatchForTile(bigSquare[0, bigSquareSide - 1], tileEdges[key], topEmpty=True, rightEmpty=True)
print("0, bigSquareSide - 1")
printTile(tiles[bigSquare[0, bigSquareSide - 1])
# for i in range(bigSquareSide):
#     for j in range(bigSquareSide):
#         ijTile = bigSquare.get((i, j), "")

# key = 1951
# printTile(tiles[key])
# print(tileEdges[key].__dict__)
# print
# matches = findMatchForTile(key, tileEdges[key], topEmpty=True, rightEmpty=True)
# printTile(tiles[key])
# print(tileEdges[key].__dict__)

# key = 2971
# bigSquareSide - 1, 0
# matches = findMatchForTile(key, tileEdges[key], leftEmpty=True, bottomEmpty=True)
# printTile(tiles[2971])

# key = 1171
# printTile(tiles[key])
# print(tileEdges[key].__dict__)
# print
# matches = findMatchForTile(key, tileEdges[key], bottomEmpty=True, rightEmpty=True)
# printTile(tiles[key])
# print(tileEdges[key].__dict__)

# 0, 0
# key = 1951
# matches = findMatchForTile(key, tileEdges[key], leftEmpty=True, topEmpty=True)
# del matches[0]
# print matches


# printTile(tiles[1951])
# print(tileEdges[1951].__dict__)
# print


# flip(1951)
# printTile(tiles[1951])
# print(tileEdges[1951].__dict__)
# print

# printTile(rotate(rotate(tiles[1951])))
# print
# printTile(rotate(rotate(rotate(tiles[1951]))))
# print
# printTile(rotate(rotate(rotate(rotate(tiles[1951])))))