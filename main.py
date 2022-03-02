from datetime import datetime

import requests

GENDER = "male"
WEIGHT_KG = Your Weight in KG
HEIGHT_CM = Your Height in CM
AGE = Your Age

APP_ID = "Your APPID"
API_KEY = "your API KEY"

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheet_endpoint = "https://api.sheety.co/yourendpoint/myWorkouts/workouts"

excerise_text = input("Tell me which exercises you did: ")

parameters = {
    "query": excerise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

sheet_headers = {"Authorization": "Bearer MYREALLYLONGTOKENIGOT" }

exercise_headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "x-remote-user-id": "0"
}

response = requests.post(exercise_endpoint, json=parameters, headers=exercise_headers)

data = response.json()
print(data)

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in data["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(sheet_endpoint, json=sheet_inputs, headers=sheet_headers)

    print(sheet_response.text)
