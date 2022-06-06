import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

X1 = np.array([1, 2, 3], dtype=np.float128)
X2 = np.zeros(3)
X3 = np.ones(3)
print(X1)
print(X2)
print(X3)
print(2*X1**2 + X3**X1)
print(np.sin(X3))

X4 = np.linspace(0, 1, 11)
print(X4)
X5 = np.arange(0, 1, .1)
print(X5)

# wykresy

# plt.plot([1, 2, 3], [4, 5, 5], '-.c', [5, 3, 3], '--g', marker='*',
#          markersize=10, markerfacecolor='red', label='kropki')
# x = np.arange(0, np.pi, .01)
# plt.plot(x, np.sin(x)*2*np.cos(2*x)**2, label='oscylacje')
# var = np.arange(0, 2 * np.pi, .01)
# plt.plot(4 * np.cos(var), 2 * np.sin(var), label='elipsa')
# plt.legend()
# plt.axis('equal')
# plt.show()

# wycinki

X = np.linspace(0, 1, 11)
print(X, X[2:], X[:2])
Y = np.logical_or(X < .5, X > .8)
# X[4:] = 0
# X[4:] = np.linspace(4, 5, 7)
# X[4:] = 2*X[4:]
X[Y] = 2*X[Y]
print(X)

#

print(np.array([-1, 0, 1]) / np.array([0, 0, 0]))

# x = np.linspace(-4, 4, 801)
# y = 1/x
# y[np.abs(y) > 4] = np.NaN
# plt.plot(x, y)
# plt.axis('equal')
# plt.show()

# tablice dwuwymiarowe
A = np.zeros((3, 4))
print(A)
A = np.ones((3, 4))
print(A)
A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(A)
print(A[1:, :-1])

X = np.linspace(1, 3, 3)
Y = np.linspace(4, 6, 3)
print(X, Y)

X, Y = np.meshgrid(X, Y) # iloczyn kartezjanski z robiciem wspolrzednych na dwie siatki
print(X)
print(Y)

#

X = np.linspace(-2, 2, 401)
Y = np.linspace(-2, 2, 401)

X, Y = np.meshgrid(X, Y)

Z = X**2 + Y**2 + .25 * X**3
Z[(X-1)**2 + (Y-1)**2 < .25] = np.NaN
# plt.contour(X, Y, Z, 25)
# plt.contourf(X, Y, Z, 25)
# plt.axis('equal')
# plt.show()

#

fig = plt.figure()
ax = Axes3D(fig)
ax.plot_surface(X, Y, Z)
plt.show()