from turtle import Turtle

FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        self.score = 0
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-290, 260)
        self.color("black")
        self.showScore()
           

    def showScore(self):
        self.write(f"Score: {self.score}", move=False, align="left", font=(FONT))


    def addScore(self):
        self.score += 1
        self.clear()
        self.showScore()

    def gameOver(self):
        self.penup()
        self.goto(0, 0)
        self.write(f"You lose!", move=False, align="center", font=(FONT))    


