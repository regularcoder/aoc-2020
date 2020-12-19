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

def generateRule(ruleDict, exactMatch = 0):
    expression = ruleDict["0"]

    ruleDict["8"] = "(?:42)+"
    if exactMatch == 0:
        ruleDict["11"] = "((42)+)((31)+)"
    else:
        ruleDict["11"] = "(?:42)NUM(?:31)NUM"
        # print("now it is ", ruleDict["11"])

    while True:
        subExps = re.findall("\d+", expression)

        if len(subExps) == 0:
            break

        for subExp in subExps:
            replacement = ruleDict[subExp]
            if "|" in replacement:
                replacement = "(?:" + replacement + ")"

            # print "replacing %s with %s in %s" % (subExp, replacement, expression)
            expression = re.sub(r"\b%s\b" % subExp, replacement, expression)
        
    return "^" + expression.replace(" ", "").replace("NUM", "{%s}" % exactMatch) + "$"

expression = generateRule(ruleDict)
print("final expression", expression)

## Now perform matching
matchCount = 0
testData = lines[lines.index('')+1:]

for testLine in testData:
    matches = re.match(expression, testLine)

    if matches:
        length = matches.group(3).count(matches.group(4))
        preciseRule = generateRule(ruleDict, length)

        # print("precise", preciseRule, length)
        if re.match(preciseRule, testLine):
            matchCount = matchCount + 1
            # print("valid", testLine)
        else:
            print("precise", preciseRule, length)
            print("INVALID", testLine)
            # break
    # else:
    #     print("INVALID", testLine)

print matchCount