# Pixela habit tracker
# Learnt About HTTP - get, post, put and delete requests

from datetime import datetime
import requests
import os
from dotenv import load_dotenv
load_dotenv(dotenv_path="./pixela.env")

TOKEN = os.environ["PIXELA_TOKEN"]
USERNAME = os.environ["PIXELA_USERNAME"]
headers = {
    "X-USER-TOKEN": TOKEN
}

pixela_endpoint = "https://pixe.la/v1/users"
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(os.environ["PIXELA_USERNAME"])
# print(response.text)
# /v1/users/<username>/graphs

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_params = {
    "id": "graph1",
    "name": "Coding",
    "unit": "hr",
    "type": "float",
    "color": "ajisai",
}

# response = requests.post(
#     url=graph_endpoint, json=graph_params, headers=headers)

# print(response.text)

date = datetime.now().strftime("%Y%m%d")

add_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph1"
pixel_params = {
    "date": date,
    "quantity": "2",
}
# response = requests.post(url=add_pixel_endpoint,
#                          json=pixel_params, headers=headers)
# print(response.text)

update_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph1/20220211"

update_pixel_params = {
    "quantity": "4",
}

# response = requests.put(url=update_pixel_endpoint,
#                         json=update_pixel_params, headers=headers)
# print(response.text)

delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph1/20220211"
# response = requests.delete(url=delete_endpoint, headers=headers)
# print(response.text)
