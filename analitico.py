import math

def f(x):
    return 1 - math.exp(-2*x)

def calcula_integral_analitica(a, b):
    integral = b + 0.5*math.exp(-2*b) - (a + 0.5*math.exp(-2*a))
    return integral

a = 0
b = 4

integral_analitica = calcula_integral_analitica(a, b)

print("A integral analítica é:", integral_analitica)
