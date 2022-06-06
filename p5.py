import math

print(dir(math))
print(math.atan(2)*180/math.pi)
print(math.tan(63.43494882292201/180*math.pi))

print(math.log(math.e))
print(math.log2(1024))

import random

print(random.random()) # liczba z przedzialu [1, 0] z rozkladem jednostajnym
print(random.randint(1, 2))
print(*[random.randint(0,20) for _ in range(20)])