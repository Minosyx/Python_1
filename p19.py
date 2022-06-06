from socket import SOL_SOCKET, SO_REUSEADDR, socket
from threading import Thread


def con(c, a):
    try:
        while True:
            x = c.recv(8)
            print(x)
            if x == b'':  # wykrywanie zerwania polaczenia
                break
            c.sendall(x)
    finally:
        c.close()


s = socket()  # AF_INET; SOCK_STREAM; TCP
s.bind(('localhost', 4444))
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
s.listen(1)
try:
    while True:
        # c, a = s.accept()
        Thread(target=con, args=s.accept()).start()
        # w = Thread(target=con, args=(c, a))
        # w.start()
        # try:
        #     while True:
        #         x = c.recv(8)
        #         print(x)
        #         if x == b'':  # wykrywanie zerwania polaczenia
        #             break
        #         c.sendall(x)
        # finally:
        #     c.close()
finally:
    s.close()
