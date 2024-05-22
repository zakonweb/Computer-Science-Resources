# python code for recurive binary search
# global variables
binArr = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i','j', 'k', 'l']

def binSearch(lb, ub, value):
    if lb > ub:
        return -1 # base case
    else: 
        mid = (lb + ub) // 2
        if binArr[mid] == value: # base case
            return mid
        elif binArr[mid] < value: # general case
            return binSearch(mid + 1, ub, value)
        else: # general case
            return binSearch(lb, mid - 1, value)

lb = 0
ub = len(binArr) -1
value = input('enter a value to search: ')
index = binSearch(lb, ub, value)
if index == -1:
    print('value not found')
else:
    print('value found at index: ', index+1)
# end of program