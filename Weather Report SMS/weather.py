from requests import request
import os


class HourlyWeather():
    def get_hourly_data(self):
        response = request(url=self.URL, params=self.PARAMS, method="get")
        response.raise_for_status()
        response_data = response.json()
        return response_data["hourly"]

    def __init__(self) -> None:
        self.API_KEY = os.environ.get("OWM_API_KEY")
        self.LATITUDE = 19.075983
        self.LONGITUDE = 72.877655
        self.URL = f"https://api.openweathermap.org/data/2.5/onecall?"
        self.PARAMS = {
            "lat": self.LATITUDE, "lon": self.LONGITUDE,
            "appid": self.API_KEY
        }
        self.data = self.get_hourly_data()
        self.data = self.data[0:12]
        self.weather_id = [data['weather'][0]["id"] for data in self.data]

    def get_weather_ids(self):
        return self.weather_id
