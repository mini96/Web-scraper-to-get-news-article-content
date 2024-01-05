import requests
from bs4 import BeautifulSoup
import sys

# The below variable collects the URL Argument the users enter when running this script
URL = sys.argv[1]
page = requests.get(URL)


# Soup is the variable used to store all the html content
soup = BeautifulSoup(page.content, "html.parser")

# Below are the variables for the respective items requested to display from the website
headline = soup.find("title")
timestamp = soup.find(attrs={'class':'timestamp'})
content = soup.find(attrs={'class':'article__content-container'})

# Printing the items with formatting
## content_div = soup.find(id="ResultsContainer")
print("**** Title of the web article is ****")
print()
print(headline.text)
print()
print("**** Timestamp ****")
print(timestamp.text)
print()
print("**** Content ****")
print(content.text)

