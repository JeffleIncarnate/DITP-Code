def guessing_game(userInput):
    try:
        if userInput == "Dhruv":
            return True
    except:
        return False

n = 0
while (n > 0):
    userInput = input("Guess my name: ")
    guessing_game(userInput)

    if guessing_game(userInput) == True:
        print("You guessed the word")
        break
    else:
        if i == 9:
            print("You didnt guess the word.")
        print("You were wrong.")
        print("You have {} more guessed".format(i))
        continue
    n += 1