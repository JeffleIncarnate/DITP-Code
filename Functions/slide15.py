def maximum(a, b, c):
    if (a >= b) and (a >= c): largest = a 
    elif (b >= a) and (b >= c): largest = b
    else: largest = c
    return largest

a = 10; b = 14; c = 12; print(maximum(a, b, c))

# ---------------------------------------

def sum_in_array(arraySum):
    total = 0
    for i in arraySum: total += i
    return total

arraySum = [10, 20, 304, 5, 6]
print(sum_in_array(arraySum))

# ---------------------------------------

def multiply_in_array(arrayMul):
    total = 1
    for i in arrayMul: total = total * i
    return total

arrayMul = [10, 20, 304, 5, 6]
print(multiply_in_array(arrayMul))

# ---------------------------------------

def reverse_string(revedString):
    return revedString[::-1]

print(reverse_string("Dhruv"))

# ---------------------------------------

def recur_factorial(n):
   if n == 1:
       return n
   else:
       return n*recur_factorial(n-1)

userInput = int(input("Enter num: "))

if userInput % 2 == 0:
    print(recur_factorial(userInput))
else:
    print("haha bad")