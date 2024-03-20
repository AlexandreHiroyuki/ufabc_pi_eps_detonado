def inserir():
    v = [None] * 10
    for i in range(10):
        v[i] = int(input())
    return v

def imprimir(v):
    for e in v:
        print(e, end=" ")
    print("")

def shift(v):
    for i in range(len(v))[::-1]:
        if (i-1 < 0): break
        v[i], v[i-1] = v[i-1], v[i]
