import sys

lines = [l.rstrip('\n\n') for l in sys.stdin]
rules = []

class Rule:
  def __init__(self, rule1, rule2):
    self.rule1 = rule1
    self.rule2 = rule2

class SubRule:
  def __init__(self, min, max):
    self.min = min
    self.max = max

print(lines)

for l in lines:
    if " or " in l:
        ruleParts = l.split(" ")[-3:]

        rule1Parts = ruleParts[0].split("-")
        rule1 = SubRule(int(rule1Parts[0]), int(rule1Parts[1]))

        rule2Parts = ruleParts[2].split("-")
        rule2 = SubRule(int(rule2Parts[0]), int(rule2Parts[1]))

        rules.append(Rule(rule1, rule2))

nearbyTickets = lines[lines.index('nearby tickets:')+1:]

invalidSum = 0
for ticket in nearbyTickets:
    ticketValues = ticket.split(",")

    for ticketValue in ticketValues:
        print("checking", ticketValue)
        ticketInt = int(ticketValue)

        valid = False
        for rule in rules:
            print(rule.rule1.__dict__)
            print(rule.rule2.__dict__)
            if (ticketInt >= rule.rule1.min and ticketInt <= rule.rule1.max) or (ticketInt >= rule.rule2.min and ticketInt <= rule.rule2.max):
                print("valid", ticketInt)
                valid = True
                break

        if not valid:
            print ticketInt
            invalidSum = invalidSum + ticketInt

print(invalidSum)