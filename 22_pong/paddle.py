from turtle import Turtle

LEFT_PADDLE = (40, 20, 0, -20, -40)
RIGHT_PADDLE = (40, 20, 0, -20, -40)
LEFT_X = -580
RIGHT_X = 570


UP = 90
DOWN = 270

class Paddle:
    def __init__(self):
        self.paddle_left_body = []
        self.paddle_right_body = []
        self.create_paddle(LEFT_PADDLE, LEFT_X, self.paddle_left_body)
        self.create_paddle(RIGHT_PADDLE, RIGHT_X, self.paddle_right_body)
        self.bot_direction = None

        self.left_paddle_top = self.paddle_left_body[0]
        self.left_paddle_bottom = self.paddle_left_body[len(self.paddle_left_body) - 1]
        self.right_paddle_top = self.paddle_right_body[0]
        self.right_paddle_bottom = self.paddle_right_body[len(self.paddle_right_body) - 1]
        

    def create_paddle(self, yaxis, xaxis, paddle_body):
        for cord in yaxis:
            new_block = Turtle()
            new_block.shape("square")
            new_block.color("white")
            new_block.penup()
            new_block.goto(xaxis, cord)
            paddle_body.append(new_block)


    def left_up(self):
        self.left_paddle_top.setheading(UP)
        for block in range(len(self.paddle_left_body) - 1, 0, -1):
            new_x = self.paddle_left_body[block - 1].xcor()
            new_y = self.paddle_left_body[block - 1].ycor()
            self.paddle_left_body[block].goto(new_x, new_y)
        self.left_paddle_top.forward(20)


    def left_down(self):
        self.left_paddle_bottom.setheading(DOWN)
        for block in range(0, len(self.paddle_left_body) - 1, +1):
            new_x = self.paddle_left_body[block + 1].xcor()
            new_y = self.paddle_left_body[block + 1].ycor()
            self.paddle_left_body[block].goto(new_x, new_y)
        self.left_paddle_bottom.forward(20)


    def auto_up(self):
        self.right_paddle_top.setheading(UP)
        for block in range(len(self.paddle_right_body) - 1, 0, -1):
            new_x = self.paddle_right_body[block - 1].xcor()
            new_y = self.paddle_right_body[block - 1].ycor()
            self.paddle_right_body[block].goto(new_x, new_y)
        self.right_paddle_top.forward(20)


    def auto_down(self):
        self.right_paddle_bottom.setheading(DOWN)
        for block in range(0, len(self.paddle_right_body) - 1, +1):
            new_x = self.paddle_right_body[block + 1].xcor()
            new_y = self.paddle_right_body[block + 1].ycor()
            self.paddle_right_body[block].goto(new_x, new_y)
        self.right_paddle_bottom.forward(20)


    def botCheck(self):
        if self.right_paddle_top.ycor() > 290:
            self.bot_direction = False
            print(self.bot_direction)
            print("TOP")
        elif self.right_paddle_bottom.ycor() < -290:
            self.bot_direction = True
            print("BOTTOM")
            print(self.bot_direction)


        if self.bot_direction == True: 
            self.auto_up()
        elif self.bot_direction == False:
            self.auto_down()
        elif self.bot_direction == None:
            self.auto_down()    
           

        
            