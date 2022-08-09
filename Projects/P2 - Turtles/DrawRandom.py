'''
DrawRandom.py

@author: Carter Cribbs
'''

import turtle, BoundingBox, random, TurtleShapes


def drawEverywhere(turt, func):
    '''
    This function draws a shape chosen by the user
    at random locations, a certain number of times also
    specifed by the user
    '''
    numberofshapes = int(input("number of shapes to be drawn"))
    for item in range(numberofshapes):
        xcoordinate = random.randint(-250, 250)
        ycoordinate = random.randint(-180, 180)
        size = random.randint(15, 70)
        turt.penup()
        turt.goto(xcoordinate, ycoordinate)
        turt.pendown()
        func(turt, size)



if __name__ == '__main__':
    win = turtle.Screen()
    BoundingBox.drawBoundingBox()
    cribbs = turtle.Turtle()
    choice = int(input("Choose 0 to draw a compass or Choose 1 to draw a "
                       "star"))
    '''
    Gives user the choice to draw a compass or a star
    '''
    if choice == 0:
        drawEverywhere(cribbs, TurtleShapes.drawOneCompass)
    else:
        drawEverywhere(cribbs, TurtleShapes.drawOneShape)
    win.exitonclick()









