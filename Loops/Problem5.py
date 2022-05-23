def main():
    print("Please enter a number:")
    number = int(input())
    print("Please enter a maximum value:")
    max = int(input())
    for i in range(number, max + 1, number):
        print(i)

main()