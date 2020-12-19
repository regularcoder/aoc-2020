# To run: python day19_1.py < input_19.txt
import sys
import re

lines = [l.rstrip('\n') for l in sys.stdin]

rules = lines[:lines.index('')]
rules.reverse()

ruleDict = {}
for rule in rules:
    ruleParts = rule.split(":")

    ruleDict[ruleParts[0]] = ruleParts[1].replace("\"", "").lstrip()

expression = ruleDict["0"]
runs = 0
while True:
    print
    print expression
    subExps = re.findall("\d+", expression)

    if len(subExps) == 0:
        break

    for subExp in subExps:
        print("search ruleDict for", subExp)
        replacement = ruleDict[subExp]
        if "|" in replacement:
            replacement = "(?:" + replacement + ")"

        expression = re.sub(r"\b%s\b" % subExp, replacement, expression)
        # expression = expression.replace(subExp, replacement)
    
    runs = runs + 1

expression = "^" + expression.replace(" ", "") + "$"

print("final expression", expression)

## Now perform matching
matchCount = 0
testData = lines[lines.index('')+1:]

for testLine in testData:
    matches = re.match(expression, testLine)

    if matches:
        matchCount = matchCount + 1
        print("match", testLine)
    else:
        print("NO match", testLine)

print matchCount