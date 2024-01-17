from turtle import Turtle, Screen
import pandas

us_image = "E:/Programming/Python/daily_python/25_states_game/blank_states_img.gif"
states_csv = "E:/Programming/Python/daily_python/25_states_game/50_states.csv"

states_data = pandas.read_csv(states_csv)
state_list = states_data["state"]
guessed_list = []


# gray_squirrel_count = squirrel_data[squirrel_data["Primary Fur Color"] == "Gray"]

turtle = Turtle()

screen = Screen()
screen.title("US States Game")
screen.addshape(us_image)
turtle.shape(us_image)

pen = Turtle()
pen.penup()
pen.hideturtle()


def question():
    answer_state = screen.textinput(title="Guess the state", prompt="Type a state name.")
    return answer_state


def check_answer(guess):
    global guessed_list

    for state in state_list:
        if state == guess:
            state_info = states_data[states_data["state"] == guess]
            
            x_loc = state_info.x.values[0]
            y_loc = state_info.y.values[0]

            pen.goto(x_loc, y_loc)
            pen.write(f"{guess}", move=False, align="center", font=("Arial"))
            guessed_list.append(guess)
            print(guessed_list)
            


def show_answer():
    for state in state_list:
        if state not in guessed_list:
            state_info = states_data[states_data["state"] == state]
               
            x_loc = state_info.x.values[0]
            y_loc = state_info.y.values[0]

            pen.color("red")
            pen.goto(x_loc, y_loc)
            pen.write(f"{state}", move=False, align="center", font=("Arial"))


def gameLoop():
    global guessed_list
    answer = question()
    
    if answer == "stop":
        return

    if answer == "surrender":
        show_answer()
        return
        
    check_answer(answer)

    if len(guessed_list) == 49:
        print("You win!")
        return
    
    gameLoop()


gameLoop()

screen.exitonclick()