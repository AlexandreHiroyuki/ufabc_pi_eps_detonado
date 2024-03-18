def matriz(n):
    for i in range(n):
        for j in range(n):
            if (j < i):
                print(f"{(i+1):02}", end=" ")
            else:
                print(f"{(j+1):02}", end=" ")
        print()

# Código para testar
print(matriz(3))
print(matriz(6))
print(matriz(10))
