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

#draw the clock
for aNumber in range(12):
    kathrin.penup()
    kathrin.forward(100)
    kathrin.pendown()
    kathrin.forward(15)
    kathrin.penup()
    kathrin.forward(20)
    kathrin.stamp()
    kathrin.backward(135)
    kathrin.left(360/12)

#kathrin.stamp()
#kathrin.forward(100)

theWindow.mainloop()