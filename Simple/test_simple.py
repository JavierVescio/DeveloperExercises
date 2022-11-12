from simple import generateHashMaps,orderByAge

def testLenFromGenerateHashmaps():
  assert len(generateHashMaps()) == 10

def testAgeFromGenerateHashmaps():
  for e in generateHashMaps():
    assert (e['age'] >= 1 and e['age'] <= 100)
  
def testDescendentOrderByAge():
  l = orderByAge(generateHashMaps())
  i = 0
  while i < len(l) - 1 and l[i]['age'] >= l[i + 1]['age']: 
    i += 1
  assert (i == len(l) - 1)