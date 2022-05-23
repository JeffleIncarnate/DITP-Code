#A cup of tea is the right temperature to drink at 112 degrees. If the temperature starts at 115, how can we write a while loop to tell a person when it is cool enough to drink?

def main():
    temp = int(input("What is the temperature of your tea? "))
    while temp > 112:
        print("The temperature is", temp, "degrees. It is not time to drink yet.")
        temp = temp - 1
    print("The temperature is", temp, "degrees. It is time to drink.")

main()