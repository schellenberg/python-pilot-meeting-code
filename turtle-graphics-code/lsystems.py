#L-Systems
#Nov 4, 2015

import turtle

def applyRules(character):
    if character == "F":
        newCharacter = "FF"
    elif character == "X":
        newCharacter = "--FXF++FXF++FXF--"
    else:
        newCharacter = character
    return newCharacter

def processString(theString):
    newString = ""
    for theLetter in theString:
        newString += applyRules(theLetter)
    return newString

def createLSystem(axiom, depth):
    endingString = axiom
    for i in range(depth):
        endingString = processString(endingString)
    return endingString

def drawLSystem(aTurtle, instructions, angle, distance):
    for theCommand in instructions:
        if theCommand == "F":
            aTurtle.forward(distance)
        elif theCommand == "B":
            aTurtle.backward(distance)
        elif theCommand == "+":
            aTurtle.right(angle)
        elif theCommand == "-":
            aTurtle.left(angle)

theWindow = turtle.Screen()
theWindow.screensize(10000,10000)
theWindow.tracer(3)    #only update window every 10 frames
adrian = turtle.Turtle()
adrian.speed(0)

adrian.penup()
adrian.goto(-450,-300)
adrian.pendown()

theInstructions = createLSystem("FXF--FF--FF", 7)
drawLSystem(adrian, theInstructions, 60, 5)

theWindow.mainloop()