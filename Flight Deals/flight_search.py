from datetime import datetime, timedelta
from os import environ
from flight_data import FlightData
import requests
from dotenv import load_dotenv
load_dotenv(dotenv_path="./envvar.env")
TEQUILA_KEY = environ['TEQUILA_API_KEY']
TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com"


class FlightSearch:
    def __init__(self) -> None:
        self.url = TEQUILA_ENDPOINT
        self.header = {
            "apikey": TEQUILA_KEY
        }
        pass

    def get_code(self, city):
        body = {"term": city, "location_types": "city"}
        response = requests.get(
            url=f"{self.url}/locations/query", params=body, headers=self.header)
        response = response.json()['locations'][0]['code']
        return response

    def get_flight_data(self, city):
        today = datetime.now()
        tomorrow = (today + timedelta(days=1)).strftime("%d/%m/%Y")
        later = (today + timedelta(days=45)).strftime("%d/%m/%Y")
        body = {
            "fly_from": "BOM",
            "fly_to": city,
            "date_from": tomorrow,
            "date_to": later,
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 1,
            "curr": "INR",
        }
        response = requests.get(
            url=f"{self.url}/search",
            params=body,
            headers=self.header
        )

        try:
            data = response.json()['data'][0]
        except IndexError:
            print(f"No Flights available for {city}")
            return

        flight_data = FlightData(
            price=data['price'],
            origin_city=data["cityFrom"],
            origin_airport=data["flyFrom"],
            destination_city=data['cityTo'],
            destination_airport=data['flyTo'],
        )
        # print(f"{flight_data.destination_city[0]}: INR {flight_data.price[0]}")
        return flight_data
    pass
