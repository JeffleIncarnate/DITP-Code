'''
    Date: 3/4/2022
    Author: Dhruv Rayat
'''

num = int(input('Please Enter Number '))

while num > 0:
    if num % 2 == 0:
        print(num, "is a even number")
    else: 
        print(num, "is not an even number")
    num -= 1