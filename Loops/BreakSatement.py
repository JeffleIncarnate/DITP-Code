'''
    Date: 3/4/2022
    Author: Dhruv Rayat
'''

name = "Dhruv"
size = len(name)
i = 0

while i < size:
    if name[i].isdecimal():
        break
    print(name[i], end='\n')
    i += 1