import requests
from datetime import datetime
import os

app_id = os.environ.get('APP_ID')
app_key = os.environ.get('APP_KEY')
username = os.environ.get('USERNAME')
APP_ID = app_id
APP_KEY = app_key
USERNAME = username

nutritionix_end_point = "https://trackapi.nutritionix.com/v2/natural/exercise"
nutritionix_header = {
    "x-app-id": APP_ID,
    "x-app-key": APP_KEY
}
parameters = {
    "query": input("enter the exercise you had today ?")
}
nutritionix_response = requests.post(url=nutritionix_end_point, json=parameters, headers=nutritionix_header)
data = nutritionix_response.json()["exercises"][0]
exercise = data["user_input"].title()
duration = data["duration_min"]
calories = data["nf_calories"]
# TO RETRIEVE A ROW FROM A SHEET
# retrieve_end_point = f"https://api.sheety.co/{USERNAME}/workoutTracking/workouts"
#
# retrieve_response = requests.get(url=retrieve_end_point)
# print(retrieve_response.json())

# TO POST A DATA TO SHEET
post_endpoint = f"https://api.sheety.co/{USERNAME}/workoutTracking/workouts"
date_time = datetime.now()
date = date_time.strftime(f"%d/%m/%Y")
time = date_time.strftime("%T")
post_parameters = {
    "workout": {
        "date": date,
        "time": time,
        "exercise": exercise,
        "duration": duration,
        "calories": calories
    }
}
post_response = requests.post(url=post_endpoint, json=post_parameters)

# basic authentication
authentication_header = {
    "Authorization": "Basic YXZpbmFzaDA1OkF2aW5hc2hAMTIz"
}
authentication_response = requests.post(post_endpoint, json=post_parameters, headers=authentication_header)
print(authentication_response.text)