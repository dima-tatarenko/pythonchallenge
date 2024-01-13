import time
from turtle import Turtle, Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Play Snake")
screen.tracer(0)

gameOn = True

snake = Snake()
food = Food()
scoreboard = Scoreboard()
screen.update()

screen.listen()
screen.onkey(snake.up, "w")
screen.onkey(snake.left, "a")
screen.onkey(snake.down, "s")
screen.onkey(snake.right, "d")

while gameOn:
    screen.update()
    time.sleep(0.1)
    snake.auto_snake()

    # Detecting collision with food
    if snake.head.distance(food) < 15:
        food.refreshFood()
        scoreboard.nomFood()
        scoreboard.showScore()
        snake.addBody()

    # Detecting collision with the walls
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        scoreboard.gameOver()   
        gameOn = False


    # Detect collision with tail
    if snake.ouroborosCheck():
        scoreboard.gameOver()   
        gameOn = False


screen.exitonclick()