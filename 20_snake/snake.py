from turtle import Turtle

MOVE_DISTANCE = 20

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.snake_body = []
        self.create_snake()
        self.snek_direction = 0
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

    
    def auto_snake(self):
        for turtle in range(len(self.snake_body) - 1, 0, -1):
            new_x = self.snake_body[turtle - 1].xcor()
            new_y = self.snake_body[turtle - 1].ycor()
            self.snake_body[turtle].goto(new_x, new_y)
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