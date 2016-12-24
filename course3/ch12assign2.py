import urllib
from bs4 import BeautifulSoup

url = raw_input('Enter URL:')
runs = int(raw_input('Enter count:'))
posi = int(raw_input('Enter position:'))

print url

while runs > 0:
    html = urllib.urlopen(url).read()
    soup = BeautifulSoup(html, "html.parser")
    tags = soup('a')
    newurl = tags[posi - 1].get('href', None)
    runs = runs - 1
    print newurl
    url = newurl
