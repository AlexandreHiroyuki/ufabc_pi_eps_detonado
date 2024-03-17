def batalha_naval(m):
  size = 5 # matriz m de tamanho 5x5
  visited = [[False]*size for _ in range(size)]
  count_1 = 0
  count_2 = 0

  for i in range(size):
    for j in range(size):
      if(not visited[i][j]):
        visited[i][j] = True
        if (m[i][j] == 1):
          if ((i+1) < 5):
            if(m[i+1][j] == 1):
              count_2 += 1
              visited[i+1][j] = True
              continue
          if ((j+1) < 5):
            if(m[i][j+1] == 1):
              count_2 += 1
              visited[i][j+1] = True
              continue
          count_1 += 1
  print(f"Navios de comprimento 1: {count_1}")
  print(f"Navios de comprimento 2: {count_2}")

# Testes
mt = [[0, 0, 0, 0, 0],
[0, 1, 0, 0, 0],
[0, 0, 0, 0, 0],
[0, 0, 0, 0, 0],
[0, 0, 0, 1, 1]]
batalha_naval(mt)
print()

mt = [[0, 0, 0, 0, 0],
[0, 1, 0, 0, 1],
[0, 0, 1, 0, 0],
[0, 0, 0, 0, 0],
[1, 0, 0, 0, 1]]
batalha_naval(mt)
print()

mt = [[0, 0, 0, 0, 1],
[0, 1, 1, 0, 0],
[0, 0, 0, 0, 1],
[0, 0, 0, 0, 1],
[1, 1, 0, 1, 0]]
batalha_naval(mt)
print()

mt = [[1, 1, 0, 1, 1],
[0, 0, 1, 0, 0],
[0, 1, 0, 0, 0],
[0, 1, 0, 0, 1],
[0, 0, 1, 0, 1]]
batalha_naval(mt)
