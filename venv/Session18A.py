import requests
from bs4 import BeautifulSoup

response = requests.get("https://twitter.com/dna")

# HTML Response shall be printed
# print(response.text)

# Web Scrapping
# HTML Parsing -> Extract Meaningful data from HTML Response

soup = BeautifulSoup(response.text, "html.parser")
print("TYPE:",type(soup))
print(">>>>>>>>>><<<<<<<<<")
# print(soup) # Print HTML Response, It will remove indentation
# print(soup.prettify())

print("Fetching title of Web Page")
print(soup.title.text)

print()

"""
children = soup.children
for child in children:
    print(child)
    print("***********************")
"""

"""
pTags = soup.find_all("p")

for tag in pTags:
    print(tag)
    print("^^^^^^^^^^^^^^^^^^^^^^^^^")
"""

"""
divTags = soup.find_all("div")

print(divTags[0])
print(divTags[0].text)
"""

"""
for tag in divTags:
    print(tag)
    print("^^^^^^^^^^^^^^^^^^^^^^^^^")
"""

divTags = soup.find_all("div", class_="js-tweet-text-container")
# print(divTags[0])
# print(divTags[0].text)

for tag in divTags:
    print(tag.text)
    print("^^^^^^^^^^^^^^^^^^^^^^^^^")