import sqlite3

connect = sqlite3.connect("hw20database.sqlite")
cursor = connect.cursor()
query = ('CREATE TABLE IF NOT EXISTS new_table ('
         'id INTEGER PRIMARY KEY AUTOINCREMENT, '
         'first_name TEXT UNIQUE NOT NULL, '
         'last_name TEXT UNIQUE NOT NULL, '
         'age INTEGER)')
cursor.execute(query)
try:
    insert = ('INSERT INTO new_table(first_name, last_name, age) VALUES '
              '("Vadym", "Demchenko", 29), '
              '("Michael", "Orlando", 25), '
              '("Jerry", "Tompson", 22), '
              '("Eniko", "Snow", 39), '
              '("Alex", "Sheppart", 16)')
    cursor.execute(insert)
    connect.commit()
except sqlite3.IntegrityError:
    print("You're trying to add not a UNIQUE first name or last name")
