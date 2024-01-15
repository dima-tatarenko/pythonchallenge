import time
import random
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

# Initialize player
player = Player()
player.create_turtle()

# Initialize cars
traffic = CarManager()

# Initialize scoreboard
score = Scoreboard()






screen.listen()
screen.onkey(player.move,"w")

  

gameOn = True
while gameOn:
    time.sleep(0.1)
    screen.update()
    
    traffic.add_car()
    traffic.auto_move()

    for car in traffic.garage:
        if car.distance(player.turtle) < 20:
                gameOn = False
                score.gameOver()

    if player.turtle.ycor() > 270:
        player.reset_player()
        score.addScore()
        traffic.increase_speed()
            

screen.exitonclick()

