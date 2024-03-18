n = int(input()) # Recebe o valor de 'n'

print("2")
i = 1
y = 3
while (i < n):
    x = 3
    while (x < y):
        if (y % x) == 0:
            break
        x += 2
    if (x == y):
        print(x)
        i += 1
    y += 2
