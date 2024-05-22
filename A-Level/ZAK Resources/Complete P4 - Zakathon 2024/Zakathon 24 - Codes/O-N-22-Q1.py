# Part 1(a)
# DECLARE DataArray : ARRAY [0:99] OF INTEGER
DataArray = [0 for i in range(100)]

# Part 1(b)
def ReadFile():
    try:
        file = open('IntegerData.txt', 'rt')
        lines = file.readlines()

        for i in range(100):
            # data retrieved from files is always text
            # we use int() to cast str line into integer.
            DataArray[i] = int(lines[i].strip())

        file.close()

    except FileNotFoundError:
        print("Error: The file was not found.")


# Part 1(c)
def FindValues():
    # range check validation
    number = int(input("Enter a number between 1 and 100: "))
    while not (1 <= number <= 100):   # number < 1 or number > 100  # not(number >= 1 and number <= 100)
        print("Please enter a number within the range 1 to 100.")
        number = int(input("Enter a number between 1 and 100: "))

    # count = DataArray.count(number)

    # linear search
    count = 0
    for value in DataArray:
        if value == number:
            count += 1
    return count