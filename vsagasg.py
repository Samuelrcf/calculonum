import numpy as np
import scipy.linalg

A = np.array(((1, 1, -1, 2), (2, 3, -4, 0), (0, -2, 0, -10), (4, -1, 0, -5)))
b = np.array((2, 2, 2, 20))


def LU(A, b):
    L, U = scipy.linalg.lu(A, permute_l=True)
    y = scipy.linalg.solve(L, b)
    x = scipy.linalg.solve(U, y)
    return x


solution = LU(A, b)
print("A solução do sistema linear é:", solution)

autovalores = np.linalg.eigvals(A)
print("Autovalores:", autovalores)

