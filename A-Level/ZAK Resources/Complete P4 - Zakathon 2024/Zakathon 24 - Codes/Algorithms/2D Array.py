# 2D Array
cols, rows = 6, 6
x = [[None for i in range(cols)] for j in range(rows)]
y = [[0] * cols] * rows
n = 0
for i in range(6):
    for j in range(6):
        x[i][j] = 8
        n += 1

n = 0
for i in range(6):
    for j in range(6):
        y[i][j] = 0
        n += 1

x[3][4] = 9
print("\n 2D array X")
for i in range(6):
    for j in range(6):
        print(x[i][j], end = ' ')
    print()

y[3][4] = 5
print("\n\n 2D array Y")
for i in range(6):
    for j in range(6):
        print(y[i][j], end = ' ')
    print()



