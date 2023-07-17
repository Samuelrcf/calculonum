import numpy as np

# Dados iniciais
A = np.array([[55, 25, 25],
              [30, 45, 20],
              [15, 30, 55]])

B = np.array([[4200],
              [4500],
              [5500]])

epsilon = 1e-6  # Critério de parada: erro máximo
max_iterations = 30  # Critério de parada: máximo de iterações

# Solução inicial
X = np.array([[0],
              [0],
              [0]])

# Iterações do método de Gauss-Jacobi
for iteration in range(max_iterations):
    X_old = X.copy()  # Copiar a solução anterior
    
    for i in range(A.shape[0]):
        sum_1 = np.dot(A[i, :i], X_old[:i])  # Somatório das componentes anteriores
        sum_2 = np.dot(A[i, i+1:], X_old[i+1:])  # Somatório das componentes seguintes
        
        X[i] = (B[i] - sum_1 - sum_2) / A[i, i]  # Atualização da solução
    
    error = np.linalg.norm(X - X_old)  # Cálculo do erro
    
    if error < epsilon:
        print("Convergência alcançada após", iteration+1, "iterações.")
        break

# Imprimir a solução encontrada
print("Solução encontrada:")
print(X)
