import sqlite3
import json
import xml.etree.ElementTree as ET

conn = sqlite3.connect('coursedb.sqlite')
cur = conn.cursor()

cur.executescript('''
drop table if exists User;
drop table if exists Course;
drop table if exists Member;
''')

cur.executescript('''

    CREATE TABLE User(
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        name TEXT,
        email TEXT
    );

    CREATE TABLE Course(
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        title TEXT
    );

    CREATE TABLE Member(
        user_id INTEGER,
        course_id INTEGER,
        role    INTEGER,
        PRIMARY KEY (user_id, course_id)
    )''')

filename = raw_input('Enter filename:')
if len(filename) < 1 :
    filename = 'roster_data.json'

str_data = open(filename).read()
json_data = json.loads(str_data)

for entry in json_data:
    name = entry[0];
    title = entry [1];
    role = entry [2]
    print name, title, role

    cur.execute('''INSERT OR IGNORE INTO User (name)
        VALUES (?)''', (name, ))
    cur.execute('SELECT id FROM User WHERE name = ?', (name,))
    user_id = cur.fetchone() [0]

    cur.execute('''INSERT OR IGNORE INTO Course (title)
        VALUES (?)''', (title, ))
    cur.execute('SELECT id FROM Course WHERE title = ?', (title,))
    course_id = cur.fetchone() [0]

    cur.execute('''INSERT OR REPLACE INTO Member
        (user_id, course_id, role) VALUES (?,?,?)''',
        (user_id, course_id, role))

cur.execute('''
    SELECT User.name, Member.role, Course.title
    FROM User JOIN Member JOIN Course
    ON Member.user_id = User.id AND Member.course_id = Course.id
    ORDER BY Course.title, Member.role DESC, User.name
    ''')

conn.commit()
