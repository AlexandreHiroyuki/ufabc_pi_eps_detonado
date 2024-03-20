def comparar_matrizes(matriz1, matriz2):
    # Se as dimensões da matriz1 forem diferentes das dimensões da matriz2, a função deve retornar False.
    if(len(matriz1) != len(matriz2) or len(matriz1[0]) != len(matriz2[0])):
        return False
    for i in range(len(matriz1)):
        for j in range(len(matriz1[0])):
            if ((matriz1[i][j] * 2) != matriz2[i][j]):
                return False
    return True
