import numpy as np
import matplotlib.pyplot as plt
from time import time

T = 25*np.ones((100, 100))
T[:, 0] = 0
T[:, -1] = 0
T[0, :] = 50
T[-1, :] = 50
kQ = np.zeros((100, 100))
kQ[25, 25] = 50000
dx = .1

t = time()

for _ in range(1000):  # liczba usrednien
    # Laplace'a
    T[1:-1, 1:-1] = (T[:-2, 1:-1] + T[2:, 1:-1] + T[1:-1, 0:-2] + T[1:-1, 2:])/4  # lewo, prawo, gora, dol
    # Poissona
    # T[1:-1, 1:-1] = (T[:-2, 1:-1] + T[2:, 1:-1] + T[1:-1, :-2] + T[1:-1, 2:] + kQ[1:-1, 1:-1]*dx**2)/4  # lewo, prawo, gora, dol


# ŹLE!
"""
    for i in range(1, 99):
        for j in range(1, 99):
            T[i, j] = (T[i+1, j] + T[i-1, j] + T[i, j+1] + T[i, j-1])/4
"""

print(time() - t)

plt.imshow(T, cmap='jet')
plt.show()
