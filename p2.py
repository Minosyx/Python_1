l = [1, 2, 3]
print(sum(l))

l = [(1,), (2,), (3,)]
print(sum(l, tuple()))

l = [1, 2, 3]
print(l[0], l[1], l[2])
print(*l)  # operator spakowania sekwencji

###################
print('#'*40)

for i in 'Ala':
    print(i)

for i in 'żółw'.encode('utf8'):
    print(i)

for i in range(2, 20, 2):
    print(i)

for i in range(5):
    if i < 2:
        continue
    print(i)
else:
    print('ok')  # jeżeli wyjdziemy z petli czysto

###############
print('#'*40)

l = [4, 3, 6, 5]
l1 = []
for i in l:  # niepoprawne
    l1.append(i*i)
print(l1)

l2 = [x**2 for x in l]  # poprawne
print(l2)

l3 = []
for i in l:
    if i % 2 == 1:
        l3.append(i*i)
print(l3)

l4 = [x**2 for x in l if x % 2]  # poprawne
print(l4)

for i in range(5):
    for j in range(i):
        print((i, j))

l5 = [(i, j) for i in range(5) for j in range(i)]
print(l5)

l6 = [(1, 2, 3), (4, 1), (3, 4), (1,), (3, 2), (3, 2, 3)]

lsum = [sum(i) for i in l6 if len(i) % 2 == 0]
print(lsum)

last = [i[-1] for i in l6]
print(last)

##################
print('#'*40)

d = {'1': 'jeden', '2': 'dwa'}
print(d['1'])
print(d.get('3', 'nie ma'))

print(d.pop('2'))
print(d)
d['2'] = 'dwa'
print(d)
d['2'] = 'dwie'
print(d)

print('1' in d, '3' in d)  # operator członkostwa
k = d.keys()
v = d.values()
print(k)
print(v)
d['3'] = 'trzy'
print(k)
print(v)

####################
print('#'*40)


def funkcja(x):
    return(2*x)


print(funkcja(2))
print(funkcja('2'))


def funkcja(x, a=2, b=0):
    return(a*x + b)


print(funkcja(2))
print(funkcja(2, 3))
print(funkcja(2, 3, 1))
print(funkcja(2, b=1))

args = (2, 3, 1)
print(funkcja(*args))

kw_args = {'x': 2, 'a': 3, 'b': 1}
print(funkcja(**kw_args))  # operator spakowania slownika


def pole(a, b=None):
    if b == None:
        b = a
    return a*b


print(pole(2, 3))
print(pole(3))


def pole(a, b=None):
    return a*(a if b == None else b)


print(pole(2, 3))
print(pole(3))


def f(*args):  # funkcja o zmiennej liczbie argumentow
    return args


print(f('1', 'żółw', (-2)**.5, 1.0))


def f1(x):
    global y  # y będzie zmienną globalną
    y = 2
    return y*x


y = 3
print(f1(5))
print(y)

#####################
print("#"*40)


def kwadrat(a):
    return a**2


def kwadrat(a): return a**2  # konstrukcja funkcji anonimowej


def pole(a, b=None): return a*(a if b == None else b)


srednia = lambda *args: sum(args)/len(args)

l = [1, 3, 2, 4]
print([x**2 for x in l])
print(list(map(kwadrat, l)))
print(list(map(lambda a: a**2, l)))
print(list(filter(lambda x: x % 2 == 1, l)))

lf = [lambda x:1, lambda x:x, lambda x:x**2-1, lambda x:x-1]
l = [i(0) for i in lf]
print(l)

l1 = list(map(lambda i: i(0), lf))
print(l1)

l2 = list(filter(lambda i: i(-1) >= 0, lf))
print(l2)

lt = [(1, 4), (2, 3), (0, 5)]
print(sorted(lt))
print(sorted(lt, key=lambda x: x[-1]))

d = {'a': 10, 'b': -1, 'c': 2}
k = d.keys()
print(k)

print(sorted(k, key=lambda x: d[x]))
print(sorted(k, key=lambda x: d.get(x)))
print(sorted(k, key=d.get))

ls = "Ala ma kota".split()
print(ls)
print(sorted(ls, key=len))

print(min(ls), max(ls))
print(min(ls, key=len), max(ls, key=len))

ls.sort(key=len)  # sortowanie listy w miejscu
print(ls)
