def multiplos(numeros, divisores):
  counters = []
  for d in divisores:
    count = 0
    for n in numeros:
      if (n % d == 0):
        count += 1
    counters.append(count)
  return counters

# Testes
print(multiplos([48, 6, 10, 5, 64, 9, 12, 34], [3, 4, 8]))
print(multiplos([7, 12, 11, 6, 14, 3], [9, 17]))
print(multiplos([3, 3, 3, 3, 3], [1, 2, 3]))
