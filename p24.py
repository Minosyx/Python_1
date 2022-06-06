import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

def pole_wektorowe(p, t):
    alfa, omega = p
    return(omega, -9.81 * np.sin(alfa))


punkt_poczatkowy = (0.98 * np.pi, 0)
zakres_czasu = np.arange(1, 10, .01)

y = odeint(pole_wektorowe, punkt_poczatkowy, zakres_czasu)

plt.plot(zakres_czasu, y[:, 0])
plt.show()