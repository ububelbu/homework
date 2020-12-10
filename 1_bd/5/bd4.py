import sqlite3


con = sqlite3.connect("4_entities.db")
cur = con.cursor()
lst_1 = cur.execute("""INSERT INTO cinema VALUES (1, "Крист", "улица Мира 75", "8.00-21.00", 5)""").fetchall()
lst_2 = cur.execute("""INSERT INTO cinema VALUES (2, "Омд",  "улица Попова 27", "9.00-22.00", 6)""").fetchall()
lst_3 = cur.execute("""INSERT INTO cinema VALUES (3, "Шлд",  "улица Кояновская 15", "5.00-00.00", 7)""").fetchall()
lst_4 = cur.execute("""INSERT INTO films VALUES (21, "Дуб", 190, "Комедия", 8)""").fetchall()
lst_5 = cur.execute("""INSERT INTO films VALUES (22, "Поле", 162, "Ужасы", 10)""").fetchall()
lst_6 = cur.execute("""INSERT INTO films VALUES (23, "Мстители", 300, "Триллер", 12)""").fetchall()

first = cur.execute("""UPDATE films SET genre = "Боевик" WHERE id_fil= 23""").fetchall()
second = cur.execute("""DELETE FROM films WHERE id_fil = 21""").fetchall()
con.commit()
con.close()