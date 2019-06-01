import turtle
Window = turtle.Screen()
Window.bgcolor("black")
Window.title("Spiral your name")
colors = ["blue violet", "dark olive green", "dodger blue", "gold4"]
TurtlePen = turtle.Pen()
turtle.speed(10)
# TurtlePen.pencolor("red")
your_name = turtle.textinput("Enter your name please","What is your name?")
for counter in range(100):
    TurtlePen.pencolor(colors[counter % 4])
    TurtlePen.penup()
    TurtlePen.forward(counter*4)
    TurtlePen.pendown()
    TurtlePen.write(your_name, font=("Edwardian Script ITC Regular", int((counter+4)/4), "bold"))
    TurtlePen.left(145)
    # Last prodgect
    # TurtlePen.forward(counter)
    # TurtlePen.left(145)
    # if(counter > 50):
    #     TurtlePen.pensize(15)
    #     Window.bgcolor("blue")
    # else:
    #     TurtlePen.pensize(20)
    #     Window.bgcolor("white")
    