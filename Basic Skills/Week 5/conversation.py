import random

hi_s = ["hello", "hi", "heyo", "what's up?"]
rnd_Hi = random.choice(hi_s)
n = 0


while n < 3:
    print(rnd_Hi)

    input("How are you? ")
    print("Wow! Thats so interesting or super sad!")

    input("What is your name: ")
    print("Wow! That's such as good or bad name!")

    input("What is your favourite food: ")
    print("Wow! That food sucks!")
