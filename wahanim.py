import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


def pole_wektorowe(p, t):
    alfa, omega = p
    return(omega, -9.81 * np.sin(alfa))


punkt_poczatkowy = (0.98 * np.pi, 0)
zakres_czasu = np.arange(1, 10, .01)

y = odeint(pole_wektorowe, punkt_poczatkowy, zakres_czasu)

# plt.plot(zakres_czasu, y[:, 0])
# plt.show()

fig, ax = plt.subplots()
trajektoria, = ax.plot([punkt_poczatkowy[0]], [punkt_poczatkowy[1]])
punkt, = ax.plot([punkt_poczatkowy[0]], [punkt_poczatkowy[1]], '.')

def anim(i):
    punkt.set_xdata(zakres_czasu[i])
    punkt.set_ydata(y[i, 0])
    trajektoria.set_xdata(zakres_czasu[:i])
    trajektoria.set_ydata(y[:i, 0])


a = FuncAnimation(fig, anim, range(len(y)), interval=5, repeat=False)
#ax.axis('equal')
ax.set_xlim([1, 10])
ax.set_ylim([-5, 5])

plt.show()
