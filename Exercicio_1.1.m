prob_cara = 0.7;  % Probabilidade de sair cara (1)
prob_coroa = 0.3;  % Probabilidade de sair coroa (0)

lancamentos = 2;  % Número de lançamentos
num_simulacoes = 1000;  % Número de simulações

resultados = rand(num_simulacoes, lancamentos) < prob_cara;  % Generar resultados de lanzamiento aleatorios
medias = mean(resultados, 2);  % Calcular las medias

% Imprimir los resultados detallados y ordenados
resultados_ordenados = sort(resultados, 2);
for i = 1:num_simulacoes
    disp(['Simulação ', num2str(i), ': ', num2str(resultados_ordenados(i,:))]);
end

% Plotear el histograma de las medias
histogram(medias, 'Normalization', 'probability', 'EdgeColor', 'black', 'DisplayName', 'Simulação');

% Calcular y plotear la PMF teórica
x = 0:lancamentos;
pmf_teorica = binopdf(x, lancamentos, prob_cara);
hold on
plot(x/2, pmf_teorica, 'ro-', 'DisplayName', 'PMF Teórica');

xlabel('Média da variável aleatória associada');
ylabel('Frequência / Probabilidade');
title('Simulação do lançamento da moeda viciada');
legend('Location', 'best');