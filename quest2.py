x = [2.0, 2.2, 2.4, 2.6, 2.8, 3.0]
f = [4.5, 6.8, 10.2, 11.2, 15.8, 20.0]

def calcula_integral_trapezio(x, f):
    integral = 0
    n = len(x) - 1

    for i in range(n):
        h = x[i + 1] - x[i]
        integral += (f[i] + f[i + 1]) / 2 * h

    return integral

a = 2
b = 3

integral_aproximada = calcula_integral_trapezio(x, f)

print("A integral aproximada é:", integral_aproximada)
