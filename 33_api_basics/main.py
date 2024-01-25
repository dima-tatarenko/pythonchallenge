import requests

# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# response.raise_for_status()

# data = response.json()
# print(data)

# longitude = data["iss_position"]["longitude"]
# latitude = data["iss_position"]["latitude"]

# print(longitude)
# print(latitude)

parameters = {
    "lat": 40.463669,
    "lng": -3.749220,
}

response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
data = response.json()

print(data)