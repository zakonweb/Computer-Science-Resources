'''9618/42/M/J/22
A program needs to use a stack data structure. The stack can store up to 10 integer elements.
A 1D array StackData is used to store the stack globally. The global variable StackPointer
points to the next available space in the stack and is initialised to 0.
(a) Write program code to declare the array and pointer as global data structures. Initialise the
pointer to 0'''
StackData = [0 for i in range(10)]
StackPointer = 0

# Write a procedure to output all 10 elements in the stack and the value of StackPointer
def outputStack():
    print("Stack Data:")
    for i in range(10):
        print(StackData[i])
    print(f'StackPointer = {StackPointer}')

'''The function Push() takes an integer parameter and returns FALSE if the stack is full. If the
stack is not full, it puts the parameter value on the stack, updates the relevant pointer and
returns TRUE.
Write program code for the function Push().'''
def Push(x):
    global StackPointer
    if StackPointer == 10:
        return False
    StackData[StackPointer] = x
    StackPointer += 1
    return True

'''The function Pop() returns -1 if the stack is empty. If the stack is not empty, it returns the
element at the top of the stack and updates the relevant pointer.
(i) Write program code for the function Pop().'''
def Pop():
    global StackPointer
    if StackPointer == 0:
        return -1
    StackPointer -= 1
    return StackData[StackPointer]

'''(d) (i) Edit the main program to test the Push() function. The main program needs to:
• allow the user to enter 11 numbers and attempt to add these to the stack
• output an appropriate message when a number is added to the stack
• output an appropriate message when a number is not added to the stack if it is full
• output the contents of the stack after attempting to add all 11 numbers.'''
for i in range(11):
    if Push(int(input("Enter a number: "))):
        print("Number added to stack")
    else:
        print("Stack is full")
outputStack()

'''After the code you wrote in the main program for part 1(d)(i), add program code to:
• remove two elements from the stack using Pop()
• output the updated contents of the stack.
Test your program and take a screenshot to show the output.'''
x = Pop()
print(f'Popped value: {x}')
x = Pop()
print(f'Popped value: {x}')
outputStack()
# End of program