from turtle import Turtle
import random

COLORS = ["red", "orange", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

POSITIONS = (280, 300)


class CarManager:
    def __init__(self):
        self.garage = []
        self.traffic_speed = STARTING_MOVE_DISTANCE
        self.faster_traffic = MOVE_INCREMENT

        
    def add_car(self):
        create = random.randint(1, 6)
        if create != 1:
            return

        random_x = random.randint(300, 340)
        random_y = random.randint(-250, 250)
        
        new_car = Turtle("square")
        new_car.shapesize(stretch_wid=1, stretch_len=2)
        new_car.color(random.choice(COLORS))
        new_car.penup()
        new_car.goto(random_x, random_y)
        new_car.setheading(180)
        self.garage.append(new_car)


    def auto_move(self):
        for car in self.garage:
            car.forward(STARTING_MOVE_DISTANCE)


    def increase_speed(self):
        self.traffic_speed = self.traffic_speed + self.faster_traffic


            



        
        
        

        


