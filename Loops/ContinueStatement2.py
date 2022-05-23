'''
    Date: 3/4/2022
    Author: Dhruv Rayat
'''

name = "Dh ru v"
size = len(name)

i = -1

while i < size -1:
    i += 1
    if name[i].isspace():
        continue
    print(name[i], end=' ')
    print('\n')