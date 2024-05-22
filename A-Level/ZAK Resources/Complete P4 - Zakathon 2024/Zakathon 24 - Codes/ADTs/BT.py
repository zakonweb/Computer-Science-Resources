"""
Python code for BT with SD arrays for LP, Data, RP

//Global Space
DECLARE LP : ARRAY [0:5] OF INTEGER
DECLARE DATA : ARRAY [0:5] OF CHARACTER
DECLARE RP : ARRAY [0:5] OF INTEGER

DECLARE FREE : INTEGER
CONSTANT NULL = -1

PROCEDURE InitBT()
   DECLARE i : INTEGER
   FOR i = 0 TO 5
       LP[i] = NULL
       RP[i] = NULL
       DATA[i] = ''
   NEXT
   FREE = 0 //ROOT = 0
END PROCEDURE

PROCEDURE addBT(val : CHARACTER)
    DECLARE NewNode, PreNode, CurrNode : INTEGER
    DECLARE Direction : CHARACTER
    IF FREE = 6 THEN
       OUTPUT "BT Overflow..."
    ELSEIF FREE = 0 THEN
       DATA[FREE] = val
       FREE = FREE + 1
    ELSE
       NewNode = FREE
       FREE = FREE + 1
       DATA[NewNode] = val
       CurrNode = 0 //ROOT
       WHILE CurrNode <> NULL
          PreNode = CurrNode
          IF val < DATA[CurrNode] THEN
             CurrNode = LP[CurrNode]
             Direction = 'L'
          ELSE
             CurrNode = RP[CurrNode]
             Direction = 'R'
          ENDIF
      END WHILE
      IF Direction = 'L' THEN
         LP[PreNode] = NewNode 
      ELSE
         RP[PreNode] = NewNode 
      ENDIF
    ENDIF   
END PROCEDURE

"""

# Global Space
LP = [None for i in range(6)]
DATA = [None for i in range(6)]
RP = [None for i in range(6)]
Null = -1
Free = 0

def InitBT():
    for i in range(6):
        LP[i] = Null
        RP[i] = Null
        DATA[i] = ''
    global Free
    Free = 0

def addBT(val):
    global Free
    if Free == 6:
        print("BT Overflow...")
    elif Free == 0:
        DATA[Free] = val
        Free = Free + 1
    else:
        NewNode = Free
        Free = Free + 1
        DATA[NewNode] = val
        CurrNode = 0
        while CurrNode != Null:
            PreNode = CurrNode
            if val < DATA[CurrNode]:
                CurrNode = LP[CurrNode]
                Direction = 'L'
            else:
                CurrNode = RP[CurrNode]
                Direction = 'R'
        if Direction == 'L':
            LP[PreNode] = NewNode
        else:
            RP[PreNode] = NewNode

# display BT SD arrays, i.e. LP, DATA, RP
def displayBT():
    print("LP\t", "DATA\t", "RP\t")
    for i in range(6):
        print(LP[i], "\t", DATA[i], "\t", RP[i], "\t")

# BT traversal in inorder, preorder, postorder
def inorderBT(root):
    if root != Null:
        inorderBT(LP[root]) # left subtree
        print(DATA[root], end = " ") # root
        inorderBT(RP[root]) # right subtree

def preorderBT(root):
    if root != Null:
        print(DATA[root], end = " ") # root
        preorderBT(LP[root]) # left subtree
        preorderBT(RP[root]) # right subtree

def postorderBT(root):
    if root != Null:
        postorderBT(LP[root]) # left subtree
        postorderBT(RP[root]) # right subtree
        print(DATA[root], end = " ") # root

def searchBT(root, val): # recursive
    if root == Null:
        return False
    elif val == DATA[root]:
        return True
    elif val < DATA[root]:
        return searchBT(LP[root], val)
    else:
        return searchBT(RP[root], val)

def serachBTIterative(root, val): # iterative
    while root != Null and val != DATA[root]:
        if val < DATA[root]:
            root = LP[root]
        else:
            root = RP[root]
    if root == Null:
        return False
    else:
        return True

# main program
choice = 0
while choice != 8:
    print("\n1. InitBT()")
    print("2. addBT(val)")
    print("3. displayBT()")
    print("4. inorderBT(root)")
    print("5. preorderBT(root)")
    print("6. postorderBT(root)")
    print("7. searchBT(root, val)")
    print("8. Exit")
    choice = int(input("Enter choice: "))

    if choice == 1:
        InitBT()
    elif choice == 2:
        val = input("Enter value: ")
        addBT(val)
    elif choice == 3:
        displayBT()
    elif choice == 4:
        inorderBT(0)
    elif choice == 5:
        preorderBT(0)
    elif choice == 6:
        postorderBT(0)
    elif choice == 7:
        val = input("Enter value: ")
        print(searchBT(0, val))
    elif choice == 8:
        print("End of program")
    else:
        print("Invalid choice")
        
# end of program
