import numpy as np # A.x =b (L.U)x=b

A = np.array(((9, 5, 2), (5, 10 ,3), (2, 3, 6)))

b = np.array((960, 510, 610))

def LU(A,b): #Ax=b, LUx=b, Ly=b, Ux=y, x=Linv.Uinv.b : solução

    import scipy.linalg

    L,U =scipy.linalg.lu(A,permute_l=True)

    y=scipy.linalg.solve(L,b)

    x=scipy.linalg.solve(U,y)

    return x

print("A solução do sistema linear é: ", LU(A,b))

import numpy as np
autovalores = np.linalg.eig(A)
print(autovalores)

Determinante = np.linalg.det(A)
print(Determinante)

Inversa = np.linalg.inv(A)
print("A inversa de A é: ", Inversa)

numero_condicionamento = np.linalg.cond(A)
print(numero_condicionamento)

norma = np.linalg.norm(A)
print(norma)

norma1 = np.linalg.norm(Inversa)
print(norma1)

cond = norma*norma1
print(cond)

rank = np.linalg.matrix_rank(A)
print(rank)