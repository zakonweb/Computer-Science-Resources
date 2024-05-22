"""
Wting a python code for the following binary search pseudocode algorithm.
Where the binary Search array BinArr[] is already made in global space
The content of array is already sorted to run smooth bin search algo
// Binary Search Algorithm
FUNCTION BinSearch(value : CHARACTER) RETURNS INTEGER
    DECLARE Middle, LB, UB : INTEGER
    Middle = -1
    LB = 0
    UB = LEN(BinArr) -1

    WHILE LB <= UB DO
      Middle = (UB+LB) DIV 2
      IF BinArr(Middle) = value THEN
         RETURN Middle
      ELSEIF BinArr(Middle) < value THEN
         LB = Middle +1
      ELSE
         UB = Middle -1
      ENDIF
    ENDWHILE
    RETURN -1  //Value not found  
END FUNCTION
"""
# global variables and array
BinArr = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

# function to search the array with binary search algorithm
def BinSearch(value):
    global BinArr
    Middle = -1
    LB = 0
    UB = len(BinArr) -1

    while LB <= UB:
        Middle = (UB+LB) // 2
        if BinArr[Middle] == value:
            return Middle
        elif BinArr[Middle] < value:
            LB = Middle +1
        else:
            UB = Middle -1
    return -1  #Value not found

# main menu program
choice = 0
while choice != 2:
      print("1. Search the array with binary search algorithm")
      print("2. Exit")
      choice = int(input("Enter your choice: "))
      if choice == 1:
         value = input("Enter the value to search: ")
         index = BinSearch(value)
         if index != -1:
               print("Value found at index: ", index +1)
         else:
               print("Value not found")
      elif choice == 2:
         print("Exiting the program")
      else:
         print("Wrong choice, try again")