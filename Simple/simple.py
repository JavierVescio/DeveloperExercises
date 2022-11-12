import random

# time complexity O(n)
def generateHashMaps():
    return [{'id': i, 'age': random.randint(1, 100)} for i in range(10)]


# avg time complexity O(n²)
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

    youngestPersonId = list[-1]['id']
    oldestPersonId = list[0]['id']
    print(
        f'Youngest person id: {youngestPersonId}. Oldest person id: {oldestPersonId}')
    return list


orderedAges = orderByAge(generateHashMaps())
