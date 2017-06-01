from array import *
row = input("Please enter the row value. ")
column = input("Please enter the column value. ")

arrayValue = array[row][column]

for r in arrayValue.length:
    for c in arrayValue[0].length:
        v = input("Please enter your array value")
        arrayValue[r][v] = v
else:
    print("Your array is full.")

print(arrayValue)