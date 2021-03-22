import sqlite3

connection = sqlite3.connect("../lesson6/db.sqlite3")

cursor = connection.cursor()
cursor.execute("CREATE TABLE course (id INTEGER PRIMARY KEY, name TEXT NOT NULL)")

cursor.close()
connection.close()