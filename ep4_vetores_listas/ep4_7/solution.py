# Escreva um programa que leia um vetor de inteiros com n elementos.
n = int(input())
v = []
for i in range(n):
    v.append(int(input()))

# Calcula o índice do meio do vetor.
half1 = int(n/2)-1
half2 = half1+1 if (n%2==0) else half1+2

# Depois verifique se o vetor é "espelhado", ou seja, a primeira metade é igual ao inverso da segunda.
isMirrored = True

for i in range(half1+1):
    if (v[half1 - i] != v[half2 + i]):
        isMirrored = False
        break

# Imprima "SIM" se o vetor for "espelhado" e "NAO" caso contrário (observe que não há um til no NAO)
if (isMirrored):
    print("SIM")
else:
    print("NAO")
