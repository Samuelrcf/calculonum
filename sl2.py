import  numpy as np   # A.x =b   (L.U)x=b

A = np.array(((2,3,1), (1,2,3), (3,1,2)))

b = np.array((9,6,8))

import time

inicio = time.time()

def LU(A,b):   #Ax=b, LUx=b, Ly=b, Ux=y, x=Linv.Uinv.b : solução

    import scipy.linalg

    L,U =scipy.linalg.lu(A,permute_l=True)

    y=scipy.linalg.solve(L,b)

    x=scipy.linalg.solve(U,y)

    return x

print("A solução do sistema linear é: ", LU(A,b))
print()

fim = time.time()

 

print("O tempo de execução para encontrar a solução do sistema é: ",(fim - inicio)*1000)