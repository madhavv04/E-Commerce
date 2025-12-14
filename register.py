import os
import hashlib

class Register:

    def create_user(self):
        while True:
            name = input("Enter your name: ")
            if not name.isalpha():
                print("Name should contain only alphabets")
                continue
            break

        while True:
            email = input("Enter your email: ")
            errors = []

            if not email.strip():
                errors.append("Email cannot be empty")
            if any(ch in email for ch in "$!#%^&*()"):
                errors.append("Invalid characters in email")
            if "@" not in email or ".com" not in email:
                errors.append("Email must contain @ and .com")
            if email[0].isdigit():
                errors.append("Email cannot start with a number")
            if not (("gmail" in email) or ("hotmail" in email) or ("yahoo" in email)):
                errors.append("Email must contain gmail/yahoo/hotmail")

            filename = f"users/{email}.txt"
            if os.path.exists(filename):
                print("Email already registered\n")
                continue

            if errors:
                print("Fix these issues:")
                for e in errors:
                    print("-", e)
                continue

            break

        while True:
            password = input("Enter password: ")
            pwd_errors = []

            if len(password) not in range(8, 17):
                pwd_errors.append("Password must be 8–16 characters")
            if not any(c.isupper() for c in password):
                pwd_errors.append("Must contain uppercase letter")
            if not any(c.islower() for c in password):
                pwd_errors.append("Must contain lowercase letter")
            if not any(c.isdigit() for c in password):
                pwd_errors.append("Must contain a number")
            if not any(c in "@$!#%*?&" for c in password):
                pwd_errors.append("Must contain a special character")

            if pwd_errors:
                print("Fix password issues:")
                for e in pwd_errors:
                    print("-", e)
                continue
            break

        os.makedirs("users", exist_ok=True)
        hashed = hashlib.sha256(password.encode()).hexdigest()

        with open(filename, "w") as f:
            f.write(f"Name:{name}\n")
            f.write(f"Email:{email}\n")
            f.write(f"Password:{hashed}\n")

        print("\nRegistration Successful!")
        return True
