'''
# this can't be a serial file
# this has to be a sequential file
1*ali                         |25    0   3*25=75-1
2*zafar                       |50    25+1
3*ahmed                       |75    50+1   (3-1)*25=50
4*abdul rehman                |100
5*muhammad raza ali khan      |125
'''

def createSeqFile():
    stuFile = open('studentFile.txt', 'wt')

    id = input("Enter unique ID (0 to exit): ")
    while id != '0':
        stuName = input("Enter student name: ")
        newRecord = id + '*' + stuName    #.ljust(25) + '\n'
        newRecord = newRecord.ljust(25)  # left justify with space padding to make it width 25
        newRecord = newRecord + '\n'

        stuFile.write(newRecord)
        id = input("Enter unique ID (0 to exit): ")

    stuFile.close()

def readSeqFile():
    try:
        file = open('studentFile.txt', 'rt')

        for thisLine in file:
            # print(repr(thisLine))

            id, name = thisLine.strip().split('*')
            print('ID:', id)
            print('Name:', name)

        file.close()
    except:
        print("File error occured.")

def searchSeqFile():  # direct access
    fixed_length = 25
    x = input("Enter ID to search: ")
    found = False

    #  calculate record number
    position = (int(x)-1) * fixed_length

    try:
        file = open('studentFile.txt', 'rt')
        file.seek(position)
        thisLine = file.read(fixed_length)

        if not thisLine:
            print(f'ID:{x}, could not found!')
        else:
            id, name = thisLine.strip().split('*')
            print('ID:', id)
            print('Name:', name)
        file.close()

    except:
        print("File error occured.")

# createSeqFile()
#readSeqFile()
searchSeqFile()
