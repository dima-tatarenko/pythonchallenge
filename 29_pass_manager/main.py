from tkinter import *
from tkinter import messagebox
import random

# Could import pyperclip to save password automatically so user can paste it
# to wherever they want to register

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


FONT = "Times New Roman"

pass_file = "E:/Programming/Python/daily_python/29_pass_manager/pw.txt"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def gen_pass():
    password_list = []
    [password_list.append(random.choice(letters)) for _ in range(random.randint(8, 10))]
    [password_list.append(random.choice(symbols)) for _ in range(random.randint(2, 4))]
    [password_list.append(random.choice(numbers)) for _ in range(random.randint(2, 4))]

    random.shuffle(password_list)
    password = "".join([char for char in password_list])

    pass_value.delete(0, END)
    pass_value.insert(0, password)



# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_pass():
    web = web_value.get()
    user = user_value.get()
    pw = pass_value.get()
    result = f"{web} | {user} | {pw} \n"

    if any(len(value) == 0 for value in [web, user, pw]):
        messagebox.showwarning(title="Empty fields", message="All fields must be complete.")
        return

    is_ok = messagebox.askokcancel(title=web, message=f"Are these details correct? \n{user} \n{pw} \nProceed?")
    if is_ok:
        with open(pass_file, mode="a") as file:
            file.write(result)
            web_value.delete(0, END)
            pass_value.delete(0, END)
    
    




def on_add():
    save_pass()


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)


canvas = Canvas(width=200, height=200)
lock = PhotoImage(file="E:/Programming/Python/daily_python/29_pass_manager/logo.png")
canvas.create_image(100, 100, image=lock)
canvas.grid(column=1, row=0)


#label group
web_label = Label(text="Website:", font=(FONT, 12, "bold"))
web_label.grid(column=0, row=1)

user_label = Label(text="Username:", font=(FONT, 12, "bold"))
user_label.grid(column=0, row=2)

pass_label = Label(text="Password:", font=(FONT, 12, "bold"))
pass_label.grid(column=0, row=3)

# value group
web_value = Entry(width=35)
web_value.grid(column=1, row=1, columnspan=2)
web_value.focus()
web_value.insert(0, "www.happy.com")

user_value = Entry(width=35)
user_value.grid(column=1, row=2, columnspan=2)
user_value.insert(0, "username@gmail.com")

pass_value = Entry(width=21)
pass_value.grid(column=1, row=3)
pass_value.insert(0, "asdf1234")

# Button group
start_button = Button(text="Generate password", command=gen_pass)
start_button.grid(column=2, row=3)

start_button = Button(text="Add", width=36, command=on_add)
start_button.grid(column=1, row=4, columnspan=2)





window.mainloop()