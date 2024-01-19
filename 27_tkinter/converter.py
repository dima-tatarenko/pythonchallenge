from tkinter import *

window = Tk()
window.title("Tkinter GUI")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)


def convert(gValue):
    return int(gValue * 0.62)


print(convert(10))

def on_click():
    miles = convert(int(initial_value.get()))
    result.config(text=miles)


initial_value = Entry()
initial_value.grid(column=2, row=0)

km_label = Label(text="Km")
km_label.grid(column=3, row=0)

equal = Label(text="is equal to")
equal.grid(column=0, row=1)

result = Label(text=0)
result.grid(column=2, row=1)

miles_label = Label(text="Miles")
miles_label.grid(column=3, row=1)


button = Button(text="Calculate", command=on_click)
button.grid(column=1, row=3)


window.mainloop()