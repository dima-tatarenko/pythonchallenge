from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)

colors = ["PaleGreen", "PaleTurquoise", "PaleVioletRed", "Plum", "PeachPuff", "PowderBlue"]
gameOn = False
turtles = []
turtle_initial = -150

# Initial setup
for color in colors:
    original_color = color
    color = Turtle()
    color.shape("turtle")
    color.color(original_color)
    turtles.append(color)


for turtle in turtles:
    turtle.penup()
    turtle.goto(x=-230, y=turtle_initial)
    turtle_initial = turtle_initial + 50

user_turtle = screen.textinput(title="Make your bet", prompt=f"Which turtle will win the race? Possible colors: {colors}. ")

if user_turtle:
    gameOn = True
# Initial setup


def checkVictory(givenColor):
    if user_turtle == givenColor:
        print("You win!")
    else:
        print("You lose!")


while gameOn:

    for turtle in turtles:
        if turtle.xcor() > 220:
            print(user_turtle)
            print(turtle.pencolor())
            gameOn = False
            checkVictory(turtle.pencolor())

        turtle.forward(random.randint(0, 10))


screen.exitonclick()