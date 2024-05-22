'''9618/43/M/J/22
2 A computer game is being developed using object-oriented programming.
One element of the game is a balloon. This is designed as the class Balloon.
The class has the following attributes and methods.
Balloon
Health : INTEGER
Colour : STRING
DefenceItem : STRING
The health of the balloon
The colour of the balloon
The item the balloon uses to defend itself
Constructor()
ChangeHealth()
GetDefenceItem()
CheckHealth()
Initialises the defence item and colour using the
parameters
Initialises health to 100
Takes the change as a parameter and adds this to the
health
Returns the defence item of the object
If the health is 0 or less, it returns TRUE, otherwise it
returns FALSE
(a) The constructor takes the name of the defence item and the balloon’s colour as parameters
and sets these to the attributes. The health is initialised to 100.
Write program code to declare the class Balloon and its constructor. Do not write any other
methods.
Use your language appropriate constructor.
All attributes should be private. If you are writing in Python include attribute declarations using
comments.
'''
class Balloon:
    # Attributes
    # PRIVATE Health : INTEGER
    # PRIVATE Colour : STRING
    # PRIVATE DefenceItem : STRING

    def __init__(self, Colour, DefenceItem):
        self.__Health = 100
        self.__Colour = Colour
        self.__DefenceItem = DefenceItem
    
    '''The get method GetDefenceItem() returns the defence item of the object.
    Amend your program code to include the get method GetDefenceItem().'''
    def GetDefenceItem(self):
        return self.__DefenceItem
    
    '''The object's method ChangeHealth() takes an integer number as a parameter and adds
    this to the health attribute of the object.
    Amend your program code to include the method ChangeHealth().'''
    def ChangeHealth(self, change):
        self.__Health += change
    

    '''The object's method CheckHealth() returns TRUE if the health of the object is 0 or less (no
    health remaining) and returns FALSE otherwise (health remaining).
    Amend your program code to include the method CheckHealth().'''
    def CheckHealth(self):
        return self.__Health <= 0

'''Amend the main program to:
• take as input a defence item and colour from the user
• create a new balloon with the identifier Balloon1 using the data input.'''
baloonColour = input("Enter the colour of the baloon: ")
defenceItem = input("Enter the defence item: ")
Balloon1 = Balloon(baloonColour, defenceItem)

'''The function Defend():
• takes a balloon object as a parameter
• takes as input the strength of an opponent from the user
• uses the ChangeHealth() method to subtract the strength input from the object's health
• outputs the defence item of the balloon
• checks the health of the object and outputs an appropriate message if it has no health
remaining, or if it has health remaining
• returns the amended balloon object.
Write program code to declare the function Defend().'''

def Defend(balloon):
    strength = int(input("Enter the strength of the opponent: ")) # Taking the positive strength of the opponent
    balloon.ChangeHealth(-strength) # Subtracting the strength of the opponent
    print("The defence item of the baloon is: ", balloon.GetDefenceItem())
    if balloon.CheckHealth():
        print("The balloon has no health remaining")
    else:
        print("The balloon has health remaining")
    return balloon

#(g) (i) Amend the main program to call the function Defend().
#Balloon1 = Defend(Balloon1)

'''(ii) Test your program using the following inputs:
• balloon defence method "Shield"
• balloon colour "Red"
• strength of opponent 50
Take a screenshot to show the output.'''
# Output:
# Enter the colour of the baloon: Red
# Enter the defence item: Shield
# Enter the strength of the opponent: 50
# The defence item of the baloon is:  Shield
# The balloon has health remaining

Balloon2 = Balloon("Red", "Shield")
Balloon2 = Defend(Balloon2)
