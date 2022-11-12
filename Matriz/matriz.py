"""Crear una matriz de 5x5 randomizada con números enteros, encontrar secuencia de 4
números consecutivos horizontal o vertical y si se encuentra mostrar la posición inicial y
final."""

import random

matrix = [[random.randint(1, 10) for j in range(5)] for i in range(5)]
#matrix = [[3,3,7,8,9],[3,3,7,9,9],[4,2,3,10,5],[5,5,3,11,5],[6,5,3,5,5]]

def consecutiveNumbers(list):
  i = 0
  while (i < len(list) - 1) and list[i] + 1 == list[i + 1]:
    i += 1
  return i == len(list) - 1


# change n to any other number if you want to find more or less consecutive numbers
n = 4

print('Iterating over rows')
for r, row in enumerate(matrix):
  for c in range(len(row) - n + 1):
    if consecutiveNumbers(row[c:c+n]):
      print(f'Initial: ({r},{c}). Final: ({r},{c+n-1})')

print('Iterating over columns')
c = 0
while c < len(matrix):
  for r in range(len(matrix) - n + 1):
    list = [matrix[r+i][c] for i in range(n)]
    if consecutiveNumbers(list):
      print(f'Initial: ({r},{c}). Final: ({r+n-1},{c})')
  c += 1
