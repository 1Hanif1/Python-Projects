from os import environ
from requests import put, get

from flight_search import FlightSearch


class DataManager:
    def __init__(self) -> None:
        self.sheety_url = environ['SHEETY_API_URL']
        self.sheety_key = environ['SHEETY_API_KEY']
        self.header = {
            "Authorization": f"Bearer {self.sheety_key}"
        }

    def get_sheety_data(self):
        response = get(url=self.sheety_url, headers=self.header)
        response = response.json()['prices']
        return response

    def add_iata_code(self, FS: FlightSearch):
        sheety_data = self.get_sheety_data()
        for city in sheety_data:
            id = city['id']
            city_name = city['city']
            if not city['iataCode']:
                code = FS.get_code(city_name)
                self.PUT(id, f"{code}")

    def PUT(self, row_id, iata_code):
        body = {
            "price": {
                "iataCode": iata_code
            }
        }
        put(url=f"{self.sheety_url}/{row_id}",
            json=body, headers=self.header)

    pass
