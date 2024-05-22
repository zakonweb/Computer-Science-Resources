"""
Writing python code for the following insertion sort alogorithm:
Insertion Sort Peudocode.
// Global space
arr = [4, 3, 2, 10, 12, 1, 5, 6]

PROCEDURE insertSort()
    DECLARE redP, blackP, revP, temp : INTEGER
    FOR redP = 1 TO LEN(arr) -1
        FOR blackP = 0 TO redP -1
            IF arr[redP] < arr[blackP] THEN
               temp = arr[redP]
               FOR revP = redP TO blackP+1 STEP -1
                   arr[revP] = arr[revP-1]
               NEXT revP 
               arr[blacP] = temp
               EXIT FOR
            ENDIF
         NEXT blackP 
    NEXT redP 
END PROCEDURE
"""
# Global space
arr = [4, 3, 2, 10, 12, 1, 5, 6]

def insertionSortA():
    """Insertion Sort Algorithm"""
    for redP in range(1, len(arr)):
        for blackP in range(0, redP):
            if arr[redP] < arr[blackP]:
                temp = arr[redP]
                for revP in range(redP, blackP, -1):
                    arr[revP] = arr[revP-1]
                arr[blackP] = temp
                break

# insertion sort python code standard alpgorthm
def insertionSortB():
    """Insertion Sort Algorithm"""
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j>=0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key

# main program
print("Before Insertion Sort: ", arr)
insertionSortB()
print("After Insertion Sort: ", arr)
# end of program
