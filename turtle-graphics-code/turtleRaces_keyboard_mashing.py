#Turtle Races

import turtle
import random

finishLineX = 200

#setup window
theWindow = turtle.Screen()
theWindow.bgcolor("lightgreen")

#setup turtles that will race
steven = turtle.Turtle()
harry = turtle.Turtle()
steven.shape("turtle")
harry.shape("turtle")
steven.color("black")
harry.color("white")
steven.penup()
harry.penup()
harry.goto(-200,100)
steven.goto(-200,-100)

#setup turtle to draw finish line
theRef = turtle.Turtle()
theRef.hideturtle()
theRef.penup()
theRef.goto(finishLineX,200)
theRef.pendown()
theRef.goto(finishLineX,-200)

#actually run the race
areTheyStillRacing = True

def stevenMoves():
    stevenRandomStep = random.randint(1,5)
    steven.forward(stevenRandomStep)

def harryMoves():
    harryRandomStep = random.randint(1,5)
    harry.forward(harryRandomStep)


theWindow.onkey(stevenMoves, "s")
theWindow.onkey(harryMoves, "h")
theWindow.listen()




#    if steven.xcor() > finishLineX:
#        areTheyStillRacing = False
#    if harry.xcor() > finishLineX:
#        areTheyStillRacing = False

theWindow.mainloop()