# To run: python day21_1.py < input_21.txt
import sys
import re

lines = [l.rstrip('\n') for l in sys.stdin]

allergenDict = {}
confirmedAllergensDict = {}
confirmedAllergensSet = set()
allIngredients = []
for line in lines:
    splitLine = line.split(" (contains ")

    ingredients = splitLine[0].split(" ")
    allIngredients.append(ingredients)
    allergens = splitLine[1].rstrip(")").split(", ")

    for allergen in allergens:
        if allergen in allergenDict:
            # print
            # print "%s find intersection between" % allergen
            # print allergenDict[allergen]
            # print set(ingredients)
            allergenDict[allergen] = allergenDict[allergen].intersection(set(ingredients)).difference(confirmedAllergensSet)
            # print allergenDict[allergen]

            if len(allergenDict[allergen]) == 1:
                confirmed = allergenDict[allergen].pop()
                confirmedAllergensSet.add(confirmed)
                confirmedAllergensDict[confirmed] = allergen

                del allergenDict[allergen]
        else:
            allergenDict[allergen] = set(ingredients)

# print allergenDict

# reduce
while True:
    reductionDone = False
    for key, value in allergenDict.items():
        reducedSet = value.difference(confirmedAllergensSet)

        if len(reducedSet) == 1:
            confirmed = reducedSet.pop()
            confirmedAllergensSet.add(confirmed)
            confirmedAllergensDict[confirmed] = key

            del allergenDict[key]
            reductionDone = True
            # print "reduction done"

    if not reductionDone:
        break

# print
# print
# print confirmedAllergensSet
# print allIngredients

safeCount = 0
for ingredients in allIngredients:
    nonAllergens = set(ingredients).difference(confirmedAllergensSet)

    safeCount = safeCount + len(nonAllergens)
    # print nonAllergens
# print confirmedAllergensDict

print safeCount