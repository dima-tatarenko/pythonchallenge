from turtle import Turtle

SCORE = 0

class Scoreboard(Turtle):

    def __init__(self):
        self.score = 0
        super().__init__()

        

        self.hideturtle()
        self.goto(-290, 280)
        self.color("white")
        self.showScore()
           

    def showScore(self):
        self.write(f"Score: {self.score}", move=False, align="left", font=("Arial", 10, "normal"))


    def nomFood(self):
        self.score = self.score + 1
        self.clear()
        self.showScore()

    def gameOver(self):
        self.penup()
        self.goto(0, 0)
        self.write (f"You lose!", move=False, align="left", font=("Arial", 16, "normal"))    


