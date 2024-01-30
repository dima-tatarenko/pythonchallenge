## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

## STEP 3: Use https://www.twilio.com - NO, using SMTP because of Twilio restrictions
# Send a seperate message with the percentage change and each article's title and description to your phone number. 


# END OF INSTRUCTIONS, consider this to be line 0 :)
import requests
from datetime import datetime, timedelta
import smtplib

# DOTENV SETUP
# .env was explained, not cheating anymore
from dotenv import load_dotenv
import os
load_dotenv()
av_api_key = os.getenv("ALPHAVANTAGE_API_KEY")
news_api_key = os.getenv("NEWS_API_KEY")
my_user = os.getenv("DTUSER")
my_pass = os.getenv("DTTOKEN")
dest_user = os.getenv("AIUSER")
# DOTENV SETUP


# Stocks API config
STOCK = "TSLA"
INTERVAL = 60

# News API config
COMPANY_NAME = "Tesla Inc"


# GET DATA FROM API FUNCTION!

# Had to use a local file to make sure everything works before using the actual API.
from news_test import news_data
from stonks_test import stock_data

news_title = news_data["articles"][0]["title"]
news_article = news_data["articles"][0]["description"]

# def get_stock_data():
#     url = f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={STOCK}&interval={INTERVAL}min&apikey={av_api_key}'
#     r = requests.get(url)
#     data = r.json()
#     # close_data = data["Time Series (60min)"]["2024-01-26 19:00:00"]["4. close"]
#     # meow = data["Time Series (60min)"]
#     return data

# stock_data = get_stock_data()


# def get_news_data():
#     url = f'https://newsapi.org/v2/everything?q=tesla&language=en&sortBy=popularity&pageSize=1&apiKey={news_api_key}'
#     r = requests.get(url)
#     data = r.json()
#     return data

# news_data = get_news_data()

# GET DATA FROM API FUNCTION!


# Find the latest data

today = datetime.now().strftime('%Y-%m-%d')
yesterday = None

def check_dates(date_list, target_date):
    date_exists = False
    for date in date_list:
        if date[:10] == target_date:
            date_exists = True
    
    if date_exists:
        return True
    else:
        return False


def recalculate_date(date):
    given_date = datetime.strptime(date, "%Y-%m-%d")
    if given_date.weekday() == 6:
        new_date = given_date - timedelta(days=2)
    elif given_date.weekday() == 0:
        new_date = given_date - timedelta(days=3)
    else:
        new_date = given_date - timedelta(days=1)
    return new_date


def find_last_update(data):
    global attempts
    global today
    global yesterday
    dates = sorted(data.keys(), reverse=True)
    if check_dates(dates, today):
        base_yesterday = recalculate_date(today)
        yesterday = base_yesterday.date().strftime("%Y-%m-%d")
        today = f"{today} 19:00:00"
        yesterday = f"{yesterday} 19:00:00"
    else:
        new_date = recalculate_date(today)
        today = new_date.date().strftime("%Y-%m-%d")
        find_last_update(stock_data["Time Series (60min)"])


find_last_update(stock_data["Time Series (60min)"])


# Calculate stock price fluctuation
yesterdays_close = stock_data["Time Series (60min)"][yesterday]["4. close"]
todays_close = stock_data["Time Series (60min)"][today]["4. close"]


def calc_fluctuation(num1, num2):
    difference = num1 - num2
    fluctuation = (difference / num1) * 100
    return fluctuation


def check_message():
    result = calc_fluctuation(float(todays_close), float(yesterdays_close))
    if result > 5:
        send_mail(f"gone up by {round(result, 2)}%")
    elif result < -5:
        send_mail(f"gone down by {round(result, 2)}%")
    else:
        send_mail(f"not changed - {round(result, 2)}% difference from yesterday")


def send_mail(change_direction):
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(my_user, my_pass)
        connection.sendmail(
            from_addr=my_user, 
            to_addrs=dest_user, 
            msg=f"Subject: Tesla actions have {change_direction}.\n\n{news_title}.\n{news_article}...")
        

check_message()






