# python code for iterative binary search
arr = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

def binary_search(value):
    lb = 0
    ub = len(arr) - 1
    while lb <= ub:
        mid = (lb + ub) // 2
        if arr[mid] == value:
            return mid
        elif arr[mid] < value:
            lb = mid + 1
        else:
            ub = mid - 1
    return -1

# main program menu and loop
choice = 0
while choice != 2:
    print("1. Search for a value")
    print("2. Quit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        value = input("Enter a value to search for: ")
        index = binary_search(value)
        if index != -1:
            print("Found at index", index)
        else:
            print("Not found")
    elif choice != 2:
        print("Invalid choice")
# end of program
