import turtle, random

theWindow = turtle.Screen()
theWindow.colormode(255)

jacob = turtle.Turtle()
jacob.speed(0)

for i in range(36):
    redStuff = random.randint(0,255)
    greenStuff = random.randint(0,255)
    blueStuff = random.randint(0,255)

    jacob.color(redStuff, blueStuff, greenStuff)
    jacob.forward(300)
    jacob.left(170)

theWindow.mainloop()


