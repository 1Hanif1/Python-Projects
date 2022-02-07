from requests import request

response = request(
    url="https://opentdb.com/api.php?",
    params={
        "amount": "10",
        "category": "31",
        "difficulty": "easy",
        "type": "boolean",
    },
    method="get"
)

response = response.json()

question_data = response["results"]
