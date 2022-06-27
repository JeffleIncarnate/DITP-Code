numbers = []
i = 0
index = 0

while i < 3:
    num  = float(input("Enter Flaot: "))    
    numbers.append(num)
    i += 1

for f in numbers:
    numbers.remove(f)
    f = f * 3
    numbers.insert(index, f)
    index += 1

print(numbers)