values = []
total = 0
avnum = 0

def loop():
    global values, total, avnum
    if len(values) == 3:
        for i in values:
            total += i
        avnum = total / len(values)
        return avnum
    else:
        x = int(input("Please enter a number: "))
        values.append(x)
        loop()

loop()

print(avnum)