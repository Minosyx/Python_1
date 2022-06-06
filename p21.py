from sqlite3 import connect

conn = connect('baza.db')
try:
    c = conn.cursor()
    # c.execute("SELECT * FROM tablica")
    # odczyt z bazy danych
    # x = c.fetchall()
    # x = c.fetchone()
    # for wiersz in c:
    #     print(wiersz)
    # print(x)
    c.execute("INSERT INTO tablica VALUES ('bonifacy', 6, 10, 'kot')")
    conn.commit()
except:
    conn.rollback()
finally:
    conn.close()
