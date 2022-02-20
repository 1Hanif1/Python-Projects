from email import message
import os
from twilio.rest import Client
from dotenv import load_dotenv
load_dotenv(dotenv_path='./envvar.env')


class NotificationManager:
    def __init__(self) -> None:
        self.sid = os.environ['TWILIO_ACC_SID']
        self.key = os.environ['TWILIO_API_KEY']
        self.client = Client(self.sid, self.key)

    def send_message(self, flight):
        msg = f"Lowest Price Alert! Only INR {flight.price[0]} to fly from {flight.origin_city[0]}-{flight.origin_airport[0]} to {flight.destination_city[0]}-{flight.destination_airport[0]}"
        message = self.client.messages.create(
            body=msg,
            from_="+19106138585",
            to="+919137237618"
        )
        print(message.sid)
