# Entrada: 3 notas de testes e 2 notas de provas
t_sum = 0
for i in range(0, 3):
    t_sum += float(input())
p1 = float(input())
p2 = float(input())

# Processamento: Calcula a media ponderada
t_mean = t_sum / 3

score = (t_mean * 0.2) + (p1 * 0.4) + (p2 * 0.4)

# Saida: Imprime a media ponderada e o conceito final
print(f"{score:.2f}")
if (score >= 9.0):
    print("A")
elif (score >= 7.5):
    print("B")
elif (score >= 6.0):
    print("C")
elif (score >= 5.0):
    print("D")
else:
    print("F")
