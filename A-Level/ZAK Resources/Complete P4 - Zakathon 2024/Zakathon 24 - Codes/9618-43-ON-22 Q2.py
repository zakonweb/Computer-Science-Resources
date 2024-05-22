'''9618/43/O/N/22 Q2
A computer program is being developed that uses a set of cards. The program is written using
object-oriented programming.
The program has two classes: Card and Hand.
The methods and attributes of these classes are shown:

Card class
Attributes (all private):
Number : INTEGER    # stores the card number from 1 to 5 inclusive
Colour : STRING     # stores the card colour: red, blue or yellow

# Methods
Constructor()   # initialises Number and Colour to its parameter values
GetNumber()     # returns the card number
GetColour()     # returns the card colour

Hand class
Attributes (all private):
Aggregation of Card objects
Cards : ARRAY[0:9] OF Card  # 1D array of type Card that stores the cards in the hand

FirstCard : INTEGER # stores the position of the first card in the hand
NumberCards : INTEGER   # stores the number of cards in the hand

Methods:
Constructor takes five card objects as parameters, assigns each card to the array Cards[], initialises FirstCard to 0 and NumberCards to 5
Constructor()

takes an index as a parameter and returns the card at that index in the array
GetCard()
'''

class Card:
    # Attributes
    # PRIVATE Number : INTEGER    # stores the card number from 1 to 5 inclusive
    # PRIVATE Colour : STRING     # stores the card colour: red, blue or yellow

    def __init__(self, Number, Colour):
        self.__Number = Number
        self.__Colour = Colour
    
    # Methods
    def GetNumber(self):
        return self.__Number

    def GetColour(self):
        return self.__Colour

'''The program is tested with the following cards:
Number Colour
1 red
2 red
3 red
4 red
5 red
1 blue
2 blue
3 blue
4 blue
5 blue
1 yellow
2 yellow
3 yellow
4 yellow
5 yellow
Write program code to declare each of these cards as a variable of type Card in the main program.'''

# Create the cards
Card1 = Card(1, "red")
Card2 = Card(2, "red")
Card3 = Card(3, "red")
Card4 = Card(4, "red")
Card5 = Card(5, "red")
Card6 = Card(1, "blue")
Card7 = Card(2, "blue")
Card8 = Card(3, "blue")
Card9 = Card(4, "blue")
Card10 = Card(5, "blue")
Card11 = Card(1, "yellow")
Card12 = Card(2, "yellow")
Card13 = Card(3, "yellow")
Card14 = Card(4, "yellow")
Card15 = Card(5, "yellow")

'''Write program code to declare the class Hand, its attributes and constructor.
The constructor should take the five card objects as parameters, assign each card to the array Cards[], initialise FirstCard to 0 and NumberCards to 5.'''

class Hand:
    # Attributes
    # PRIVATE Aggregation of Card objects
    # PRIVATE Cards : ARRAY[0:9] OF Card  # 1D array of type Card that stores the cards in the hand

    # PRIVATE FirstCard : INTEGER # stores the position of the first card in the hand
    # PRIVATE NumberCards : INTEGER   # stores the number of cards in the hand

    def __init__(self, Card1, Card2, Card3, Card4, Card5):
        self.__Cards = [Card1, Card2, Card3, Card4, Card5]
        self.__FirstCard = 0
        self.__NumberCards = 5

    # Methods
    def GetCard(self, index):
        return self.__Cards[index]
    
'''Two players are declared with 5 cards each.
Player 1 has the cards: 1 red, 2 red, 3 red, 4 red, 1 yellow.
Player 2 has the cards: 2 yellow, 3 yellow, 4 yellow, 5 yellow, 1 blue.
Write program code to declare player 1 and player 2 as objects of type Hand, with the cards indicated.'''
Player1 = Hand(Card1, Card2, Card3, Card4, Card11)
Player2 = Hand(Card12, Card13, Card14, Card15, Card6)

'''The function CalculateValue() takes a player's hand as a parameter and returns a score
calculated using the following rules:
• If a card is red, 5 points are added to the player's score.
• If a card is blue, 10 points are added to the player's score.
• If a card is yellow, 15 points are added to the player's score.
• The number of each card in the hand is added to the player's score.
(i) Write program code for the function CalculateValue().
Assume that there are only 5 cards in the player's hand in this function.'''
def CalculateValue(Player):
    Score = 0
    for i in range(5):
        if Player.GetCard(i).GetColour() == "red":
            Score += 5
        elif Player.GetCard(i).GetColour() == "blue":
            Score += 10
        elif Player.GetCard(i).GetColour() == "yellow":
            Score += 15
        Score += Player.GetCard(i).GetNumber()
    return Score

'''Amend the main program by writing program code to use the function
CalculateValue() for each of the two players. The player with the highest score wins.
Output an appropriate message to identify the winning player, or if the game was a draw
(both players have the same number of points).'''
Player1Score = CalculateValue(Player1)
Player2Score = CalculateValue(Player2)

if Player1Score > Player2Score:
    print("Player 1 wins")
elif Player2Score > Player1Score:
    print("Player 2 wins")
else:   # Draw
    print("It's a draw")