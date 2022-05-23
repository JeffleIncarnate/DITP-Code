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
