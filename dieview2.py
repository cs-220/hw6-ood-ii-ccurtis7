# dieview.py
import sys
sys.path.insert(0, 'C:\\Users\\5007906431\\Dropbox (NSC)\\NSC\\fall2021\\cs135')
from graphics import *


class DieView():
    """
    DieView is a widget that displays a graphical representation of a standard
    six-sided die.
    """

    def __init__(self, win, center, size):
        """
        Create a view of a die, e.g.:
        d1 = DieView(myWin, Point(40,50), 20)
        creates a die centered at (40,50) having sides of length 20.
        """

        # first define some standard values
        self.win = win              # save this for drawing pips later
        self.background = 'white'   # color of die face
        self.foreground = 'black'   # color of the pips
        self.psize = 0.1*size      # radius of each pip
        hsize = size / 2.0          # half the size of the die
        offset = 0.6*hsize          # distance from center to outer pips

        # create a square for the face
        cx, cy = center.getX(), center.getY()
        p1 = Point(cx - hsize, cy - hsize)
        p2 = Point(cx + hsize, cy + hsize)
        self.rect = Rectangle(p1, p2)
        self.rect.draw(win)
        self.rect.setFill(self.background)

        # Create 7 circles for standard pip locations
        self.pips = [self.__makePip(cx-offset, cy-offset),
                    self.__makePip(cx-offset, cy),
                    self.__makePip(cx-offset, cy+offset),
                    self.__makePip(cx, cy),
                    self.__makePip(cx+offset, cy-offset),
                    self.__makePip(cx+offset, cy),
                    self.__makePip(cx+offset, cy+offset)]

        self.onTable = [ [], [3], [2, 4], [2, 3, 4], [0, 2, 4, 6],
                         [0, 2, 3, 4, 6], [0, 1, 2, 4, 5, 6]]

        # Draw an initial value
        self.setValue(1)

    def __makePip(self, x, y):
        "Internal helper method to draw a pip at (x,y)"
        pip = Circle(Point(x,y), self.psize)
        pip.setFill(self.background)
        pip.setOutline(self.background)
        pip.draw(self.win)
        return pip

    def setValue(self, value):
        "Set this die to display value."
        # turn all pips off
        for pip in self.pips:
            pip.setFill(self.background)

        # Turn the appropriate pips back on
        for i in self.onTable[value]:
            self.pips[i].setFill(self.foreground)

    def setColor(self, color):
        self.foreground = color
        for pip in self.pips:
            pip.setFill(self.foreground)
