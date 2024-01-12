import time
from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Play Snake")
screen.tracer(0)

gameOn = True

#Temporary initial setup

turtle_army = []
turtle_initial = 0

for _ in range(3):
    new_turtle = Turtle()
    new_turtle.shape("square")
    new_turtle.color("white")
    new_turtle.penup()
    new_turtle.goto(x=turtle_initial, y=0)
    turtle_initial = turtle_initial - 20

    turtle_army.append(new_turtle)

screen.update()

while gameOn:
    screen.update()
    time.sleep(0.3)
    for turtle in range(len(turtle_army) - 1, 0, -1):
        new_x = turtle_army[turtle - 1].xcor()
        new_y = turtle_army[turtle - 1].ycor()
        turtle_army[turtle].goto(new_x, new_y)
    turtle_army[0].forward(20)





screen.exitonclick()