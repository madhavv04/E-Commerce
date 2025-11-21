import os
import hashlib
def login():
    name = input("Enter your name: ")
    email = input("Enter your email: ")
   
    # Check if user file exists
    filename = f"{email}.txt"
    if not os.path.exists(filename):
        print(f"No file found with name '{filename}'")
        print("Please register yourself and then try to login.\n")    
        return None # stop execution if user not found
    
    password = input("Enter your password: ")
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    data = open(filename,'r')
    f=data.read()

    if (name in f) and (hashed_password in f):
        print("Login Successfully")
        current_user = {
            "name": name,
            "email": email
        }
        print(f"Welcome , {name}! {(current_user)} ")
        return current_user
    
    else:
        print("Invalid name or password ")
        print("Please try again.\n")
        return None
    
# login()
    
