'''
3 Ejaz is creating a program that will allow the user to create quizzes. He is using object-oriented
programming (OOP).
There are two classes: QuestionClass and QuizClass.
The class attributes and methods are in the following tables. All attributes are declared as private.

QuestionClass
Attributes:
Question : STRING       // stores the question
Answer : STRING         // stores the correct answer
Difficulty : INTEGER    // stores the difficulty as an integer from 0(easy) to 10(hard)

Methods:
Constructor(QuestionP, AnswerP, DifficultyP)    // creates an instance of QuestionClass
                                                // sets the attributes to the parameter values
GetQuestion()                               // returns the question
GetDifficulty()                            // returns the difficulty level
GetAnswer()                                 // returns the answer


QuizClass
Attributes:
Questions : ARRAY OF QuestionClass    // stores the questions
NumberQuestions : INTEGER              // stores the number of questions in the quiz

Methods:
Constructor()                           // creates an instance of QuizClass
AddQuestion(QuestionP, AnswerP, DifficultyP) // adds a question to the quiz
GetQuestion(Number)                     // returns the question at the specified position
GetDifficulty(Number)                   // returns the difficulty level of the question at the specified position
'''

class QuestionClass:
    # DECLARE Question : STRING       // stores the question
    # DECLARE Answer : STRING         // stores the correct answer
    # DECLARE Difficulty : INTEGER    // stores the difficulty as an integer from 0(easy) to 10(hard)

    # constructor
    def __init__(self, QuestionP, AnswerP, DifficultyP):
        self.__Question = QuestionP         # __ dunder means private
        self.__Answer = AnswerP
        self.__Difficulty = DifficultyP

    # getters, also called accessors
    def GetQuestion(self):
        return self.__Question
    
    def GetDifficulty(self):
        return self.__Difficulty
    
    def GetAnswer(self):
        return self.__Answer

class QuizClass:
    # DECLARE Questions : ARRAY OF QuestionClass    // this is called aggregation
    # DECLARE NumberQuestions : INTEGER              // stores the number of questions in the quiz

    # constructor
    def __init__(self):
        self.__Questions = []    # empty array of questions. 
        self.__NumberQuestions = 0

    ''' adds a question to the quiz
    The QuizClass method AddQuestion() takes a question object as a parameter and stores
    it in the next available location in the array Questions. It returns TRUE if it is successfully
    stored, and FALSE otherwise.'''
    def AddQuestion(self, QuestionP, AnswerP, DifficultyP):
        if self.__NumberQuestions == 20:
            return False
        else:
            self.__Questions.append(QuestionClass(QuestionP, AnswerP, DifficultyP))
            self.__NumberQuestions += 1 
            return True
    
    # returns the question at the specified position
    def GetQuestion(self, Number):
        return self.__Questions[Number].GetQuestion()

    # returns the difficulty level of the question at the specified position
    def GetDifficulty(self, Number):
        return self.__Questions[Number].GetDifficulty()

'''(c) The first quiz is created with the identifier FirstQuiz.
The first question in this quiz is: “What is 100 / 5 ?”.
The answer is “20” and the difficulty level is 1.
Write program code to:
• declare an instance of QuizClass with the identifier FirstQuiz
• declare an instance of QuestionClass with the identifier Question1
• add Question1 to the array in FirstQuiz using AddQuestion().'''

FirstQuiz = QuizClass()
Question1 = QuestionClass("What is 100 / 5 ?", "20", 1)
FirstQuiz.AddQuestion(Question1.GetQuestion(), Question1.GetAnswer(), Question1.GetDifficulty())