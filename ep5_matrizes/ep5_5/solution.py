size = int(input())

sum = 0
for i in range(size):
    line = input().split(" ")
    for j in range(size):
        if (j == i):
            break
        line[j] = int(line[j])
        if (line[j] % 2 == 0):
            sum += line[j]

print(sum)
