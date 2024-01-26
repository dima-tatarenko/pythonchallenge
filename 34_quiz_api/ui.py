from tkinter import *

THEME_COLOR = "#375362"
FONT = "Arial"
CORRECT_IMG = "E:/Programming/Python/daily_python/34_quiz_api/images/true.png"
WRONG_IMG = "E:/Programming/Python/daily_python/34_quiz_api/images/false.png"

class QuizInterface:

    def __init__(self):
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        score_label = Label(text="Score: 0", font=(FONT, 12, "bold"))
        score_label.grid(column=0, row=0, pady=50)

        canvas = Canvas(width=300, height=250, bg="white", highlightthickness=0)
        question_text = canvas.create_text(150, 125, text="meow", font=(FONT, 20, "italic"), fill=THEME_COLOR)
        canvas.grid(column=0, row=1, columnspan=2)

        correct_image = PhotoImage(file=CORRECT_IMG)
        correct_button = Button(text="", image=correct_image)
        correct_button.grid(column=0, row=2, pady=50)

        wrong_image = PhotoImage(file=WRONG_IMG)
        wrong_button = Button(text="", image=wrong_image)
        wrong_button.grid(column=1, row=2, pady=50)

        self.window.mainloop()

    def update_score(self, score):
        self.score_label.config(text=f"Score: {score}")

    
    def update_question(self, question):
        self.canvas.itemconfig(self.question_text, text=question)