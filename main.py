import requests

GENDER = "male"
WEIGHT_KG = Your Weight in KG
HEIGHT_CM = Your Height in CM
AGE = Your Age

APP_ID = "Your APPID"
API_KEY = "your API KEY"

exercise_endpooint = "https://trackapi.nutritionix.com/v2/natural/exercise"

excerise_text = input("Tell me which exercises you did: ")

parameters = {
    "query": excerise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "x-remote-user-id": "0"
}

response = requests.post(exercise_endpooint, json=parameters, headers=headers)

data = response.json()
print(data)

