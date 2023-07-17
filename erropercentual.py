def f(x):
    return 4.5 + 0.3*x

def calcula_integral_trapezio(a, b, n):
    h = (b - a) / n

    integral = 0

    for i in range(n):
        x0 = a + i * h
        x1 = a + (i + 1) * h
        integral += (f(x0) + f(x1)) / 2

    integral *= h

    return integral

def calcula_erro_percentual(aproximado, analitico):
    erro_absoluto = abs(aproximado - analitico)
    erro_percentual = (erro_absoluto / analitico) * 100
    return erro_percentual

a = 2
b = 3
n = 500

integral_aproximada = calcula_integral_trapezio(a, b, n)
integral_analitica = 5.25

erro_percentual = calcula_erro_percentual(integral_aproximada, integral_analitica)

print("O erro percentual no cálculo da integral do trapézio é:", erro_percentual, "%")
