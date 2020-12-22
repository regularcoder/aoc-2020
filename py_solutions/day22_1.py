# To run: python day22_1.py < input_21.txt
import sys
import re

lines = [l.rstrip('\n') for l in sys.stdin]

player1cards = []
player2cards = []
currentCards = player1cards
for line in lines:
    if "Player 1" in line:
        currentCards = player1cards
    elif "Player 2" in line:
        currentCards = player2cards
    elif line != "":
        currentCards.append(int(line))

print player1cards
print player2cards

def playRound(player1cards, player2cards):
    player1Card = player1cards.pop(0)
    player2Card = player2cards.pop(0)
    print player1Card, player2Card

    if player1Card > player2Card:
        print "player 1 wins"
        player1cards.append(player1Card)
        player1cards.append(player2Card)
    else:
        print "player 2 wins"
        player2cards.append(player2Card)
        player2cards.append(player1Card)

while len(player1cards) > 0 and len(player2cards) > 0:
    playRound(player1cards, player2cards)
    # break

def calculateScore(playerCards):
    playerCards.reverse()

    score = 0
    for i, card in enumerate(playerCards):
        score += (i + 1) * card
    return score

if len(player1cards) > len(player2cards):
    print "ultimate winner player 1"
    print player1cards
    print calculateScore(player1cards)
else:
    print "ultimate winner player 2"
    print player2cards
    print calculateScore(player2cards)