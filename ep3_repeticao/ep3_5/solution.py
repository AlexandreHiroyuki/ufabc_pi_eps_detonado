# Recebe o tamanho do triângulo
n = int(input())

for i in range(1, n+1): # Repete o loop 'n' vezes
    for j in range(1, i+1): # Repete o loop 'i' vezes, 'i' é o número da linha atual
        print(i, end="")
    print("")
