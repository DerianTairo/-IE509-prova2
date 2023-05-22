import numpy as np
import matplotlib.pyplot as plt

# Gerar a sequência de números pseudoaleatórios
np.random.seed(42)  # Definir semente para reproduzibilidade
sequence = np.random.uniform(0, 1, 200000)

# Criar a grade de subplots
fig, axs = plt.subplots(2, 2, figsize=(12, 10))

# Plotar histograma
axs[0, 0].hist(sequence, bins=50, density=True, alpha=0.7, label='Histograma')
axs[0, 0].set_xlabel('Valores')
axs[0, 0].set_ylabel('Densidade de probabilidade')
axs[0, 0].set_title('Histograma')

# Plotar PDF teórica esperada
x = np.linspace(0, 1, 100)
pdf = np.ones_like(x)  # Distribuição uniforme U(0,1) tem PDF constante igual a 1
axs[0, 1].plot(x, pdf, 'r', lw=2, label='PDF teórica')
axs[0, 1].set_xlabel('Valores')
axs[0, 1].set_ylabel('Densidade de probabilidade')
axs[0, 1].set_title('PDF teórica')

# Plotar as duas curvas superpostas e normalizadas
axs[1, 0].hist(sequence, bins=50, density=True, alpha=0.7, label='Histograma')
axs[1, 0].plot(x, pdf, 'r', lw=2, label='PDF teórica')
axs[1, 0].set_xlabel('Valores')
axs[1, 0].set_ylabel('Densidade de probabilidade')
axs[1, 0].set_title('Histograma e PDF teórica')

# Plotar a função de autocorrelação
axs[1, 1].acorr(sequence, maxlags=50)
axs[1, 1].set_xlabel('Lags')
axs[1, 1].set_ylabel('Autocorrelação')
axs[1, 1].set_title('Função de autocorrelação da sequência')

plt.tight_layout()
plt.show()


import numpy as np
import matplotlib.pyplot as plt

# Gerar a sequência de números pseudoaleatórios
np.random.seed(42)  # Definir semente para reproduzibilidade
sequence = np.random.uniform(0, 1, 200000)

# Criar a grade de subplots
fig, axs = plt.subplots(2, 2, figsize=(12, 10))

# Plotar histograma
axs[0, 0].hist(sequence, bins=50, density=True, alpha=0.7, label='Histograma')
axs[0, 0].set_xlabel('Valores')
axs[0, 0].set_ylabel('Densidade de probabilidade')
axs[0, 0].set_title('Histograma')

# Plotar PDF teórica esperada
x = np.linspace(0, 1, 100)
pdf = np.ones_like(x)  # Distribuição uniforme U(0,1) tem PDF constante igual a 1
axs[0, 1].plot(x, pdf, 'r', lw=2, label='PDF teórica')
axs[0, 1].set_xlabel('Valores')
axs[0, 1].set_ylabel('Densidade de probabilidade')
axs[0, 1].set_title('PDF teórica')

# Plotar as duas curvas superpostas e normalizadas
axs[1, 0].hist(sequence, bins=50, density=True, alpha=0.7, label='Histograma')
axs[1, 0].plot(x, pdf, 'r', lw=2, label='PDF teórica')
axs[1, 0].set_xlabel('Valores')
axs[1, 0].set_ylabel('Densidade de probabilidade')
axs[1, 0].set_title('Histograma e PDF teórica')

# Plotar a função de autocorrelação
axs[1, 1].acorr(sequence, maxlags=50)
axs[1, 1].set_xlabel('Lags')
axs[1, 1].set_ylabel('Autocorrelação')
axs[1, 1].set_title('Função de autocorrelação da sequência')

plt.tight_layout()
plt.show()


