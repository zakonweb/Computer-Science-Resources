"""
Python code for following recursive binary search algorithm pseudocode.
Where array BinArr is already sorted in ascending order and found in 
global space.
// Recursive Binary Search
FUNCTION BinSearchR(LB, UB : INTEGER, Value: CHARACTER) : INTEGER
    DECLARE Middle : INTEGER
    Middle = (LB+UB) DIV 2
    IF LB > UB THEN RETURN -1
    ELSEIF BinArr(Middle) = Value THEN RETURN Middle
    ELSEIF BinArr(Middle) < Value THEN RETURN BinSearchR(Middle+1, UB, Value)
    ELSE RETURN BinSearchR(LB, Middle-1, Value)
    ENDIF
END FUNCTION 
"""
BinArr = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'] # Global space

def BinSearchR(LB, UB, Value):
    Middle = (LB+UB) // 2
    if LB > UB: # Base case
        return -1
    elif BinArr[Middle] == Value: # Base case
        return Middle 
    elif BinArr[Middle] < Value: # General case
        return BinSearchR(Middle+1, UB, Value)
    else: # General case
        return BinSearchR(LB, Middle-1, Value)

# main menu program
choice = 0
while choice != 2:
    print("1. Search for a value in the array")
    print("2. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        Value = input("Enter a value to search for: ")
        Index = BinSearchR(0, len(BinArr)-1, Value)
        if Index == -1:
            print("Value not found")
        else:
            print("Value found at index", Index+1)
    elif choice == 2:
        print("Goodbye...")
    else:
        print("Invalid choice")