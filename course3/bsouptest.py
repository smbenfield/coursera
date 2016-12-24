# Imports libraries
import urllib
from bs4 import BeautifulSoup

# Input your URL
url = raw_input('Enter - ')

# Reads all of url
html = urllib.urlopen(url).read()
soup = BeautifulSoup(html, "html.parser")

# Retrieve a list of the anchor tags
# Each tag is like a dictionary of HTML attributes

# Creates list/parsed object of attributes looks for anchor tags
tags = soup('a')

# Loops through attributes and prints urls
for tag in tags:
    print tag.get('href', None)
