import math

def f(x):
    return 1 - math.exp(-2*x)

def calcula_integral_simpson_repetida(a, b, n):
    h = (b - a) / n

    integral = 0

    for i in range(n):
        x0 = a + i * h
        x1 = a + (i + 0.5) * h
        x2 = a + (i + 1) * h

        integral += (f(x0) + 4*f(x1) + f(x2)) / 6

    integral *= h

    return integral

a = 0
b = 4
n = 500

integral_aproximada = calcula_integral_simpson_repetida(a, b, n)

print("A integral aproximada é:", integral_aproximada)
