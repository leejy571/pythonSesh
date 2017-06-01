from array import*
from operator import add

arrayOne = [0,1,2,3,4]
arrayTwo = [4,3,2,1,0]
arrayThree = map(add,arrayOne, arrayTwo)

print(arrayThree)