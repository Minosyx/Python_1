from time import time

t = time()
l = []
for i in range(0, 1000000):
    l.append(i**2)
print(time()-t)

t = time()
[i**2 for i in range(0, 1000000)]
print(time()-t)

t = time()
list(map(lambda i:i**2, range(1000000)))
print(time()-t)

t = time()
list(map((2).__rpow__, range(1000000)))
print(time()-t)