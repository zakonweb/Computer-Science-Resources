'''9618/41/O/N/21
1 Study the following pseudocode for a recursive function.
FUNCTION Unknown(BYVAL X, BYVAL Y : INTEGER) RETURNS INTEGER
    IF X < Y THEN
        OUTPUT X + Y
        RETURN (Unknown(X + 1, Y) * 2)
    ELSE
        IF X = Y THEN
            RETURN 1
        ELSE
            OUTPUT X + Y
        RETURN (Unknown(X - 1, Y) DIV 2)
        ENDIF
    ENDIF
ENDFUNCTION
The operator DIV returns the integer value after division e.g. 13 DIV 2 would give 6
(a) Write program code to declare the function Unknown().
'''

def Unknown(X, Y):
    if X < Y:
        print(X + Y)
        return (Unknown(X + 1, Y) * 2)
    else:
        if X == Y:
            return 1
        else:
            print(X + Y)
            return (Unknown(X - 1, Y) // 2)
        
'''
(b) The main program needs to run all three of the following function calls and output the result
of each call:
Unknown(10, 15)
Unknown(10, 10)
Unknown(15, 10)
(i) For each of the three function calls, the main program needs to:
• output the value of the two parameters
• call the function with those parameters
• output the return value.
Write the program code for the main program.
'''
print('Unknown(10, 15):')
print(Unknown(10, 15))

print('Unknown(10, 10):')
print(Unknown(10, 10))

print('Unknown(15, 10):')
print(Unknown(15, 10))

# Rewrite the function Unknown() as an iterative function, IterativeUnknown().
def IterativeUnknown(X, Y):
    result = 1
    while X != Y:
        print(X + Y)
        if X < Y:
            result *= 2
            X += 1
        else:
            result //= 2
            X -= 1
    return result

print('IterativeUnknown(10, 15):')
print(IterativeUnknown(10, 15))

print('IterativeUnknown(10, 10):')
print(IterativeUnknown(10, 10))

print('IterativeUnknown(15, 10):')
print(IterativeUnknown(15, 10))
    