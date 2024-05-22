# 9618/42/M/J/21 Q3
''''3 A computer game requires users to travel around a world to find and open treasure chests. Each
treasure chest has a mathematics question inside. The user enters the answer. The number of
points awarded depends on the number of attempts before the user gives the correct answer.
The program will be created using object-oriented programming (OOP).
The following class diagram describes the class TreasureChest.

TreasureChest
// stores the question
question : STRING

// stores the answer
answer : INTEGER

// stores the maximum possible number of points available for this chest
points : INTEGER

Methods:
// takes question, answer and points as parameters and creates an instance of an object
constructor()

// returns the question
getQuestion()

// takes the user's answer as a parameter and returns True if it is correct, otherwise returns False
checkAnswer()

// takes the number of attempts as a parameter and returns the number of points awarded
getPoints()


(a) Create a new program.
Write program code to declare the class TreasureChest.
Do not write any other methods.
The attributes are private.
If you are using the Python programming language, include attribute declarations using comments.
'''

class TreasureChest:
    # private attributes
    # PRIVATE question : STRING
    # PRIVATE answer : INTEGER
    # PRIVATE points : INTEGER

    def __init__(self, question, answer, points):
        self.__question = question
        self.__answer = answer
        self.__points = points

    '''The main program repeats each question until the user inputs the correct answer. The
    number of points awarded depends on the number of attempts before the user gives the
    correct answer.
    (i) The class TreasureChest has a method getQuestion() that returns the question.
    Write the method getQuestion().'''
    def getQuestion(self):
        return self.__question

    '''The class TreasureChest has a method checkAnswer() that takes the user’s
    answer as a parameter. It returns True if the answer is correct and False otherwise.
    Write the method checkAnswer()'''
    def checkAnswer(self, userAnswer):
        return userAnswer == self.__answer

    '''The class TreasureChest has a method getPoints() that takes the number of
    attempts as a parameter.
    • If the number of attempts is 1, it returns the value of points.
    • If the number of attempts is 2, it returns the integer value of points divided by
    2 (DIV 2).
    • If the number of attempts is 3 or 4, it returns the integer value of points divided by
    4 (DIV 4).
    • If the number of attempts is not 1 or 2 or 3 or 4, it returns 0 (zero).
    For example, a question is worth 100 points and the user took 2 attempts to give the
    correct answer. The user is awarded 50 points (100 DIV 2).
    Write the method getPoints().'''
    def getPoints(self, attempts):
        if attempts == 1:
            return self.__points
        elif attempts == 2:
            return self.__points // 2       # // is integer division, % is modulus
        elif attempts == 3 or attempts == 4:
            return self.__points // 4
        else:
            return 0

'''The text file TreasureChestData.txt stores data for five questions, in the order of
question, answer, points.
For example, the first three lines of the file are for the first question:
2*2 question
4 answer
10 points
Write program code for the procedure, readData() to:
• read each question, answer and points from the text file
• create an object of type TreasureChest for each question
• declare an array named arrayTreasure of type TreasureChest
• append each object to the array
• use exception handling to output an appropriate message if the file is not found.'''

def readData():
    arrayTreasure = []
    try:
        file = open("TreasureChestData.txt", "rt")
        data = file.readlines()
        for i in range(0, len(data), 3):
            question = data[i].strip()
            answer = int(data[i+1].strip())
            points = int(data[i+2].strip())
            arrayTreasure.append(TreasureChest(question, answer, points))
        file.close()
    except FileNotFoundError:
        print("File not found")
    return arrayTreasure


'''Write program code for the main program to:
• call the procedure readData()
• ask the user to enter a question number between 1 and 5
• output the question that matches the question number entered by the user
• check if the answer input by the user is correct using the method checkAnswer()
• repeat the question until the user inputs the correct answer
• count how many times the user attempted the question
• use the method getPoints() to return the number of points awarded
• output the number of points the user is awarded.'''

attempts = 0

questions = readData()
questionNumber = int(input("Enter a question number between 1 and 5: "))
question = questions[questionNumber - 1]
print(question.getQuestion())
userAnswer = int(input("Enter your answer: "))
attempts += 1
while not question.checkAnswer(userAnswer):
    userAnswer = int(input("Enter your answer: "))
    attempts += 1
points = question.getPoints(attempts)
print(f"Points awarded: {points}")