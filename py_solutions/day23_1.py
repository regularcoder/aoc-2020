# To run: python day23_1.py
import sys
import re

input = "156794823"

cups = [int(cupStr) for cupStr in input]

def pickNext3(cups, index):
    result = cups[index:index+3]
    
    if len(result) != 3:
        extraNeeded = 3 - len(result)
        result = result + cups[:extraNeeded]
    return result

def findDestinationCup(cups, pickedCups, currentCupIndex):
    searchFor = cups[currentCupIndex] - 1

    while True:
        if searchFor not in pickedCups and searchFor in cups:
            return cups.index(searchFor)
        else:
            searchFor = searchFor - 1

            if searchFor <= 0:
                searchFor = 9

def removeItems(targetList, listToRemove):
    setToRemove = set(listToRemove)

    return [x for x in targetList if x not in setToRemove]

moveCount = 1
def makeMove(cups, currentCupIndex):
    global moveCount
    print
    print "-- move %d --" % moveCount
    print "cups", cups
    print "current cup %d" % cups[currentCupIndex]

    currentCup = cups[currentCupIndex]
    pickedCups = pickNext3(cups, currentCupIndex + 1)
    print "pick up", pickedCups

    destinationCupIndex = findDestinationCup(cups, pickedCups, currentCupIndex)
    print "destination", cups[destinationCupIndex]

    movedCups = removeItems(cups[0:destinationCupIndex+1], pickedCups) + pickedCups + removeItems(cups[destinationCupIndex+1:], pickedCups)
    
    moveCount += 1

    currentCupIndex = (movedCups.index(currentCup) + 1) % len(cups)

    return movedCups, currentCupIndex

currentCupIndex = 0

for i in range(100):
    (cups, currentCupIndex) = makeMove(cups, currentCupIndex)

# find final answer
answer = ""
index = cups.index(1)
for i in range(len(cups) - 1):
    index = (index + 1) % len(cups)
    answer += str(cups[index])

print
print answer