# To run: python day23_2.py
import sys
import re
import time
from collections import deque 

input = "156794823"

def buildCups(input):
    cupsList = [int(cupStr) for cupStr in input]

    cups = {}
    for i, n in enumerate(cupsList):
        next = (i + 1) % len(cupsList)

        cups[n] = cupsList[next]

    return (cupsList[0], cups)

def printCups(cups, current):
    pointer = current
    counter = 0

    cupList = [current]
    while True:
        cupList.append(cups[pointer])
        pointer = cups[pointer]

        if pointer == current:
            break

    print(cupList)

moveCount = 1
def makeMove(cups, current):
    global moveCount
    # print("\n-- move %d --" % moveCount)
    # printCups(cups, current)

    # print("current cup %d" % current) 

    # pick up 3 and remove them
    next3 = []
    pointer = current
    for i in range(3):
        pointer = cups[pointer]
        next3.append(pointer)
    
    cups[current] = cups[pointer]

    # print("picked up", next3)

    # decide destination
    destination = current - 1 or len(cups)
    while destination in next3:
        destination = destination - 1 or len(cups)
    
    # print("destination", destination)

    # add picked up after destination
    (cups[destination], cups[next3[2]]) = (next3[0], cups[destination])

    moveCount += 1

    return (cups, cups[current])

tic = time.perf_counter()
(current, cups) = buildCups(input)

# add extra elements
lastPointer = int(input[-1])
for i in range(10, 1000001):
    cups[lastPointer] = i
    lastPointer = i
cups[lastPointer] = current

for i in range(10000000):
    (cups, current) = makeMove(cups, current)
toc = time.perf_counter()

print(f"Finished processing in in {toc - tic:0.4f} seconds")

next1 = cups[1]
next2 = cups[next1]
print ("%d * %d = %d" % (next1, next2, next1 * next2))