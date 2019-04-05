import turtle
Window = turtle.Screen()
Window.bgcolor("black")
Window.title("Damien's super fun and boring game of code")
TurtlePen = turtle.Pen()
turtle.speed(10)
Window.colormode(255)
TurtlePen.pencolor(66, 134, 244)
for counter in range(9000):
    TurtlePen.forward(counter)
    TurtlePen.left(60)
    if(counter > 50):
        turtle.speed(10)
        TurtlePen.pensize(15)
        Window.bgcolor("red")
    else:
        TurtlePen.pensize(20)
        Window.bgcolor("white")
ChildProcessError
copyright
