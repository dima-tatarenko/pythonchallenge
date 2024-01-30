import requests
from datetime import datetime

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
nutri_id = os.getenv("NUTRIID")
nutri = os.getenv("NUTRITIONIX")
sheety_pass = os.getenv("SHEETY")
# DOTENV SETUP

base_url = "https://trackapi.nutritionix.com/"
endpoint_url = f"{base_url}v2/natural/exercise"

headers = {
    "x-app-id":nutri_id,
    "x-app-key":nutri
}

activity = input("What exercise did you do?")

nutri_params = {
    "query":activity,
    "gender":"male",
    "height_cm":184,
    "age":31
}


exercise = requests.post(endpoint_url, nutri_params, headers=headers)
exercise_stats = exercise.json()
print(exercise_stats)


exercise = exercise_stats["exercises"][0]["name"]
duration = exercise_stats["exercises"][0]["duration_min"]
calories = exercise_stats["exercises"][0]["nf_calories"]


# Static example for nutrition api
# exercise_stats = {"exercises":[{"tag_id":255,"user_input":"skated","duration_min":30,"met":7.5,"nf_calories":262.5,"photo":{"highres":None,"thumb":None,"is_user_uploaded":False},"compendium_code":15591,"name":"rollerblading","description":None,"benefits":None}]}

today = datetime.now()
today_date = today.strftime("%Y%m%d")
today_time = today.strftime("%H:%M:%S")


# Sheety setup
sheety_endpoint = "https://api.sheety.co/7996f48f69bebdc0237d5efd939d5232/pythonWorkoutExercise/workouts"

sheety_headers = {
    "Authorization":sheety_pass,
    "Content-Type":"application/json"
}

sheety_body = {
    "workout": {
        "date":today_date,
        "time":today_time,
        "exercise":exercise,
        "duration":duration,
        "calories":calories
        }
}

response = requests.post(sheety_endpoint, json=sheety_body, headers=sheety_headers)
print(response.text)



