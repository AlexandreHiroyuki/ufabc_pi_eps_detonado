# Inicializa as variáveis que armazenarão a entrada, a soma e o número de valores lidos
sum = 0
x = 5
i = 0

while(x != 0): # Lê os valores enquanto o valor lido for diferente de 0
    x = int(input()) # Lê o valor
    if (x == 0): # Se o valor lido for 0, interrompe o loop
        break
    sum += x # Acumula a soma
    i += 1 # Incrementa o número de valores lidos

print(f"{(sum/i):.2f}") # Imprime a média
