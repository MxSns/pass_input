# Script: WIP

import getpass
import hashlib

# Variables
name = input("Enter your username : ")
password = None

def password_set():
    while True:
        global password
        password = getpass.getpass("Set a password: ")
        first_check = getpass.getpass("Please confirm your password: ")

        if first_check == password:
            hashed_password = hashlib.sha256(password.encode()).hexdigest()
            print("Password set")
            return hashed_password        
        else:
            print("Passwords don't match")
        
password = password_set()
user = [name, password]

print(f"\nHello {name}")
print(user)

check = getpass.getpass("Please enter your password: ")

if hashlib.sha256(check.encode()).hexdigest() == user[1]:
    print("\nAccess granted")
else:
    print("\nWrong password")
