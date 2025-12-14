import os
import hashlib

class Login:

    def authenticate(self):
        name = input("Enter your name: ")
        email = input("Enter your email: ")

        filename = f"users/{email}.txt"
        if not os.path.exists(filename):
            print("User not found. Register first.\n")
            return None

        password = input("Enter password: ")
        hashed = hashlib.sha256(password.encode()).hexdigest()

        with open(filename, "r") as f:
            data = f.read()

        if (name in data) and (hashed in data):
            print("Login Successful!\n")
            return {"name": name, "email": email}
        else:
            print("Invalid credentials!\n")
            return None
