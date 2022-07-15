import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
data = response.text

soup = BeautifulSoup(data, "html.parser")
all_titles = soup.findAll(name="h3", class_="title")

list_titles = [title.getText() for title in all_titles]
titles = list_titles[::-1]

with open("movies.txt", mode="w") as file:
    for title in titles:
        file.write(f"{title}\n")

