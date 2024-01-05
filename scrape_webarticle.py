import requests
from bs4 import BeautifulSoup
import sys

URL = sys.argv[1]
page = requests.get(URL)



soup = BeautifulSoup(page.content, "html.parser")

headline = soup.find("title")

content_div = soup.find(id="ResultsContainer")

print(headline.string)

