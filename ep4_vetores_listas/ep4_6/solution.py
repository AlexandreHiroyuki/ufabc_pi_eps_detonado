n = int(input())
v = []
ones = []

for i in range(n):
    v.append(int(input()))
    if (v[i] == 1):
        ones.append(i)

sum = 0

for i in ones:
    if (i-1 >= 0):
        sum += v[i-1]
    if (i+1 <= len(v)-1):
        sum += v[i+1]

print(sum)
