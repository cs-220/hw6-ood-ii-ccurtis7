from random import randrange
from interface import TextInterface
from graphpoker import GraphicsInterface
from splashscreen import SplashScreen

class Dice:
    def __init__(self):
        self.dice = [0]*5
        self.rollAll()

    def roll(self, which):
        for pos in which:
            self.dice[pos] = randrange(1, 7)

    def rollAll(self):
        self.roll(range(5))

    def getValues(self):
        return self.dice[:] # Use slice to create a copy of the dice list so it isn't overridden somewhere else

    def score(self):
        # Create the counts list: How many 1s, how many 2s, etc.
        counts = [0]*7 # counts[0] will always be zero, as dice start at 1
        for value in self.dice:
            counts[value] = counts[value] + 1

        # score the hand
        if 5 in counts:
            return 'Five of a Kind', 30
        elif 4 in counts:
            return "Four of a Kind", 15
        elif (3 in counts) and (2 in counts):
            return "Full House", 12
        elif 3 in counts:
            return "Three of a Kind", 8
        elif not (2 in counts) and (counts[1] == 0 or counts[6] == 0):
            return 'Straight', 20
        elif counts.count(2) == 2:
            return "Two Pairs", 5
        else:
            return 'Garbage', 0

class PokerApp:
    def __init__(self, interface):
        self.interface = interface
        self.dice = Dice()
        self.money = 100

    def run(self):
        while self.money >= 10 and self.interface.wantToPlay():
            self.playRound()
        self.interface.close()

    def playRound(self):
        self.money -= 10
        self.interface.setMoney(self.money)
        self.doRolls()
        result, score = self.dice.score()
        self.interface.showResult(result, score)
        self.money += score
        self.interface.setMoney(self.money)

    def doRolls(self):
        self.dice.rollAll()
        self.interface.setDice(self.dice.getValues())
        roll = 1
        toRoll = self.interface.chooseDice()
        while roll < 3 and toRoll != []:
            self.dice.roll(toRoll)
            self.interface.setDice(self.dice.getValues())
            roll += 1
            if roll < 3:
                toRoll = self.interface.chooseDice()

def main():
    splash = SplashScreen()
    if splash.wantToPlay():
        splash.close()
        inter = GraphicsInterface()
        app = PokerApp(inter)
        app.run()
    else:
        splash.close()

main()
