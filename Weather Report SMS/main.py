from weather import HourlyWeather
from sms import TwilioClient

Weather = HourlyWeather()
SMS = TwilioClient()
registered_twilio_number = ""
weather_id = Weather.get_weather_ids()


def check_weather():
    for id in weather_id:
        if id < 700:
            status = SMS.send_message(
                registered_twilio_number, "It may rain today so take an umbrella with you just in case ☔")
            if status:
                print("Message sent successfully")
            break
        else:
            print("All Clear Today")
            break


check_weather()
