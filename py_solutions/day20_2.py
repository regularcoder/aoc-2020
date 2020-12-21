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
def rotate(tileName):
    tileToRotate = tiles[tileName]
    rotatedTuples = list(zip(*tileToRotate[::-1]))
    rotated = []
    for rotatedTuple in rotatedTuples:
        rotated.append("".join(rotatedTuple))

    tiles[tileName] = rotated
    tileEdges[tileName] = computeEdge(tiles[tileName])

# https://stackoverflow.com/questions/8421337/rotating-a-two-dimensional-array-in-
def rotateCCW(tileName):
    tileToRotate = tiles[tileName]
    rotatedTuples = list(zip(*tileToRotate)[::-1])
    rotated = []
    for rotatedTuple in rotatedTuples:
        rotated.append("".join(rotatedTuple))

    tiles[tileName] = rotated
    tileEdges[tileName] = computeEdge(tiles[tileName])


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

def findExactMatchForEdge(edgeToLookFor, keyToExclude):
    for key, edge in tileEdges.items():
        if key != keyToExclude:
            if edgeToLookFor == edge.top:
                return ("top", key)
            if edgeToLookFor == edge.bottom:
                return ("bottom", key)
            if edgeToLookFor == edge.left:
                return ("left", key)
            if edgeToLookFor == edge.right:
                return ("right", key)

def findMatchForTile(tileName, tile, topEmpty = False, bottomEmpty = False, leftEmpty = False, rightEmpty = False):
    matchingEdgesWithNone = []
    topMatch = None
    bottomMatch = None
    leftMatch = None
    leftMatchRev = None
    rightMatchRev = None
    if tile.top:
        topMatch = findMatchForEdge(tile.top, tileName)
        matchingEdgesWithNone.append(topMatch)
        
        topMatchRev = findMatchForEdge(tile.top[::-1], tileName)  
        matchingEdgesWithNone.append(topMatchRev)
    if tile.bottom:
        bottomMatch = findMatchForEdge(tile.bottom, tileName) 
        matchingEdgesWithNone.append(bottomMatch) 

        bottomMatchRev = findMatchForEdge(tile.bottom[::-1], tileName)  
        matchingEdgesWithNone.append(bottomMatchRev)
    if tile.left:
        leftMatch = findMatchForEdge(tile.left, tileName)
        matchingEdgesWithNone.append(leftMatch) 

        leftMatchRev = findMatchForEdge(tile.left[::-1], tileName)
        matchingEdgesWithNone.append(leftMatchRev)
    if tile.right:
        rightMatch = findMatchForEdge(tile.right, tileName)
        matchingEdgesWithNone.append(rightMatch) 

        rightMatchRev = findMatchForEdge(tile.right[::-1], tileName)
        matchingEdgesWithNone.append(rightMatchRev) 
    
    if (topEmpty and topMatch) or (bottomEmpty and bottomMatch):
        print "flipping upside down"
        flipUpsideDown(tileName)
    if (rightEmpty and rightMatchRev) or (leftEmpty and leftMatchRev):
        print "flipping left/right"
        flipLeftRight(tileName)

    matchingEdges = [edge for edge in matchingEdgesWithNone if edge] 

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

bigSquare[0, 0] = corners.pop()

findMatchForTile(bigSquare[0, 0], tileEdges[bigSquare[0, 0]], topEmpty=True, leftEmpty=True)

def findExactMatchForTile(tileName, tile):
    matchingEdgesWithNone = []
    topMatch = None
    bottomMatch = None
    leftMatch = None
    leftMatchRev = None
    rightMatchRev = None
    if tile.top:
        topMatch = findExactMatchForEdge(tile.top, tileName)
        if topMatch:
            return topMatch + (False,)
        
        topMatchRev = findExactMatchForEdge(tile.top[::-1], tileName)  
        if topMatchRev:
            return topMatchRev + (True,)
    if tile.bottom:
        bottomMatch = findExactMatchForEdge(tile.bottom, tileName) 
        if bottomMatch:
            return bottomMatch + (False,) 

        bottomMatchRev = findExactMatchForEdge(tile.bottom[::-1], tileName)  
        if bottomMatchRev:
           return bottomMatchRev + (True,)
    if tile.left:
        leftMatch = findExactMatchForEdge(tile.left, tileName)
        if leftMatch:
            return leftMatch + (False,) 

        leftMatchRev = findExactMatchForEdge(tile.left[::-1], tileName)
        if leftMatchRev:
            return leftMatchRev + (True,)
    if tile.right:
        rightMatch = findExactMatchForEdge(tile.right, tileName)
        if rightMatch:
            return rightMatch + (False,) 

        rightMatchRev = findExactMatchForEdge(tile.right[::-1], tileName)
        if rightMatchRev:
            return rightMatchRev + (True,)

del tileEdges[bigSquare[0, 0]]
for i in range(bigSquareSide):
    row = ""
    for j in range(bigSquareSide):
        keyIJ = bigSquare.get((i, j), "*")

        if keyIJ == "*":
            topEmpty = i == 0
            leftEmpty = j == 0
            rightEmpty = j == bigSquareSide - 1
            bottomEmpty = i == bigSquareSide - 1
            leftEdge = None
            topEdge = None
            lookForPosition = ""

            adjacentPos = ""
            if i > 0 and lookForPosition == "":
                adjacentPos = bigSquare[i - 1, j]
                lookForPosition = "top"
                topEdge = computeEdge(tiles[adjacentPos]).bottom
            if j > 0 and lookForPosition == "":
                adjacentPos = bigSquare[i, j - 1]
                lookForPosition = "left"
                leftEdge = computeEdge(tiles[adjacentPos]).right
            searchTile = Edge(topEdge, None, leftEdge, None)
            
            findExactResults = findExactMatchForTile("9999", searchTile)
            if not findExactResults:
                print "SOMETHING FISHY", lookForPosition, topEdge
            (position, matchingTile, reverse) = findExactResults

            if lookForPosition == position and reverse:
                flipUpsideDown(matchingTile)
            elif (lookForPosition == "top" and position == "bottom" and not reverse) or (lookForPosition == "bottom" and position == "top" and not reverse):
                flipUpsideDown(matchingTile)
            elif (lookForPosition == "left" and position == "bottom"):
                rotate(matchingTile)
                if reverse:
                    flipUpsideDown(matchingTile)
            elif (lookForPosition == "left" and position == "right" and not reverse):
                flipLeftRight(matchingTile)       
            elif (lookForPosition == "top" and position == "right" and not reverse):
                flipLeftRight(matchingTile)
                rotate(matchingTile)
                flipLeftRight(matchingTile)
            elif (lookForPosition == "top" and position == "right" and reverse):
                rotateCCW(matchingTile)
                flipLeftRight(matchingTile)
            elif (lookForPosition == "left" and position == "top"):
                rotateCCW(matchingTile)
                if not reverse:
                    flipUpsideDown(matchingTile)
            elif (lookForPosition == "top" and position == "left" and reverse):
                rotate(matchingTile)
            elif (lookForPosition == "top" and position == "left" and not reverse):
                rotate(matchingTile)
                flipLeftRight(matchingTile)
            elif lookForPosition != position:
                print "ALARM ALARM, action needed!", matchingTile, reverse, lookForPosition, position

                print adjacentPos
                printTile(tiles[adjacentPos])
                print
                print matchingTile
                printTile(tiles[matchingTile])
                print
                quit()

            bigSquare[i, j] = matchingTile
            del tileEdges[bigSquare[i, j]]

        row = row + " " + bigSquare.get((i, j), "*").__str__()
    print row

# print "3079"
# printTile(tiles[3079])
# print

# print "2473"
# printTile(tiles[2473])
# print

# # flipLeftRight(2473)
# rotateCCW(2473)
# flipLeftRight(2473)

# print "2473"
# printTile(tiles[2473])
# print


def validateEdges(bigSquare, bigSquareSide):
    for i in range(2):
        row = ""
        for j in range(bigSquareSide):
            current = computeEdge(tiles[bigSquare[i, j]])
            if j > 0:
                adjacentPos = computeEdge(tiles[bigSquare[i, j - 1]])

                if adjacentPos.right != current.left:
                    print "ERROR ERROR on left"
            if i > 0:
                adjacentPos = computeEdge(tiles[bigSquare[i - 1, j]])

                if adjacentPos.bottom != current.top:
                    print "ERROR ERROR on top"