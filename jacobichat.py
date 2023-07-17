import numpy as np

def gauss_jacobi(A, b, x, n):
    D = np.diag(np.diag(A))
    R = A - D
    
    for _ in range(n):
        x = np.dot(np.linalg.inv(D), b - np.dot(R, x))
    
    print('A solução aproximada após', n, 'iterações é:', x)

A = np.array([[55, 25, 25], [30, 45, 20], [15, 30, 55]])
b = np.array([4200, 4500, 5500])
x = np.array([0, 0, 0])

n = 150  # número de iterações

gauss_jacobi(A, b, x, n)
