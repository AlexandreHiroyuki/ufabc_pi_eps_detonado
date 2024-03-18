n = int(input()) # Recebe a quantidade de números que serão lidos

# Inicializa as variáveis que armazenarão a soma, o maior e o menor valor lido
sum = n_min = n_max = int(input())
for i in range(0, n-1): # Lê os 'n' valores e atualiza as variáveis
    x = int(input())
    sum += x # Acumula a soma
    n_min = min(n_min, x) # Compara o valor lido com o menor valor atual e atualiza, se necessário
    n_max = max(n_max, x) # Compara o valor lido com o maior valor atual e atualiza, se necessário

# Imprime os resultados
print(sum)
print(sum/n)
print(n_min)
print(n_max)
