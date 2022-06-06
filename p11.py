from pickle import dump, dumps, load, loads

l = ["Ala", 2., [1+1j, 2, {'a':(1, 2)}]]
s = dumps(l)
print(s)
print(loads(s))

with open("a.pi", "wb") as f:
    dump(l, f)

with open("a.pi", "rb") as f:
    print(load(f))