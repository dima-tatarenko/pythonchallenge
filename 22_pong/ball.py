from turtle import Turtle
from paddle import Paddle
import random

BALL_SPEED = 20
POSSIBLE_DIRECTIONS = (-20, 20)

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("green")
        self.speed("fastest")
        self.goto(0, 0)
        self.x_move = random.choice(POSSIBLE_DIRECTIONS)
        self.y_move = random.choice(POSSIBLE_DIRECTIONS)
        
        
        # self.right(random.randint(0, 360))

    
    def auto_move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    
    def bounce_y(self):
        self.y_move *= -1

    
    def bounce_x(self):
        self.x_move *= -1
       

    def reset_ball(self):
        self.goto(0, 0)
        self.bounce_x()


    def x_border(self):
        if self.xcor() > 620 or self.xcor() < -620:
            if self.xcor() > 620:
                return "player"
            elif self.xcor() < -620:
                return "computer" 
        
        
    def y_border(self):
        if self.ycor() > 280 or self.ycor() < -280:
            self.bounce_y()
            


        
        