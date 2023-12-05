from graphics import *
from button import Button

class SplashScreen:
    def __init__(self):
        win = self.win = GraphWin("Dice Poker", 200, 300)
        win.setCoords(0, 0, 2, 3)

        # Add a banner
        banner = Text(Point(1, 2.5), 'Welcome to\nDice Poker!')
        banner.setSize(26)
        banner.draw(win)

        # Add buttons
        play = Button(win, Point(0.5, 0.5), 0.8, 0.6, "Let's Play!")
        exit = Button(win, Point(1.5, 0.5), 0.8, 0.6, "Exit")

        self.buttons = [play, exit]

    def choose(self, choices):
        buttons = self.buttons

        # activate choice buttons, deactivate others
        for b in buttons:
            if b.getLabel() in choices:
                b.activate()
            else:
                b.deactivate()

        # get mouse clicks until an active button is clicked
        while True:
            p = self.win.getMouse()
            for b in buttons:
                if b.clicked(p):
                    return b.getLabel() # function exit here.

    def wantToPlay(self):
        ans = self.choose(["Let's Play!", "Exit"])
        return ans == "Let's Play!"

    def close(self):
        self.win.close()
