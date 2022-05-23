'''
    Date: 3/4/2022
    Author: Dhruv Rayat
'''

for i in range(1, 11):
    if i % 2 == 0:
        continue
    print("Multiplication of", i)
    for j in range(1, 11):
        print(i * j, end=' ')
    print('')