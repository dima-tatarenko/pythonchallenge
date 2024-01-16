#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

starting_letter = "E:/Programming/Python/daily_python/24_merge_mail/Input/Letters/starting_letter.txt"
invited_names = "E:/Programming/Python/daily_python/24_merge_mail/Input/Names/invited_names.txt"
send_folder = "E:/Programming/Python/daily_python/24_merge_mail/Output/ReadyToSend"

name_list = []
letter = ""

with open(invited_names) as file:
    name_list = [line.rstrip() for line in file]


with open(starting_letter) as file:
    letter = file.read()


for name in name_list:
    new_letter = letter.replace("[name]", name)

    with open(f"E:/Programming/Python/daily_python/24_merge_mail/Output/ReadyToSend/{name}.txt", "w") as file:
        file.write(new_letter)


