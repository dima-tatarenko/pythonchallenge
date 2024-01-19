from tkinter import *

window = Tk()
window.title("Tkinter GUI")
window.minsize(width=500, height=300)
window.config(padx=200, pady=20)

# Labels




test_label = Label(text="meow")
test_label.grid(column=0, row=0)

# Ways to interact with label
# test_label["text"] = "New text"
# test_label.config(text="New text")

def button_clicked():
    test_label.config(text=input_text.get())


button = Button(text="Click", command=button_clicked)
button.grid(column=1, row=1)

button2 = Button(text="Argh", command=button_clicked)
button2.grid(column=2, row=0)

input_text = Entry()
input_text.grid(column=3, row=3)











window.mainloop()