'''
Algorithm BubbleSort
    Input: A array of elements
    Output: The sorted array

    for i from 0 to length of array- 1 do
        swapped = false
        for j from 0 to length of array- i - 2 do
            if array[j] > array[j + 1] then
                 mark swapped happened by making swapped true
                swap array[j] and array[j + 1]
            end if
        next
        if swapped happened then get out of the loop
    next
end Algorithm

'''

def bubble_sort(arr):
    """
    Perform bubble sort on the array 'arr' with an optimization flag.

    Parameters:
    arr (array): The array of elements to be sorted.

    Returns:
    array: The sorted array.
    """
    n = len(arr)

    # Traverse through all array elements
    for i in range(n):
        # Initialize swapped flag to False
        swapped = False

        # Last i elements are already sorted
        for j in range(n - i - 1):
            # Traverse the array from 0 to n-i-1
            # Swap if the element found is greater than the next element
            # > sign is used to sort in ascending order
            # < sign is used to sort in descending order
            if arr[j] > arr[j + 1]:   # ascending order
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                '''
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
                '''
                # Set the flag to True to indicate a swap occurred
                swapped = True

        # If no two elements were swapped in the inner loop, the array is sorted
        if not swapped:
            break

    return arr


# Example usage:
arr = [64, 34, 25, 12, 22, 11, 90]
sorted_arr = bubble_sort(arr)
print("Sorted array:", sorted_arr)
