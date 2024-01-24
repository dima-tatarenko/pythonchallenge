import smtplib
import datetime as dt
import random

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

quotes_file = "E:/Programming/Python/daily_python/32_smtp/quotes.txt"
quote_list = []

with open(quotes_file) as file:
    quote_list = [line.rstrip() for line in file]

random_quote = random.choice(quote_list)

today = dt.datetime.now()


def send_mail():
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(my_user, my_pass)
        connection.sendmail(
            from_addr=my_user, 
            to_addrs=dest_user, 
            msg=f"Subject: Hello!\n\n{random_quote}")


def check_day():
    if today.weekday() == 0:
        send_mail()


check_day()