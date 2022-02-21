import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇
response = requests.get(url=URL)
response = response.text

movie_site = BeautifulSoup(response, "html.parser")

all_titles = [title.getText()
              for title in movie_site.find_all(name="h3", class_="title")]
all_titles.reverse()

with open("movies.txt", "w") as file:
    for title in all_titles:
        file.write(f"{title}\n")
