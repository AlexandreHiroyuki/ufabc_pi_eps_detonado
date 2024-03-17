def filtrar_lista(v):
  result = []
  for e in v:
    if ((e > 10) and (e % 3 == 0)):
      result.append(e)
  return result

# Testes
print(filtrar_lista([8, 12, 5, 27, 18, 9, 15, 21, 4]))
print(filtrar_lista([10, 26, 11, 97]))
print(filtrar_lista([12, 18, 27, 27, 42]))
print(filtrar_lista([6, 3, 9, 3, 6]))
