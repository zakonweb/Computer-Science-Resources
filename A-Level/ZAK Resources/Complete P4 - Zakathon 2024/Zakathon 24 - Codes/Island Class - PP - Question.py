"""
Python version for the following Island class pseudocode:

Class IslandClass()
   //Attribute
   PRIVATE Grid : ARRAY[0:9, 0:29] OF CHAR

   CONSTANT Treasure ← 'T'
   CONSTANT Treasure_Found ← 'X'
   CONSTANT Treasure_NOT_FOUND ← 'O'
   CONSTANT Sand ← '.'

   PUBLIC PROCEDURE NEW()
      DECLARE row, col : INTEGER
      FOR row = 0 TO 9
         FOR col = 0 TO 29
           Grid[row, col] = Sand
         NEXT col
      NEXT row
   END PROCEDURE

   PUBLIC PROCEDURE HideTrasure()
      DECLARE row, col : INTEGER
      
      WHILE TRUE
         row = RANDOM(0,29)
         col = RANDOM(0,9)
         IF Grid[row,col] = Sand THEN
            Grid[row,col] = Treasure
            EXIT LOOP
         END IF
      ENDWHILE
  END PROCEDURE

  PUBLIC PROCEDURE DigHole(Row : INTEGER, Column : INTEGER)
      IF Grid[Row, Column] = Treasure THEN
         Grid[Row, Column] = Treasure_FOUND
      ELSE
         Grid[Row, Column] = Treasure_NOT_FOUND
      ENDIF
  END PROCEDURE

  PUBLIC FUNCTION GetSquare(Row : INTEGER, Column INTEGER) RETURNS CHARACTER
     RETURN Grid[Row, Column]
  END FUNCTION
END CLASS
"""
class IslandClass:
    def __init__(self):
        self.__treasure = 'T'
        self.__treasure_found = 'X'
        self.__treasure_not_found = 'O'
        self.__sand = '.'
        self.__grid = [[self.__sand for col in range(30)] for row in range(10)]

    def hide_treasure(self):
        import random

        while True:
            row = random.randint(0, 9)
            col = random.randint(0, 29)
            if self.__grid[row][col] == self.__sand:
                self.__grid[row][col] = self.__treasure
                break

    def dig_hole(self, row, col):
        if self.__grid[row][col] == self.__treasure:
            self.__grid[row][col] = self.__treasure_found
        else:
            self.__grid[row][col] = self.__treasure_not_found

    def get_square(self, row, col):
        return self.__grid[row][col]

"""
python code for the following TreasureHunt class pseudocode:
//Main Program
Island ← NEW IslandClass() // instantiate object

PROCEDURE DisplayGrid()
   DECLARE row, col : INTEGER
      
   FOR row = 0 TO 9
      FOR col = 0 TO 29
         OUTPUT Island.GetSquare(row,col) //Same line
      NEXT
      // New Line
   NEXT
END PROCEDURE

PROCEDURE StartDig()
   DECLARE row, col : INTEGER
   
   REPEAT //VALIDATING Row 
      INPUT "Enter row between 0-9: ", row
   UNTITL row >=0 AND row <=9

   REPEAT //VALIDATING Col 
      INPUT "Enter col between 0-29: ", col
   UNTITL col >=0 AND col <=29

   CALL Island.DigHole()
END PROCEDURE

DECLARE Treasure : INTEGER
CALL DisplayGrid() // output island squares
FOR Treasure ← 1 TO 3 // hide 3 treasures
   CALL Island.HideTreasure()
ENDFOR
CALL StartDig() // user to input location of dig
CALL DisplayGrid() // output island squares
"""
Island = IslandClass() # instantiate object 

def DisplayGrid():
    for row in range(10):
        for col in range(30):
            print(Island.get_square(row, col), end='')
        print()

def StartDig():
    while True:
        row = int(input("Enter row between 0-9: "))
        if row >= 0 and row <= 9:
            break

    while True:
        col = int(input("Enter col between 0-29: "))
        if col >= 0 and col <= 29:
            break

    Island.dig_hole(row, col)

Treasure = 0
DisplayGrid() # output island squares
for Treasure in range(1, 4): # hide 3 treasures
    Island.hide_treasure()
StartDig() # user to input location of dig
DisplayGrid() # output island squares
# END OF PROGRAM