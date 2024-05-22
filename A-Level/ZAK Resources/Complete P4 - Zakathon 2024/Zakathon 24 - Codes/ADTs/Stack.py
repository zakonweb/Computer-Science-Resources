# Python code to demonstrate working of a Stack
# Stack array to store character values
# global variables
stack = [None for i in range(6)]

# null pointer
null = -1 # CONSTANT

# top of stack pointer
top = null

# function to initialize stack
def init_stack():
    global top
    top = null  # null pointer
    # initialize stack array
    for i in range(6):
        stack[i] = None

# procedure to push character data into stack
def push(data):
    global top
    if top == len(stack) - 1:
        print("Stack Overflow. Cannot add more elements")
    else:
        top = top + 1
        stack[top] = data

# function to pop data from stack
def pop():
    global top
    if top == null:
        print("Stack Underflow. Cannot remove more elements")
    else:
        data = stack[top]
        stack[top] = None
        top = top - 1
        return data

# function to display stack and the pointer as arrow on top
def display_stack():
    if top == null:
        print("Stack is empty!")
    else:
        # show stack vertically with an arrow pointing to the top element
        for i in range(len(stack) - 1, -1, -1):
            if i == top:
                print(stack[i], "\t<--- top")
            else:
                print(stack[i])

# main program
choice = 0
while choice != 5:
    print("\n\nStack Menu\n1. Push\n2. Pop\n3. Display\n4. Initialize Stack\n5. Exit")
    choice = int(input("Enter your choice (1 - 5) : "))
    if choice == 1:
        data = input("Enter data to push into stack : ")
        push(data)
    elif choice == 2:
        data = pop()
        if data != None:
            print("Data popped = ", data)
    elif choice == 3:
        display_stack()
    elif choice == 4:
        init_stack()
        print("Stack initialized.")
    elif choice == 5:
        print("Exiting...")
    else:
        print("Invalid choice. Please try again.")
# end of while loop and end of program