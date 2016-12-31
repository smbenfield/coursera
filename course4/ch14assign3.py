import xml.etree.ElementTree as ET
import sqlite3

conn = sqlite3.connect('library.sqlite')
cur = conn.cursor()

cur.executescript('''
drop table if exists Artist;
drop table if exists Album;
drop table if exists Genre;
drop table if exists Track;

CREATE TABLE Artist(
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name TEXT UNIQUE
);

CREATE TABLE Album(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    artist_id INTEGER,
    title TEXT UNIQUE
);

CREATE TABLE Genre(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name TEXT UNIQUE
);

CREATE TABLE Track (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title TEXT UNIQUE,
    album_id INTEGER,
    len INTEGER,
    rating INTEGER,
    count INTEGER,
    genre_id INTEGER
);
''')

fname = raw_input('Enter file name: ')
if len(fname) < 1:
    fname = 'Library.xml'

def lookup(d, key):
    found = False
    for child in d:
        if found: return child.text
        if child.tag == 'key' and child.text == key:
            found = True
    return None

stuff = ET.parse(fname)
all = stuff.findall('dict/dict/dict')
print 'Dict count:', len(all)
for entry in all:
    if lookup(entry, 'Track ID') is None:
        continue
    name = lookup(entry, 'Name')
    artist = lookup(entry, 'Artist')
    album = lookup(entry, 'Album')
    count = lookup(entry, 'Play Count')
    rating = lookup(entry, 'Rating')
    length = lookup(entry, 'Total Time')
    genre = lookup(entry, 'Genre')

    if name is None or artist is None or album is None or genre is None:
        continue

    print name, artist, album, count, rating, length, genre

    cur.execute('''INSERT OR IGNORE INTO Artist (name) VALUES (?)''', (artist, ))
    cur.execute('SELECT id from Artist WHERE name = ?', (artist, ))
    artist_id = cur.fetchone()[0]

    cur.execute('''INSERT OR IGNORE INTO Genre (name) VALUES (?)''', (genre, ))
    cur.execute('SELECT id from Genre WHERE name = ?', (genre, ))
    genre_id = cur.fetchone()[0]

    cur.execute('''INSERT OR IGNORE INTO Album (title, artist_id) VALUES (?,?)''', (album, artist_id))
    cur.execute('SELECT id from Album WHERE title = ?', (album, ))
    album_id = cur.fetchone()[0]

    cur.execute('''INSERT OR REPLACE INTO Track (title, album_id, len, rating, count, genre_id) VALUES (?,?,?,?,?,?)''', (name, album_id, length, rating, count, genre_id ))

conn.commit()
