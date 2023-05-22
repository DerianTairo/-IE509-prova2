import numpy as np
import matplotlib.pyplot as plt

n = 200000  # Tamanho da amostra
mu1, mu2 = 1, 3  # Médias das distribuições
sigma1, sigma2 = 1, 2  # Desvios padrão das distribuições
convergence_threshold = 0.05  # Critério de convergência (margem de erro)

np.random.seed(42)  # Definir semente aleatória para reprodução
X1 = np.random.uniform(0, 2, size=n)
X2 = np.random.uniform(1, 5, size=n)

mean_X1 = np.cumsum(X1) / np.arange(1, n + 1)
mean_X2 = np.cumsum(X2) / np.arange(1, n + 1)

plt.plot(range(1, n + 1), mean_X1, label='X1 ~ U(0, 2)')
plt.plot(range(1, n + 1), mean_X2, label='X2 ~ U(1, 5)')
plt.axhline(y=mu1, color='r', linestyle='--', label='Média Verdadeira X1')
plt.axhline(y=mu2, color='g', linestyle='--', label='Média Verdadeira X2')
plt.xlabel('Tamanho da Amostra')
plt.ylabel('Média Amostral')
plt.legend()
plt.show()

plt.savefig('convergence_plot.png')
plt.show()