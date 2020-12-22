# To run: python day22_2.py < input_22.txt
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

def playRound(player1cards, player2cards):
    player1Card = player1cards.pop(0)
    player2Card = player2cards.pop(0)
    print player1Card, player2Card

    if player1Card > player2Card:
        print "player 1 wins"
        return (1, player1Card, player2Card)
    else:
        print "player 2 wins"
        return (2, player1Card, player2Card)

def calculateScore(playerCards):
    score = 0
    for i in range(len(playerCards)):
        score += (i + 1) * playerCards[len(playerCards) - i - 1]

    return score

def calculateKey(playerCards):
    return ",".join([str(card) for card in playerCards])

def playGame(gameCount, player1cards, player2cards):
    player1Prev = {}
    player2Prev = {}
    round = 1
    while True:
        print
        print "Round %d (Game %d)" % (round, gameCount)

        print "player 1 deck", player1cards
        print "player 2 deck", player2cards

        config1 = calculateKey(player1cards)
        config2 = calculateKey(player2cards)

        winner = -1
        if len(player1cards) == 0:
            print "player 2 wins game %d" % gameCount
            return 2
        elif len(player2cards) == 0:
            print "player 1 wins game %d" % gameCount
            return 1
        elif config1 in player1Prev or config2 in player2Prev:
            print "there was a previous round in this game that had exactly the same cards in the same order in the same players' decks, the game instantly ends in a win for player 1."
            return 1
        elif (len(player1cards) - 1 >= player1cards[0] and len(player2cards) - 1 >= player2cards[0]):
            player1Card = player1cards.pop(0)
            player2Card = player2cards.pop(0)
            print "playing a sub-game to determine the winner..."
            winner = playGame(gameCount + 1, list(player1cards[0:player1Card]), list(player2cards[0:player2Card]))
        else:
            (winner, player1Card, player2Card) = playRound(player1cards, player2cards)

        if winner == 1:
            player1cards.append(player1Card)
            player1cards.append(player2Card)
        elif winner == 2:
            player2cards.append(player2Card)
            player2cards.append(player1Card)

        player1Prev[config1] = True
        player2Prev[config2] = True

        round += 1

winner = playGame(1, player1cards, player2cards)

if winner == 1:
    print calculateScore(player1cards)
else:
    print calculateScore(player2cards)