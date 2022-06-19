num = int(input("Enter a number: ")); prime = 0
def isPrime():
    global num, prime; n = 1
    if num > 1:
        while n <= num:
            if num % n == 0: prime += 1
            n += 1
        if prime == 2: return True
        else: return False
print(isPrime())