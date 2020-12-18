# To run: python 35.py < input_18.txt
import sys
import re

lines = [l.rstrip('\n') for l in sys.stdin]

def handleExpression(line):
    elements = line.split(" ")

    result = int(elements[0])
    operator = ""
    for el in elements[1:]:
        if el == "*" or el == "+":
            operator = el
        else:
            if operator == "*":
                result = result * int(el)
            else:
                result = result + int(el)
    return result

for i, l in enumerate(lines):
    result = handleExpression(l)
    print result