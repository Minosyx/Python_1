from sqlite3 import connect
import random
import string


def dodaj_ankiete(nazwa, kto, terminy):
    with connect('/home/patryk/Pulpit/KP/ankieta.db') as conn:
        c = conn.cursor()
        klucz = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(20))
        c.execute("INSERT INTO ankiety VALUES(?, ?, ?, ?)", (nazwa, kto, terminy, klucz,))
        conn.commit()
        return klucz


def dodaj_propozycje(kto, klucz, terminy):
    with connect('/home/patryk/Pulpit/KP/ankieta.db') as conn:
        c = conn.cursor()
        c.execute("SELECT klucz FROM ankiety WHERE klucz=?", (klucz,))
        check = c.fetchone()
        if check is None:
            return 1
        c.execute("SELECT kto, klucz FROM propozycje WHERE kto=? AND klucz=?", (kto, klucz,))
        osoba = c.fetchone()
        if osoba is None:
            c.execute("INSERT INTO propozycje VALUES(?, ?, ?)", (kto, klucz, terminy,))
        else:
            c.execute("UPDATE propozycje SET terminy=? WHERE kto=? AND klucz=?", (terminy, kto, klucz,))
        conn.commit()
        return 0


def pobierz_propozycje(klucz):
    with connect('/home/patryk/Pulpit/KP/ankieta.db') as conn:
        c = conn.cursor()
        c.execute("SELECT kto, terminy FROM propozycje WHERE klucz=?", (klucz,))
        for line in c:
            print(*line)


def pobierz_ankiete(klucz):
    with connect('/home/patryk/Pulpit/KP/ankieta.db') as conn:
        c = conn.cursor()
        c.execute("SELECT nazwa, kto, terminy FROM ankiety WHERE klucz=?", (klucz,))
        x = c.fetchone()
        print(*x)


kpKey = dodaj_ankiete("KP", "Jan Nowak", '01001010101010111101')
print(kpKey)
print(dodaj_propozycje("Patryk Tajs", kpKey, '00001000100010010101'))
print(dodaj_propozycje("Patryk Tajs", kpKey, '00001000100010010100'))
print(dodaj_propozycje("Jakub Kowalski", kpKey, '00000000100010111101'))

pobierz_propozycje(kpKey)
pobierz_ankiete(kpKey)
