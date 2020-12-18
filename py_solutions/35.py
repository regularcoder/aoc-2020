# To run: python 35.py < input_18.txt
import sys
import re

lines = [l.rstrip('\n') for l in sys.stdin]

def handleExpression(line, prev, prevExtraOperator):
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

for i, l in enumerate(lines):
    expressions = re.split("\(|\)", l)
    # expressions.reverse()

    prev = 0
    extraOperator = ""
    for subEx in expressions:
        (prev, extraOperator) = handleExpression(subEx, prev, extraOperator)
        print("returned", prev, extraOperator)
        print
    print prev