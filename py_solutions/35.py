# To run: python 35.py < input_18.txt
import sys
import re

lines = [l.rstrip('\n') for l in sys.stdin]

def handleExpression(line, prev):
    print("processsing", line)

    if line == "":
        return 0

    elements = line.split(" ")

    print elements
    result = int(elements[0])
    operator = ""
    for el in elements[1:]:
        if el == "*" or el == "+":
            operator = el
        else:
            num = prev
            if el != "":
                num = int(el)

            if operator == "*":
                result = result * num
            else:
                result = result + num
    return result

for i, l in enumerate(lines):
    expressions = re.split("\(|\)", l)
    expressions.reverse()

    prev = 0
    for subEx in expressions:
        result = handleExpression(subEx, prev)
        prev = result
        print result
    # print result