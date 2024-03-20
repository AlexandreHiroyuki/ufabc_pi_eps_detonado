size = int(input())
v = []
sum = 0

for i in range(size):
    v.append(int(input()))
    sum += v[i]

index = int(input())

if (v[index] == (sum - v[index])):
    print("Sim")
else:
    print("Nao")
