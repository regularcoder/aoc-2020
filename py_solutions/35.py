# To run: python 35.py < input_18.txt
import sys
import re

lines = [l.rstrip('\n') for l in sys.stdin]

def handleSimpleExpression(line, prev, prevExtraOperator):
    print("processsing", line, prev, prevExtraOperator)

    if line == "":
        return (prev, "")
    elif line == " + ":
        return (prev, "+")
    elif line == " * ":
        return (prev, "*")

    if prevExtraOperator != "":
        print("changing line to", line + " " + prevExtraOperator + " " + prev.__str__())
        line = (line + " " + prevExtraOperator + " " + prev.__str__())
    
    elements = line.split(" ")

    result = prev
    if elements[0] != "":
        result = int(elements[0])
    
    operator = prevExtraOperator
    print elements[1:]
    for el in elements[1:]:
        if el == "*" or el == "+":
            operator = el
        else:
            if el != "":
                num = int(el)
            else:
                break

            if operator == "*":
                result = result * num
                operator = ""
            else:
                result = result + num
                operator = ""

    return (result, operator,)

def processOnlySimple(line):
    operatorCount = line.count("*") + line.count("+")
    numberCount = len(re.findall("\d+", line))

    if operatorCount == numberCount - 1:
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
    else:
        return line

def processLine(l):
    expressions = re.split("\(|\)", l)
    print expressions
    expressions.reverse()

    simplified = ""
    for subEx in expressions:
        result = processOnlySimple(subEx)
        
        if result != "":
            if simplified == "":
                simplified = result
            else:
                operatorCount = simplified.count("*") + simplified.count("+")
                numberCount = len(re.findall("\d+", simplified))

                if operatorCount == numberCount - 1 and numberCount > 1:
                    print("appending", result, simplified)
                    simplified = result + "(" + simplified + ")"
                else:
                    simplified = result + simplified
    
    return (simplified, len(expressions) > 1,)

for i, l in enumerate(lines):
    print
    processedLine = l

    while True:
        (processedLine, shouldContinue) = processLine(processedLine)
        (processedLine, shouldContinue) = processLine(processedLine)
        (processedLine, shouldContinue) = processLine(processedLine)

        print processedLine
        # if not shouldContinue:
        break