'''
This iterative pseudocode algorithm for the function IterativeVowels() takes a string as a
parameter and counts the number of lower-case vowels in this string.
The vowels are the letters a, e, i, o and u.
FUNCTION IterativeVowels(Value : STRING) RETURNS INTEGER
    DECLARE Total : INTEGER
    DECLARE LengthString : INTEGER
    DECLARE FirstCharacter : CHAR
    Total ← 0
    LengthString ← LENGTH(Value)
    FOR X ← 0 TO LengthString - 1
        FirstCharacter ← MID(Value, 0, 1)
        IF FirstCharacter = 'a' OR FirstCharacter = 'e' OR
            FirstCharacter = 'i' OR FirstCharacter = 'o' OR
            FirstCharacter = 'u' THEN
            Total ← Total + 1
        ENDIF
        Value ← MID(Value, 1, LENGTH(Value)-1)
    NEXT X
    RETURN Total
ENDFUNCTION
The pseudocode function MID(X, Y, Z) returns Z number of characters from string X, starting
at the character in position Y. The first character in a string is in position 0, for example:
MID("computer", 0, 3) returns "com"
The pseudocode function LENGTH(X) returns the number of characters in the string X, for
example:
LENGTH("computer") returns 8'''

# (i) Write program code for the function IterativeVowels().
def IterativeVowels(Value):
    # DECLARE Total : INTEGER
    # DECLARE LengthString : INTEGER
    # DECLARE FirstCharacter : CHAR

    Total = 0
    LengthString = len(Value)

    for x in range(LengthString):
        FirstCharacter = Value[0]
        #if FirstCharacter in ['a', 'e', 'i', 'o', 'u']:
        if FirstCharacter == 'a' or FirstCharacter == 'e' or FirstCharacter == 'i' or FirstCharacter == 'o' or FirstCharacter == 'u':
            Total += 1
        Value = Value[1:]
    return Total

'''
(ii) Write program code to call the function IterativeVowels() with the parameter
"house" from the main program.
Output the return value.'''

# print(IterativeVowels("house")) # 3

#(b) (i) Rewrite the function IterativeVowels() as a recursive function with the identifier RecursiveVowels().
def RecursiveVowels(Value):
    if Value == "":  # Base case
        return 0
    else: # Recursive case
        FirstCharacter = Value[0]
        if FirstCharacter == 'a' or FirstCharacter == 'e' or FirstCharacter == 'i' or FirstCharacter == 'o' or FirstCharacter == 'u':
            return 1 + RecursiveVowels(Value[1:])
        else:
            return RecursiveVowels(Value[1:])

# ii) Write program code to call the function RecursiveVowels() with the parameter "imagine" from the main program.

print(RecursiveVowels("imagine")) #4