'''Insertion Sort
Insertion Sort is a simple and intuitive sorting algorithm that works similarly to the way you might sort playing cards in your hands. It builds the final sorted array one item at a time. It is much less efficient on large lists than more advanced algorithms such as quicksort, heapsort, or merge sort.

How Insertion Sort Works
Start with the second element (first element is already sorted).
Compare the current element with the elements in the sorted portion of the array.
Insert the current element into the correct position in the sorted portion.
Repeat the process for all elements.'''

def insertion_sort(arr):
    # Traverse from the second element to the end
    for i in range(1, len(arr)):
        key = arr[i]  # Current element to be inserted
        j = i - 1
        # Shift elements of the sorted segment to the right
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        # Insert the key at the correct location
        arr[j + 1] = key
    return arr

# Example usage
arr = [5, 2, 9, 1, 5, 6]
sorted_arr = insertion_sort(arr)
print("Sorted array is:", sorted_arr)
