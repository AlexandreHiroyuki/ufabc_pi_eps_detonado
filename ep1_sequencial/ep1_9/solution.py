# Recebe a capacidade máxima do caminhão
max_in = int(input())

# Usando apenas contas matemáticas para dividir a capacidade máxima do caminhão em caixas de 500, 100, 25 e 1
# Divide pelo maior valor possível, e depois divide o resto pelo próximo maior valor possível, e assim por diante...
a = int(max_in / 500)
b = int((max_in % 500) / 100)
c = int(((max_in % 500) % 100) / 25)
d = int(((max_in % 500) % 100) % 25)

print(a, b , c, d)
