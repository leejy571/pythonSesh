listOne = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
listTwo = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]
sum = 0

for x in range(len(listOne)):
    for y in range(len(listOne[0])):
        for k in range(len(listTwo[0])):
            sum = sum + listOne[x][k] * listTwo[k][y]
        listThree[x][y] = sum
        sum = 0

for x in range(len(listOne)):
    for y in range(len(listOne[0])):
        print(listThree[x][y])
    print()