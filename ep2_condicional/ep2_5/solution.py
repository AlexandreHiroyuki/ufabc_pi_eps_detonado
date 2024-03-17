# Entrada: temperatura
temp = int(input())

# Processamento: classifica a temperatura
if (temp <= -20):
    print("Muito Baixa")
elif (temp <= 30):
    print("Baixa")
elif (temp <= 200):
    print("Normal")
elif(temp <= 250):
    print("Alta")
else:
    print("Muito Alta")
