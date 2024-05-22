# 9618/41/O/N/23 Q2
'''A linear queue is implemented using the 1D array, Queue. 
The index of the first element in the array is 0.
(a) (i) Write program code to declare:
• Queue — a global array with space to store 50 IDs of type string
• HeadPointer — a global variable to point to the first element in the queue,
initialised to -1
• TailPointer — a global variable to point to the next available space in the queue,
initialised to 0.'''
# global variables
Queue = ['' for i in range(50)]
HeadPointer = -1
TailPointer = 0

'''Some game IDs appear in the text file more than once.
The program needs to total the number of times each game ID appears in the text file.
The record structure RecordData has the following fields:
• ID — a string to store the game ID
• Total — an integer to store the total number of times that game ID appears in the text
file.
(i) Write program code to declare the record structure RecordData.
If you are writing in Python, include attribute declarations as comments.'''
# record structure
class RecordData:
    # attributes
    # DECLARE ID : STRING
    # DECLARE Total : INTEGER
    def __init__(self):
        self.ID = ''
        self.Total = 0


'''The global 1D array Records stores up to 50 items of type RecordData.
The global variable NumberRecords stores the number of records currently in the array
Records and is initialised to 0.
Write program code to declare Records and NumberRecords.
If you are writing in Python, include attribute declarations as comments.'''
# global variables
# DECLARE Records : ARRAY[1:50] OF RecordData
# DECLARE NumberRecords : INTEGER
Records = [RecordData() for i in range(50)]
NumberRecords = 0


'''The procedure Enqueue() takes a string parameter.
If the queue is full, the procedure outputs a suitable message. If the queue is not full, the
procedure inserts the parameter into the queue and updates the relevant pointer(s).
Write program code for Enqueue().'''
def Enqueue(x):
    global TailPointer
    if TailPointer == 50:
        print("Queue is full")
    else:
        Queue[TailPointer] = x
        TailPointer += 1

'''The function Dequeue() checks if the queue is empty.
If the queue is empty, the function outputs a suitable message and returns the string "Empty".
If the queue is not empty, the function returns the first element in the queue and updates
the relevant pointer(s).
Write program code for Dequeue().'''
def Dequeue():
    global HeadPointer
    if HeadPointer == TailPointer -1:
        print("Queue is empty")
        return "Empty"
    else:
        HeadPointer += 1
        return Queue[HeadPointer]

'''
A shop sells computer games. Each game has a unique identifier (ID) of string data type.
The text file QueueData.txt contains a list of game IDs.
The procedure ReadData() reads the data from the text file and inserts each item of data
into the array Queue.
Write program code for the procedure ReadData().
Don't use with statement, instead use open and close file methods
'''
def ReadData():
    try:
        file = open("QueueData.txt", "rt")
        for line in file:
            Enqueue(line.strip())
        file.close()
    except:
        print("File not found")

'''The pseudocode algorithm for the procedure TotalData():
• uses Dequeue() to remove an ID from the queue
• checks whether a RecordData with the returned ID exists in Records
• increments the total for that ID in the record if the ID already exists
• creates a new record and stores it in Records if the ID does not exist.
PROCEDURE TotalData()
    DECLARE DataAccessed : STRING
    DECLARE Flag : BOOLEAN
    DataAccessed ← Dequeue()
    Flag ← FALSE
    IF NumberRecords = 0 THEN
        Records[NumberRecords].ID ← DataAccessed
        Records[NumberRecords].Total ← 1
        Flag ← TRUE
        NumberRecords ← NumberRecords + 1
    ELSE
        FOR X ← 0 TO NumberRecords - 1
            IF Records[X].ID = DataAccessed THEN
                Records[X].Total ← Records[X].Total + 1
                Flag ← TRUE
            ENDIF
        NEXT X
    ENDIF
    IF Flag = FALSE THEN
        Records[NumberRecords].ID ← DataAccessed
        Records[NumberRecords].Total ← 1
        NumberRecords ← NumberRecords + 1
    ENDIF
ENDPROCEDURE
Write program code for the procedure TotalData().'''

def TotalData():
    global NumberRecords
    DataAccessed = Dequeue()
    Flag = False
    if NumberRecords == 0:
        Records[NumberRecords].ID = DataAccessed
        Records[NumberRecords].Total = 1
        Flag = True
        NumberRecords += 1
    else:
        for X in range(NumberRecords):
            if Records[X].ID == DataAccessed:
                Records[X].Total += 1
                Flag = True
    if Flag == False:
        Records[NumberRecords].ID = DataAccessed
        Records[NumberRecords].Total = 1
        NumberRecords += 1

'''The procedure OutputRecords() outputs the ID and total of each record in Records in the
format:
ID 1234 Total 4
Write program code for OutputRecords().'''
def OutputRecords():
    for i in range(NumberRecords):
        print(f"ID {Records[i].ID} Total {Records[i].Total}")

'''(e) The main program needs to:
• call ReadData()
• call TotalData() for each element in the queue
• call OutputRecords().
(i) Write program code for the main program.'''
# Main Program
ReadData()
while HeadPointer < TailPointer - 1:
    TotalData()
OutputRecords()