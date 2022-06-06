from requests import get


def stolica(p):
    try:
        x = get('https://pl.wikipedia.org/wiki/'+p).text
        x = x.split('title="Stolica"', 1)[1].split('">', 1)[1].split('<')[0]
    except:
        x = 'nie znaleziono'
    return x


def stolica2(s):
    x = ''
    f = get('https://pl.wikipedia.org/wiki/'+s, stream=True)
    b, c = '', ''
    for l in f.iter_lines(decode_unicode=True):
        a, b, c = (b, c, l)
        if 'Stolica</a>' in a:
            f.close()
            x = c.split('">', 1)[1].split('<', 1)[0]
    f.close()
    if x == '':
        x = 'nie znaleziono'
        f.close()
    return x


print(stolica2("Brazylia"))

if __name__ == "__main__":

    from sys import argv

    for i in argv[2:]:
        print(stolica2(i))
