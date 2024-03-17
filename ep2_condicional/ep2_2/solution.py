# Importa as funcoes da biblioteca math
import math

# Entrada: Coeficientes da equacao de segundo grau
a = int(input())
b = int(input())
c = int(input())

# Processamento: Calcula o delta
delta = (b**2) - 4*a*c

# Saida: Imprime as raizes da equacao se existirem
if (delta < 0):
    print("Sem solucao real!")
    print(f"Delta = {delta:.2f}")
elif (delta == 0):
    x = (-b + math.sqrt(delta))/(2*a)
    print(f"x = {x:.2f}")
else:
    x1 = (-b + math.sqrt(delta))/(2*a)
    x2 = (-b - math.sqrt(delta))/(2*a)
    print(f"x1 = {(min(x1, x2)):.2f}")
    print(f"x2 = {(max(x1, x2)):.2f}")
