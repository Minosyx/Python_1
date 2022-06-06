from time import sleep
from threading import Lock, Thread


def stary_print(*args):  # emulacja print z python2 (nieatomowa)
    print(*args, end='')
    sleep(1e-5)
    print()
    sleep(1e-5)


def f(label, l):
    for i in range(5):
        with l:
            stary_print(label, i)
        sleep(1e-5)


# f()
# f()

l = Lock()

w1 = Thread(target=f, args=('watek 1: ', l),)  # daemon=True, nie czekamy na zakonczenie daemonow
w2 = Thread(target=f, args=('watek 2: ', l),)

w1.start()
w2.start()
w1.join()
w2.join()

with l:
    print('Koniec')