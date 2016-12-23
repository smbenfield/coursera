# Imports socket library
import socket

# Builds porthole = library.method(internet socket that is stream socket)
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Opens porthole = create connection to (website/host, port)
mysock.connect(('www.py4inf.com', 80))

# Data to be sent
mysock.send('GET http://www.py4inf.com/code/romeo.txt HTTP/1.0\n\n')

# Receiving/Reading - If nothing, the loop ends
while True:
    data = mysock.recv(512)
    if ( len(data) < 1 ) :
        break
    print data

mysock.close()

# Imports urllib library
import urllib

fhand = urllib.urlopen('http://www.py4inf.com/code/romeo.txt')

for line in fhand:
    print line.strip()
