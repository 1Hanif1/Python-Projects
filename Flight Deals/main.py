# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from requests import get
from data_manager import DataManager
from flight_search import FlightSearch
from os import environ
from dotenv import load_dotenv

from notification_manager import NotificationManager

load_dotenv(dotenv_path="./envvar.env")

DM = DataManager()
FS = FlightSearch()
NM = NotificationManager()
DM.add_iata_code(FS)
sheety_data = DM.get_sheety_data()


for city in sheety_data:
    flight = FS.get_flight_data(city['iataCode'])

    if not flight:
        continue

    if flight.price[0] < city['lowestPrice']:
        NM.send_message(flight)
