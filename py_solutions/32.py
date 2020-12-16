# To run: python 32.py < input_16.txt
import sys
from functools import partial

lines = [l.rstrip('\n\n') for l in sys.stdin]
rules = []

class Rule:
  def __init__(self, ruleName, rule1, rule2):
    self.ruleName = ruleName
    self.rule1 = rule1
    self.rule2 = rule2

class SubRule:
  def __init__(self, min, max):
    self.max = max
    self.min = min

for l in lines:
    if " or " in l:
        ruleParts = l.split(" ")[-3:]

        rule1Parts = ruleParts[0].split("-")
        rule1 = SubRule(int(rule1Parts[0]), int(rule1Parts[1]))

        rule2Parts = ruleParts[2].split("-")
        rule2 = SubRule(int(rule2Parts[0]), int(rule2Parts[1]))

        ruleName = l.split(":")[0]
        rules.append(Rule(ruleName, rule1, rule2))

nearbyTickets = lines[lines.index('nearby tickets:')+1:]

invalidSum = 0
validNearby = []
for ticket in nearbyTickets:
    ticketValues = ticket.split(",")

    ticketValid = True
    for ticketValue in ticketValues:
        ticketInt = int(ticketValue)

        valid = False
        for rule in rules:
            if (ticketInt >= rule.rule1.min and ticketInt <= rule.rule1.max) or (ticketInt >= rule.rule2.min and ticketInt <= rule.rule2.max):
                valid = True
                break

        if not valid:
            ticketValid = False
            invalidSum = invalidSum + ticketInt
            break

    if ticketValid:
        validNearby.append(ticket)

positionWise = {}
for ticket in validNearby:
    ticketValues = ticket.split(",")

    for i, ticketValue in enumerate(ticketValues):
        if i in positionWise:
            positionWise[i].append(ticketValue)
        else:
            positionWise[i] = [ticketValue]

yourTicketsLine = lines[lines.index('your ticket:')+1]
yourTickets = map(int, yourTicketsLine.split(","))

print("yourTickets", yourTickets, "len(validNearby)", len(validNearby), len(nearbyTickets))
answer = 1
solutions = {}
for i, positionList in positionWise.items():
    for rulex in rules:
        allValid = True

        for position in positionList:
            positionInt = int(position)
            if not ((positionInt >= rulex.rule1.min and positionInt <= rulex.rule1.max) or (positionInt >= rulex.rule2.min and positionInt <= rulex.rule2.max)):
                allValid = False
                break
        
        if allValid:
            if i in solutions:
                solutions[i].append(rulex.ruleName)
            else:
                solutions[i] = [rulex.ruleName]

print(solutions)

alreadyFound = set()

while len(alreadyFound) != len(yourTickets):
    for i, sol in solutions.items():
        intersection = set(sol).difference(alreadyFound)
        
        if len(intersection) == 1:
            toAdd = intersection.pop()
            alreadyFound.add(toAdd)
            print(i, toAdd)

            if("departure" in toAdd):
                # print("multiplying by ", yourTickets[i])
                answer = answer * yourTickets[i]

print(answer)