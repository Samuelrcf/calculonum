import numpy as np # A.x =b (L.U)x=b

A = np.array(((55, 25, 25), (30, 45, 20), (15, 30, 55)))

b = np.array((4200, 4500, 5500))

def LU(A,b): #Ax=b, LUx=b, Ly=b, Ux=y, x=Linv.Uinv.b : solução

    import scipy.linalg

    L,U =scipy.linalg.lu(A,permute_l=True)

    y=scipy.linalg.solve(L,b)

    x=scipy.linalg.solve(U,y)

    return x

print("A solução do sistema linear é: ", LU(A,b))

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