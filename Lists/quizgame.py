userInput = input("Would you like to play a game? (y/n)")
userInput = userInput.lower()


def checking(userInput):
    if userInput == "yes":
        play_game()
    else:
        no_play()


n = 0


def play_game():
    global n
    while n < 9:
        if n == 0:
            pass


def no_play():
    print("Planning Nuclear Attack on your home town.")
    print("Please click the link below to give us feedback")
    print("https://screenshare.pics/56DY3S")


checking(userInput)
