print("Método da Secante")

print("Digite os valores de x0 e x1")

x=float(input("Digite o valor de x0: "))

x1=float(input("Digite o valor de x1: "))

epsilon =eval(input("Digite o valor da precisão:  "))

y1=input("Escreva a função f:  ")

def f(x):

    y=eval(y1)

    return y

k=0  #contador

while abs(f(x))>epsilon:

    x2 = x1 - (f(x1)*(x1-x))/(f(x1)-f(x))

    x=x1

    x1=x2

    k=k+1

print(x2)

print('A raiz para a função f é',y1,'é aproximadamente x=',x2, 'com', k, 'iterações')

