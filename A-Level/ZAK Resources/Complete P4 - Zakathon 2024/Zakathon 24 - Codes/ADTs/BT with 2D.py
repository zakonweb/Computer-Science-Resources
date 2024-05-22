# python code for BT with 2D array
# Global Space

BT = [[0 for x in range(6)] for y in range(6)] # 2D array
Null = -1
Free = 0

def InitBT():
    for i in range(6):
        BT[i][0] = Null
        BT[i][2] = Null
        BT[i][1] = Null
    global Free
    Free = 0

def addBT(val):
    global Free
    if Free == 6:
        print("BT Overflow...")
    elif Free == 0:
        BT[Free][1] = val
        Free = Free + 1
    else:
        NewNode = Free
        Free = Free + 1
        BT[NewNode][1] = val
        CurrNode = 0
        while CurrNode != Null:
            PreNode = CurrNode
            if val < BT[CurrNode][1]:
                CurrNode = BT[CurrNode][0]
                Direction = 'L'
            else:
                CurrNode = BT[CurrNode][2]
                Direction = 'R'
        if Direction == 'L':
            BT[PreNode][0] = NewNode
        else:
            BT[PreNode][2] = NewNode

# display BT SD arrays, i.e. LP, DATA, RP
def displayBT():
    print("LP\t", "DATA\t", "RP\t")
    for i in range(6):
        print(BT[i][0], "\t", BT[i][1], "\t", BT[i][2], "\t")

# BT traversal in inorder, preorder, postorder
def inorderBT(root):
    if root != Null:
        inorderBT(BT[root][0]) # left subtree
        print(BT[root][1], end = " ") # root
        inorderBT(BT[root][2]) # right subtree

def preorderBT(root):
    if root != Null:
        print(BT[root][1], end = " ") # root
        inorderBT(BT[root][0]) # left subtree
        inorderBT(BT[root][2]) # right subtree

def postorderBT(root):
    if root != Null:
        inorderBT(BT[root][0]) # left subtree
        inorderBT(BT[root][2]) # right subtree
        print(BT[root][1], end = " ") # root

def searchBT(root, val): # recursive
    if root == Null:
        return False
    elif val == BT[root][1]:
        return True
    elif val < BT[root][1]:
        return searchBT(BT[root][0], val)
    else:
        return searchBT(BT[root][2], val)

def serachBTIterative(root, val): # iterative
    while root != Null and val != BT[root][1]:
        if val < BT[root][1]:
            root = BT[root][0]
        else:
            root = BT[root][2]
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
        val = int(input("Enter value: "))
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
        val = int(input("Enter value to search: "))
        print(searchBT(0, val))
    elif choice == 8:
        print("End of program")
    else:
        print("Invalid choice")
        
# end of program
