import sqlite3
import hashlib

connection = sqlite3.connect('database.db')

USERNAME = 'jake'
PASSWORD = 'football'

password_hash = hashlib.md5(PASSWORD.encode()).hexdigest()

with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO users (username, password) VALUES (?, ?)",
            (USERNAME, password_hash)
            )

print(password_hash)

connection.commit()
connection.close()