lines = int(input())
columns = int(input())

matrix = []

for i in range(lines):
    line = []
    for j in range(columns):
        line.append(int(input()))
    matrix.append(line)

target = int(input())

x = y = -1
for index_i, i in enumerate(matrix):
    for index_j, j in enumerate(i):
        if (j == target):
            x = index_i
            y = index_j

if (x >= 0 and y >= 0):
    print(x + 1, y + 1)
else:
    print(-1)
