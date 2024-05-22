def unknown(x,y):
    if x<y:
        print(x+y)
        return unknown(x+1,y) * 2
    else:
        if x==y:
            return 1
        else:
            print(x+y)
            return unknown(x-1,y) // 2

def iterativeUnknown(x,y):
    n = 1
    while x != y:
        if x<y:
            print(x+y)
            x += 1
            n *= 2
        elif x>y:
            print(x+y)
            x -= 1
            n //= 2
    return n

print("x=10, y=15")
print(iterativeUnknown(10, 15)) 

print("x=10, y=10")
print(iterativeUnknown(10, 10)) 

print("x=15, y=10")
print(iterativeUnknown(15, 10))