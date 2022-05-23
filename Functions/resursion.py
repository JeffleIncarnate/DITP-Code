def add(num):
    if num:
        return num + add(num - 1)
    else:
        return 0
        

print(add(10))
