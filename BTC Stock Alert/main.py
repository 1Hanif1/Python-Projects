from dotenv import load_dotenv
from twilio.rest import Client
import os
from requests import request
import datetime as DT
COIN_STOCK = "BTC"
COIN_NAME = "bitcoin"
TWILIO_REGISTERED_NUMBER = ""  # Enter registered Twilio phone number here
load_dotenv(dotenv_path="./sms.env")


def get_news() -> list:
    news_response = request(
        url="https://newsapi.org/v2/everything?",
        params={
            "q": COIN_NAME,
            "apikey": os.environ['NEWS_API_KEY']
        },
        method="get",
    )

    news_data = news_response.json()["articles"][:3]
    return [(data["title"], data["description"]) for data in news_data]


def get_stock_growth() -> float:
    URL = 'https://www.alphavantage.co/query?'
    PARAMS = {
        "function": "DIGITAL_CURRENCY_DAILY",
        "symbol": COIN_STOCK,
        "market": "INR",
        "apikey": os.environ["ALPHA_VANTAGE_KEY"],
    }
    response = request(url=URL, params=PARAMS, method="get")
    response.raise_for_status()
    data = response.json()
    daily_data = data["Time Series (Digital Currency Daily)"]
    # "Time Series (Digital Currency Daily)"

    todays_date = DT.datetime.now().date()
    yesterdays_date = str(todays_date - DT.timedelta(days=1))
    day_before_yesterday = str(todays_date - DT.timedelta(days=2))

    last_two_day_close = (
        float(daily_data[yesterdays_date]["4a. close (INR)"]),
        float(daily_data[day_before_yesterday]["4a. close (INR)"])
    )
    close_difference = last_two_day_close[0] - last_two_day_close[1]
    print(close_difference)
    return (close_difference/last_two_day_close[0]) * 100


def send_SMS(msg):
    account_sid = os.environ['TWILIO_ACCOUNT_SID']
    auth_token = os.environ['TWILIO_AUTH_TOKEN']
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body=msg,
        from_='+19106138585',
        to=TWILIO_REGISTERED_NUMBER
    )
    print(message.sid)


difference_percentage = round(get_stock_growth(), 1)
if abs(difference_percentage) > 0.1:
    news_data = get_news()
    up_down = "🔻" if difference_percentage < 0 else "🔺"
    for news in news_data:
        message = f"BTC {up_down}{difference_percentage}%\nHeadline: {news[0]}\nBrief: {news[1]}"
        send_SMS(message)
    print("Message Sent !")
