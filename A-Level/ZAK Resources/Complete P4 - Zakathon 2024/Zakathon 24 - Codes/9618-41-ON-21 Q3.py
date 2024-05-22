# 9618/41/O/N/21
'''An ordered binary tree stores integer data in ascending numerical order.
The data for the binary tree is stored in a 2D array with the following structure:
LeftPointer Data RightPointer
Index   [0] [1] [2]
[0]     1   10  2
[1]     -1  5   -1
[2]     -1  16  -1
Each row in the table represents one node on the tree.
The number -1 represents a null pointer.
(a) The 2D array, ArrayNodes, is declared with space for 20 nodes.
Each node has a left pointer, data and right pointer.
The program also initialises the:
• RootPointer to -1 (null); this points to the first node in the binary tree
• FreeNode to 0; this points to the first empty node in the array.
Write program code to declare ArrayNodes, RootPointer and FreeNode in the main
program.
If you are writing in Python programming language, include attribute declarations using
comments.'''

# Global Variables
# DECLARE ArrayNodes : ARRAY[0:19] OF ARRAY[0:2] OF INTEGER
# DECLARE RootPointer : INTEGER
# DECLARE FreeNode : INTEGER

ArrayNodes = [[-1, 0, -1] for i in range(20)]
RootPointer = -1
FreeNode = 0

'''The procedure AddNode() adds a new node to the array ArrayNodes.
The procedure needs to:
• take the array, root pointer and free node pointer as parameters
• ask the user to enter the data and read this in
• add the node to the root pointer if the tree is empty
• otherwise, follow the pointers to find the position for the data item to be added
• store the data in the location and update all pointers.
There are six incomplete statements in the following pseudocode for the procedure AddNode().
PROCEDURE AddNode(BYREF ArrayNodes[] : ARRAY OF INTEGER, BYREF RootPointer : INTEGER, BYREF FreeNode : INTEGER)
    OUTPUT "Enter the data"
    INPUT NodeData
    IF FreeNode <= 19 THEN
        ArrayNodes[FreeNode, 0] ← -1
        ArrayNodes[FreeNode, 1] ← ……NodeData…………………
        ArrayNodes[FreeNode, 2] ← -1
        IF RootPointer = …………-1…………………… THEN
            RootPointer ← 0
        ELSE
            Placed ← FALSE
            CurrentNode ← RootPointer
            WHILE Placed = FALSE
                IF NodeData < ArrayNodes[CurrentNode, 1] THEN
                    IF ArrayNodes[CurrentNode, 0] = -1 THEN
                        ArrayNodes[CurrentNode, 0] ← …………FreeNode…………………
                        Placed ← TRUE
                    ELSE
                        ………CurrentNode………… ← ArrayNodes[CurrentNode, 0]
                    ENDIF
                ELSE
                    IF ArrayNodes[CurrentNode, 2] = -1 THEN
                        ArrayNodes[CurrentNode, 2] ← FreeNode
                        Placed ← …………TRUE……………
                    ELSE
                        CurrentNode ← ArrayNodes[CurrentNode, 2]
                    ENDIF
                ENDIF
            ENDWHILE
        ENDIF
        FreeNode ← …………FreeNode……………… + 1
    ELSE
        OUTPUT("Tree is full")
    ENDIF
ENDPROCEDURE
Write program code for the procedure AddNode().'''
def AddNode(ArrayNodes, RootPointer, FreeNode):
    NodeData = int(input("Enter the data: "))
    if FreeNode <= 19:
        ArrayNodes[FreeNode][0] = -1
        ArrayNodes[FreeNode][1] = NodeData
        ArrayNodes[FreeNode][2] = -1
        if RootPointer == -1:
            RootPointer = 0
        else:
            Placed = False
            CurrentNode = RootPointer
            while Placed == False:
                if NodeData < ArrayNodes[CurrentNode][1]:
                    if ArrayNodes[CurrentNode][0] == -1:
                        ArrayNodes[CurrentNode][0] = FreeNode
                        Placed = True
                    else:
                        CurrentNode = ArrayNodes[CurrentNode][0]
                else:
                    if ArrayNodes[CurrentNode][2] == -1:
                        ArrayNodes[CurrentNode][2] = FreeNode
                        Placed = True
                    else:
                        CurrentNode = ArrayNodes[CurrentNode][2]
        FreeNode += 1
    else:
        print("Tree is full")
    return ArrayNodes, RootPointer, FreeNode

'''The procedure PrintAll() outputs the data in each element in ArrayNodes, in the order
they are stored in the array.
Each element is printed in a row in the order:
LeftPointer Data RightPointer
For example:
1 20 -1
-1 10 -1
Write program code for the procedure PrintAll().'''
def PrintAll(ArrayNodes):
    for i in range(20):
        print(ArrayNodes[i][0], ArrayNodes[i][1], ArrayNodes[i][2])

'''The main program should loop 10 times, each time calling the procedure AddNode(). It
should then call the procedure PrintAll().
(i) Edit the main program to perform the actions described.'''
for i in range(10):
    ArrayNodes, RootPointer, FreeNode = AddNode(ArrayNodes, RootPointer, FreeNode) # only way to handle ByRef in Python
PrintAll(ArrayNodes)

'''An in-order tree traversal visits the left node, then the root (and outputs this), then visits the
right node.
(i) Write a recursive procedure, InOrder(), to perform an in-order traversal on the tree
held in ArrayNodes.
Save your program.
Copy and paste the program code into part 3(e)(i) in the evidence document.
[7]
(ii) Test the procedure InOrder() with the same data entered in part (d)(ii).
Take a screenshot to show the output after entering the data.'''
def InOrder(RootPointer): # works left, root, right
    if RootPointer != -1:
        InOrder(ArrayNodes[RootPointer][0]) # left
        print(ArrayNodes[RootPointer][1], end = ' ')   # root
        InOrder(ArrayNodes[RootPointer][2]) # right

def PreOrder(RootPointer): # works root, left, right
    if RootPointer != -1:
        print(ArrayNodes[RootPointer][1], end = ' ')   # root
        PreOrder(ArrayNodes[RootPointer][0]) # left
        PreOrder(ArrayNodes[RootPointer][2]) # right4

def PostOrder(RootPointer): # works left, right, root
    if RootPointer != -1:
        PostOrder(ArrayNodes[RootPointer][0]) # left
        PostOrder(ArrayNodes[RootPointer][2]) # right
        print(ArrayNodes[RootPointer][1], end = ' ')   # root

print("InOrder: ", end = ' ')
InOrder(RootPointer)
print()

print("PreOrder: ", end = ' ')
PreOrder(RootPointer)
print()

print("PostOrder: ", end = ' ')
PostOrder(RootPointer)
# End of Code