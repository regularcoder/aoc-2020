# To run: python 35.py < input_18.txt
import sys
import re

lines = [l.rstrip('\n') for l in sys.stdin]

def processAddition(line):
    elements = line.split(" ")
    return int(elements[0]) + int(elements[2])

def runAddition(l):
    line = l

    while True:
        expressions = re.findall("\d+ \+ \d+", line)

        if len(expressions) == 0:
            break

        for subEx in expressions:
            result = processAddition(subEx)

            line = line.replace(subEx, result.__str__())
    
    return line

def processSimple(line):
    line = runAddition(line)

    elements = line.split(" ")
    result = int(elements[0])
    for el in elements[1:]:
        if el != "*":
            result = result * int(el)
    return result.__str__()

def processLine(l, processOnlyWrapped = True):
    if processOnlyWrapped:
        expressionRegex = "\((\d+(?: [\+\*] \d+)+)\)"
        expressions = re.findall(expressionRegex, l)
    else:
        expressions = [l]

    line = l
    for subEx in expressions:
        result = processSimple(subEx)
        if processOnlyWrapped:
            replaceEx = "(" + subEx + ")"
        else:
            replaceEx = subEx

        line = line.replace(replaceEx, result)
    
    return (line, len(expressions) > 0,)

sum = 0
for i, l in enumerate(lines):
    print
    print l
    processedLine = l

    while True:
        (processedLine, shouldContinue) = processLine(processedLine)

        if not shouldContinue:
            (processedLine, shouldContinue) = processLine(processedLine, False) 
            break

    print processedLine
    sum += int(processedLine)

print sum