# Nota: o código utiliza listas, mas podem facilmente ser substituídas por variáveis individuais
n = int(input()) # Recebe a quantidade de notas que serão lidas
CONVERT = ["A", "B", "C", "D", "F"]
grades = [0, 0, 0, 0, 0]
sum = 0

for i in range(0, n): # Lê as notas e as classifica, atualizando a lista de contagem
    x = float(input())
    sum += x
    if (x >= 9):
        grades[0] += 1
    elif (x >= 8):
        grades[1] += 1
    elif (x >= 7):
        grades[2] += 1
    elif (x >= 5):
        grades[3] += 1
    else:
        grades[4] += 1

# Imprime os resultados
for i in range(0, 5):
    print(f"{CONVERT[i]}: {grades[i]}")
print(f"Media: {(sum / n):.2f}")
