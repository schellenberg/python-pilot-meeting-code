#Turtle Races
#Dan Schellenberg
#Oct 20, 2015

import turtle
import random

#declare important variables
startXLine = -225
finishXLine = 225

#setup the window
window = turtle.Screen()
window.bgcolor("lightgreen")

#setup the turtles
manav = turtle.Turtle()
adrian = turtle.Turtle()
theRef = turtle.Turtle()

manav.color("purple")
adrian.color("red")

manav.shape("turtle")
adrian.shape("turtle")
theRef.shape("square")

manav.penup()
adrian.penup()
theRef.penup()

#go to starting locations
manav.goto(startXLine, 50)
adrian.goto(startXLine, -50)
theRef.goto(finishXLine, 100)

#draw the finish line
theRef.pendown()
theRef.goto(finishXLine, -100)
theRef.hideturtle()

#do the actual race
raceStillGoing = True

while raceStillGoing == True:
    manavsStep = random.randint(1,5)
    manav.forward(manavsStep)

    adriansStep = random.randint(1,5)
    adrian.forward(adriansStep)

    if (manav.xcor() >= finishXLine) or (adrian.xcor() >= finishXLine):
        raceStillGoing = False
#    if adrian.xcor() >= finishXLine:
#        raceStillGoing = False

#print the winner
if manav.xcor() > adrian.xcor():
    print("Manav for the win!")
else:
    print("Adrian takes this one!")

window.mainloop()



