## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 


#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

# END OF INSTRUCTIONS, consider this to be line 0 :)
import requests

# DOTENV SETUP
# .env was explained, not cheating anymore
from dotenv import load_dotenv
import os
load_dotenv()
av_api_key = os.getenv("ALPHAVANTAGE_API_KEY")
my_user = os.getenv("DTUSER")
my_pass = os.getenv("DTTOKEN")
dest_user = os.getenv("AIUSER")
# DOTENV SETUP


# Stocks API config
STOCK = "TSLA"
INTERVAL = 60

# News API config
COMPANY_NAME = "Tesla Inc"


def get_stock_data():
    url = f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={STOCK}&interval={INTERVAL}min&apikey={av_api_key}'
    r = requests.get(url)
    data = r.json()
    # close_data = data["Time Series (60min)"]["2024-01-26 19:00:00"]["4. close"]
    # meow = data["Time Series (60min)"]
    return data



stock_data = get_stock_data()
print(stock_data)
# # print(stock_data["Time Series (60min)"])
# yesterdays_close = stock_data["Time Series (60min)"]["2024-01-26 19:00:00"]["4. close"]
# todays_close = stock_data["Time Series (60min)"]["2024-01-25 19:00:00"]["4. close"]




# def calc_fluctuation(num1, num2):
#     difference = num1 - num2
#     fluctuation = (difference / num1) * 100
#     return fluctuation


# def check_message():
#     result = calc_difference(float(todays_close), float(yesterdays_close))
#     if result > 5 or result < -5:
#         print("meow")





# from datetime import datetime, timedelta

# def find_consecutive_days(data):
#     dates = sorted(data.keys())
#     print(dates)

#     for i in range(len(dates) - 1):
#         current_date = datetime.strptime(dates[i], "%Y-%m-%d %H:%M:%S")
#         print(current_date)
#         next_date = datetime.strptime(dates[i + 1], "%Y-%m-%d %H:%M:%S")
#         print(next_date)

#         if (next_date - current_date).days == 1:
#             return {dates[i]: data[dates[i]], dates[i + 1]: data[dates[i + 1]]}

#     return None

# # Example usage
# consecutive_data = find_consecutive_days(stock_data)

# if consecutive_data:
#     print("Data for two consecutive days found:")
#     print(consecutive_data)
# else:
#     print("Data for two consecutive days not found.")