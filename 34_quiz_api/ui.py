from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT = "Arial"
CORRECT_IMG = "E:/Programming/Python/daily_python/34_quiz_api/images/true.png"
WRONG_IMG = "E:/Programming/Python/daily_python/34_quiz_api/images/false.png"

class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain ):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text="Score: 0", font=(FONT, 12, "bold"))
        self.score_label.grid(column=0, row=0, pady=50)

        self.canvas = Canvas(width=300, height=250, bg="white", highlightthickness=0)
        self.question_text = self.canvas.create_text(150, 125, width=280, text="meow", font=(FONT, 20, "italic"), fill=THEME_COLOR)
        self.canvas.grid(column=0, row=1, columnspan=2)

        correct_image = PhotoImage(file=CORRECT_IMG)
        self.correct_button = Button(text="", image=correct_image, command=self.click_true)
        self.correct_button.grid(column=0, row=2, pady=50)

        wrong_image = PhotoImage(file=WRONG_IMG)
        self.wrong_button = Button(text="", image=wrong_image, command=self.click_false)
        self.wrong_button.grid(column=1, row=2, pady=50)

        self.get_next_q()

        self.window.mainloop()

    def update_score(self, score):
        self.score_label.config(text=f"Score: {score}")

    
    def get_next_q(self):
        if not self.quiz.still_has_questions():
            self.canvas.config(bg="white")
            self.correct_button.config(state="disabled")
            self.wrong_button.config(state="disabled")
            self.canvas.itemconfig(self.question_text, text=f"That's the end of the quiz! Score: {self.quiz.score}/10")
            return

        self.canvas.config(bg="white")
        self.update_score(self.quiz.score)
        q_text = self.quiz.next_question()
        self.canvas.itemconfig(self.question_text, text=q_text)

    
    def click_true(self):
        self.give_feedback(self.quiz.check_answer("True"))
    

    def click_false(self):
        self.give_feedback(self.quiz.check_answer("False"))

    
    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
            self.window.after(1000, )
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_q)
        