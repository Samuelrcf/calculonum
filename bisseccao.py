def metodo_bissecao(f,a,b,epsilon):

    fa = f(a)

    fb = f(b)    

    if fa*fb > 0:

        print("Função com o mesmo sinal nos extremos do intervalo!")

        exit(0)

    while b-a > epsilon:

        c = (a+b)/2

        fc = f(c)    

        if fa*fc < 0:

            b, fb = c, fc

        elif fa*fc > 0:

            a, fa = c, fc

        else:

            return c

    return (a+b)/2

def f(x):

    return x**3 - 9 * x + 5

print(metodo_bissecao(f,-4,-3,0.000001))