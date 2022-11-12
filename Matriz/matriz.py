"""Crear una matriz de 5x5 randomizada con números enteros, encontrar secuencia de 4
números consecutivos horizontal o vertical y si se encuentra mostrar la posición inicial y
final."""

import random

matrix = [[random.randint(1, 10) for j in range(5)] for i in range(5)]

print(matrix)