"""
//Stack with UDT Pseudocode
//Global Space
//User defined data type, UDT
TYPE stRecord
   DECLARE stID : INTEGER
   DECLARE stName : STRING
   DECLARE stFee : REAL
END TYPE

DECLARE Stack : ARRAY [0:5] OF stRecord
DECLARE TopOfStack, Null : INTEGER
Null = -1
TopOfStack = Null

PROCEDURE Iinitialise()
   DECLARE i : INTEGER
   i=0
   For i = 0 TO LEN(Stack)-1
     Stack[i].stID = 0
     Stack[i].stName = ""
     Stack[i].stFee = 0.0
   NEXT
   TopOfStack = Null
END PROCEDURE

PROCEDURE Push(data)
    IF TopOfSTack = LEN(Stack)-1 THEN
       OUTPUT "Overflow occured! Data cannot be pushed."
    ELSE
       TopOfStack = TopOfStack +1
       Stack[TopOfStack].stID = data.stID
       Stack[TopOfStack].stName = data.stName
       Stack[TopOfStack].stFee = data.stFee
    ENDIF
END PROCEDURE

FUNCTION Pop() RETURNS stRecord
    DECLARE data : stRecord
    IF TopOfStack = Null THEN
      data.stID = Null
       RETURN data
    ELSE
       data.stID = Stack[TopOfStack].stID
       data.stName = Stack[TopOfStack].stName
       data.stFee = Stack[TopOfStack].stFee

       TopOfStack = TOpOfSTack -1
       RETURN data
    ENDIF
END FUNCTION
"""

# stack UDT with class definition
class stRecord:
    def __init__(self):
        self.stID = 0
        self.stName = ""
        self.stFee = 0.0

stack = [stRecord() for i in range(6)] # stack of 5 records
Null = -1
TopOfStack = Null

def Initialise():
    global TopOfStack
    for i in range(len(stack)):
        stack[i].stID = 0
        stack[i].stName = ""
        stack[i].stFee = 0.0
    TopOfStack = Null

def Push(data):
    global TopOfStack
    if TopOfStack == len(stack)-1:
        print("Overflow occured! Data cannot be pushed.")
    else:
        TopOfStack = TopOfStack +1
        stack[TopOfStack].stID = data.stID
        stack[TopOfStack].stName = data.stName
        stack[TopOfStack].stFee = data.stFee

def Pop():
    global TopOfStack
    data = stRecord()
    if TopOfStack == Null:
        data.stID = Null
        return data
    else:
        data.stID = stack[TopOfStack].stID
        data.stName = stack[TopOfStack].stName
        data.stFee = stack[TopOfStack].stFee

        TopOfStack = TopOfStack -1
        return data

# display stack in reverse order
def Display():
    global TopOfStack
    if TopOfStack == Null:
        print("Stack is empty!")
    else:
        for i in range(TopOfStack, -1, -1):
            if i == TopOfStack:
                print(i, '\t', stack[i].stID, stack[i].stName, stack[i].stFee, "\t <--- Top of stack")
            else:
                print(i, '\t', stack[i].stID, stack[i].stName, stack[i].stFee)

# main program
choice = 0
while choice != 5:
    print("1. Initialise")
    print("2. Push")
    print("3. Pop")
    print("4. Display")
    print("5. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        Initialise()
        print("Stack initialised!")
    elif choice == 2:
        data = stRecord()
        data.stID = int(input("Enter ID: "))
        data.stName = input("Enter name: ")
        data.stFee = float(input("Enter fee: "))
        Push(data)
        print("Data pushed!")
    elif choice == 3:
        data = Pop()
        if data.stID == Null:
            print("Stack is empty!")
        else:
            print("Data popped!")
            print("ID: ", data.stID)
            print("Name: ", data.stName)
            print("Fee: ", data.stFee)
    elif choice == 4:
        Display()
    elif choice == 5:
        print("Exiting...")
    else:
        print("Invalid choice!")
# end of program