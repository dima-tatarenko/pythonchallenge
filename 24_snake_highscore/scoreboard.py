from turtle import Turtle

SCORE = 0

class Scoreboard(Turtle):

    def __init__(self):
        self.score_path = "e:/Programming/Python/daily_python/24_snake_highscore/score.txt"
        self.score = 0
        self.high_score = 0
        super().__init__()

        with open(self.score_path) as file:
            self.high_score = file.read()

        self.hideturtle()
        self.goto(-290, 280)
        self.color("white")
        self.update_board()
    

    def inc_score(self):
        self.score = self.score + 1
        self.update_board()

    def update_board(self):
        self.clear()
        self.write(f"Score: {self.score} High score: {self.high_score}", move=False, align='left', font=('Arial', 10, 'normal'))

    
    def reset(self):
        if self.score > int(self.high_score):
            self.high_score = self.score

        with open(self.score_path, mode="w") as file:
            file.write(str(self.high_score))

        self.score = 0
        self.update_board()

    # def gameOver(self):
    #     self.penup()
    #     self.goto(0, 0)
    #     self.write (f"You lose!", move=False, align="left", font=("Arial", 16, "normal"))    


