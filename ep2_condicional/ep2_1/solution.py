# Entrada: Salario fixo do vendedor e total de vendas realizadas pelo vendedor
wage = int(input())
sales = int(input())

# Processamento: Calcular o bonus do vendedor e calcular a meta de vendas
goal = wage * 0.5
bonus = sales * 0.2

# Saida: Imprimir o bonus do vendedor e se ele atingiu a meta de vendas
print(f"{bonus:.2f}")
if(bonus >= goal):
    print("Atingiu meta de vendas")
else:
    print("Nao atingiu meta de vendas")
