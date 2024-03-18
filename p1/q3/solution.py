def sequencia(n):
    count = 4
    for i in range(n):
        print(count, end=" ")
        count -= 1
        if (count <= 0):
            count = 4

# Código para testar
print(sequencia(6))
print(sequencia(3))
print(sequencia(9))