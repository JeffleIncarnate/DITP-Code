def main():
    while True:
        # Initialize variables
        money = 0
        bills = 0
        weeks = 0

        # Get user input
        money = int(input("How much money do you have? "))
        bills = int(input("How much bills do you have? "))

        # Calculate
        weeks = (money + bills) / 1000

        # Print
        print("It will take", weeks, "weeks to retire.")

main()