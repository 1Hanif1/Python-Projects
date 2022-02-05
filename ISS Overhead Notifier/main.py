import time
import requests
from datetime import datetime
import smtplib

MY_LAT = 19.075983  # Your latitude
MY_LONG = 72.877655  # Your longitude

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])


def check_position() -> bool:
    if MY_LAT-5 < iss_latitude < MY_LAT+5 and MY_LONG-5 < iss_longitude < MY_LONG+5:
        return True
    return False


def send_email():
    with smtplib.SMTP("smtp.gmail.com") as conn:
        conn.starttls()
        # Enter your own email and pass
        conn.login(user="", password="")
        conn.sendmail(from_addr="", to_addrs="",
                      msg="Subject: ISS Visible today\n\nToday you'll be able to see the International Space Station at night time so keep an eye out for it.")


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get(
    "https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now()

while True:

    if check_position() and sunrise > time_now.hour > sunset:
        send_email()

    time.sleep(3)
