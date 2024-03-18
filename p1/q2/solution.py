# n > 0
n = int(input("Entre a quantidade de números: "))

min = -1
for i in range(n):
    x = int(input())
    if (x % 3 == 0):
        if (x < min or min == -1):
            min = x

if (min != -1):
    print(f"O menor número divisível por 3 é {min}")
else:
    print("Nenhum número é divisível por 3")
