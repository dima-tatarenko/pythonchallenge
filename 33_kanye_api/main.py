from tkinter import *
import requests


kanye_quote = ""


def get_quote():
    # Kanye API data
    global kanye_quote
    print(kanye_quote)
    response = requests.get(url="https://api.kanye.rest")
    data = response.json()
    kanye_quote = data["quote"]
    canvas.itemconfig(quote_text, text=kanye_quote)


window = Tk()
window.title(f"Kanye Says...")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file="E:/Programming/Python/daily_python/33_kanye_api/background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text=kanye_quote, width=250, font=("Arial", 30, "bold"), fill="white")
canvas.grid(row=0, column=0)

kanye_img = PhotoImage(file="E:/Programming/Python/daily_python/33_kanye_api/kanye.png")
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)

get_quote()



window.mainloop()