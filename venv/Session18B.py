import requests
from bs4 import BeautifulSoup

response = requests.get("http://zeenews.india.com/")
soup = BeautifulSoup(response.text, "html.parser")


divTags = soup.find_all("div", class_="mini-con")

for tag in divTags:
    print(tag.text)
    print("^^^^^^^^^^^^^^^^^^^^^^^^^")