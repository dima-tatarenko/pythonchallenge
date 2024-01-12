import time
from turtle import Turtle, Screen
from snake import Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Play Snake")
screen.tracer(0)

gameOn = True

snake = Snake()
screen.update()

screen.listen()
screen.onkey(snake.up, "w")
screen.onkey(snake.left, "a")
screen.onkey(snake.down, "s")
screen.onkey(snake.right, "d")

while gameOn:
    screen.update()
    time.sleep(0.3)
    snake.auto_snake()


screen.exitonclick()