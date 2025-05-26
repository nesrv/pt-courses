import sqlite3

con = sqlite3.connect("people.db")
cursor = con.cursor()

# sql ='''
# CREATE TABLE people
#     (id INTEGER PRIMARY KEY AUTOINCREMENT,
#     name TEXT,
#     age INTEGER)
# '''


# sql2 = '''
# INSERT INTO people (name, age)
# VALUES ('Tom', 38)
# '''

sql3 = '''
INSERT INTO people (name, age)
VALUES (?, ?)
'''

lst_users = [("Павел", 35), ("Раиль", 28)]

# cursor.execute(sql3, ("Айрат", 30) )
cursor.executemany(sql3, lst_users )


con.commit()