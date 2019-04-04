import turtle
Window = turtle.Screen()
Window.bgcolor("black")
Window.title("Damien's super fun and boring game of code")
TurtlePen = turtle.Pen()
turtle.speed(10)
Window.colormode(255)
TurtlePen.pencolor(66, 134, 244)
for counter in range(9000):
    TurtlePen.circle(counter)
    TurtlePen.left(90)
    if(counter > 50):
        TurtlePen.pensize(5)
        Window.bgcolor("red")
    else:
        TurtlePen.pensize(20)
        Window.bgcolor("white")