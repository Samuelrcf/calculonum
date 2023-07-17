def trapezoidal_rule(x, y):
    n = len(x) - 1  # Número de subintervalos (número de pontos - 1)
    h = (x[-1] - x[0]) / n  # Tamanho do intervalo

    integral = 0.5 * (y[0] + y[-1])  # Primeiro e último termos

    for i in range(1, n):
        integral += y[i]  # Termos intermediários

    integral *= h  # Multiplicação pelo tamanho do intervalo

    return integral

# Dados da tabela
x = [2.0, 2.2, 2.4, 2.6, 2.8, 3.0]
y = [4.5, 6.8, 10.2, 11.2, 15.8, 20.0]

# Cálculo da integral usando a regra do trapézio
integral = trapezoidal_rule(x, y)

# Exibindo o resultado
print("A integral aproximada é:", integral)
