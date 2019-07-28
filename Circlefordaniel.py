import turtle
Window = turtle.Screen()
Window.bgcolor("blue")
Window.title("L'araignee")
TurtlePen = turtle.Pen()
Window.colormode(255)
TurtlePen.pencolor(255, 247, 0)
for counter in range(9000):
    TurtlePen.circle(counter)
    TurtlePen.left(45)
    if(counter > 50):
        TurtlePen.pensize(8)
        Window.bgcolor("blue")
    else:
        TurtlePen.pensize(18)
        Window.bgcolor("red")