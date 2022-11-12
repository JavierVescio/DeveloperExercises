import random

matrix = [[random.randint(1, 10) for j in range(5)] for i in range(5)]

def consecutiveNumbers(list):
  i = 0
  while (i < len(list) - 1) and list[i] + 1 == list[i + 1]:
    i += 1
  return i == len(list) - 1

# change n to any other number if you want to find more or less consecutive numbers
n = 4

def findSequenceByRow(matrix):
  seq = []
  for r, row in enumerate(matrix):
    for c in range(len(row) - n + 1):
      if consecutiveNumbers(row[c:c+n]):
        seq.append([[r,c],[r,c+n-1]])
  return seq

def findSequenceByColumn(matrix):
  c = 0
  seq = []
  while c < len(matrix):
    for r in range(len(matrix) - n + 1):
      list = [matrix[r+i][c] for i in range(n)]
      if consecutiveNumbers(list):
        seq.append([[r,c],[r+n-1,c]])
    c += 1
  return seq

seqByRow = findSequenceByRow(matrix)
print(seqByRow)
seqByColumn = findSequenceByColumn(matrix)
print(seqByColumn)

print(f'Sequences of {n} consecutive numbers found iterating over rows')
for seq in seqByRow:
  start = seq[0]
  end = seq[1]
  print(f'Initial: ({start[0]},{start[1]}). Final: ({end[0]},{end[1]})')

print(f'Sequences of {n} consecutive numbers found iterating over columns')
for seq in seqByColumn:
  start = seq[0]
  end = seq[1]
  print(f'Initial: ({start[0]},{start[1]}). Final: ({end[0]},{end[1]})')