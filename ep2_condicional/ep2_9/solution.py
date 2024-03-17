# Entrada: código de um disco com 6 dígitos
code = str(input())

# Processamento: Cria um dicionário para traduzir o código para o nome do planeta e o modelo do disco
translations = {
    "80": "Marte",
    "81": "Saturno",
    "90": "Netuno",
    "91": "HD21749b",
    "60": "A6000",
    "61": "B7500",
    "62": "C9000"
}

# Processamento: Separa o código em 3 partes
send = code[0:2]
receive = code[2:4]
model = code[4:6]

# Saida: Imprime o nome do planeta rementente, o nome do planeta destinatário e o modelo do disco equivalentes à cada parte do código
print(translations[send])
print(translations[receive])
print(translations[model])
