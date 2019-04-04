import turtle
Window = turtle.Screen()
Window.bgcolor("black")
Window.title("Damien's super fun and boring game of code called 'Color Square Spiral'")
Color = ["blue violet", "dark olive green", "dodger blue", "gold4"]
TurtlePen = turtle.Pen()
turtle.speed(10)
# TurtlePen.pencolor("red")
for counter in range(9000):
    TurtlePen.pencolor("red")
    TurtlePen.forward(counter)
    TurtlePen.left(90)
    if(counter > 50):
        TurtlePen.pensize(15)
        Window.bgcolor("blue")
    else:
        TurtlePen.pensize(20)
        Window.bgcolor("white")