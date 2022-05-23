password = "DhruvIsCool"
n = 0

while n < 3:
    password = input("Enter the password: ")
    if password == "DhruvIsCool":
        print("Access Granted")
        break
    else:
        print("Access Denied")

    n += 1
    if n == 3:
        print("You have entered the wrong password 3 times. Try again later.")