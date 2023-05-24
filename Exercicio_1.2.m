prob_cara = 0.7;  % Probabilidade de sair cara (1)
prob_coroa = 0.3;  % Probabilidade de sair coroa (0)

lancamentos = 100;  % Número de lançamentos
num_simulacoes = 1000;  % Número de simulações

resultados = rand(num_simulacoes, lancamentos) < prob_cara;  % Gerar resultados de lançamento aleatórios
medias = mean(resultados, 2);  % Calcular as médias

% Imprimir os resultados detalhados e ordenados
resultados_ordenados = sort(resultados, 2);
for i = 1:num_simulacoes
    disp(['Simulação ', num2str(i), ': ', num2str(resultados_ordenados(i,:))]);
end

% Plotar o histograma das médias
figure;
histogram(medias, 'Normalization', 'pdf', 'EdgeColor', 'black', 'DisplayName', 'Simulação');

% Calcular e plotar o PDF teórico utilizando o teorema do limite central
mu = prob_cara;  % Média da distribuição binomial
sigma = sqrt(prob_cara * prob_coroa);  % Desvio padrão da distribuição binomial
x = linspace(0, 1, 1000);
pdf_teorica = normpdf(x, mu, sigma/sqrt(lancamentos));
hold on;
plot(x, pdf_teorica, 'r-', 'DisplayName', 'PDF Teórica');

xlabel('Média da variável aleatória associada');
ylabel('Frequência / Probabilidade');
title('Simulação do lançamento da moeda viciada');
legend('Location', 'best');
hold off;
