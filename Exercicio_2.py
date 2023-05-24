import numpy as np
import matplotlib.pyplot as plt

# Tamanho da amostra e parâmetros das distribuições
n = 8000
mu1, mu2 = 1, 3
sigma1, sigma2 = 1, 2

# Semente aleatória para reprodutibilidade
np.random.seed(42)

# Geração das amostras aleatórias
X1 = np.random.uniform(0, 2, size=n)
X2 = np.random.uniform(1, 5, size=n)

# Cálculo das médias amostrais cumulativas
mean_X1 = np.cumsum(X1) / np.arange(1, n + 1)
mean_X2 = np.cumsum(X2) / np.arange(1, n + 1)

# Configurações do estilo do gráfico
plt.style.use('seaborn-whitegrid')

# Criação da figura e dos eixos
fig, ax = plt.subplots(figsize=(8, 6))

# Plot das curvas das médias amostrais
ax.plot(range(1, n + 1), mean_X1, label='X1 ~ U(0, 2)', color='blue', linewidth=1)
ax.plot(range(1, n + 1), mean_X2, label='X2 ~ U(1, 5)', color='orange', linewidth=1)

# Linhas horizontais para as médias verdadeiras

ax.axhline(y=mu1, color='r', linestyle='--', label='Média Verdadeira X1')
ax.axhline(y=mu2, color='g', linestyle='--', label='Média Verdadeira X2')
ax.set_xlabel('Tamanho da Amostra', fontsize=12)
ax.set_ylabel('Média Amostral', fontsize=12)
ax.tick_params(axis='both', labelsize=10)
ax.legend(loc='center left', bbox_to_anchor=(1, 0.5), fontsize=10)
ax.grid(linestyle='--', alpha=0.7)
plt.margins(0.02)
plt.title('Convergência das Médias Amostrais', fontsize=14, fontweight='bold')
plt.savefig('figura2.png', dpi=300, bbox_inches='tight')
plt.show()

