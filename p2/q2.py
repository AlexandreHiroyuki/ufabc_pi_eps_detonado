def filtrar_lista(v):
  exclude = ["da", "das", "do", "dos", "de", "e", ""]
  result = []
  for item in v:
    flag = True
    for ex in exclude:
      if (item == ex):
        flag = False
        break
    if (flag):
      result.append(item)
  return result

def acronimo(texto):
  words = texto.split(" ")
  filtered_words = filtrar_lista(words)
  letters = ""
  for w in filtered_words:
    letters += w[0]

  return letters

# Testes
print(acronimo("Processamento da Informação"))
print(acronimo("Pesquisa e Desenvolvimento"))
print(acronimo("Centro Acadêmico"))
print(acronimo("Uma frase com muitos espaços"))
print(acronimo("Sociedade Brasileira de Computação"))
print(acronimo("Centro de Matemática, Computação e Cognição"))
print(acronimo("Confederação Nacional dos Municípios"))
