<<<<<<< HEAD
import numpy as np
import matplotlib.pyplot as plt
from scipy.special import factorial

# Gerar a sequência de tempos entre chegadas
np.random.seed(42)  # Definir semente para reproduzibilidade
lambd = 2  # Taxa de chegada
scale = 1 / lambd
arrival_times = np.random.exponential(scale, size=200000)

# Cascatear os tempos entre chegadas para obter a linha do tempo
time = np.cumsum(arrival_times)
time = time[time <= 50000]  # Descartar o excedente além de 50.000 unidades de tempo

# Computar a frequência relativa dos números de chegadas em janelas de tempo
window_size = 100
num_windows = int(time[-1] // window_size)  # Número de janelas de tempo
window_counts = np.zeros(num_windows, dtype=int)

for i in range(num_windows):
    start_time = i * window_size
    end_time = (i + 1) * window_size
    window_counts[i] = np.sum((time >= start_time) & (time < end_time))

# Calcular a frequência relativa
frequency_relative = window_counts / window_size

# Plotar o histograma dos tempos entre chegadas
plt.figure(figsize=(8, 4))
plt.hist(window_counts, bins=20, density=True, alpha=0.7, label='Frequência relativa')

# Plotar a distribuição de probabilidade teórica
x = np.arange(0, np.max(window_counts) + 1)
pdf_theoretical = np.exp(-lambd * window_size) * (lambd * window_size) ** x / factorial(x, exact=False)
plt.plot(x, pdf_theoretical, 'r', lw=2, label='Distribuição teórica')

plt.xlabel('Número de chegadas')
plt.ylabel('Frequência relativa')
plt.title('Frequência relativa dos números de chegadas em janelas de tempo')
plt.legend()
plt.grid(True)
plt.show()

=======
import numpy as np
import matplotlib.pyplot as plt
from scipy.special import factorial

# Gerar a sequência de tempos entre chegadas
np.random.seed(42)  # Definir semente para reproduzibilidade
lambd = 2  # Taxa de chegada
scale = 1 / lambd
arrival_times = np.random.exponential(scale, size=200000)

# Cascatear os tempos entre chegadas para obter a linha do tempo
time = np.cumsum(arrival_times)
time = time[time <= 50000]  # Descartar o excedente além de 50.000 unidades de tempo

# Computar a frequência relativa dos números de chegadas em janelas de tempo
window_size = 100
num_windows = int(time[-1] // window_size)  # Número de janelas de tempo
window_counts = np.zeros(num_windows, dtype=int)

for i in range(num_windows):
    start_time = i * window_size
    end_time = (i + 1) * window_size
    window_counts[i] = np.sum((time >= start_time) & (time < end_time))

# Calcular a frequência relativa
frequency_relative = window_counts / window_size

# Plotar o histograma dos tempos entre chegadas
plt.figure(figsize=(8, 4))
plt.hist(window_counts, bins=20, density=True, alpha=0.7, label='Frequência relativa')

# Plotar a distribuição de probabilidade teórica
x = np.arange(0, np.max(window_counts) + 1)
pdf_theoretical = np.exp(-lambd * window_size) * (lambd * window_size) ** x / factorial(x, exact=False)
plt.plot(x, pdf_theoretical, 'r', lw=2, label='Distribuição teórica')

plt.xlabel('Número de chegadas')
plt.ylabel('Frequência relativa')
plt.title('Frequência relativa dos números de chegadas em janelas de tempo')
plt.legend()
plt.grid(True)
plt.show()

>>>>>>> origin/main
