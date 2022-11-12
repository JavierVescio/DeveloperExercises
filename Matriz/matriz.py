"""Crear una matriz de 5x5 randomizada con números enteros, encontrar secuencia de 4
números consecutivos horizontal o vertical y si se encuentra mostrar la posición inicial y
final."""

import random

#matrix = [[random.randint(1, 10) for j in range(5)] for i in range(5)]
matrix = [[2,3,7,8,9],[2,3,7,9,9],[2,2,3,4,5]]

def consecutiveNumbers(list):
  i = 0
  while (i < len(list) - 1) and list[i] + 1 == list[i + 1]:
    i += 1
  return i == len(list) - 1

#traverse by row
# for idx, row in enumerate(matrix):
#   for c in range(2):
#     list = row[c:c+4]
#     if consecutiveNumbers(list):
#       print(f'Initial: ({idx},{c}). Final: ({idx},{c+3})')

# change n to any other number if you want to find more or less consecutive numbers
n = 4
for idx, row in enumerate(matrix):
  for c in range(len(row) - n + 1):
    list = row[c:c+n]
    if consecutiveNumbers(list):
      print(f'Initial: ({idx},{c}). Final: ({idx},{c+n-1})')

#list = [[2,3,7,8,9],[1,2,3,4,5],[2,3,7,9,9]]
