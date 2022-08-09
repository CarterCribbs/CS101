'''
TurtleShapes.py

@author: Carter Cribbs
'''

import turtle, BoundingBox


def drawOneShape(turt, size):
    '''
    This function draws a star and takes
    parameters turt and size
    '''
    turt.pensize(4)
    turt.color("purple")
    turt.fillcolor("yellow")
    turt.begin_fill()
    for item in range(5):
        turt.left(72)
        turt.forward(size)
        turt.right(144)
        turt.forward(size)
    turt.end_fill()




def drawOneCompass(turt, size):
    '''
    This function draws a filled in compass
    using five different colors and takes parameters
    turt and size
    '''
    turt.color("light green")
    turt.fillcolor("light green")
    turt.begin_fill()
    for item in range(4):
        turt.forward(size)
        turt.right(90)
    turt.end_fill()
    turt.color("blue")
    turt.fillcolor("blue")
    turt.begin_fill()
    turt.left(60)
    turt.forward(size)
    turt.right(120)
    turt.forward(size)
    turt.right(30)
    turt.end_fill()
    turt.color("orange")
    turt.fillcolor("orange")
    turt.begin_fill()
    turt.left(60)
    turt.forward(size)
    turt.right(120)
    turt.forward(size)
    turt.right(30)
    turt.end_fill()
    turt.color("red")
    turt.fillcolor("red")
    turt.begin_fill()
    turt.left(60)
    turt.forward(size)
    turt.right(120)
    turt.forward(size)
    turt.right(30)
    turt.end_fill()
    turt.color("yellow")
    turt.fillcolor("yellow")
    turt.begin_fill()
    turt.left(60)
    turt.forward(size)
    turt.right(120)
    turt.forward(size)
    turt.right(30)
    turt.end_fill()






if __name__ == '__main__':
    win = turtle.Screen()
    BoundingBox.drawBoundingBox()
    cribbs = turtle.Turtle()
    drawOneCompass(cribbs, 75)
    cribbs.penup()
    cribbs.forward(-150)
    cribbs.pendown()
    drawOneShape(cribbs, 25)
    win.exitonclick()










