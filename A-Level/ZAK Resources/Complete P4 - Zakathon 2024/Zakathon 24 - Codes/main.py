#  Python file handling
#  text files
try:  # exception handling
    file = open('StuData.txt', 'at')  # appending
    x = input("Enter student name: ")
    while x != '':  # enter empty string to terminate the loop
        file.write(x + '\n')
        x = input("Enter student name: ")
    file.close()
except FileNotFoundError:
    print('File not found or some other error in the file.')
except Exception as e:
    print("An unexpected error occurred while reading the student file: " + e)
else:
    print("File read successfully.")

#  program continues from here
