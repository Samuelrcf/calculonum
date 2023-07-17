
import numpy as np; # biblioteca de manipulação de matrizes

 

def main ():

    ''' função apenas para matrizes quadradas NxN, chama  fatoraLU e retorn L ,U '''

    

    m = int(input("Digite o número de linhas da matriz: "))

    matriz = cria_matriz(m  )

    triangula = fatoraLU(matriz )

  

    return  triangula

 

def  cria_matriz(m ):

    matriz  =  np.zeros([m,m] )

    for  i in range(0, m ):

        for j in range(0, m ):

            matriz  [ i , j ] =  input( "Digite o elemento [" + str(i )+"] [" + str(j )+"]" )

            matriz [ i , j ] = float(matriz[ i , j ]  )   

    return  matriz

 

def fatoraLU (matriz ):

    U = np.copy(matriz )  

    n = np.shape(U)[0] # retorna o numero de linhas da matriz 

    L = np.eye(n)  

    for j in np.arange(n-1):  

        for i in np.arange(j+1,n):  

            L[i,j] = U[i,j]/U[j,j]  

            for k in np.arange(j+1,n):  

                U[i,k] = U[i,k] - L[i,j]*U[j,k]  

            U[i,j] = 0      

    return L, U;