from datetime import datetime
from requests import post
from dotenv import load_dotenv
import os
load_dotenv(dotenv_path="./envvar.env")

APP_ID = os.environ["N_APP_ID"]
API_KEY = os.environ["N_API_KEY"]
API_URL = "https://trackapi.nutritionix.com"
SHEETY_POST_URL = "https://api.sheety.co/69daa5abe606f40d78463b0e6551ab1a/myWorkouts/workouts"
SHEETY_API_KEY = os.environ["SHEETY_API_KEY"]


def write_data(exercise):

    exercise_name = exercise["name"]
    exercise_duration = exercise['duration_min']
    exercise_calories = exercise["nf_calories"]

    datetime_data = datetime.now()
    date = datetime_data.strftime("%d/%m/%Y")
    time = datetime_data.strftime("%X")

    POST_BODY = {
        "workout": {
            "date": date,
            "time": time,
            "exercise": exercise_name.title(),
            "duration": exercise_duration,
            "calories": exercise_calories,
        }
    }

    bearer_header = {
        "Authorization": f"Bearer {SHEETY_API_KEY}"
    }

    response = post(url=SHEETY_POST_URL, json=POST_BODY, headers=bearer_header)
    print(response.text)


def get_data():
    text = input("Enter Text: ")
    post_params = {
        "query": text,
        "gender": "male",
        "weight_kg": 103,
        "height_cm": 183,
        "age": 19,
    }

    headers = {
        "x-app-id": APP_ID,
        "x-app-key": API_KEY,
        "Content-Type": "application/json",
    }

    response = post(url=f"{API_URL}/v2/natural/exercise",
                    json=post_params, headers=headers)

    response = response.json()

    for exercise in response["exercises"]:
        write_data(exercise)


get_data()
