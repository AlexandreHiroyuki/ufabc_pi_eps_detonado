# Importa a biblioteca math para usar a função sqrt
import math

# Representando as coordenadas de A pelo par(Ax, Ay), e as coordenadas de B pelo par (Bx, By)
# Escreva um programa que receba as coordenadas de dois pontos A e B
Ax = float(input())
Ay = float(input())
Bx = float(input())
By = float(input())

# Calcule a distância entre os dois pontos
dist = math.sqrt(((Bx - Ax)**2) + ((By - Ay)**2))

print(f"{dist:.2f}")
