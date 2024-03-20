lines = int(input())
columns = int(input())

matrix = []

for i in range(lines):
    line = input().split(" ")
    sum = 0
    for j in range(columns):
        line[j] = float(line[j])
        sum += line[j]
    line.append(sum / columns)
    matrix.append(line)

for i in matrix:
    for j in i:
        print(f"{j:.2f}", end=" ")
    print("")
