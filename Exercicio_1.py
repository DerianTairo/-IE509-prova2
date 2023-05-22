import numpy as np
import matplotlib.pyplot as plt

prob_cara = 0.7  # Probabilidade de sair cara (1)
prob_coroa = 0.3  # Probabilidade de sair coroa (0)

lançamentos = 2  # Número de lançamentos
num_simulacoes = 1000  # Número de simulações

resultados = np.random.choice([1, 0], size=(num_simulacoes, lançamentos), p=[prob_cara, prob_coroa])
medias = np.mean(resultados, axis=1)

# Imprimindo os resultados detalhados e ordenados
resultados_ordenados = np.sort(resultados, axis=1)
for i in range(num_simulacoes):
    print(f"Simulação {i+1}: {resultados_ordenados[i]}")

# Plotando o histograma das médias
plt.hist(medias, bins=20, density=True, edgecolor='black')
plt.xlabel('Média da variável aleatória associada')
plt.ylabel('Frequência')
plt.title('Simulação do lançamento da moeda viciada')
plt.show()
