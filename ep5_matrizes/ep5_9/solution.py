rows = int(input())
columns = int(input())

matrix = []

is_multiple_of_10 = True
for i in range(rows):
    row = input().split(" ")
    for j in range(columns):
        row[j] = int(row[j])
        if (row[j] % 10 != 0):
            is_multiple_of_10 = False
    matrix.append(row)

is_sorted = True
for i in range(rows):
    is_ascending = (matrix[i][0] <= matrix[i][columns-1])
    for j in range(1, columns):
        if (matrix[i][j-1] != matrix[i][j]):
            if ((matrix[i][j-1] < matrix[i][j]) != is_ascending):
                is_sorted = False
                break

if (is_multiple_of_10 and is_sorted):
    print("SIM")
else:
    print("NAO")
