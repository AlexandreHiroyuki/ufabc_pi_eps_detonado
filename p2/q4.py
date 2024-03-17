def busca(v, m):
  n = len(v)
  result = False
  for i in range(n):  # iterating lines
    line_check = True
    column_check = True
    for j in range(n):  # compare
      if (m[i][j] != v[j]):
        line_check = False
      if (m[j][i] != v[j]):
        column_check = False
    if (line_check or column_check):
      result = True
  return result

# Testes
test_v = [1, 2, 3]
test_m = [[0, 0, 0],
          [1, 1, 1],
          [2, 2, 2]]
print(busca(test_v, test_m))

test_v = [5, 2]
test_m = [[5, 3],
          [2, 1]]
print(busca(test_v, test_m))

test_v = [3, 4, 5, 2]
test_m = [[0, 0, 1, 0],
          [6, 9, 1, 2],
          [3, 4, 5, 2],
          [1, 1, 8, 4]]
print(busca(test_v, test_m))

test_v = [0, 0, 0, 4, 0]
test_m = [[1, 0, 0, 0, 0],
          [0, 2, 0, 0, 0],
          [0, 0, 3, 0, 0],
          [0, 0, 0, 4, 1],
          [0, 0, 0, 0, 5]]
print(busca(test_v, test_m))
