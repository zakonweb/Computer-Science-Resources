# Implementation of a Stack using a Linked List
# Key Concepts:
# 1. The order of elements in the linked list (stackList) is not relevant.
# 2. Stack operations are achieved by adding and removing nodes at the head of the list.
# 3. 'head' keeps track of the top of the stack pointer.
# 4. 'free' points to the next available (free) node in the linked list.
# 5. Overflow is checked when 'free' is -1, indicating no more free nodes are available.
# 6. Underflow is checked when 'head' is -1, indicating the stack is empty.
# 7. The linked list is implemented as a fixed-size array of Node UDT.

class Node: # User-defined type (UDT) for a node
    def _init_(self):
        self.data = None  # Data part of the node
        self.next = None  # Pointer to the next node

# Global variables for stack management
head = -1  # Initially, 'head' is set to -1 indicating an empty stack
free = -1  # Initially, 'free' is set to -1
stackList = [Node() for i in range(10)]  # Fixed-size array of Node UDT

def init():
    # Initializes the stack and prepares the free list
    global head, free
    for i in range(10):
        stackList[i].next = i+1  # Set the 'next' pointer of each node
    stackList[9].next = -1  # Last node points to -1
    head = -1  # Stack is initially empty
    free = 0   # First free node is at index 0

def push(data):
    # Adds a new element to the top of the stack
    global head, free
    if free == -1:
        print("Stack Overflow")  # No free nodes available
        return
    temp = free  # Use the next free node
    free = stackList[free].next  # Update 'free' to the next free node
    stackList[temp].data = data  # Set data to the new node
    stackList[temp].next = head  # New node points to the current head
    head = temp  # Update head to the new node

def pop():
    # Removes and returns the top element of the stack
    global head, free
    if head == -1:
        print("Stack Underflow")  # Stack is empty
        return
    temp = head  # Node to be popped
    head = stackList[head].next  # Update head to the next node
    stackList[temp].next = free  # Add popped node to the free list
    free = temp  # Update 'free' to the popped node
    return stackList[temp].data  # Return the data of the popped node

def printStack():
    # Prints the current elements in the stack
    global head
    if head == -1:
        print("Stack is empty")  # Stack is empty
        return
    cn = head
    while cn != -1:
        print(stackList[cn].data)  # Print each node's data
        cn = stackList[cn].next  # Move to the next node
    print()

# Main program loop for stack operations
init()
choice = 0
while choice != 4:
    print("1. Push")
    print("2. Pop")
    print("3. Print")
    print("4. Quit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        data = input("Enter the data: ")
        push(data)
    elif choice == 2:
        data = pop()
        print("Popped data is: ", data)
    elif choice == 3:
        printStack()
    elif choice == 4:
        break
    else:
        print("Wrong choice")
    print()