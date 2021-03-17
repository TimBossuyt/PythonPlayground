import math
import turtle




def drawspiro(R, r, l):
    turtle.shape('turtle')
    turtle.up()
    turtle.setpos(R, 0)
    turtle.down()
    k = r/float(R)

    for i in range(0, 10000):
        t = math.radians(i)

        x = R*((1 - k)*math.cos(t) + l*k*math.cos((1-k)*t/k))
        y = R*((1 - k)*math.sin(t) - l*k*math.sin((1-k)*t/k))
        turtle.setpos(x, y)



drawspiro(297, 32, 5)
turtle.mainloop()




