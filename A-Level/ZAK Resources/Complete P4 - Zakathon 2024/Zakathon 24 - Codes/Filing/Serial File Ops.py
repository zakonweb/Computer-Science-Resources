"""
Serial and Sequential filing.
Serial file has chronological (Time) order of data.
Sequential file has logical (Key) order of data.
Both are text files.
"""
# inserting the data in the serial file
# w for write mode, a for append mode
# t for text file, b for binary file

def insert_serial_file():
    student_data = open("student_data.txt", "wt")
    stu_name = input("Enter student name. Leave blank to end: ")
    while stu_name != "":
        stu_marks = int(input("Enter student marks: "))
        stu_fee = float(input("Enter student fee: "))

        student_data.write(stu_name + "\n")
        student_data.write(str(stu_marks) + "\n")
        student_data.write(str(stu_fee) + "\n")

        stu_name = input("Enter student name. Leave blank to end: ")
    student_data.close()

# reading the data from the serial file
# r for read mode
# exception handling will be used to give file not found error
# and avoid program crash run time error
def read_serial_file():
    try:
        student_data = open("student_data.txt", "rt")
        stu_name = student_data.readline().strip()
        while stu_name != "":
            stu_marks = int(student_data.readline())
            stu_fee = float(student_data.readline())

            print("Student Name: ", stu_name)
            print("Student Marks: ", stu_marks)
            print("Student Fee: ", stu_fee)
            print()

            stu_name = student_data.readline().strip()
        student_data.close()
    except:
        print("File not found. Please insert data first.")

def search_serial_file():
    try:
        student_data = open("student_data.txt", "rt")
        Found = False # Flag
        search_name = input("Enter student name to search: ")

        stu_name = student_data.readline().strip()
        while stu_name != "":
            stu_marks = int(student_data.readline())
            stu_fee = float(student_data.readline())

            if stu_name == search_name:
                print("Student Name: ", stu_name)
                print("Student Marks: ", stu_marks)
                print("Student Fee: ", stu_fee)
                Found = True
                break
            stu_name = student_data.readline().strip()
        student_data.close()
        if not Found:
            print("Student not found.")
    except:
        print("File not found. Please insert data first.")

def sequential_file_insert():
    seqFile = open("seqFile.txt", "wt")
    stuID = int(input("Enter student ID. Enter 0 to end: "))
    while stuID != 0:
        stu_name = input("Enter student name: ")
        stu_marks = int(input("Enter student marks: "))
        stu_fee = float(input("Enter student fee: "))

        seqFile.write(str(stuID) + "\n")
        seqFile.write(stu_name + "\n")
        seqFile.write(str(stu_marks) + "\n")
        seqFile.write(str(stu_fee) + "\n")

        stuID = int(input("Enter student ID. Leave blank to end: "))
    seqFile.close()

def sequential_file_read():
    try:
        seqFile = open("seqFile.txt", "rt")
        stuID = seqFile.readline().strip()
        while stuID != "":
            stu_name = seqFile.readline().strip()
            stu_marks = int(seqFile.readline())
            stu_fee = float(seqFile.readline())

            print("Student ID: ", stuID)
            print("Student Name: ", stu_name)
            print("Student Marks: ", stu_marks)
            print("Student Fee: ", stu_fee)

            stuID = seqFile.readline().strip()
        seqFile.close()
    except:
        print("File not found. Please insert data first.")

def search_sequential_file():
    try:
        seqFile = open("seqFile.txt", "rt")
        Found = False
        searchID = int(input("Enter student ID to search: "))

        stuID = seqFile.readline().strip()
        while stuID != "":
            stu_name = seqFile.readline().strip()
            stu_marks = int(seqFile.readline())
            stu_fee = float(seqFile.readline())

            if int(stuID) == searchID:
                print("Student ID: ", stuID)
                print("Student Name: ", stu_name)
                print("Student Marks: ", stu_marks)
                print("Student Fee: ", stu_fee)
                Found = True
                break
            if int(stuID) > searchID:
                break
            stuID = seqFile.readline().strip()
        seqFile.close()
        if not Found:
            print("Student not found.")
    except:
        print("File not found. Please insert data first.")

# main program menu
choice = 0
while choice != 7:
    print("1. Insert data in serial file.")
    print("2. Read data from serial file.")
    print("3. Search data in serial file.")
    print("4. Insert data in sequential file.")
    print("5. Read data from sequential file.")
    print("6. Search data in sequential file.")
    print("7. Exit.")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        insert_serial_file()
    elif choice == 2:
        read_serial_file()
    elif choice == 3:
        search_serial_file()
    elif choice == 4:
        sequential_file_insert()
    elif choice == 5:
        sequential_file_read()
    elif choice == 6:
        search_sequential_file()
    elif choice == 7:
        print("Program ended.")
    else:
        print("Invalid choice. Please enter again.")










