import random
import smtplib
import pandas
import datetime as dt

# DOTENV SETUP - not included in the lesson
# For VERY obvious reasons, I can't include sensitive info here
# so I created a .env file to feed the program the data it needs.
from dotenv import load_dotenv
import os
load_dotenv()
my_user = os.getenv("DTUSER")
my_pass = os.getenv("DTTOKEN")
dest_user = os.getenv("AIUSER")
# DOTENV SETUP


birthdays_file = "E:/Programming/Python/daily_python/32_birthday_smtp/birthdays.csv"
birthdays = pandas.read_csv(birthdays_file)

final_letter = "E:/Programming/Python/daily_python/32_birthday_smtp/letter_templates/final_letter.txt"
today = dt.datetime.now()


##################### Edit letter ######################

def prepare_letter(user_name):
    random_letter = f"E:/Programming/Python/daily_python/32_birthday_smtp/letter_templates/letter_{random.randint(1,3)}.txt"

    with open(random_letter) as file:
        letter = file.read()

    edited_letter = letter.replace("[NAME]", user_name)

    with open(final_letter, "w") as file:
        file.write(edited_letter)


##################### Pandas ######################


def check_bd():
    for index, row in birthdays.iterrows():
        if today.day == row["day"] and today.month == row["month"]:
            prepare_letter(row["name"])
            send_mail(row["email"])


##################### Email func ######################
        

def send_mail(user_mail):
    with open(final_letter) as file:
        letter = file.read()

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(my_user, my_pass)
        connection.sendmail(
            from_addr=my_user, 
            to_addrs=user_mail, 
            msg=f"Subject: Happy birthday!\n\n{letter}")
        

check_bd()

##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.




