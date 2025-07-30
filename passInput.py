# Script: WIP

import getpass

# Variables
name = input("Enter your name : ")
password = None

def password_set():
    global password
    password = getpass.getpass("Set a password: ")
    first_check = input("Please confirm your password: ")

    if first_check == password:
        print("Password set")
        return password        
    else:
        print("Passwords don't match")
        password_set()

password_set()

user = [name, password]

print(f"\nHello {name}")
print(user)

check = input("Please enter your password: ")

if user[1] == check:
    print("\nAccess granted")
else:
    print("\nWrong password")
