from capital import stolica2 as c
from time import time
from threading import Lock, Thread
from queue import Queue

l = ['Litwa', 'Łotwa', 'Estonia', 'Finlandia',
     'Szwecja', 'Norwegia', 'Polska', 'Niemcy']

###################

t = time()

for p in l:
    print(c(p))
print(time()-t)

###################

t = time()
lock = Lock()


def cap(kraj, lock):
    x = c(kraj)
    with lock:
        print(x)


threads = [Thread(target=cap, args=(kraj, lock)) for kraj in l]

for th in threads:
    th.start()
for th in threads:
    th.join()
print(time()-t)

###################


def work_thread(q, l, i):
    while not q.empty():
        x = q.get()
        s = c(x)
        with l:
            print("watek:", i, " : ", s)


t = time()

q = Queue()

for kraj in l:
    q.put(kraj)

N = 8  # ilosc watkow zatrudnionych do pracy
threads = [Thread(target=work_thread, args=(q, lock, i)) for i in range(N)]

for th in threads:
    th.start()
for th in threads:
    th.join()
print(time()-t)
