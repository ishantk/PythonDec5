import requests

# Read Data from Server
response = requests.get("https://twitter.com/dna")

"""
Send Data to Server
url = "http://delhihighcourt.nic.in/case.asp"
data = {"sno":2, "party":"John", "pyear":2018}
response = requests.post(url=url, data=data)
"""

print(response.text)

