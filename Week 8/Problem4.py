personATotal = 0
personBTotal = 0

for i in range(1, 3 + 1):
    print("Round {}".format(i))
    personA = int(input("Enter score for Player A: "))
    personB = int(input("Enter score for Player B: "))

    personATotal += personA
    personBTotal += personB

print("Player A: {}".format(personATotal))
print("Player B: {}".format(personBTotal))
print("Rounds played {}".format(i))
if personATotal > personBTotal:
    print("Player A is winner!")
elif personATotal < personBTotal:
    print("Player B is winner")
elif personATotal == personBTotal:
    print("Tie")
else:
    print("Unknown Error")