"""
We are writing a python linear search code for the following pseudocode:
//Linear Search Algorithm

FUNCTION LinearSearch(arr[], Targ : INTEGER) RETURN INTEGER
   DECLARE n, result, count : INTEGER
   n ← LEN(arr)
   result ← -1

   FOR count ← 0 TO n-1
      IF arr[count] = Targ THEN
         result ← count
      ENDIF
   NEXT

   RETURN result
END FUNCTION

DECLARE arr : ARRAY [0:10] OF INTEGER
arr ← [25, 10, 5, 89, 24, 18, 45, 72, 31, 16, 87]

DECLARE val, x : INTEGER

OUTPUT "Enter a value to search for: "
INPUT val

x ← LinearSearch(arr, val)
IF x = -1 THEN
   OUTPUT "Value not found!"
ELSE
   OUTPUT "Value found at: " & x
ENDIF
"""
# python code for linear search

def LinearSearch(arr, Targ):
    n = len(arr)
    result = -1
    for count in range(0, n):
        if arr[count] == Targ:
            result = count
    return result

# main program
arr = [25, 10, 5, 89, 24, 18, 45, 72, 31, 16, 87]
val = int(input("Enter a value to search for: "))
x = LinearSearch(arr, val)
if x == -1:
    print("Value not found!")
else:
    print("Value found at: ", x)
# End of code
