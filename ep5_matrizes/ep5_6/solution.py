size = int(input())

matrix = []
for i in range(size):
    line = input().split(" ")
    for j in range(size):
        line[j] = int(line[j])
    matrix.append(line)

r_matrix = []
for i in range(size//2):
    line = []
    for j in range(size//2):
        sum = 0
        sum += matrix[i][j]
        sum += matrix[i][size - j - 1]
        sum += matrix[size - i - 1][j]
        sum += matrix[size - i - 1][size - j - 1]

        line.append(sum)
    r_matrix.append(line)

for line in r_matrix:
    for column in line:
        print(column, end=" ")
    print("")
