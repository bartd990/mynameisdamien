"""
ColorSpiralInput.py -print a colorful spiral of users name
"""
# inport turtle graphics
import turtle
# T is for turtle pen
T = turtle.Pen()
T.speed = 10
turtle.bgcolor("red")
# set up a list of 7 valid Python color names
colors = ["black","yellow","blue","green","orange","violet","white"]
# ask user for the number of sides, between 1 and 8, with a default of 4
sides = int(turtle.numinput("Number of sides","How many sides do you want (1-7)?", 4, 1, 7))
# draw a colorful spiral with user-specified number of sides
for colorCounter in range(360):
    # print their name folled by a space, not a new line
    T.pencolor(colors[colorCounter % sides])
    # changes the size to match the number of sides
    T.forward(colorCounter*3 / sides+colorCounter)
    # turn 360 / sides + 1 degrees
    T.right(360 / sides + 1)
    # make pen larger as it goes outside
    T.width(colorCounter * sides / 200)