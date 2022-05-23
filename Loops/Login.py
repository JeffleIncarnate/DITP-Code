'''
    Date: 3/4/2022
    Author: Dhruv Rayat
'''

def Login():
    while True:
        username = input("What is your Username: ")
        password = input("What is your Password: ")
        
        if username == "admin" and password == "1234":
            print("Welcome")
            Methods()
            break
        else:
            print("Invalid")

def Methods():
    while True:
        print("""
        1. Create Account
        2. View Account
        3. Delete Account
        4. Logout
        """)
        choice = int(input("Enter your choice: "))
        if choice == 1:
            print("Create Account")
            break
        elif choice == 2:
            print("View Account")
            break
        elif choice == 3:
            print("Delete Account")
        elif choice == 4:
            print("Logout")
            Login()
            break
        else:
            print("Invalid")

        
Login()
