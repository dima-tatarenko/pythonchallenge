import random

# These were my initial ideas and thought process + some info about the Blackjack game itself
# 1. Define basic interface
# 2. Values must be randomized at start. Possible 3 functions: deal one more card (repeatable), 
# check status and give final result

# BJ Rules
# Can't go over 21 total (losing = bust)
# J/Q/K = 10
# Ace value can be chosen to adapt. Too low? Can add 11. Too high? Can count as 1.
# Dealers 1st card = revealed / 2nd card + = conceiled
# Same score = draw (Duh...)
# If dealers hand is lower than 17, must pull another card.


print("Welcome to a cool blackjack game!")



deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
player_hand = []
dealer_hand = []
gameOn = True
playerBust = False


def dealCard(targetArr):
    targetArr.append(random.choice(deck))

def initialDeal():
    for _ in range(2):
        dealCard(player_hand)
        dealCard(dealer_hand)
    print(player_hand)
    print(dealer_hand[0])

initialDeal()

def checkAce(score):
    print(score)
    if score + 11 > 21:
        return 1
    else:
        return 11

def checkScore(givenHand):
    total = 0
    for x in givenHand:
        if x == 11:
            x = checkAce(total)
        total = total + x
    return total

def checkDealer():
    global gameOn
    currentScore = checkScore(dealer_hand)
    if currentScore < 17:
        dealCard(dealer_hand)
    newCurrent = checkScore(dealer_hand)
    if newCurrent > 21 and playerBust == True:
        print("It's a bust for our dealer!")
        gameOn = False
    return newCurrent

def checkPlayer():
    global gameOn
    global playerBust
    currentScore = checkScore(player_hand)
    print(player_hand)
    if currentScore > 21:
        print("It's a bust, you lose!")
        playerBust = True
        gameOn = False
        continueGame()
    return currentScore

def checkContinue():
    global gameOn
    deal_pass = input(f"Type 'd' to get another card or 'p' to pass: ")
    if deal_pass == "d":
        dealCard(player_hand)
        checkPlayer()
        checkDealer()
        if gameOn == True:
            checkContinue()
    elif deal_pass == "p": 
        dealerScore = checkScore(dealer_hand)
        while dealerScore < 17:
            checkDealer()
            dealerScore = checkScore(dealer_hand)
        compareFinal()
        continueGame()
        gameOn = False

def compareFinal():
    dealerScore = checkScore(dealer_hand)
    playerScore = checkScore(player_hand)
    print(dealer_hand)
    print(player_hand)
    print(dealerScore)
    print(playerScore)
    if dealerScore > 21:
        print("You win!")
    elif playerScore < dealerScore and dealerScore < 22:
        print("You lose!")
    elif playerScore == dealerScore:
        print("It's a tie!")
    else:
        print("You win!")

def continueGame():
    global player_hand
    global dealer_hand
    global gameOn
    global playerBust
    check = input(f"Type 'c' to continue or 's' to stop: ")
    if check == "c":
        player_hand = []
        dealer_hand = []
        gameOn = True
        playerBust = False
        initialDeal()
        checkContinue()
    else:
        print("Thank you for playing!")

checkContinue()