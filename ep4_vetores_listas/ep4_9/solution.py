
# Escreva um programa que leia dois vetores (A e B) de mesmo comprimento n.
n = int(input())
a = input().split(" ")
b = input().split(" ")

# Converte a entrada de texto para números inteiros.
for i in range(n):
    a[i] = int(a[i])
    b[i] = int(b[i])

# Calcula o múltiplo que transforma o valor do menor vetor para igual o maior vetor.
multiplier = max(a[0], b[0]) / min(a[0], b[0])
is_a_bigger = a[0] >= b[0]

# Depois verifique se um vetor é o resultado de uma multiplicação de todos os elementos do outro pelo mesmo valor.
is_possible = True
for i in range(n):
    if (is_a_bigger):
        if (b[i] * multiplier != a[i]):
            is_possible = False
            break
    else:
        if (a[i] * multiplier != b[i]):
            is_possible = False
            break

# Ao final, o programa deve imprimir "SIM" se um vetor for o resultado de uma multiplicação de todos os elementos do outro pelo mesmo valor,
# ou "NAO" caso contrário (não há til ~ em NAO).
if (is_possible):
    print("SIM")
else:
    print("NAO")
