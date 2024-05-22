# 9618/41/M/J/21 Q1
'''
An unordered linked list uses a 1D array to store the data.
Each item in the linked list is of a record type, node, with a field data and a field nextNode.
The current contents of the linked list are:
startPointer ← 0 
emptyList ← 5 

Index data nextNode
0   1 1
1   5 4
2   6 7
3   7 -1
4   2 2
5   0 6
6   0 8
7   56 3
8   0 9
9   0 -1
(a) The following is pseudocode for the record type node.
TYPE node
    DECLARE data : INTEGER
    DECLARE nextNode : INTEGER
ENDTYPE
Write program code to declare the record type node.'''
# Global Variables
# DECLARE startPointer : INTEGER
# DECLARE emptyList : INTEGER

class node:
    def __init__(self):
        self.data = 0
        self.nextNode = 0

'''Write program code for the main program.
Declare a 1D array of type node with the identifier linkedList, and initialise it with the data
shown in the table on page 2. Declare the pointers.'''
linkedList = [node() for i in range(10)]
linkedList[0].data = 1
linkedList[0].nextNode = 1

linkedList[1].data = 5
linkedList[1].nextNode = 4

linkedList[2].data = 6
linkedList[2].nextNode = 7

linkedList[3].data = 7
linkedList[3].nextNode = -1

linkedList[4].data = 2
linkedList[4].nextNode = 2

linkedList[5].data = 0
linkedList[5].nextNode = 6

linkedList[6].data = 0
linkedList[6].nextNode = 8

linkedList[7].data = 56
linkedList[7].nextNode = 3

linkedList[8].data = 0
linkedList[8].nextNode = 9

linkedList[9].data = 0
linkedList[9].nextNode = -1

startPointer = 0
emptyList = 5

'''The procedure outputNodes() takes the array and startPointer as parameters. The
procedure outputs the data from the linked list by following the nextNode values.
(i) Write program code for the procedure outputNodes().'''

def outputNodes(linkedList, startPointer):
    currentPointer = startPointer
    while currentPointer != -1:
        print(linkedList[currentPointer].data, end = ' ')
        currentPointer = linkedList[currentPointer].nextNode

# outputNodes(linkedList, startPointer)

'''The function, addNode(), takes the linked list and pointers as parameters, then takes as
input the data to be added to the end of the linkedList.
The function adds the node in the next available space, updates the pointers and returns
True. If there are no empty nodes, it returns False.
(i) Write program code for the function addNode().'''
def addNode(linkedList, startPointer, emptyList, data):
    if emptyList == -1:
        return False
    else: # add new node to the end of the linked list
        newPointer = emptyList
        emptyList = linkedList[emptyList].nextNode
        linkedList[newPointer].data = data
        linkedList[newPointer].nextNode = -1
        currentPointer = startPointer
        while linkedList[currentPointer].nextNode != -1:
            currentPointer = linkedList[currentPointer].nextNode
        linkedList[currentPointer].nextNode = newPointer
        return True

'''Edit the main program to:
• call addNode()
• output an appropriate message depending on the result returned from addNode()
• call outputNodes() twice; once before calling addNode() and once after calling
addNode().'''
outputNodes(linkedList, startPointer)
x = addNode(linkedList, startPointer, emptyList, 100)
if x:
    print('\n Node added successfully')
else:
    print('\n No empty node available')
outputNodes(linkedList, startPointer)
