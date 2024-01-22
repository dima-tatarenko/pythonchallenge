from tkinter import *
from tkinter import messagebox
import random
import json

# Working with JSON
# json.dump() -> write
# json.load() -> read
# json.update() -> update

# Could import pyperclip to save password automatically so user can paste it
# to wherever they want to register

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


FONT = "Times New Roman"

pass_file = "E:/Programming/Python/daily_python/29_pass_manager/pw.txt"
pass_json = "E:/Programming/Python/daily_python/30_pass_manager_update/pw.json"

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
    result = {
        web: {
            "user":user,
            "pw":pw
        }
    }


    # Could be simplified with a separate function
    # This works as an explanation in one place.

    if any(len(value) == 0 for value in [web, user, pw]):
        messagebox.showwarning(title="Empty fields", message="All fields must be complete.")
        return
    else:
        try:
            with open(pass_json, mode="r") as file:
                data = json.load(file)
        except FileNotFoundError:
            with open(pass_json, mode="w") as file:
                json.dump(result, file, indent=4)
        else:
            data.update(result)

            with open(pass_json, mode="w") as file:
                json.dump(data, file, indent=4)
        finally:    
            web_value.delete(0, END)
            pass_value.delete(0, END)

    
    
def on_add():
    save_pass()


# ---------------------------- UI SETUP ------------------------------- #
    
def search_pass():
    with open(pass_json, mode="r") as file:
        data = json.load(file)
    if web_value.get() in data:
        result = data[web_value.get()]
        print(result)
        messagebox.showinfo(title="User information", message=f"Username: {result["user"]} \nPassword: {result["pw"]}")
    else:
        messagebox.showinfo(title="Error", message=f"{web_value.get()} doesn't exist.")
        


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
web_value = Entry(width=21)
web_value.grid(column=1, row=1)
web_value.focus()
web_value.insert(0, "www.happy.com")

user_value = Entry(width=40)
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

search_button = Button(text="Search", command=search_pass)
search_button.grid(column=2, row=1)





window.mainloop()