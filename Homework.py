import turtle
Window = turtle.Screen()
Window.bgcolor("black")
Window.title("Damien's super fun and boring game of code he did for homework")
TurtlePen = turtle.Pen()
turtle.speed(10)
Window.colormode(255)
TurtlePen.pencolor("white")
for counter in range(9000):
    TurtlePen.forward(counter)
    TurtlePen.left(20)
    if(counter > 50):
        TurtlePen.pensize(15)
    else:
        TurtlePen.pensize(20)
ChildProcessError
copyright
