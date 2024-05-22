#  Direct access binary file

def createSeqBinaryFile():
    stuFile = open('students_sequential.dat', 'wb')

    id = input("Enter unique ID (0 to exit): ")
    while id != '0':
        stuName = input("Enter student name: ")
        newRecord = id + '*' + stuName
        newRecord = newRecord.ljust(30, ' ')  # left justify with space padding to make it width 30
        stuFile.write(newRecord.encode())  # Encode the string to bytes

        id = input("Enter unique ID (0 to exit): ")

    stuFile.close()
# Run the function to create the file
# createSeqBinaryFile()

def search_by_id():
    # input search ID
    search_id = input("Enter ID: ")

    # Define the fixed length for each line
    fixed_length = 30

    # Calculate the position of the record
    record_number = int(search_id) - 1  # Convert ID to zero-based index
    position = record_number * fixed_length

    # Open the file in read mode
    file = open('students_sequential.dat', "rb")
    # Seek to the position of the record
    file.seek(position)

    # Read the fixed length record
    line = file.read(fixed_length)

    if not line:
        print(f"ID:{search_id} not found.")
    else:
        # Decode the bytes to a string
        line = line.decode()
        id, name = line.strip().split('*')
        print(f"ID: {id}, Name: {name}")
        print("ID: " + id + ", Name: " + name)

search_by_id()
