lines_a = int(input())
columns_a = int(input())

matrix_a = []

for i in range(lines_a):
    line = input().split(" ")
    for j in range(columns_a):
        line[j] = int(line[j])
    matrix_a.append(line)

lines_b = int(input())
columns_b = int(input())

matrix_b = []

for i in range(lines_b):
    line = input().split(" ")
    for j in range(columns_b):
        line[j] = int(line[j])
    matrix_b.append(line)

result_matrix = [[0]*columns_b for _ in range(lines_a)]

# Itera sobre as linhas de A
for i in range(lines_a):
    # Itera sobre as colunas de B
    for j in range(columns_b):
        # Itera sobre as linhas de B
        for k in range(lines_b):
            result_matrix[i][j] += (matrix_a[i][k] * matrix_b[k][j]) * 3

for i in result_matrix:
    for j in i:
        print(j, end=" ")
    print()
