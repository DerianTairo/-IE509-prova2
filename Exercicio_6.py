import numpy as np
import matplotlib.pyplot as plt

# Definir os parâmetros
arrival_rate = 2  # Taxa de chegada (λ)
service_times = np.linspace(0.1, 0.5, 5)  # Tempos de serviço (1/μ)
traffic_intensity = arrival_rate * service_times

# Calcular o número médio de usuários no servidor (teórico)
mean_users_theoretical = traffic_intensity / (1 - traffic_intensity)

# Plotar o número médio de usuários no servidor
plt.figure(figsize=(8, 4))
plt.plot(traffic_intensity, mean_users_theoretical, 'r', lw=2, label='Teórico')
plt.xlabel('Intensidade do Tráfego (ρ)')
plt.ylabel('Número Médio de Usuários no Servidor')
plt.title('Número Médio de Usuários no Servidor em função da Intensidade do Tráfego')
plt.legend()
plt.grid(True)
plt.show()
import numpy as np
import matplotlib.pyplot as plt

# Definir os parâmetros
arrival_rate = 2  # Taxa de chegada (λ)
service_times = np.linspace(0.1, 0.5, 5)  # Tempos de serviço (1/μ)
traffic_intensity = arrival_rate * service_times

# Calcular o número médio de usuários no servidor (teórico)
mean_users_theoretical = traffic_intensity / (1 - traffic_intensity)

# Plotar o número médio de usuários no servidor
plt.figure(figsize=(8, 4))
plt.plot(traffic_intensity, mean_users_theoretical, 'r', lw=2, label='Teórico')
plt.xlabel('Intensidade do Tráfego (ρ)')
plt.ylabel('Número Médio de Usuários no Servidor')
plt.title('Número Médio de Usuários no Servidor em função da Intensidade do Tráfego')
plt.legend()
plt.grid(True)
plt.show()
