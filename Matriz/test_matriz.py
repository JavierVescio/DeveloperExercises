from matriz import findSequenceByColumn, findSequenceByRow

def testFindSequenceByColumn():
  matrix = [[3,3,7,8,9],[3,3,7,9,9],[4,3,4,5,6],[5,5,3,11,5],[6,5,3,5,5]]
  ouput = findSequenceByColumn(matrix)
  expected_ouput = [[[1, 0], [4, 0]]]
  assert(ouput == expected_ouput)

def testFindSequenceByRow():
  matrix = [[3,3,7,8,9],[3,3,7,9,9],[4,3,4,5,6],[5,5,3,11,5],[6,5,3,5,5]]
  ouput = findSequenceByRow(matrix)
  expected_ouput = [[[2, 1], [2, 4]]]
  assert(ouput == expected_ouput)