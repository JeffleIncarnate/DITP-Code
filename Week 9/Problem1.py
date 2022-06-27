numbers = []
i = 0

while i <= 60:
    if i == 53:
        numbers.append(353)
    
    numbers.append(i)
    i += 1

numbers.remove(53)

index = 0

for num in numbers:
    if num == 353:
        numbers.remove(num)
        numbers.insert(index, 53)
    index += 1

print(numbers)
