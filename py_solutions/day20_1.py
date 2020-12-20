# To run: python day20_1.py < input_20.txt
import sys
import re

lines = [l.rstrip('\n') for l in sys.stdin]

# process input - basic
tiles = {}
currentTile = ''
for line in lines:
    if "Tile" in line:
        currentTile = line
        tiles[currentTile] = []
    elif line != "":
        tiles[currentTile].append(line)

class Edge:
  def __init__(self, top, bottom, left, right):
    self.top = top
    self.bottom = bottom
    self.left = left
    self.right = right

# compute edges
tileEdges = {}
for key, tile in tiles.items():
    topEdge = tile[0]
    bottomEdge = tile[-1]
    leftEdge = "".join([tileLine[0] for tileLine in tile])
    rightEdge = "".join([tileLine[-1] for tileLine in tile])

    tileEdges[key] = Edge(topEdge, bottomEdge, leftEdge, rightEdge)

def findMatch(edgeToLookFor, keyToExclude):
    for key, edge in tileEdges.items():
        if key != keyToExclude:
            if edgeToLookFor in [edge.top, edge.bottom, edge.left, edge.right]:
                return key

result = 1
for key, edge in tileEdges.items():  
    topMatch = findMatch(edge.top, key)  
    topMatchRev = findMatch(edge.top[::-1], key)  
    bottomMatch = findMatch(edge.bottom, key)  
    bottomMatchRev = findMatch(edge.bottom[::-1], key)  
    leftMatch = findMatch(edge.left, key)
    leftMatchRev = findMatch(edge.left[::-1], key)
    rightMatch = findMatch(edge.right, key)
    rightMatchRev = findMatch(edge.right[::-1], key)

    matchingEdgesWithNone = [topMatch, topMatchRev, bottomMatch, bottomMatchRev, leftMatch, leftMatchRev, rightMatch, rightMatchRev]
    matchingEdges = [edge for edge in matchingEdgesWithNone if edge] 

    if len(matchingEdges) == 2:
        tileNumber = int(re.search("\d+", key).group(0))
        result = result * tileNumber

        print tileNumber

print result