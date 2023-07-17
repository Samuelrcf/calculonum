import math

def f(x):
    return 1 - math.exp(-2*x)

def calcula_integral_trapezio_repetida(a, b, n):
    h = (b - a) / n

    integral = 0

    for i in range(n):
        x0 = a + i * h
        x1 = a + (i + 1) * h

        integral += (f(x0) + f(x1)) / 2

    integral *= h

    return integral

a = 0
b = 4
n = 500

integral_aproximada = calcula_integral_trapezio_repetida(a, b, n)
integral_analitica = 3.500167731313951

erro_percentual = abs((integral_aproximada - integral_analitica) / integral_analitica) * 100

print("A integral aproximada é:", integral_aproximada)
print("A integral analítica é:", integral_analitica)
print("Erro percentual:", erro_percentual, "%")
