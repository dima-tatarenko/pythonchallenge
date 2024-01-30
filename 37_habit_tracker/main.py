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
px_user = os.getenv("PXUSER")
# DOTENV SETUP

headers = {
    "X-USER-TOKEN":news_api_key
}

pixela_endpoint = "https://pixe.la/v1/users"

# User registration at Pixela
# pixela_params = {
#     "token":"super secret token",
#     "username":"dimchik",
#     "agreeTermsOfService":"yes",
#     "notMinor":"yes"
# }

# response = requests.post(pixela_endpoint, json=pixela_params)
# print(response.text)

# Register a graph

graph_endpoint = f"{pixela_endpoint}/{px_user}/graphs"

# graph_params = {
#     "id":"g1",
#     "name":"Job application graph",
#     "unit":"Applications",
#     "type":"int",
#     "color":"shibafu"
# }

# response = requests.post(url=graph_endpoint, json=graph_params, headers=headers)
# print(response.text)

add_pixel_endpoint = f"{graph_endpoint}/g1"
print(add_pixel_endpoint)

today_full = datetime.now()
today = today_full.date().strftime("%Y%m%d")
print(today)

add_pixel_params = {
    "date":today,
    "quantity":"1",
}

response = requests.post(url=add_pixel_endpoint, json=add_pixel_params, headers=headers)
print(response.text)