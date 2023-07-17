import numpy as np
import pylab as plt

def f(y, x):
    return y + 7

x0 = 0
y0 = 2
a = 0
b = 10
Num = 100
h = (b - a) / Num

x_points = np.arange(a, b, h)
y_points = []

for x in x_points:
    y_points.append(y0)
    k1 = h * f(y0, x)
    k2 = h * f(y0 + 0.5 * k1, x + 0.5 * h)
    k3 = h * f(y0 - k1 + 2 * k2, x + h)
    y0 += (k1 + 4 * k2 + k3) / 6

plt.plot(x_points, y_points, color='#FF4500', linewidth=1.5, label='função dy/dx = y + 7')
plt.title('Gráfico da função')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.show()