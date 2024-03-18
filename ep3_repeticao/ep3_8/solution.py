def calcular_pi(n): # Define a função que calcula o valor de pi
    sum = 0
    for i in range(0, n): # Repete o loop 'n' vezes
        if (i % 2 == 0): # Se o índice for par, soma o valor
            sum += 1/(1 + (2*i))
        else: # Se o índice for ímpar, subtrai o valor
            sum -= 1/(1 + (2*i))
    return 4*sum
