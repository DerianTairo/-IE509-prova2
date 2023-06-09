import numpy as np
import matplotlib.pyplot as plt

# Sequência de tempos entre chegadas
np.random.seed(42)  # Definir semente para reproduzibilidade
lambd = 2  # Taxa de chegada
scale = 1 / lambd
arrival_times = np.random.exponential(scale, size=200000)

# Plotar histograma
plt.figure(figsize=(8, 4))
plt.hist(arrival_times, bins=50, density=True, alpha=0.7, edgecolor='black', linewidth=0.8, label='Histograma')

# Plotar PDF teórica
x = np.linspace(0, 10, 1000)
pdf = lambd * np.exp(-lambd * x)
plt.plot(x, pdf, 'r', lw=2, label='PDF teórica')

plt.style.use('seaborn-whitegrid')

plt.xlabel('Tempo entre chegadas')
plt.ylabel('Densidade de probabilidade')
plt.title('Histograma e PDF teórica do tempo entre chegadas')
plt.legend()
plt.grid(True)
plt.savefig('figura4.1.png', dpi=900, bbox_inches='tight')
plt.ylim([0, 1.2 * max(pdf)])
plt.show()
