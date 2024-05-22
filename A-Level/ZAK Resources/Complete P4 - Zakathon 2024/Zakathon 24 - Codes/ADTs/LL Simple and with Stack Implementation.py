'''
Stack over LL
Ordered Linked List code using python.
The list has 3 global variables: head, tail and free.
Initially the list is empty, so head and tail are set to -1.
And it will be treated as the free list.
An item when inserted in the linked list, it checks for following conditions:
1. If the list is empty, it inserts the item at the beginning.
2. If the list is full, it returns -1. Item cannot be inserted.
3. If the item is less than the head, it inserts the item at the beginning.
4. If the item is greater than the tail, it inserts the item at the end.
5. Otherwise, it inserts the item in the middle of the list.
'''

# create Node UDT
# Node has two fields: data and next
# TYPE Node
#   DECLARE data : STRING
#   DECLARE next : INTEGER
# END TYPE
class Node:
    def _init_(self):
        self.data = ' '
        self.next = -1

# create global variables and List
thisList = [Node() for i in range(10)]
head = -1
tail = -1
free = 0

# initialize the list and global variables
def init_list():
    global head, tail, free
    for i in range(10):
        thisList[i].next = i + 1
    thisList[9].next = -1
    head = -1
    tail = -1
    free = 0

# insert item in the list
def insert_inorder(item):
    global head, tail, free
    if free == -1: # list is full
        return -1
    else:
        new_node = free
        thisList[new_node].data = item
        free = thisList[free].next
        if head == -1: # list is empty
            head = new_node # head points to new node i.e. first node 0
            tail = new_node # tail points to new node i.e. first node 0
            thisList[new_node].next = -1
        elif item < thisList[head].data: # insert at the beginning
            thisList[new_node].next = head
            head = new_node
        elif item > thisList[tail].data: # insert at the end
            thisList[tail].next = new_node
            tail = new_node
            thisList[new_node].next = -1
        else: # insert in the middle, i.e. between head and tail
            prev = head
            current = thisList[head].next
            while item > thisList[current].data:
                prev = current
                current = thisList[current].next
            thisList[new_node].next = current
            thisList[prev].next = new_node
    return 0

def delete_inorder(item):
    global head, tail, free
    if head == -1: # list is empty
        return -1
    else:
        prev = -1
        current = head
        while current != -1 and item != thisList[current].data:
            prev = current
            current = thisList[current].next
        if current == -1: # item not found
            return -1
        else:
            if current == head: # item is at the beginning
                head = thisList[head].next
            else:
                thisList[prev].next = thisList[current].next
            thisList[current].next = free
            free = current
            return 0

def search_inorder(item):
    if head == -1: # list is empty
        return -1
    else:
        current = head
        while current != -1 and item != thisList[current].data:
            current = thisList[current].next
        if current == -1: # item not found
            return -1
        else:
            return current

def display_contents_inorder():
    if head == -1: # list is empty
        print("List is empty")
    else:
        current = head
        while current != -1:
            print(thisList[current].data, end=' ')
            current = thisList[current].next
        print()

def display_list():
    print("head = ", head)
    print("tail = ", tail)
    print("free = ", free)
    print()
    print("List contents: ")
    print('i', '\t', 'Data', '\t', 'Next')
    for i in range(10):
        print(i, '\t', thisList[i].data, '\t', thisList[i].next)

# now we use thisList as a Stack UDT
# Where tail is the top of the stack
# And head is the bottom of the stack
# And free is the free list
# We make insert_inStack() and delete_inStack() functions
        
def insert_inStack(item):
    # always insert at the top of the stack, i.e. tail. Push operation
    global head, tail, free
    if free == -1: # stack is full
        return -1
    else:
        new_node = free
        thisList[new_node].data = item
        free = thisList[free].next
        if head == -1: # stack is empty
            head = new_node # head points to new node i.e. first node 0
            tail = new_node # tail points to new node i.e. first node 0
            thisList[new_node].next = -1
        else:
            thisList[new_node].next = tail
            tail = new_node

def delete_inStack(): # delete from the top of the stack, i.e. tail. Pop operation
    global head, tail, free
    if head == -1: # stack is empty
        return None
    else:
        data = thisList[tail].data
        if head == tail: # only one node in the stack
            init_list()
        else:
            # delete from the top of the stack, i.e. tail
            # tail node will be given to free list
            # update tail to the previous node by making it the new tail
            temp = free
            free = tail
            tail = thisList[tail].next
            thisList[free].next = temp
        return data

def display_contents_inStack():
    if head == -1: # stack is empty
        print("Stack is empty")
    else:
        current = tail
        while current != -1:
            print(thisList[current].data, end=' ')
            current = thisList[current].next
        print()

# main program for Stack
init_list()
print("Stack operations")
choice = 0
while choice != 4:
    print("1. Push")
    print("2. Pop")
    print("3. Display")
    print("4. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        item = input("Enter the item to be pushed: ")
        insert_inStack(item)
    elif choice == 2:
        item = delete_inStack()
        if item == None:
            print("Stack is empty")
        else:
            print("Popped item is: ", item)
    elif choice == 3:
        display_contents_inStack()
    elif choice == 4:
        print("Exiting...")
    else:
        print("Invalid choice")
# end of main program for Stack