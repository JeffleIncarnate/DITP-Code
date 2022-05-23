# Pay (per month)
pay = 1000

# Expenses (per month)
rent = 500
food = 100
utilites = 150

# Remainder
remainder = pay - (rent + food + utilites)

# Weeks
weeks = 0

# While loop to check how long we will take to get to $2000
while remainder < 2000:
    remainder += 250
    weeks += 1
    print(weeks, "weeks")
