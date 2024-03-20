# Escreva um programa que leia um vetor de inteiros com n elementos.
n = int(input())
v = []

v = input().split(" ")

# Depois verifique se o vetor está ordenado em ordem crescente.
isUnordered = False
for i in range(1, n):
    if (int(v[i-1]) > int(v[i])):
        isUnordered = True
        break

if (isUnordered):
    print("NAO")
else:
    print("SIM")
