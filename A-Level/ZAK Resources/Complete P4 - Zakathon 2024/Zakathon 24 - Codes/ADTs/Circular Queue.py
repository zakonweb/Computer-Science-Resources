"""
*Python code for circular Q as per following pseudocde.*
//Circular Q
//GLOBAL SPACE
DECLARE Q : ARRAY [0:7] OF CHARACTER
DECLARE head, tail, Qsize, Qlen : INTEGER

PROCEDURE initQ():
   DECLARE i : INTEGER
   FOR i = 0 TO 7
       Q[i] = ''
   NEXT i

   head = -1
   tail = -1
   Qsize = 0
   Qlen = len(Q)
END PROCEDURE

PROCEDURE Enqueue(data : CHARACTER)
   IF Qsize = Qlen THEN
      OUTPUT "Overflow. Queue is full."
   ELSE
      IF tail = Qlen -1 THEN //tail at UB?
         tail = 0
      ELSE
         tail = tail + 1
      END IF
      Q[tail] = data
   END IF
END PROCEDURE

FUNCTION Dequeue() : CHARACTER
   DECLARE data : CHARACTER
   data = ''
   IF Qsize = 0 THEN
      OUTPUT "Underflow. Queue is empty."
   ELSE
      IF head = Qlen -1 THEN //head at UB?
         head = 0
      ELSE
         head = head + 1
      END IF
      data = Q[head]
   END IF
   
   RETURN data
END FUNCTION
""" 
# GLOBAL SPACE
Q = [None for i in range(8)]
head = -1
tail = -1
Qsize = 0
Qlen = len(Q)

def initQ():
    global head, tail, Qsize, Qlen
    for i in range(8):
        Q[i] = ''
    head = -1
    tail = -1
    Qsize = 0
    Qlen = len(Q)

def Enqueue(data):
    global head, tail, Qsize, Qlen
    if Qsize == Qlen:
        print("Overflow. Queue is full.")
    else:
        if tail == Qlen -1: #tail at UB?
            tail = 0
        else:
            tail = tail + 1
        Q[tail] = data
        Qsize += 1

def Dequeue():
    global head, tail, Qsize, Qlen
    data = ''
    if Qsize == 0:
        print("Underflow. Queue is empty.")
    else:
        if head == Qlen -1: #head at UB?
            head = 0
        else:
            head = head + 1
        data = Q[head]
        Qsize -= 1
    return data

def displayQ():
    global head, tail, Qsize, Qlen
    print("\nQ = ", Q)
    print("Qlen = ", Qlen)
    print("Qsize = ", Qsize)
    print("head = ", head)
    print("tail = ", tail)

# main program
choice = 0
while choice != 5:
    print("\nMENU")
    print("1. Initialize Q")
    print("2. Enqueue")
    print("3. Dequeue")
    print("4. Display Q")
    print("5. Quit")
    choice = int(input("Enter your choice (1..5): "))
    if choice == 1:
        initQ()
    elif choice == 2:
        data = input("Enter data to enqueue: ")
        Enqueue(data)
    elif choice == 3:
        data = Dequeue()
        if data != '':
            print("Dequeued data = ", data)
    elif choice == 4:
        displayQ()
    elif choice == 5:
        print("Program terminated")
    else:
        print("Invalid choice. Try again.")
# end of program