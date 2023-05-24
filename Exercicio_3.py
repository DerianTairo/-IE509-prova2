import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

# Gerar a sequência de números pseudoaleatórios
np.random.seed(42)  # Definir semente para reproduzibilidade
sequence = np.random.uniform(0, 1, 200000)

# Plotar histograma e PDF teórica
fig, ax = plt.subplots(figsize=(8, 6))

# Plotar histograma
n, bins, _ = ax.hist(sequence, bins=50, density=True, alpha=0.7, color='steelblue', edgecolor='black', label='Histograma')

# Plotar PDF teórica
x = np.linspace(0, 1, 100)
pdf = np.ones_like(x)  # Distribuição uniforme U(0,1) tem PDF constante igual a 1
ax.plot(x, pdf, 'r--', lw=2, label='PDF teórica')

ax.set_xlabel('Valores')
ax.set_ylabel('Densidade de probabilidade')
ax.set_title('Histograma e PDF teórica')
ax.legend()

plt.tight_layout()
plt.savefig('figura3.1.png', dpi=900, bbox_inches='tight')
plt.show()

# Plotar função de autocorrelação
autocorr = signal.correlate(sequence - np.mean(sequence), sequence - np.mean(sequence), mode='full', method='auto')
autocorr /= np.max(autocorr)  # Normalizar a autocorrelação pelo valor máximo
lags = np.arange(-(len(sequence)-1), len(sequence))
plt.figure(figsize=(8, 4))
plt.plot(lags, autocorr)
plt.xlabel('Lags')
plt.ylabel('Autocorrelação')
plt.title('Função de autocorrelação')
plt.grid(True)
plt.savefig('figura3.2.png', dpi=900, bbox_inches='tight')
plt.show()