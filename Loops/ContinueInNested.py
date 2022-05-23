'''
    Date: 3/4/2022
    Author: Dhruv Rayat
'''

for i in range(1, 11):
    print("Multiplication table of ", i)
    for j in range(1, 11):
        if j == 5:
            continue
        print(i * j, end=' ')
    print('')