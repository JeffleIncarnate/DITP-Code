"""
    DATE: 11/03/2022
    AUTHOR = DHRUV RAYAT
"""

clothes = input("How much would you spend on a Clothes per month? ")
transport = input("How much would you spend on Transport per month? ")
food = input("How much would you spend on Food per month? ")
rent = input("How much would you spend on Rent per month? ")

clothes = int(clothes)
transport = int(transport)
food = int(food)
rent = int(rent)

total = clothes + transport + food + rent

print("Your total spending is $", total)
