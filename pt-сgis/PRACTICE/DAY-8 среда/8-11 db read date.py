import sqlite3

con = sqlite3.connect("people.db")
cursor = con.cursor()


sql3 = '''
SELECT * FROM people
'''

sql4 = '''
SELECT name, age FROM people
WHERE name='Павел'
'''

sql5 = '''
SELECT name, age FROM people
WHERE age > 30
'''
cursor.execute(sql5)

# lst_users = cursor.fetchall()

# for user in lst_users:
#     print(user[1], user[2])

# print(cursor.fetchone())
# print(cursor.fetchone())
# print(cursor.fetchone())

# print(cursor.fetchmany(3))
print(cursor.fetchall())