from turtle import Turtle, Screen
# import colorgram
import random

tim = Turtle()
tim.pen(pencolor="PaleGreen", pensize=10, speed=10)
tim.ht()

screen = Screen()
screen.colormode(255)

# unfiltered_colors = colorgram.extract('E:\Programming\Python\daily_python\\18_auto_paint\img.jpg', 5)

# colors = []

# for color in unfiltered_colors:
#     colors.append(color.rgb)

colors = ["PaleGreen", "PaleTurquoise", "PaleVioletRed", "Plum", "PeachPuff", "PowderBlue"]


def drawDot():
    tim.dot(20, random.choice(colors))
    tim.penup()
    tim.forward(50)
    tim.pendown()


def drawDotLine(yAxis):
    tim.penup()
    tim.goto(-250, yAxis)
    tim.pendown()
    for _ in range(10):
        drawDot()


def createPainting():
    yAxis = -250
    for _ in range(10):
        drawDotLine(yAxis)
        yAxis = yAxis + 50


createPainting()

screen.exitonclick()