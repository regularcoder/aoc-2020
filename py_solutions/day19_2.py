# To run: python day19_2.py < input_19.txt
import sys
import re

lines = [l.rstrip('\n') for l in sys.stdin]

rules = lines[:lines.index('')]
rules.reverse()

ruleDict = {}
for rule in rules:
    ruleParts = rule.split(":")

    ruleDict[ruleParts[0]] = ruleParts[1].replace("\"", "").lstrip()

def generateRule(ruleDict, startWith = "0", exactMatch = False):
    expression = ruleDict[startWith]

    ruleDict["8"] = "(?:42)+"
    if exactMatch:
        ruleDict["11"] = "(?:42)NUM(?:31)NUM"
    else:
        ruleDict["11"] = "((42)+)((31)+)"

    while True:
        subExps = re.findall("\d+", expression)

        if len(subExps) == 0:
            break

        for subExp in subExps:
            replacement = ruleDict[subExp]
            if "|" in replacement:
                replacement = "(?:" + replacement + ")"

            expression = re.sub(r"\b%s\b" % subExp, replacement, expression)
        
    return expression.replace(" ", "")

expression = "^" + generateRule(ruleDict) + "$" 
exactExpression = "^" + generateRule(ruleDict, exactMatch=True) + "$" 
expression42 = generateRule(ruleDict, "42")
expression31 = generateRule(ruleDict, "31")

## Now perform matching
matchCount = 0
testData = lines[lines.index('')+1:]

for testLine in testData:
    matches = re.match(expression, testLine)

    if matches:
        count42 = len(re.findall(expression42, matches.group(1)))
        count31 = len(re.findall(expression31, matches.group(3)))

        preciseRule = exactExpression.replace("NUM", "{%s}" % count31)

        if re.match(preciseRule, testLine):
            matchCount = matchCount + 1

print matchCount