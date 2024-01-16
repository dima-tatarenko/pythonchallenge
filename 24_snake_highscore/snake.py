import turtle
from turtle import Turtle

MOVE_DISTANCE = 20

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.snake_body = []
        # self.image = "D:/snake.gif"
        self.create_snake()
        self.head = self.snake_body[0]
        

    def create_snake(self):  
        turtle_initial = 0

        for _ in range(3):
            new_turtle = Turtle()
            new_turtle.shape("square")
            new_turtle.color("white")
            new_turtle.penup()
            new_turtle.goto(x=turtle_initial, y=0)
            turtle_initial = turtle_initial - 20

            self.snake_body.append(new_turtle)
        # turtle.register_shape(self.image)
        # self.snake_body[0].shape(self.image) 

    
    def auto_snake(self):
        for part in range(len(self.snake_body) - 1, 0, -1):
            new_x = self.snake_body[part - 1].xcor()
            new_y = self.snake_body[part - 1].ycor()
            self.snake_body[part].goto(new_x, new_y)
        self.snake_body[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.snake_body[0].setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.snake_body[0].setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.snake_body[0].setheading(RIGHT)

    def addBody(self):
        new_turtle = Turtle()
        new_turtle.shape("square")
        new_turtle.color("white")
        new_turtle.penup()
        self.snake_body.append(new_turtle)   

    def ouroborosCheck(self):
        for part in self.snake_body[1:]:
            if self.head.distance(part) < 10:
                return True
            

    def reset(self):
        for part in self.snake_body:
            part.goto(2000, 2000)
        self.snake_body.clear()
        self.create_snake()
        self.head = self.snake_body[0]        
