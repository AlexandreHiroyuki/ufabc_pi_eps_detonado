# Recebe a quantidade de linhas e calcula a largura da base
height = int(input())
width = 1 + (2*(height))

for h in range(height): # Repete o loop para cada linha, até a altura máxima
    current = 1 + (2*h) # Calcula a largura da linha atual
    blank = int((width - current - 1) / 2) # Calcula a quantidade de espaços em branco
    # Imprime os caracteres da linha atual
    for i in range(blank):
        print('-', end='')
    for i in range(current):
        print('1', end='')
    for i in range(blank):
        print('-', end='')
    print('')
