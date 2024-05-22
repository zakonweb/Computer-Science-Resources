'''
(b) A shop sells computer games. Each game has a unique identifier (ID) of string data type.
The text file QueueData.txt contains a list of game IDs.
The procedure ReadData() reads the data from the text file and inserts each item of data
into the array Queue.
Write program code for the procedure ReadData().
'''

def ReadData():
    # Initialize an empty list to store the game IDs
    Queue = ['' for i in range(50)]

    # array index starting from 0 and till 49, 50 elements
    i = 0

    try:
        # Open the file in read mode
        file = open('QueueData.txt', 'rt')

        # Read each line from the file
        for line in file:
            # Strip any leading/trailing whitespace and append to the Queue list
            game_id = line.strip()
            Queue[i] = game_id

            #  increase index by 1
            i += 1
        file.close()

    except FileNotFoundError:
        print("Error: QueueData.txt file not found.")
    return Queue

# Example usage
Queue = ReadData()
print(Queue)
