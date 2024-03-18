withdraw = int(input("Quanto você quer sacar? "))

bill_50 = withdraw // 50
bill_20 = (withdraw % 50) // 20
bill_5 = ((withdraw % 50) % 20) // 5
bill_1 = ((withdraw % 50) % 20) % 5

if (bill_1 != 0):
    print("Não é possível sacar esse valor")
else:
    print(f"Notas de 50: {bill_50}")
    print(f"Notas de 10: {bill_20}")
    print(f"Notas de 5: {bill_5}")
