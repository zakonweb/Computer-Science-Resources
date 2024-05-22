# python code for binary search array
# global space 
arr = ['a','b','c','d','e','f','g','h','i','j','k']

# function to binary search for a value in an array
def binary_search(value): 
    # set the start and end points of the array
    start = 0 # LB
    end = len(arr)-1 # UB
    # loop through the array
    while start <= end:
        # set the mid point of the array
        mid = (start + end) // 2 # // is floor division; DIV 
        # if the value is the mid point of the array return the index
        if arr[mid] == value:
            return mid
        # if the value is less than the mid point of the array set the end point to the mid point -1
        else:
            if value < arr[mid]:
                end = mid - 1
        # if the value is greater than the mid point of the array set the start point to the mid point +1
            else:
                start = mid + 1
    # if the value is not in the array return -1
    return -1

# get the value to search for
value = input('enter a value to search: ')
# call the binary search function
index = binary_search(value)
# if the index is -1 print value not found
if index == -1:
    print('value not found')
# else print the index of the value
else:
    print('value found at index: ', index+1)
# end of program