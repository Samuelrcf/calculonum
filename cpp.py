import numpy
import math

def f(x):
    return 525-9.8 * x * (1-numpy.exp(-135/x))

def new_x(a,b):
    return (a * f(b) - b * f(a)) / (f(b) - f(a))

def solver(a,b,x,epsilon):
    if (abs(f(x))) <= epsilon:
        print("FIND ROOT[" , x , "] = ", abs(f(x)))

    if (f(a) * f(x) <= 0):
        b = x 
        x = new_x(a,b)
        return solver(a,b,x,epsilon)

    if (f(x) * f(b) <= 0):
        b = x 
        x = new_x(a,b)
        return solver(a,b,x,epsilon)

a = 0
b = 60
x = new_x(a,b)
epsilon = 0.0001

if (solver(a,b,x,epsilon) == 0):
    print('Nao foi encontrada raiz no intervalo', a, ',', b)

