n = 1
def count(i, size):
    global n
    if i <= 100 and size <= 20:
        while n <= 100: 
            print("___________________"); print("Dress Mart Clothing"); print("   --Size: {}--".format(size)); print("|_________________|"); n += 1
        i += 1; size += 2; n = 1; count(i, size)
    else: 
        if i == 100: return None
count(10, 6)