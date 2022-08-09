'''
DrawRow.py

@author: Carter Cribbs
'''

import turtle, BoundingBox, TurtleShapes


def drawRowsOfRows(turt, func):
    '''
    This function draws 11 rows of a shape chosen by the user.
    Each row has at least 10 shapes. Every shape on each row
    is the same size and different rows have different size shapes.
    '''
    orginalxcoordinate = -320
    xcoordinate = -320
    ycoordinate = 250
    turt.speed(0)
    turt.penup()
    turt.goto(xcoordinate, ycoordinate)
    size = 10
    xcoordinateincrement = 50
    ycoordinateincrement = 35
    for item in range(11):
        turt.pendown()
        while xcoordinate < 300:
            xcoordinate = xcoordinate + xcoordinateincrement
            func(turt, size)
            turt.penup()
            turt.goto(xcoordinate, ycoordinate)
            turt.pendown()
        turt.penup()
        ycoordinate = ycoordinate - ycoordinateincrement
        turt.goto(orginalxcoordinate, ycoordinate)
        xcoordinate = -300
        size = size + 1.75
        xcoordinateincrement = xcoordinateincrement*1.025
        ycoordinateincrement = ycoordinateincrement*1.04




if __name__ == '__main__':
    win = turtle.Screen()
    BoundingBox.drawBoundingBox()
    cribbs=turtle.Turtle()
    drawRowsOfRows(cribbs, TurtleShapes.drawOneCompass)
    win.exitonclick()







