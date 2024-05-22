# RECURSION
# BASE CASE
# RECURSIVE CASE/GENERAL CASE

# factorial function
# n!
'''
Mathematically
0! = 1 (Base case)
n! = n * (n-1)! (recursive case)

def factorial1(n):
    # Base case: when n is 0 or 1
    if n == 0 or n == 1:
        print('Base case arrived, returning 1.')
        return 1
    # Recursive case: n * factorial of (n-1)
    else:
        print(f'{n} * factorial1({n-1})')
        x = n * factorial1(n - 1)
        print("result =", x)
        return x

# Example usage
print(factorial1(5))  # Output: 120
'''
def factorial1(n):
    # Base case: when n is 0 or 1
    if n == 0 or n == 1:
        return 1
    # Recursive case: n * factorial of (n-1)
    else:
        return n * factorial1(n - 1)
# Example usage
# print(factorial1(5))  # Output: 120

'''
Example 1: Fibonacci Sequence
The Fibonacci sequence is a series of numbers where each number is the sum of 
the two preceding ones. The sequence starts with 0 and 1.

Mathematically:
f(0) = 0 (base case)
f(1) = 1 (base case)
f(n) = f(n-1) + f(n-2) (recursive case)

def fibonacci(n):
    # Base cases
    if n == 0:
        return 0
    elif n == 1:
        return 1
    # Recursive case
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Example usage
# 1 2 3 5 8 13 21 34 55
print(fibonacci(10))  # Output: 55
'''

# sum of array
def sum_array(arr):
    # Base case: if the array is empty
    if len(arr) == 0:
        return 0
    # Recursive case
    else:
        return arr[0] + sum_array(arr[1:])

# Example usage
arr = [1, 2, 3, 4, 5]
print(sum_array(arr))  # Output: 15
