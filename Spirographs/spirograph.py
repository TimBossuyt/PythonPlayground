import turtle
import math


class Spiro:
    def __init__(self, xc, yc, col, R, r, l):

        self.t = turtle.Turtle()
        self.t.shape('turtle')

        self.step = 5

        self.drawingComplete = False

        #set the parameters
        self.setparams(xc, yc, col, R, r, l)



        self.restart()

    def setparams(self, xc, yc, col, R, r, l):
        self.xc = xc
        self.yc = yc
        self.R = int(R)
        self.r = int(r)
        self.