
from twilio.rest import Client


class TwilioClient():
    def __init__(self) -> None:
        self.account_sid = ""
        self.auth_token = ""
        self.client = Client(self.account_sid, self.auth_token)

    def send_message(self, number, text):
        message = self.client.messages \
            .create(
                body=text,
                from_='+19106138585',
                to=number
            )
        return message.status
