import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt


def pole_wektorowe(p, t):
    xt, yt, dxdt, dydt = p
    ddxddt = -1 * xt / (xt**2 + yt**2)**1.5
    ddyddt = -1 * yt / (xt**2 + yt**2)**1.5
    return (dxdt, dydt, ddxddt, ddyddt)


punkt_poczatkowy = (1, 0, 0, 1.2)
zakres_czasu = np.arange(0, 15, .01)

values = odeint(pole_wektorowe, punkt_poczatkowy, zakres_czasu)

print(values)

plt.plot(values[:, 0], values[:, 1])
plt.plot([0], [0], '.')
plt.axis('equal')
plt.show()