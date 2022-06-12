names = ["Marama", "Cheyenne", "Dyani"]

for i in names:
    print(i)

print("")

a = 21
for name in names:
    print("{} is {}".format(name, a))
    a -= 1


print("")

namesbigger = [
    ["Sally", "15"],
    ["Regina", "16"],
    ["Anne", "15"],
    ["Lila", "14"],
    ["Maleah", "16"],
]

for i in namesbigger:
    print(i)

print("")

for i in namesbigger:
    for nameAndAge in i:
        print(nameAndAge)

print("")

yes = ""
x = 0
for i in namesbigger:
    x = 0
    yes = ""
    for nameAndAge in i:
        if x == 0:
            yes = yes + nameAndAge + " is "
            x += 1
        elif x == 1:
            yes = yes + nameAndAge
            x += 1
            print(yes)
        else:
            continue
