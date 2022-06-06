from socket import SOL_SOCKET, SO_REUSEADDR, socket
from threading import Thread, Lock

d = {}  # slownik par (nick, gniazdo)
l = Lock()  # blokada slownika


def validate(x):
    if x == b'':
        return ">Nie może być pusty, podaj swój nick: ".encode("utf8")
    elif x in d:
        return ">Już w słowniku, podaj swój nick: ".encode("utf8")
    elif b'*' in x or b'<' in x or b'>' in x:
        return ">Podano niedozwolony znak w nicku. Podaj nowy nick: ".encode("utf8")


def con(c, a):
    try:
        c.sendall(">Witamy na serwerze, podaj swój nick: ".encode("utf8"))
        x = c.recv(1024)
        while True:  # faza logowania
            if x == b'':
                c.close()
                return
            x = x.strip()
            with l:
                v = validate(x)
                if v is None:
                    d[x] = c
                    nick = x
                    break  # z with
                    break  # z while
                c.sendall(v)
                x = c.recv(1024)
        c.sendall(">Teraz możesz wysyłać i odbierać wiadomości\n".encode("utf8"))
        while True:  # faza rozmowy
            x = c.recv(1024)
            if x == b'':
                c.close()
                return
            x = x.strip()
            if b'<' not in x:
                c.sendall(">Nieprawidłowy format wiadomości\n".encode("utf8"))
                continue
            adr, message = x.split(b'<', 1)
            with l:
                ca = d.get(adr)
            if adr == b"*":
                list(d[x].sendall(nick + b'>' + message + b'\n') for x in d if x != nick)
            elif b',' in adr:
                list(d[a].sendall(nick + b'>' + message + b'\n') for a in adr.split(b',') if a != nick and a in d)
            elif ca is None and message == b"E":
                break
            elif ca is None and message == b"L":
                c.sendall(">Dostępni użytkownicy:\n".encode("utf8"))
                list(c.sendall(x + b'\n') for x in d if x != nick)
            elif ca is None:
                c.sendall(">Użytkownik nie istnieje\n".encode("utf8"))
                continue
            else:
                ca.sendall(nick + b'>' + message + b'\n')
        with l:
            del d[nick]
    finally:
        c.close()


s = socket()  # AF_INET; SOCK_STREAM; TCP
s.bind(('localhost', 4444))
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
s.listen(1)
try:
    while True:
        Thread(target=con, args=s.accept()).start()
finally:
    s.close()
