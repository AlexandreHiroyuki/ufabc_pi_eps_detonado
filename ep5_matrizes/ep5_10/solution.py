rows = int(input())
columns = int(input())

matrix = []

for i in range(rows):
    row = input().split(" ")
    for j in range(columns):
        row[j] = int(row[j])
    matrix.append(row)

cell_x = int(input())
cell_y = int(input())

bombs = 0

if (cell_x - 1 >= 0):
    if (cell_y - 1 >= 0):
        bombs += matrix[cell_x - 1][cell_y - 1]
    if (cell_y + 1 < columns):
        bombs += matrix[cell_x - 1][cell_y + 1]
    bombs += matrix[cell_x - 1][cell_y]

if (cell_y - 1 >= 0):
    bombs += matrix[cell_x][cell_y - 1]
if (cell_y + 1 < columns):
    bombs += matrix[cell_x][cell_y + 1]

if (cell_x + 1 < columns):
    if (cell_y - 1 >= 0):
        bombs += matrix[cell_x + 1][cell_y - 1]
    if (cell_y + 1 < columns):
        bombs += matrix[cell_x + 1][cell_y + 1]
    bombs += matrix[cell_x + 1][cell_y]

print(bombs)
