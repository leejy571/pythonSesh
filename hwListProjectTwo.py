listOneRow = input("Please enter the first array's row value. ")
listOneColumn = input("Please enter the first array's column value. ")

listOneComplete = [[0 for x in range(listOneRow)] for y in range(listOneColumn)]

for x in range(listOneRow):
    row = []
    for y in range(listOneColumn):
        column = []
    listOneComplete.append(row)

print listOneComplete