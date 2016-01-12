import turtle

#setup the window
theWindow = turtle.Screen()
theWindow.bgcolor("lightgreen")

#setup the turtle
kathrin = turtle.Turtle()
kathrin.shape("turtle")
kathrin.color("blue")
kathrin.pensize(5)
kathrin.speed(0)

#draw the shape
for aNumber in range(4):
    for theAngle in [90,270,90]:
        kathrin.forward(100)
        kathrin.left(theAngle)


theWindow.mainloop()