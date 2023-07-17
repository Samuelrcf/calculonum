from __future__ import division

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

    return x**3 - 9 * x + 5

print(posicao_falsa(f,0.0,1.0,2.e-16,100))