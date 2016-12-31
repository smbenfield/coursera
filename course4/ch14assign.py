import urllib
import sqlite3
import re
from bs4 import BeautifulSoup

ect = dict()
elst = list()

conn = sqlite3.connect('emaildb.sqlite')
cur = conn.cursor()

cur.execute('''DROP TABLE IF EXISTS Counts''')

cur.execute('''CREATE TABLE Counts (org TEXT, count INTEGER)''')

filename = raw_input("Enter Filename:")
if len(filename) < 1:
    filename = 'mbox.txt'
hand = open(filename)
for line in hand:
    line = line.rstrip()
    if re.search('^From:', line): # ^ means starts with
        line = line.split()
        email = line[1]
        email = email.split('@')
        domain = email[1]
        elst.append(domain)

for item in elst:
    ect[item] = ect.get(item, 0) + 1

print ect
for item in ect:
    cur.execute('''INSERT INTO Counts (org, count) VALUES (?, ?)''', (item, ect[item]))
    conn.commit()

sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'

for row in cur.execute(sqlstr) :
    print str(row[0]), row[1]

cur.close()
