# Imports socket library
import socket

# Builds porthole = library.method(internet socket that is stream socket)
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Opens porthole = create connection to (website/host, port)
mysock.connect(('data.pr4e.org', 80))

# Data to be sent
mysock.send('GET http://data.pr4e.org/intro-short.txt HTTP/1.0\n\n')

# Receiving/Reading - If nothing, the loop ends
while True:
    data = mysock.recv(512)
    if ( len(data) < 1 ) :
        break
    print data

mysock.close()

# you can parse out the strings from an html page you find
# Scraping/Crawling - writing apps to parse out the urls and
# loop/for through the page.

# Reasons?
# Pull data, making up for export capability, site monitoring, social

# Parsing html
html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)

tags = soup('a')
for tag in tags:
    print tag.get('href', None)
