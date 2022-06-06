import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


def pole_wektorowe(p, t):
    x, y, vx, vy = p
    m = (x**2 + y**2)**(-1.5)
    return [vx, vy, -m*x, -m*y]


punkt_poczatkowy = (1, 0, 0, 1.2)
zakres_czasu = np.arange(0, 15, .04)

values = odeint(pole_wektorowe, punkt_poczatkowy, zakres_czasu)

print(values)

plt.plot(values[:, 0], values[:, 1])
plt.plot([0], [0], '.')
plt.axis('equal')
plt.show()

fig, ax = plt.subplots()
trajektoria, = ax.plot([100*punkt_poczatkowy[0]], [100*punkt_poczatkowy[1]])
punkt, = ax.plot([100*punkt_poczatkowy[0]], [100*punkt_poczatkowy[1]], '.')
ax.plot([0], [0], '.')


def anim(i):  # uaktualnia wykres dla itej chwili czasowej
    punkt.set_xdata(100*values[i, 0])
    punkt.set_ydata(100*values[i, 1])
    trajektoria.set_xdata(100*values[:i, 0])
    trajektoria.set_ydata(100*values[:i, 1])


a = FuncAnimation(fig, anim, range(len(values)), interval=40, repeat=False)
ax.axis('equal')
ax.set_xlim([-300, 300])
ax.set_ylim([-200, 200])

plt.show()
