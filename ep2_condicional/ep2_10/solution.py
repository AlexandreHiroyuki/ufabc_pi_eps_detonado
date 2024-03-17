import math

# Definição: Função que calcula a distância que um avão possui autonomia baseado no peso
def check_load(weight):
    if weight <= 50000:
        return 18000
    if weight <= 200000:
        return 9000
    if weight <= 250000:
        return 3000
    return 0

# Entrada: Peso do avião, coordenadas do ponto de partida e do ponto de chegada
load = int(input())
Ax = int(input())
Ay = int(input())
Bx = int(input())
By = int(input())

# Processamento: Calcula a distância entre os pontos
dist = math.sqrt(((Bx - Ax)**2) + ((By - Ay)**2))

print(f"{dist:.2f}")

# Processamento: Verifica se o avião possui autonomia para chegar ao destino
max_dist = check_load(load)

# Saida: Imprime se o avião possui autonomia para chegar ao destino
if (dist <= max_dist):
    print("SIM")
elif (dist <= (max_dist * 1.1)):
    print("TALVEZ")
else:
    print("NAO")
