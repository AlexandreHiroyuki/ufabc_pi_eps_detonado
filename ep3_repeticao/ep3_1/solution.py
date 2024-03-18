# Função que calcula e retorna um valor de acordo com a fórmula ilustrada no enunciado
def obter_valor_funcao(a, b, c):
    sum = a # Acumula a somatória
    for d in range(1, b+1): # Percorre os valores de 1 até b, replicando o comportamento da somatória
        sum += c * d
    return sum
