
import pandas as pd
import random
import smtplib
import datetime as dt

birthday_data = pd.read_csv("birthdays.csv")

all_birthdays = [(row[1].person, row[1].email, row[1].month, row[1].day)
                 for row in birthday_data.iterrows()]


def get_letter(person) -> str:
    name, email, month, day = person
    letter = ""
    with open(f"./letter_templates/letter_{random.randint(1, 3)}.txt", "r") as template:
        lines = template.readlines()
        lines[0] = lines[0].replace("[NAME]", name)

        for line in lines:
            letter += line

    return letter


def send_email(letter):
    MY_EMAIL = ""
    PASSWORD = ""
    try:
        with smtplib.SMTP("smtp.gmail.com") as mail:
            mail.starttls()
            mail.login(user=MY_EMAIL, password=PASSWORD)
            mail.sendmail(from_addr=MY_EMAIL, to_addrs="",
                          msg=f"Subject:Happy Birthday ^^\n\n{letter}")
        return True
    except Exception:
        return False


for people in all_birthdays:
    curr_date = dt.datetime.now()

    if curr_date.month == people[2] and curr_date.day == people[3]:
        letter = get_letter(people)
        status = send_email(letter)
        if status:
            print("Birthday wish sent successfully")
        else:
            print("There was an error in sending the message")
