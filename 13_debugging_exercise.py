############DEBUGGING#####################

# Describe Problem
# Range is used incorrectly. Must go to 21 for it to count until 20.
# def my_function():
#   for i in range(1, 20):
#     print(i)
#     if i == 20:
#       print("You got it")
# my_function()


# Reproduce the Bug
# Swap 1 -> 6 to reproduce it.
# There is no position 6 in the array, randint must be (0,5)
# from random import randint
# dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num = randint(1, 6)
# print(dice_imgs[dice_num])


# Play Computer
# By not having <= or >= in the function, year 1994 is never included, hence the bug.
# year = int(input("What's your year of birth?"))
# if year > 1980 and year < 1994:
#   print("You are a millenial.")
# elif year > 1994:
#   print("You are a Gen Z.")

# # Fix the Errors
# Missing indentation and "f" in print. Missing int() for the input.
# age = int(input("How old are you?"))
# if age > 18:
#     print(f"You can drive at age {age}.")

#Print is Your Friend
# There is a double equal sign, which doesn't reassign the value to word_per_page. Whatever * 0 is always 0...
# pages = 0
# word_per_page = 0
# pages = int(input("Number of pages: "))
# word_per_page == int(input("Number of words per page: "))
# total_words = pages * word_per_page
# print(total_words)

#Use a Debugger
# It's a simple indentation problem. But I do know how useful a debugger can be.
# b_list.append is not inside the for loop.
# def mutate(a_list):
#   b_list = []
#   for item in a_list:
#     new_item = item * 2
#   b_list.append(new_item)
#   print(b_list)

# mutate([1,2,3,5,8,13])