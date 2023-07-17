import numpy as np
from scipy.linalg import solve

def gauss(A,b,x,n):
    L = np.tril(A)
    U = A - L
    for i in range(n):
        x = np.dot(np.linalg.inv(L), b - np.dot(U, x))
    print('A solução aproximada após', n, 'iterações é:', x)

A = np.array([[55, 25, 25],[30, 45, 20],[15, 30, 55]])
b = [4200, 4500, 5500]
x = [0,0,0]

n = 30 #numero de iteraçoes

gauss(A, b, x, n)