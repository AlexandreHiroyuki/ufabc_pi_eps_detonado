lines = int(input())
columns = int(input())

matrix = []
count = 1
for index in range(lines):
    iteration = []
    if (index % 2 == 0):
        iteration = range(columns)
    else:
        iteration = reversed(range(columns))

    line = [None] * columns
    for it in iteration:
        line[it] = count
        count += 1
    matrix.append(line)

for i in matrix:
    for j in i:
        print(j, end=" ")
    print("")
