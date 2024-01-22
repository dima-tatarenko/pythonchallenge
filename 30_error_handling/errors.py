# File not found

# # try / except are very similar to try/catch
# try:
#     file = open("random_file.txt")
# except FileNotFoundError:
#     print("File doesn't exist.")
#     file = open("random_file.txt", "w")
# except KeyError as error_message:
#     print("Sad key {error_message} error.")
# else:
#     # everything went right and there were no errors
#     content = file.read()
#     print(content)
# finally:
#     # always runs, no matter what happens or if there's an error
#     file.close()
#     raise KeyError
#     # raise creates a custom exception

# raise an exception REALLY feels like creating custom validators in Angular :)


height = float(input("Height: "))
weight = int(input("Weight: "))

if height > 3:
    raise ValueError("Humans can't be higher than 3m.")

bmi = weight / height ** 2
print(bmi)