import random

totalNum = random.randint(1, 10)


def guessing(humanGuess):
    print("You guessed: {}".format(humanGuess))
    computorGuess = random.randint(1, 10)
    print("The computor guessed: {}".format(computorGuess))

    if humanGuess == totalNum and computorGuess == totalNum:
        return 4
    elif humanGuess == totalNum:
        return 3
    elif computorGuess == totalNum:
        return 2
    else:
        return 1


i = 10
rangeMin = 1
rangeMax = 10
while i > 0:
    try:
        humanGuess = int(input("Guess a number between 1-10: "))
    except ValueError:
        print("Only use numbers")
        continue

    i += 1

    if humanGuess >= rangeMin and humanGuess <= rangeMax:
        k = guessing(humanGuess)
        if k == 4:
            print("You both are correct!")
            break
        elif k == 3:
            print("You won!")
            break
        elif k == 2:
            print("Computor won.")
            break
        else:
            print("You both are wrong.")
            continue
