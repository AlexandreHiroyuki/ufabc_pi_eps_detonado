# Entrada: Ano de produção, código do motor principal, distância percorrida em anos-luz
year = int(input())
code = int(input())
distance = int(input())

# Processamento: Verifica em qual caso da tabela o disco se encaixa
if (year >= 1901 and year <= 2000):
    if (code == 100 or code == 101):
        print("SIM")
    else:
        print("NAO")
elif (year >= 2001 and year <= 2020):
    if (distance > 5000):
        print("SIM")
    else:
        print("NAO")
elif (year == 2021):
    if ((code == 200 or code == 201) and (distance > 200)):
        print("SIM")
    else:
        print("NAO")
else:
    print("NAO")
