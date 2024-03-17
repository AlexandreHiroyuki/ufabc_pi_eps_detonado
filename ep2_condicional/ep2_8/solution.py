# Entrada: coordenadas de um ponto
x = int(input())
y = int(input())

# Processamento: Verifica se o ponto está dentro do retângulo
if(x < -800 or x > 22 or y < -20 or y > 35):
    print("NAO")
else:
    print("SIM")
