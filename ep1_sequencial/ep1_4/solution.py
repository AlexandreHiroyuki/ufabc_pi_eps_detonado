# A função/método  possui os parâmetros x1, y1, x2, y2 (números inteiros) e deverá retornar o valor da distância de Manhattan entre os pontos (x1, y1) e (x2, y2)
def calcular_distancia(x1, y1, x2, y2):
    return abs(x2 - x1) + abs(y2 - y1)
