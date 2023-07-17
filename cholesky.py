import numpy as np

A = np.array([[9.0,5.0,2.0], [5.0,10.0,3.0],[2.0,3.0,6.0]]) 

l11=np.sqrt(A[0,0])

l12=0

l13=0

l21=(A[1,0]/l11)

l22=np.sqrt(A[1,1]-l21**2)

l23=0

l31=(A[2,0]/l11)

l32=((A[2,1]-l21*l31)/l22)

l33=np.sqrt(A[2,2]-l31**2-l32**2)

L=((l11,0,0),(l21,l22,0),(l31,l32,l33))

print(L)

 

#Solução do Sistema

b = np.array((960,510,610))

Lt = np.transpose(L)

Inversa1 = np.linalg.inv(L)

Inversa2 = np.linalg.inv(Lt)

y  = np.dot(Inversa1, b)

x = np.dot(Inversa2,y)

print("A solução dos sitema é:", x)

