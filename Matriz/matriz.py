"""Crear una matriz de 5x5 randomizada con números enteros, encontrar secuencia de 4
números consecutivos horizontal o vertical y si se encuentra mostrar la posición inicial y
final."""

import random

matrix = [[random.randint(1, 10) for j in range(5)] for i in range(5)]

def consecutiveNumbers(list):
  i = 0
  while (i < len(list) - 1) and list[i] + 1 == list[i + 1]:
    i += 1
  return i == len(list) - 1

list = [1,2,3,4]

print(consecutiveNumbers(list))