# For the first time, import random is not a thing. O.O

# Gotta build a simple coffee machine interface. Ask for stuff, make sure it has ingredients
# Coin-operated. User inserts coins, must do the addition and return money if it's not enough

# 

# local imps
# Didn't know python had such strict naming conventions :(
# https://peps.python.org/pep-0008/#package-and-module-names

from coffee_data import *

# menu espresso, latte, cappuccino
# Best approach in my head is to create a single function for every product and pass the product to it.
# Could easily break assuming some ingredients are not included in the corresponding dict, but that would be
# a major problem for the entire machine. It's a feature, I guess.

# print(m_menu)
# print(m_resources)

product_data = None
coins = ["penny", "nickel", "dime", "quarter"]
outOfStock = False


def offerDrink():
    user_choice = input(f"Would you like an espresso (e), latte (l) or cappuccino (c)? You can also type(r) to check whether the machine needs refilling. ")
    if user_choice == "e":
        user_choice = "espresso"
    elif user_choice == "l":
        user_choice = "latte"
    elif user_choice == "c":
        user_choice = "cappuccino"
    elif user_choice == "r":
        print(m_resources['water'])
        print(m_resources['coffee'])
        print(m_resources['milk'])
        takeOrder()   
    else:
        return print("No product found with this name.")
    return user_choice


def addCoins(coinName, amount):
    coin_values = {
        'penny': 0.01,
        'nickel': 0.05,
        'dime': 0.1,
        'quarter': 0.25
        }
    
    if coinName in coin_values:
        value = coin_values[coinName]
        print(value)
        total = value * amount
        return round(total, 2)

    print(coinName)
    print(amount)
    total = coinName * amount
    return int(total)


def checkPrice():
    global product_data
    total_inserted = 0

    for coin in coins:
        user_choice = int(input(f"How many {coin}s do you want to add? "))
        user_choice = addCoins(coin, user_choice)
        total_inserted = round((total_inserted + user_choice), 2)

    print(total_inserted)
    if total_inserted > product_data['cost']:
        change = round((total_inserted - product_data['cost']), 2)
        print(f"Here's your change: {change}")
        return True
    else:
        print("You didn't insert enough coins. Your coins have been returned and ordered cancelled.")


def checkIngredients():
    global product_data
    global outOfStock
    ingredients = product_data['ingredients']
    enoughMilk = None    

    if 'milk' in ingredients:
        enoughMilk = m_resources['milk'] > ingredients['milk']
    else:
        enoughMilk = True

    enoughWater = m_resources['water'] > ingredients['water']
    enoughCoffee = m_resources['coffee'] > ingredients['coffee']

    if enoughWater and enoughCoffee and enoughMilk:
        m_resources['water'] = m_resources['water'] - ingredients['water']
        m_resources['coffee'] = m_resources['coffee'] - ingredients['coffee']
        if 'milk' in ingredients:
            m_resources['milk'] = m_resources['milk'] - ingredients['milk']
        return True
    else:
        outOfStock = True
        print('Sorry, the machine needs refilling!')


def continueCheck():
    user_choice = input(f"Would you like anything else? (y) or (n) ")
    if user_choice == "y":
        return takeOrder()
    else:
        return print("Enjoy your drink!")


def takeOrder():
    global outOfStock
    global product_data

    if outOfStock == True:
        return
    else:
        product_data = m_menu[offerDrink()]
        payment = checkPrice()
        availability = checkIngredients()
        if payment and availability:
            print('Enjoy your drink!')
        continueCheck()


takeOrder()





# user_choice = oldItem["follower_count"] < newItem["follower_count"]
# if (check and higherlower == "h" or not check and higherlower == "l"):





