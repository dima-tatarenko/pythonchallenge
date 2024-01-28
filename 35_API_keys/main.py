import requests
import smtplib

# DOTENV SETUP
# .env was explained, not cheating anymore
from dotenv import load_dotenv
import os
load_dotenv()
api_key = os.getenv("WEATHER")
my_user = os.getenv("DTUSER")
my_pass = os.getenv("DTTOKEN")
dest_user = os.getenv("AIUSER")
# DOTENV SETUP
# Adding env to python anywhere:
# Console -> export VARIABLE=THING (no quotation needed!)
# Access through os.environ.get(THING), almost the same as getenv
# Python anywhere is fine - code is not public :)

weather_api = "https://api.openweathermap.org/data/2.5/forecast"
gonna_rain = False

weather_params = {
    "lat": 41.6062,
    "lon": 2.2871,
    "appid": api_key,
    "cnt": 4,
}


def get_weather():
    response = requests.get(url=weather_api, params=weather_params)
    data = response.json()
    weather_by_hour = data["list"]
    return weather_by_hour
    

def check_for_rain():
    global gonna_rain
    weather_hourly = get_weather()
    for hour in weather_hourly:
        weather = hour["weather"][0]
        if need_umbrella(weather["id"]):
            gonna_rain = True
    if gonna_rain:
        send_mail()


def need_umbrella(num):
    if num in range(600, 900):
        return True


def send_mail():
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(my_user, my_pass)
        connection.sendmail(
            from_addr=my_user, 
            to_addrs=dest_user, 
            msg=f"Subject: A rainy day!\n\nIt's gonna rain!")


check_for_rain()