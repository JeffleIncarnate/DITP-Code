rangeMin = 10; rangeMax = 20
def range(n):
    if n <= rangeMin: return 0
    elif n > rangeMax: return 0
    elif n == rangeMax or n == rangeMin: return 1 
    else: return 1

if range(15) == 1: print("It's in Range")
else: print("Not in Range")

# ---------------------------------------

upper = 0
lower = 0

def upper_lower(name):
    global upper, lower
    for i in name:
        if i.isupper():
            upper += 1
        else:
            lower += 1

upper_lower("Dhruv")
print("upper: {}, lower: {}".format(upper, lower))

# ---------------------------------------

def new_list(oldList):
    oldList = tuple(set(oldList))
    return oldList

t = (1, 1, 2, 3, 4, 5, 5)
print(new_list(t))

# ---------------------------------------

num = 8
prime = 0

def isPrime():
    global num, prime
    n = 1
    if num > 1:
        while n <= num:
            if num % n == 0:
                prime += 1
            n += 1
        if prime == 2:
            return True
        else:
            return False

print(isPrime())

# ---------------------------------------

evenList = []
evenOddList = [1, 2, 3, 4, 5, 6, 7, 7, 8, 8]

def printEven(evenOddList):
    for i in evenOddList:
        if i % 2 == 0:
            evenList.append(i)
    return evenList

print(printEven(evenOddList))

# ---------------------------------------