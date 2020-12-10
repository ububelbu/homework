import sqlite3


con = sqlite3.connect("films.db")
cur = con.cursor()
result = cur.execute("""SELECT all FROM genres WHERE id in (SELECT genre FROM Films WHERE year = 2010)""").fetchall()
for elem in result:
    print(elem)
con.close()