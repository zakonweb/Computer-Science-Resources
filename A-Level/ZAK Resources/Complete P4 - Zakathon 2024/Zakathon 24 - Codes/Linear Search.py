'''
Understanding:
Algorithm LinearSearch
    Input: A list of elements (an array), a target value
    Output: The index of the target value in the list or -1 if the target is not found

    for index from 0 to length of array - 1 do
        if array[index] == target then
            return index
    next

    return -1
end Algorithm
'''

def linear_search(arr, target):
    """
    Perform a linear search on the array 'arr' to find the 'target' value.

    Parameters:
    arr (array): The list of elements to search through.
    target: The value to search for.

    Returns:
    int: The index of the target value if found, otherwise -1.
    """
    for index in range(len(arr)):
        if arr[index] == target:
            return index
    return -1


# Example usage:
arr = [3, 5, 2, 4, 9]
target = 4
result = linear_search(arr, target)

if result != -1:
    print(f"Element found at index {result}")
else:
    print(f"{target} element not found")
