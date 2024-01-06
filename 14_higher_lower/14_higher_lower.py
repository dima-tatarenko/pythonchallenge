# Outside imps

import random

# Inside imps

import art
import game_data

print(art.logo)

# Started to code right away 'cause I was kinda excited for this one. It's a game I've played myself :)
# Gonna go for simple "fill the variables" method and reassign them each time with a function.
# Prompt the user to choose, do the math and execute first function again.
# Will have to keep the highscore somehow, easy counter I guess.


oldItem = None
newItem = None

highscore = 0
gameOn = True


def fillInfo(targetObject):
    targetObject = game_data.data[random.randint(0,len(game_data.data) -1)]
    # targetObject = game_data.data[random.randint(len(game_data-1))]
    print(f"{targetObject['name']} | {targetObject['description']} from {targetObject['country']}.")
    return targetObject

def reassignNew():
    global newItem
    newItem = fillInfo(newItem)

oldItem = fillInfo(oldItem)
print(art.vs)
newItem = fillInfo(newItem)

print(oldItem["follower_count"])



def userChoice():
    global oldItem
    global newItem
    global highscore
    higherlower = input(f"Does {newItem['name']} have higher (h) or lower (l) follower count on Instagram than {newItem['name']}?: ")
    check = oldItem["follower_count"] < newItem["follower_count"]
    if (check and higherlower == "h" or not check and higherlower == "l"):
        highscore += 1
        print(f"Correct! New highscore of {highscore}. Keep climbing!")
        oldItem = newItem
        print(art.vs)
        reassignNew()
        userChoice()
    else:
        print(f"You lose! Your highscore is {highscore}.")

userChoice()

