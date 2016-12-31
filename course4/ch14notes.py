#CRUD - Create - Retrieve - Update - Delete

import sqlite3

INSERT INTO Users(name, email) VALUES('Kristin','kf@umich.edu')

DELETE FROM Users WHERE email = 'csev@umich.edu'

UPDATE Users SET name = 'Dicklord' WHERE email = 'jeewing@umich.edu'

SELECT * FROM Users

SELECT * FROM Users WHERE email = 'jeewing@umich.edu'

SELECT * FROM Users ORDER BY email

SELECT * FROM Users ORDER BY name
