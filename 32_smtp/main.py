import smtplib
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


# with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
#     connection.starttls()
#     connection.login(my_user, my_pass)
#     connection.sendmail(
#         from_addr=my_user, 
#         to_addrs=dest_user, 
#         msg="Subject: Hello!\n\nMeow.")


now = dt.datetime.now()
print(now)