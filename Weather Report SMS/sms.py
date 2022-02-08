
from twilio.rest import Client

account_sid = "AC7f197493ade2043a1971abbee3a621d5"
auth_token = "cfe6aacef6b886c8b4a00b07c9614f88"


class TwilioClient():
    def __init__(self) -> None:
        self.account_sid = "AC7f197493ade2043a1971abbee3a621d5"
        self.auth_token = "cfe6aacef6b886c8b4a00b07c9614f88"
        self.client = Client(self.account_sid, self.auth_token)

    def send_message(self, number, text):
        message = self.client.messages \
            .create(
                body=text,
                from_='+19106138585',
                to=number
            )
        return message.status
