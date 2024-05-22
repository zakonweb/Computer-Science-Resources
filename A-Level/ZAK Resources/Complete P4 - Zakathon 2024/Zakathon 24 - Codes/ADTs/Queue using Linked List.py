"""
# Implementation of a Queue using a Linked List
# Key Concepts:
# 1. The order of elements in the linked list (QList) is not relevant.
# 2. Queue operations are achieved by adding at tail and removing nodes at the head of the Qlist.
# 3. 'head' keeps track of the head of the queue pointer for Dequeue.
# 4. 'tail' keeps track of the tail of the queue pointer for Enqueue.
# 4. 'free' points to the next available (free) node in the linked list.
# 5. Overflow is checked when 'free' is -1, indicating no more free nodes are available.
# 6. Underflow is checked when 'head' is -1, indicating the queue is empty.
# 7. The linked list is implemented as a fixed-size array of Node UDT.
"""

class Node:
    def __init__(self):
        self.data = None
        self.next = None

head = -1
tail = -1
free = 0
QList = [Node() for i in range(10)]

def init():
    global head, tail, free
    head = -1
    tail = -1
    free = 0
    for i in range(0, len(QList)-1):
        QList[i].next = i+1
    QList[len(QList)-1].next = -1

def enqueue(data):
    global head, tail, free
    if free == -1:
        print("Overflow")
        return
    temp = free
    free = QList[temp].next
    QList[temp].data = data
    QList[temp].next = -1
    if head == -1:
        head = temp
    else:
        QList[tail].next = temp
    tail = temp

def dequeue():
    global head, tail, free
    if head == -1:
        print("Underflow")
        return
    temp = head
    head = QList[temp].next
    if head == -1:
        tail = -1
    QList[temp].next = free
    free = temp
    return QList[temp].data

def printQ():
    global head, tail, free
    if head == -1:
        print("Queue is empty")
        return
    temp = head
    while temp != -1:
        print(QList[temp].data, end=" ")
        temp = QList[temp].next
    print()
    print("head: ", head)
    print("tail: ", tail)
    print("free: ", free)

# main program
init()
choice = 0
while choice != 4:
    print("1. Enqueue")
    print("2. Dequeue")
    print("3. Print")
    print("4. Quit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        data = input("Enter data: ")
        enqueue(data)
    elif choice == 2:
        data = dequeue()
        print("Dequeued data: ", data)
    elif choice == 3:
        printQ()
    elif choice == 4:
        break
    else:
        print("Invalid choice")
    print()
# end of main program