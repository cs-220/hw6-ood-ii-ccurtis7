class TextInterface:
    def __init__(self):
        print("Welcome to dice poker!")
        print("May the odds be ever in your favor!")

    def setMoney(self, amt):
        print('You currently have ${}'.format(amt))

    def setDice(self, values):
        print('Dice:', values)

    def wantToPlay(self):
        ans = input("Do you want to try your luck? [Yes/No]")
        return ans[0] in 'yY'

    def close(self):
        print('\nThanks for playing!')

    def chooseDice(self):
        return eval(input("Enter list of which dice to change (Enter [] to stop): "))

    def showResult(self, msg, score):
        print("{}. You win ${}".format(msg, score))
