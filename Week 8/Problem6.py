names = []

i = 1

while i < 6:
    name = input("Enter the winners name for race {}: ".format(i))
    names.append(name)

    print(name)
    name = ""
    i += 1
