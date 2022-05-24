multiplyListed = []
mulNum = 0
sampleList = [1, 2, 3, 4, 5 , 6]

def multiplyList(sampleList):
    for i in sampleList:
        mulNum = i * i
        multiplyListed.append(mulNum)
        mulNum = 0

    return multiplyListed

print(multiplyList(sampleList))

# ---------------------------------------
name = "dhruv123"

def revString(name):
    return name[::-1]

print(revString(name))

# ---------------------------------------

factorial = 10

def GetFact(n):
    global factorial 
    if n < 0:
        return "Factorial does not exist for negative numbers"
    elif n == 0:    
        return "The factorial of 0 is 1"
    else:
        for i in range(1, n + 1):   
            factorial = factorial*i  
        return factorial

print(GetFact(7))

# ---------------------------------------

def palendromeDef(string):
    revedString = string[::-1]

    if revedString == string:
        return True
    else:
        return False

print(palendromeDef("racecar"))

# ---------------------------------------
oneToThirty = []
squaredList = []

for i in range(0, 31):
    oneToThirty.append(i)

def squaredListFunc(oneToThirty):
    for i in oneToThirty:
        squaredList.append(i*i)
    return squaredList

print(squaredListFunc(oneToThirty))
