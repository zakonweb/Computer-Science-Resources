#Serail file operation
#one field per line

import os

def addFieldWiseSer():
    sf = open("studentGAL.txt","at")

    stName = input("Enter name (Leave blank to end): ")
    while stName != "":
        stClass = input("Enter class: ")
        stFee = float(input("Enter fee: "))

        sf.write(stName + "\n")
        sf.write(stClass + "\n")
        sf.write(str(stFee) + "\n")

        stName = input("Enter name (Leave blank to end): ")

    sf.close()

def displayFieldWiseSer():
    try:
        sf = open("studentGAL.txt","rt")
        stName = sf.readline()
        while stName != "":
            stClass = sf.readline()
            stFee = sf.readline()

            print(stName.strip())
            print(stClass, end="")
            print(stFee)
            stName = sf.readline()

        sf.close()
    except:
        print("File doesn't exists...")

def searchFieldWiseSer():
    found = False # flag
    searchName = input("Enter name to search for: ")
    try:
        sf = open("studentGAL.txt","rt")
        stName = sf.readline()
        while stName != "":
            stClass = sf.readline()
            stFee = sf.readline()

            if searchName == stName.strip():
                found = True
                print(stName.strip())
                print(stClass, end='')
                print(stFee)
            stName = sf.readline()
        sf.close()
        if not found:
            print(searchName, "is not found...")
    except:
        print("File doesn't exists...")

def delFieldWiseSer():
    found = False
    searchName = input("Enter name to delete record: ")
    try:
        sf = open("studentGAL.txt","rt")
        tf = open("temp.txt","wt")

        stName = sf.readline()
        while stName != "":
            stClass = sf.readline()
            stFee = sf.readline()

            if searchName != stName.strip():
                tf.write(stName)
                tf.write(stClass)
                tf.write(stFee)
            else:
                found = True
            stName = sf.readline()
        sf.close()
        tf.close()
        if not found:
            print(searchName, "is not found...")
            os.remove("temp.txt")
        else:
            os.remove("studentGAL.txt")
            os.rename("temp.txt","studentGAL.txt")
    except:
        print("File doesn't exists...")

def editFieldWiseSer():
    found = False
    searchName = input("Enter name to edit record: ")
    try:
        sf = open("studentGAL.txt","rt")
        tf = open("temp.txt","wt")

        stName = sf.readline()
        while stName != "":
            stClass = sf.readline()
            stFee = sf.readline()

            if searchName != stName.strip():
                tf.write(stName)
                tf.write(stClass)
                tf.write(stFee)
            else:
                found = True
                print(stName, end='')
                print(stClass, end='')
                print(stFee)
                print("Now enter new data or enter blank to keep previous data.")
                sN = input("Enter updated name:")
                if sN == "":
                    sN = stName.strip()
                sC = input("Enter updated class:")
                if sC == "":
                    sC = stClass.strip()
                sF = input("Enter updated fee:")
                if sF == "":
                    sF = stFee.strip()
                tf.write(sN + "\n")
                tf.write(sC + "\n")
                tf.write(sF + "\n")
            stName = sf.readline()
        sf.close()
        tf.close()
        if not found:
            print(searchName, "is not found...")
            os.remove("temp.txt")
        else:
            os.remove("studentGAL.txt")
            os.rename("temp.txt","studentGAL.txt")
    except:
        print("File doesn't exists...")

def options():
    print("1. Add field wise record.")
    print("2. Read field wise record.")
    print("3. Search field wise record.")
    print("4. Delete field wise record.")
    print("5. Edit field wise record.")
    print("0. Quit.")
    opt = int(input("Enter the choice... "))
    return opt

# main program
opt = options()
while opt != 0:
    if opt == 1: addFieldWiseSer()
    if opt == 2: displayFieldWiseSer()
    if opt == 3: searchFieldWiseSer()
    if opt == 4: delFieldWiseSer()
    if opt == 5: editFieldWiseSer()
    opt = options()