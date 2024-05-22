"""
Pyhthon code for sequential text filing withfollowing fields: 
stuID as a key field, integer
stuName, string
stuClass, string
stuFee, real/float

following filie operations will be performed:
1. Add (append) new records
2. Display all records
3. Search for a record by ID
4. Delete a record by ID
5. Update a record by ID, where ID is the key field and it cannot be changed
"""

import os # for delete and edit file operations

def addRecord():
    sFile = open("studentBCCD23.txt", "at")
   
    stuID = 0
    stuID = int(input("Enter student ID. (Enter blank to exit.): ") or "0") # or 0 is to handle blank input
    while stuID != 0:
        stuName = input("Enter student name: ")
        stuClass = input("Enter student class: ")
        stuFee = float(input("Enter student fee: "))

        sFile.write(str(stuID) + "\n")
        sFile.write(stuName + "\n")
        sFile.write(stuClass + "\n")
        sFile.write(str(stuFee) + "\n")

        stuID = 0
        stuID = int(input("Enter student ID. (Enter blank to exit.) ") or "0")
    sFile.close()

def displayAll():
    sFile = open("studentBCCD23.txt", "rt")
    print("Student ID\tStudent Name\tStudent Class\tStudent Fee")
    print("------------------------------------------------------------")
    stuID = sFile.readline()
    while stuID != "":
        stuName = sFile.readline()
        stuClass = sFile.readline()
        stuFee = sFile.readline()

        stuID = stuID.strip()
        stuName = stuName.strip()
        stuClass = stuClass.strip()
        stuFee = stuFee.strip()

        print(stuID + "\t\t" + stuName + "\t\t" + stuClass + "\t\t" + stuFee)
        stuID = sFile.readline()
    sFile.close()

def searchRecord(): # Search for a record by ID
    found = False # flag variable

    searchID = input("Enter student ID to search: ")

    sFile = open("studentBCCD23.txt", "rt")
    stuID = sFile.readline()
    while stuID != "":
        stuName = sFile.readline()
        stuClass = sFile.readline()
        stuFee = sFile.readline()

        stuID = stuID.strip()
        stuName = stuName.strip()
        stuClass = stuClass.strip()
        stuFee = stuFee.strip()

        if stuID == searchID:
            print("Student ID\tStudent Name\tStudent Class\tStudent Fee")
            print("------------------------------------------------------------")
            print(stuID + "\t\t" + stuName + "\t\t" + stuClass + "\t\t" + stuFee)
            found = True
            break
        stuID = sFile.readline()
    if not found:
        print("Student ID not found.")
    sFile.close()

def deleteRecord(): # Delete a record by ID and using temp file
    found = False # flag variable

    searchID = input("Enter student ID to delete: ")

    sFile = open("studentBCCD23.txt", "rt")
    tempFile = open("temp.txt", "wt")

    stuID = sFile.readline()
    while stuID != "":
        stuName = sFile.readline()
        stuClass = sFile.readline()
        stuFee = sFile.readline()

        stuID = stuID.strip()
        if stuID != searchID:
            tempFile.write(stuID + "\n")
            tempFile.write(stuName)
            tempFile.write(stuClass)
            tempFile.write(stuFee)
        else:
            found = True
        stuID = sFile.readline()
    sFile.close()
    tempFile.close()

    os.remove("studentBCCD23.txt")
    os.rename("temp.txt", "studentBCCD23.txt")

    if found:
        print("Student ID deleted.")
    else:
        print("Student ID not found.")

def updateRecord(): # Update a record by ID, where ID is the key field and it cannot be changed
    found = False # flag variable

    searchID = input("Enter student ID to update: ")

    sFile = open("studentBCCD23.txt", "rt")
    tempFile = open("temp.txt", "wt")

    stuID = sFile.readline()
    while stuID != "":
        stuName = sFile.readline()
        stuClass = sFile.readline()
        stuFee = sFile.readline()

        stuID = stuID.strip()
        if stuID != searchID:
            tempFile.write(stuID + "\n")
            tempFile.write(stuName)
            tempFile.write(stuClass)
            tempFile.write(stuFee)
        else:
            found = True
            stuName = input("Enter student name: ")
            stuClass = input("Enter student class: ")
            stuFee = float(input("Enter student fee: "))

            tempFile.write(stuID + "\n")
            tempFile.write(stuName + "\n")
            tempFile.write(stuClass + "\n")
            tempFile.write(str(stuFee) + "\n")
        stuID = sFile.readline()
    sFile.close()
    tempFile.close()

    os.remove("studentBCCD23.txt")
    os.rename("temp.txt", "studentBCCD23.txt")

    if found:
        print("Student ID updated.")
    else:
        print("Student ID not found.")

# main menu and main program
choice = 0
while choice != 6:
    print("1. Add new records")
    print("2. Display all records")
    print("3. Search for a record by ID")
    print("4. Delete a record by ID")
    print("5. Update a record by ID")
    print("6. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        addRecord()
    elif choice == 2:
        displayAll()
    elif choice == 3:
        searchRecord()
    elif choice == 4:
        deleteRecord()
    elif choice == 5:
        updateRecord()
    elif choice == 6:
        print("Goodbye!")
    else:
        print("Invalid choice. Please try again.")
# end of program