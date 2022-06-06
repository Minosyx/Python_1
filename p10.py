from requests import get
from sys import argv
from time import time

from requests.models import Response


def stolica(x):
    try:
        x = get("https://pl.wikipedia.org/wiki/"+x).text
        x = x.split('title="Stolica"', 1)[1].split('">', 1)[1].split("</")[0]
    except:
        x = "nie znaleziono"
    return x


# print(stolica('Polska'))


def capital(x):
    y = ''
    try:
        x = get("https://pl.wikipedia.org/wiki/"+x, stream=True)
    except:
        return 'nie znaleziono'
    found = False
    for line in x.iter_lines():
        if b'title="Stolica"' in line:
            found = True
            continue
        if found is True and b'">' in line:
            y = line.split(b'title="', 1)[1].split(b'">')[0]
            Response.close(x)
            break
    if isinstance(y, bytes):
        y = y.decode('utf-8')
    return y


# print(capital('Polska'))

if(__name__):
    for i in argv[1:]:
        t = time()
        print(stolica(i))
        print(f"czas: {time()-t}")
        t = time()
        print("For: "+capital(i))
        print(f"czas: {time()-t}")
