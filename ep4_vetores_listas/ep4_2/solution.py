n = int(input())
v = []
isPair = True

for i in range(n):
    v.append(int(input()))
    if (i % 2 != 0):
        if (v[i] != v[i - 1]):
            isPair = False
            break

if (len(v) % 2 != 0 or not isPair):
    print("Nao eh um vetor de duplas!")
else:
    print("Eh um vetor de duplas!")
