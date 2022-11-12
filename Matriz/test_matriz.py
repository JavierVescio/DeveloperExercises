from matriz import findSequenceByColumn, findSequenceByRow

def getMatrix():
  matrixList = []
  matrixList.append(
    {'matrix':[[3,3,7,8,9],[3,3,7,9,9],[4,3,4,5,6],[5,5,3,11,5],[6,5,3,5,5]],
    'expected_col_seq':[[[1, 0], [4, 0]]],
    'expected_row_seq':[[[2, 1], [2, 4]]]})
  matrixList.append(
    {'matrix':[[1,1,1,1,1],[2,2,2,2,2],[1,1,1,1,1],[2,2,2,2,2],[1,1,1,1,1]],
    'expected_col_seq':[],
    'expected_row_seq':[]})
  matrixList.append(
    {'matrix':[[1,1,1,1,1],[2,2,2,2,2],[3,5,3,9,8],[4,4,7,8,9],[0,0,0,0,0]],
    'expected_col_seq':[[[0, 0], [3, 0]]],
    'expected_row_seq':[]})
  matrixList.append(
    {'matrix':[[1,1,1,1,1],[2,2,2,2,2],[1,2,3,4,4],[2,2,2,2,2],[1,1,1,1,1]],
    'expected_col_seq':[],
    'expected_row_seq':[[[2, 0], [2, 3]]]})
  matrixList.append(
    {'matrix':[[1,1,1,1,1],[2,2,2,2,2],[1,2,3,4,5],[2,2,2,2,2],[1,1,1,1,1]],
    'expected_col_seq':[],
    'expected_row_seq':[[[2, 0], [2, 3]],[[2, 1], [2, 4]]]})
  return matrixList

def testFindSequenceByColumn():
  for e in getMatrix():
    matrix = e['matrix']
    expected = e['expected_col_seq']
    ouput = findSequenceByColumn(matrix)
    assert(ouput == expected)

def testFindSequenceByRow():
  for e in getMatrix():
    matrix = e['matrix']
    expected = e['expected_row_seq']
    ouput = findSequenceByRow(matrix)
    assert(ouput == expected)