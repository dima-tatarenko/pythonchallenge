# First exercise - write down how you're going to approach it.

# All of the elements seem to be turtle based (even the score feels like turtle art)
# Platforms: turtle 20x20, move up and down on click. Need to figure out keypress down
# Pong ball is a head that auto travells all the time. It only bounces from platforms.
# Losing condition: pong ball goes over -number in X axis or +number on the other side.
# This would be an easy way to track score

# class - pong board, can be recycled for both.
# class - pong ball
# class - scoreboard

# The only thing that feels weird is the separation line in the middle.
# Not sure if it's simply visual or it has something more to it.

# Important idea: to move the paddle up and down - create a function
# which takes "head" as a parameter and simply change from first position
# in the array and then last

import time
from turtle import Screen
from paddle import Paddle
from ball import Ball

screen = Screen()
screen.setup(width=1200, height=600)
screen.bgcolor("black")
screen.title("PONG")
screen.tracer(0) # Allows for manual update (screen)


screen.listen()


gameOn = True

paddle = Paddle()
ball = Ball()
screen.update()

screen.onkey(paddle.left_up, "w")
screen.onkey(paddle.left_down, "s")



def paddle_check():
    for block in paddle.paddle_left_body:
        if ball.distance(block) < 40:
            ball.bounce_x()
    for block in paddle.paddle_right_body:
        if ball.distance(block) < 40:
            ball.bounce_x()


while gameOn == True:
    screen.update()
    time.sleep(0.1)

    paddle.botCheck()
    ball.auto_move()
    paddle_check()

    ball.x_border()
    ball.y_border()

    if ball.x_border() == "player":
        print("Player scores a point!")
        ball.reset_ball()
    elif ball.x_border() == "computer":
        print("Computer scores a point!")
        ball.reset_ball()











screen.exitonclick()

