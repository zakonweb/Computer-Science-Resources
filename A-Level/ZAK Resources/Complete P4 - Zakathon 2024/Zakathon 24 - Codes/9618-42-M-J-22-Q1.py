'''
A 2D array stores data entered by a user.
(a) The main program declares a 2D array of 10 by 10 integer elements.
The array is initialised with a random number between 1 and 100 in each element.
Write program code for the main program.
'''
import random as r

# DECLARE randomArray : ARRAY[0:9, 0:9] OF INTEGER
randomArray = [[0 for i in range(10)] for j in range(10)]

for i in range(10):
    for j in range(10):
        randomArray[i][j] = r.randint(1, 100)

def printArray(array):
    for i in range(10):
        for j in range(10):
            print(array[i][j], end=' ')
        print()


print("Before sorting: ")
printArray(randomArray)

'''
(b) The following bubble sort pseudocode algorithm sorts the data in the first dimension of the 2D
array into ascending numerical order.
ArrayLength 10
FOR X 0 TO ArrayLength - 1
    FOR Y 0 TO ArrayLength - 2
        FOR Z 0 TO ArrayLength - Y - 2
            IF ArrayData[X, Z] > ArrayData[X, Z + 1] THEN
                TempValue ArrayData[X, Z]
                ArrayData[X, Z] ArrayData[X, Z+1]
                ArrayData[X, Z + 1] TempValue
            ENDIF
        NEXT Z
    NEXT Y
NEXT X
(i) Amend your main program by writing program code to implement the bubble sort
algorithm after the initialisation of the array elements.
You must not use any built-in sorting functions for your programming language.'''

for x in range(len(randomArray)):
    for y in range(len(randomArray) - 1):
        for z in range(len(randomArray) - y - 1):
            if randomArray[x][z] > randomArray[x][z+1]:
                tempValue = randomArray[x][z]
                randomArray[x][z] = randomArray[x][z+1]
                randomArray[x][z+1] = tempValue

'''
Write program code for a procedure to output all the values in the 2D array. The values
should be output as a 2D grid, with values in rows and columns.
Call the procedure before and after your bubble sort code.
'''


print("After sorting: ")
printArray(randomArray)

'''The following pseudocode function uses recursion to perform a binary search in the first row
of the array, for the value SearchValue in the array SearchArray.
The function returns -1 if the item was not found, or it returns the index where it is found.
There are six incomplete statements.
FUNCTION BinarySearch(SearchArray, Lower, Upper, SearchValue) RETURNS INTEGER
    IF Upper >= Lower THEN
        Mid ← (Lower + (Upper - 1)) DIV …………2…………………
        IF SearchArray[0, Mid] = …………SearchValue……………… THEN
            RETURN ……………Mid………………
        ELSE
            IF SearchArray[0, Mid] > SearchValue THEN
                RETURN BinarySearch(SearchArray, ……………Lower………………, Mid - 1, SearchValue)
            ELSE
                RETURN BinarySearch(SearchArray, Mid + 1, …………Upper………………, SearchValue)
            ENDIF
        ENDIF
    ENDIF
    RETURN …………-1…………………
ENDFUNCTION
Note: the arithmetic operator DIV performs integer division, e.g. the result of 10 DIV 3 will be 3.
(i) Write program code for the recursive function BinarySearch().
'''

def BinarySearch(SearchArray, Lower, Upper, SearchValue):

    if Upper >= Lower:
        Mid = (Lower + (Upper-1)) // 2
        if SearchArray[0][Mid] == SearchValue:
            return Mid
        else:
            if SearchArray[0][Mid] > SearchValue:
                return BinarySearch(SearchArray, Lower, Mid - 1, SearchValue)
            else:
                return BinarySearch(SearchArray, Mid + 1, Upper, SearchValue)
    return -1

'''
(ii) In the main program, test the function BinarySearch() twice, outputting the returned
value each time.
One test should be for a number that is in the first line of the array.
One test should be for a number that is not in the first line of the array.
Take a screenshot to show the output.
'''
x = int(input("Enter a number to search in the first row of the array: "))
print(BinarySearch(randomArray, 0, 10, x))

x = int(input("Enter a number to search in the first row of the array: "))
print(BinarySearch(randomArray, 0, 10, x))
