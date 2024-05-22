TheData = [20, 3, 4, 8, 12, 99, 4, 26, 4]
"""
PROCEDURE InsertionSort(TheData[]:INTEGER)
 FOR Count ← FirstElement TO 8 //LEN(TheData) - 1
    DataToInsert ← TheData[Count]
    Inserted ← 0
    NextValue ← Count - 1
    WHILE (NextValue >= 0 AND Inserted <> 1)
        IF (DataToInsert < TheData[NextValue]) THEN
            TheData[NextValue + 1] ← TheData[NextValue]
            NextValue ← NextValue - 1
            TheData[NextValue + 1] ← DataToInsert
        ELSE
            Inserted ← 1
        ENDIF
    ENDWHILE
 NEXT
END PROCEDURE
"""

def InsertionSort():
    """Insertion Sort Algorithm"""
    for Count in range(1, len(TheData)):
        DataToInsert = TheData[Count]
        Inserted = 0
        NextValue = Count - 1
        while (NextValue >= 0 and Inserted != 1):
            if (DataToInsert < TheData[NextValue]):
                TheData[NextValue + 1] = TheData[NextValue]
                NextValue = NextValue - 1
                TheData[NextValue + 1] = DataToInsert
            else:
                Inserted = 1

# main program
print("Before Insertion Sort: ", TheData)
InsertionSort()
print("After Insertion Sort: ", TheData)
# end of program