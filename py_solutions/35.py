# To run: python 35.py < input_18.txt
import sys
import re

lines = [l.rstrip('\n') for l in sys.stdin]

def processSimple(line):
    elements = line.split(" ")
    operator = ""
    result = int(elements[0])
    for el in elements[1:]:
        if el == "*" or el == "+":
            operator = el
        else:
            num = int(el)
            if operator == "*":
                result = result * num
            else:
                result = result + num
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
        print("replacing", subEx, result)

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