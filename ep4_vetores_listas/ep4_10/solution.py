# Escreva um programa que leia um valor n e depois os n elementos de um vetor de inteiros.
n = int(input())
v = input().split(" ")

# Depois imprima apenas a primeira ocorrência de cada número, ou seja, se um número aparece mais de uma vez no vetor, apenas a primeira ocorrência dele ser impressa.

# Elimina os números repetidos do vetor. Para isso, substitua os números repetidos por "NaN" (nome arbitrário escolhido para representar a sigla "Not a Number").
for i in range(n):
    if (v[i] == "NaN"):
        continue
    for j in range(i+1, n):
        if (v[i] == v[j]):
            v[j] = "NaN"
# Imprime o vetor sem as ocorrências repetidas (marcadas como "NaN").
for i in v:
    if (i != "NaN"):
        print(i, end=" ")
