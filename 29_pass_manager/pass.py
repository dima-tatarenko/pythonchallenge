#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# nr_letters = random.randint(8, 10)
# nr_symbols = random.randint(2, 4)
# nr_numbers = random.randint(2, 4)

password_list = []

[password_list.append(random.choice(letters)) for _ in range(random.randint(8, 10))]
[password_list.append(random.choice(symbols)) for _ in range(random.randint(2, 4))]
[password_list.append(random.choice(numbers)) for _ in range(random.randint(2, 4))]

# Edited using list comprehension
# for char in range(nr_letters):
#   password_list.append(random.choice(letters))
#   print(password_list)

# for char in range(nr_symbols):
#   password_list += random.choice(symbols)

# for char in range(nr_numbers):
#   password_list += random.choice(numbers)

# used join and list comprehension to simplify pw generation
# password = ""
# for char in password_list:
#   password += char

random.shuffle(password_list)
password = "".join([char for char in password_list])

print(f"Your password is: {password}")