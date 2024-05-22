'''
Understanding:

Prerequisite: The list must be sorted.
------------------------------------------
Algorithm BinarySearch
    Input: A sorted list of elements (an array), a target value
    Output: The index of the target value in the array or -1 if the target is not found

    low ← 0
    high ← length of array - 1

    while low <= high do
        mid ← (low + high) DIV 2    # mid ← INT((low + high) / 2)
        if arr[mid] == target then
            return mid
        else if arr[mid] < target then
            low ← mid + 1
        else
            high ← mid - 1
    end while

    return -1
end Algorithm
'''

def binary_search(arr, target):
    """
    Perform a binary search on the sorted array 'arr' to find the 'target' value.

    Parameters:
    arr : The sorted array of elements to search through.
    target: The value to search for.

    Returns:
    int: The index of the target value if found, otherwise -1.
    """
    lower = 0
    upper = len(arr) - 1

    while lower <= upper:
        mid = (lower + upper) // 2  # Calculate the middle index

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            lower = mid + 1
        else:
            upper = mid - 1

    return -1


# Example usage:
arr = [1, 3, 5, 7, 9, 11, 13]
target = 7
result = binary_search(arr, target)

if result != -1:
    print(f"Element found at index {result}")
else:
    print("Element not found")

