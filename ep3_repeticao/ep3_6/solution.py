value = int(input()) # Recebe o valor de 'n'

def summatory(n): # Define a função que calcula a somatória
    sum = 0
    for i in range(1, n+1):
        for j in range(1, 9):
            sum += (i + 1) * j
    return sum

print(summatory(value)) # Imprime o resultado da somatória
