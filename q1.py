def bissecao(f, a, b, TOL):



    import numpy as np



    N= np.floor((np.log(b - a) - np.log(TOL)) / np.log(2)) + 1



    i=1



    fa=f(a)



    while (i<=N):



        p=a+(b-a)/2 #iteracao da bissecao



        fp=f(p)



        if ((fp==0)) or ((b-a)/2<TOL):#condicao de parada



            return p



        i=i+1



        if(fa*fp>0): #bissecta o intervalo



            a=p



            fa=fp



        else:



            b=p



    raise NameError('Num. max. de iter. excedido!');  #raise invoca uma Exception no momento oportuno. 



 



import numpy as np



def f(x):



    return (750 - 200*ln(150.000/(150.000 - (2700*x))))/(-9.81)



 



print(bissecao(f,54,54.5,2.e-16))



Posição falsa:

from __future__ import division

from numpy import log as ln



def posicao_falsa(f, a, b, TOL,N):



    i=1



    fa=f(a)



    while (i<=N):



        p=(a * f(b) - b * f(a)) / (f(b) - f(a)) #iteracao da bissecao



        fp=f(p)



        if ((fp==0)) or ((b-a)<TOL):#condicao de parada



            return p



        i=i+1



        if(fa*fp>0): #bissecta o intervalo



            a=p



            fa=fp



        else:



            b=p



    raise NameError('Num. max. de iter. excedido!');  #raise invoca uma Exception no momento oportuno. 



 



def f(x):



    return (750 - 200*ln(150.000/(150.000 - 2700*x)))/(-9.81)



print(posicao_falsa(f,50,54.6,2.e-16,1000))

