import requests
from bs4 import BeautifulSoup

response = requests.get("https://www.imdb.com/india/top-rated-indian-movies/")
soup = BeautifulSoup(response.text, "html.parser")


divTags = soup.find_all("td", class_="titleColumn")

movies = []

for tag in divTags:
    print(tag.text)
    movies.append(tag.text.strip())


for m in movies:
    print(m)

# Assignment : Create a Line Graph Ratings Vs Year | Sorted
# H.W. -> 2018 Top Bollywood Singer !!