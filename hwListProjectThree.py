listOne = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
listTwo = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]

for x in range (len(listOne)):
    for y in range (len(listOne[0])):
        listThree = listOne[x][y] + listTwo[x][y]
        print(listThree)
