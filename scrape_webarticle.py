import requests
from bs4 import BeautifulSoup
import sys

URL = sys.argv[1]
page = requests.get(URL)



soup = BeautifulSoup(page.content, "html.parser")

headline = soup.find("title")
timestamp = soup.find(attrs={'class':'timestamp'})

content_div = soup.find(id="ResultsContainer")
print("**** Title of the web article is ****")
print()
print(headline.text)
print()
print("**** Timestamp ****")
print(timestamp.text)

