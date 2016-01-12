import turtle

#turtle setup
theWindow = turtle.Screen()
avani = turtle.Turtle()
avani.pencolor("blue")

#draw the star
for i in range(5):
    avani.right(144)
    avani.forward(150)

theWindow.mainloop()