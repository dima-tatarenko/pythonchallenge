from tkinter import *
import pandas
import random
import json

BACKGROUND_COLOR = "#B1DDC6"
FONT = "Arial"

card_front = "E:/Programming/Python/daily_python/31_flashcard/images/card_front.png"
card_back = "E:/Programming/Python/daily_python/31_flashcard/images/card_back.png"
right_b = "E:/Programming/Python/daily_python/31_flashcard/images/right.png"
wrong_b = "E:/Programming/Python/daily_python/31_flashcard/images/wrong.png"

fw_file = "E:/Programming/Python/daily_python/31_flashcard/data/french_words.csv"
learnt_file = "E:/Programming/Python/daily_python/31_flashcard/data/learnt_list.json"

french_data = pandas.read_csv(fw_file)
learnt_data = {}






# This was me, figuring out how to access the data I need.
# print(french_data)
# print(random.choice(french_data["French"]))
# print(french_data.iloc[100])

# test = french_data.iloc[100]
# print(test["French"])
# print(test["English"])



# ---------------------------- Functions ------------------------------- #

current_words = ""

def random_word():
    global current_words, learnt_data
    with open(learnt_file, mode="r") as file:
        learnt_data = json.load(file)

    
    current_words = french_data.iloc[random.randint(0, len(french_data)-1)]
    if current_words["French"] in learnt_data:
        print("MEOW")
        print(current_words)
        random_word()


def show_original():
    canvas.itemconfig(card_background, image=front)
    canvas.itemconfig(language_text, text="French")
    random_word()
    global current_words
    original = current_words["French"]
    canvas.itemconfig(word_text, text=f"{original}")
    

def show_solution():
    canvas.itemconfig(card_background, image=back)
    canvas.itemconfig(language_text, text="English")
    global current_words
    solution = current_words["English"]
    canvas.itemconfig(word_text, text=f"{solution}")


def mark_learnt():
    global current_words
    result = {f"{current_words["French"]}":f"{current_words["English"]}"}

    with open(learnt_file, mode="r") as file:
        data = json.load(file)
        data.update(result)

    with open(learnt_file, mode="w") as file:
        json.dump(data, file, indent=4)


def check_progress():
    global flip_timer, learnt_data
    if len(learnt_data) == len(french_data):
        canvas.itemconfig(language_text, text="No more words to learn!")
        canvas.itemconfig(word_text, text="")
        window.after_cancel(flip_timer)
        return True


def click_yes():
    print(len(learnt_data))
    print(len(french_data))
    if check_progress():
        return
    
    global flip_timer
    window.after_cancel(flip_timer)
    mark_learnt()
    flip_timer = window.after(3000, show_solution)
    show_original()
    
    
def click_no():
    if check_progress():
        return

    global flip_timer
    window.after_cancel(flip_timer)
    show_original()
    flip_timer = window.after(3000, show_solution)


# ---------------------------- UI ------------------------------- #

window = Tk()
window.title("Flash card game")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=show_solution)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)

front = PhotoImage(file=card_front)
back = PhotoImage(file=card_back)
card_background = canvas.create_image(410, 263, image=front)
language_text = canvas.create_text(400, 150, text="French", fill="black", font=(FONT, 40, "italic")) 
word_text = canvas.create_text(400, 263, text="Example", fill="black", font=(FONT, 60, "bold")) 
canvas.grid(column=1, row=1, columnspan=2)

yes_image = PhotoImage(file=right_b)
yes_button = Button(text="", image=yes_image, command=click_yes, highlightthickness=0, bg=BACKGROUND_COLOR)
yes_button.grid(column=1, row=2, pady=50)

no_image = PhotoImage(file=wrong_b)
no_button = Button(text="", image=no_image, command=click_no, highlightthickness=0)
no_button.grid(column=2, row=2, pady=50)

click_no()


window.mainloop()