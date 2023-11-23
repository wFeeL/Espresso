import sqlite3

con = sqlite3.connect('coffee.sqlite')
cur = con.cursor()

print(cur.execute('SELECT * FROM coffee').fetchall())
