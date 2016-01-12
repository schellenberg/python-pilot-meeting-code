import turtle

#setup window
theWindow = turtle.Screen()
theWindow.bgcolor("lightgreen")

#setup turtle
jaden = turtle.Turtle()
jaden.color("hotpink")
jaden.pensize(3)
jaden.speed(0)

#define functions
def drawSquare(aTurtle, size):
    for i in range(4):
        aTurtle.forward(size)
        aTurtle.left(90)

def pyramidTop(aTurtle, numberOfSides):
    sizeOfCurrentSquare = 20
    for aNumber in range(numberOfSides):
        drawSquare(aTurtle, sizeOfCurrentSquare)
        aTurtle.penup()
        aTurtle.right(90)
        aTurtle.forward(10)
        aTurtle.right(90)
        aTurtle.forward(10)
        aTurtle.right(180)
        aTurtle.pendown()
        sizeOfCurrentSquare = sizeOfCurrentSquare + 20

def drawRotatedSquares(aTurtle, size, numberOfSquares):
    for aNumber in range(numberOfSquares):
        drawSquare(aTurtle, size)
        aTurtle.right(360/numberOfSquares)

#draw the shape
#pyramidTop(jaden, 13)
drawRotatedSquares(jaden, 100, 50)

theWindow.mainloop()