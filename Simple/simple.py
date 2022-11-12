import random

def generateHashMaps():
    return [{'id': i, 'age': random.randint(1, 100)} for i in range(10)]

# avg time complexity of buble sort O(n²), where n is the length of the list.
def orderByAge(list):
    # bubble sort algorithm used to sort.
    x = 0
    while x < len(list):
        y = 0
        while y < len(list) - 1:
            if list[y]['age'] < list[y+1]['age']:
                aux = list[y]
                list[y] = list[y+1]
                list[y+1] = aux
            y += 1
        x += 1

    return list

orderedAges = orderByAge(generateHashMaps())

youngestPersonId = orderedAges[-1]['id']
oldestPersonId = orderedAges[0]['id']

print(f'Youngest person id: {youngestPersonId}. Oldest person id: {oldestPersonId}')
