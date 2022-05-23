def outer(a, b):
    def inner():
        return a + b;

    total = inner()
    return total + 5

sum = outer(10, 10)
print(sum)