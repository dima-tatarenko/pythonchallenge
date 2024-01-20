from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
timer = None
reps = 1
check_text = ""

# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    global reps
    global check_text

    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text=f"00:00")

    reps = 1
    check_text = ""
    check_icon.config(text=check_text)


    

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps
    global check_text

    # Didn't use real timer for obvious reasons. 
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60


    if reps == 5:
        check_text = check_text + "✔"
        check_icon.config(text=check_text)
        timer_label.config(text="Break", fg=RED)
        count_down(3)
        print("meow")
        print(reps)
        reps = 0
    elif reps % 2 != 0:
        timer_label.config(text="Work", fg=GREEN)
        print("meow")
        print(reps)
        count_down(5)
    elif reps % 2 == 0:
        check_text = check_text + "✔"
        check_icon.config(text=check_text)
        timer_label.config(text="Break", fg=PINK)
        print("meow")
        print(reps)
        count_down(2)
    

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 



def count_down(count):
    global timer
    global reps
    global check_text

    count_min = math.floor(count / 60)
    count_sec = count % 60

    # teacher's solution
    # if count_sec < 10:
    #     count_sec = f"0{count_sec}"

    if count_min in range(0,10):
        count_min = f"0{count_min}"

    if count_sec in range(0,10):
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count >= 0:
        timer = window.after(1000, count_down, count -1)

    if count == -1:
        if reps == 0:
            check_text = ""
            check_icon.config(text=check_text)

        reps += 1
        start_timer()

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)




timer_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 35, "bold"))
timer_label.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
le_tomato = PhotoImage(file="E:/Programming/Python/daily_python/28_pomodoro/tomato.png")
canvas.create_image(100, 112, image=le_tomato)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)



start_button = Button(text="Start", command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", command=reset_timer)
reset_button.grid(column=2, row=2)

check_icon = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 20))
check_icon.grid(column=1, row=3)



window.mainloop()