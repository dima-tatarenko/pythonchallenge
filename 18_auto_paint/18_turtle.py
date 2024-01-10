from turtle import Turtle, Screen
import random

tim = Turtle()
screen = Screen()
screen.colormode(255)

tim.shape("turtle")
tim.color("PaleTurquoise")

colors = ["PaleGreen", "PaleTurquoise", "PaleVioletRed", "Plum", "PeachPuff", "PowderBlue"]

tim.pen(pencolor="pink", pensize=10, speed=10)
# def drawSquare():
#     for _ in range(4):
#         tim.forward(100)
#         tim.right(90)

# drawSquare()

# def drawDash():
#     for _ in range(10):
#         tim.forward(10)
#         tim.penup()
#         tim.forward(10)
#         tim.pendown()

# drawDash()

# Calculate degree of a figure
# 360 / 4 for square, 360 / 5 for pentagon



# Create figures (square, pentagon and so on)
# def drawFigure(timesRep):
#     for _ in range(timesRep):
#         tim.forward(100)
#         tim.right(360 / timesRep)
    

# def drawAll():
#     starting_sides = 3
#     total_figures = 6
#     counter = starting_sides

#     for _ in range(total_figures):
#         drawFigure(counter)
#         tim.pencolor(colors[counter - starting_sides])
#         counter += 1

# drawAll()




# Make the turtle breakdance (aka Random Walk)
# possible_directions = [0, 90, 180, 270]

def randomColors():
    return (random.randint(1,255), random.randint(1,255), random.randint(1,255))

# def moveRandom():
#         randirection = random.choice(possible_directions)
#         tim.pencolor(randomColors())
#         tim.right(randirection)
#         tim.forward(20)
        
        

# for _ in range(100):
#     moveRandom()



# Random circles

def drawCircle(circleGap):
    tim.circle(100)
    tim.right(360 / circleGap)
    # I understand how to use random colors, but I don't really like them
    # tim.pencolor(randomColors())
    tim.pencolor(random.choice(colors))


def drawCircles(totalCircles):  
    for _ in range(totalCircles):
        drawCircle(totalCircles)

drawCircles(8)


screen.exitonclick()