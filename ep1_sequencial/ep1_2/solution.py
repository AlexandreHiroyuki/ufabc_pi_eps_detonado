# Seu programa irá receber 3 valores
a = int(input())
b = float(input())
c = float(input())

# Então deverá imprimir o primeiro formatado com nenhuma casa decimal
print(f"Primeiro numero = {a}")
# O segundo com duas casas
print(f"{b:.2f} eh o segundo numero")
# E o terceiro com três casas, seguindo o mesmo estilo da saída de exemplo
print(f"Finalmente {c:.3f} eh o terceiro numero")
