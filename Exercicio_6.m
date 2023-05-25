RandomSeed = 123;
XRange = [0, 1];
N= 200000;
rng(RandomSeed); 
X = rand(1, N) * (XRange(2) - XRange(1)) + XRange(1);

% Distribuição contínua para a exponencial
Lambda = 2; 
T = zeros(1, N);
for n = 1:N
    T(n) = (1 / Lambda) * log(1 / (1 - X(n)));
end

% Cascateando os tempos de chegadas
Tarrival = zeros(1, N);

for n = 1:N
    if n == 1
        Tarrival(n) = T(n);
    else
        Tarrival(n) = Tarrival(n - 1) + T(n);
    end
end

% Calcule-se os tempos de saída
Mu = linspace(1/0.1, 1/0.5, 100);
Tdeparture = zeros(length(Mu), N);

for mu = 1:length(Mu)
    for n = 1:N
        if n == 1
            Tdeparture(mu, n) = Tarrival(n) + 1 / Mu(mu);
        else
            % Se a próxima chegada ocorrer antes da próxima saída, a saída só ocorrerá 1/Mu após a última
            if Tarrival(n) < (Tdeparture(mu, n-1) + 1 / Mu(mu))
                Tdeparture(mu, n) = Tdeparture(mu, n-1) + 1 / Mu(mu);
            % Caso contrário, a próxima saída ocorrerá 1/Mu após a chegada
            else
                Tdeparture(mu, n) = Tarrival(n) + 1 / Mu(mu);
            end
        end
    end
end

% Número de usuários no sistema
Win = 100;
BinsPerWin = 100;
Users = zeros(length(Mu), Win * BinsPerWin);

for mu = 1:length(Mu)
    IndexArrival = 1;
    IndexDeparture = 1;

    for n = 1:Win * BinsPerWin
        Change = 0;

        while Tarrival(IndexArrival) < n
            Change = Change + 1;
            IndexArrival = IndexArrival + 1;
        end

        while Tdeparture(mu, IndexDeparture) < n
            Change = Change - 1;
            IndexDeparture = IndexDeparture + 1;
        end

        if n == 1
            Users(mu, n) = Change;
        else
            Users(mu, n) = Users(mu, n - 1) + Change;
        end
    end
end

% Plotar a Curva Teórica
muRho = linspace(min(Mu), max(Mu), 500);
Rho = Lambda ./ muRho;
Rho(Rho >= 1) = [];
Nmean = Rho + (1 / 2) * (Rho.^2 ./ (1 - Rho));

% Plotagem
figure;
scatter(Lambda ./ Mu, mean(Users, 2), 'blue', 'filled');
hold on;
plot(Rho, Nmean, 'LineWidth', 2);
hold off;
legend('Valores da simulação', 'Curva Teórica');
xlabel('\lambda / \mu');
ylabel('Média de usuários');
title(['Número médio de usuários']);
grid on;
