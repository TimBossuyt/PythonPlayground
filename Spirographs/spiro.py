import math
import turtle

def drawcircle(r):
    turtle.up()
    turtle.setpos(r, 0)
    turtle.down()

    for i in range(0, 365):
        a = math.radians(i)
        x = math.cos(a) * r
        y = math.sin(a) * r
        turtle.setpos(x, y)


def drawspiro(R, r, l):
    turtle.up()
    turtle.setpos(R + r, 0)
    turtle.down()
    k = r/float(R)

    for i in range(0, 2000):
        t = math.radians(i)

        x = R*((1 - k)*math.cos(t) + l*k*math.cos((1-k)*t/k))
        y = R*((1 - k)*math.sin(t) - l*k*math.sin((1-k)*t/k))
        turtle.setpos(x, y)



drawspiro(100, 30, 5)
turtle.mainloop()




