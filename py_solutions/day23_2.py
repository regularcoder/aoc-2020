# To run: python day23_2.py
import sys
import re
import time
from collections import deque 

input = "389125467"
cups = deque([int(cupStr) for cupStr in input])

moveCount = 1
def makeMove(cups):
    global moveCount
    print("\n-- move %d --" % moveCount)
    print("cups", cups)

    current = cups.popleft()

    print("current cup %d" % current) 

    pickedUp = [cups.popleft(), cups.popleft(), cups.popleft()] 
    print("pick up %s" % pickedUp)

    cups.appendleft(current)
    destination = current - 1
    if destination == 0:
        destination = len(cups) - 1
    while destination in pickedUp:
        # print("subsr %d" % destination)
        destination = destination - 1
        if destination == 0:
            destination = len(cups) - 1
    
    # print("destination %d" % destination)

    # destinationIndex = current - 1
    for i in range(3):
        cups.insert(destination + i, pickedUp[i])
    
    moveCount += 1

    # cups.append(cups.popleft())
    cups.rotate(-1)

    # print(cups)

# for i in range(10, 10000):
#     cups.append(i)

tic = time.perf_counter()
for i in range(10):
    makeMove(cups)
toc = time.perf_counter()

# print(cups)
print(f"Finished processing in in {toc - tic:0.4f} seconds")

index1 = cups.index(1)
answer = cups[(index1 + 1) % len(cups)] * cups[(index1 + 2) % len(cups)]
print("answer %d" % answer)