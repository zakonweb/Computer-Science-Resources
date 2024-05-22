"""
Insertion sort algorithm in python for the following pseudocode

arr = [4,3,2,10,12,1,5,6]

FOR i = 1 TO LEN(arr)-1
    key = arr[i]
    j = i-1
    WHILE j >= 0 AND arr[j] > key
        arr[j+1] = arr[j]
        j = j -1
    END WHILE
    arr[j+1] = key
NEXT i 
"""
arr = [4,3,2,10,12,1,5,6]

def insertion_sort(arr):
    for i in range(1,len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j = j -1
        arr[j+1] = key

print("Unsorted array: ", arr)
insertion_sort(arr)
print("Sorted array: ", arr)
