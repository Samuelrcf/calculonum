import matplotlib.pyplot as plt

# Constantes e condições iniciais
g = 9.81  # aceleração da gravidade (m/s^2)
cd = 0.225  # coeficiente de arrasto de segunda ordem (kg/m)
m = 90  # massa do objeto (kg)
h = 0.01  # tamanho do intervalo de tempo (s)
t = 0  # tempo inicial (s)
v_euler = 0  # velocidade inicial (m/s) para o método de Euler
v_rk4 = 0  # velocidade inicial (m/s) para o método de Runge-Kutta de quarta ordem
x = 1000  # altura inicial (m)

# Listas para armazenar os valores calculados
time_euler = []
vel_euler = []
time_rk4 = []
vel_rk4 = []

# Iteração para calcular velocidade e posição usando os métodos de Euler e Runge-Kutta de quarta ordem
while x > 0:
    dv_dt_euler = g - (cd/m) * v_euler**2  # derivada da velocidade em relação ao tempo para o método de Euler
    v_euler += dv_dt_euler * h  # atualizar a velocidade usando o método de Euler

    k1 = h * (g - (cd/m) * v_rk4**2)
    k2 = h * (g - (cd/m) * (v_rk4 + k1/2)**2)
    k3 = h * (g - (cd/m) * (v_rk4 + k2/2)**2)
    k4 = h * (g - (cd/m) * (v_rk4 + k3)**2)
    v_rk4 += (k1 + 2*k2 + 2*k3 + k4) / 6  # atualizar a velocidade usando o método de Runge-Kutta de quarta ordem

    x -= v_euler * h  # atualizar a posição usando o método de Euler

    t += h  # avançar para o próximo intervalo de tempo

    # Armazenar os valores calculados nas listas
    time_euler.append(t)
    vel_euler.append(v_euler)
    time_rk4.append(t)
    vel_rk4.append(v_rk4)

# Plotar o gráfico
plt.plot(time_euler, vel_euler, label='Euler')
plt.plot(time_rk4, vel_rk4, label='Runge-Kutta 4ª ordem')
plt.xlabel('Tempo (s)')
plt.ylabel('Velocidade (m/s)')
plt.title('Velocidade em função do tempo')
plt.legend()
plt.show()
