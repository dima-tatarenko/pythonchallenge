import random

# This lesson was focused on scope. So I gotta play with that concept to create a number guessing game.
# Imported random even before this because I know I will need a random num between 1-100.

# Initial thoughts

# Player lives must be global to have 2 different game levels (easy and hard)
# Easy - 10 tries, hard - 5

# Create a while loop or a callback function to prompt the user to write a number.
# it will then compare the number (another func?) and state whether it's too low, too high or the user guessed it.
# Gonna just give it a go at this point.

# Dima from the future decided to add a "change difficulty" option. I'll need to store user's choice.

print("Welcome to a my guess the number game!")
print("Rules are simple: you must try to guess a number between 1 and 100 before you run out of lives. Easy - 10 attempts. Hard - 5 attempts. Good luck!")

secret_number = random.randint(1, 100)
player_lives = 10
player_difficulty = 10

gameOn = True

def gameDifficulty():
    global player_lives
    global player_difficulty
    player_choice = input(f"Type 'e' for easy or 'h' for hard: ")
    if player_choice == "h":
        player_lives = 5
        player_difficulty = 5

gameDifficulty()

print(player_lives)


def evaluateNumber(number):
    global secret_number
    global player_lives
    global gameOn
    if number < secret_number:
        print("Too low!")
        player_lives -= 1
    elif number > secret_number:
        print("Too high!")
        player_lives -= 1
    elif number == secret_number:
        print("You win!")
        gameOn = False
    print(player_lives)

def offerGuess():
    global player_lives
    global secret_number
    global gameOn
    if player_lives == 0:
        print("You lose!")
        print(secret_number)
        gameOn = False
        return
    player_number = int(input(f"Choose a number: "))
    evaluateNumber(player_number)

while gameOn == True:
    offerGuess()
