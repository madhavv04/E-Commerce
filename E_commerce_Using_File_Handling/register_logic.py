import os 
import hashlib

def register():
    
    while True:
        name = input("Enter your name: ")
        if not name.isalpha():
            print("Name should contain only alphabets")
            continue #skip the rest of the loop body and start the next iteration of loop.”
        break

    while True:
        email = input("Enter your email: ")
        errors = []

        if  not email.strip():
            errors.append("Email cannot be empty or just spaces")

        if any(special_char in email for special_char in "$!#%^&*()"):
            errors.append("Special characters like $!#%^&*() are not allowed")

        if "@" not in email:
            errors.append("@ must be included")

        if ".com" not in email:
            errors.append(".com is mandatory")
            
        if email[0].isdigit():
            errors.append("Email id should not start with number")
            
        if not (("gmail" in email) or ("hotmail" in email) or ("yahoo" in email)):
            errors.append("Email must contain gmail, hotmail or yahoo")
        
        filename = f"{email}.txt"
        if os.path.exists(filename):
            print(" This email is already registered. Please enter another email.\n")
            continue
        
        if errors:
            print("Please fix the following issues : ")
            for err in errors:
                print("-",err,end="\n")
            continue

        while True:
            password = input("Enter your password: ")
            pwd_errors = []

            if len(password) < 8 or len(password) > 16:
                pwd_errors.append("Password must be between 8 and 16 characters.")
            if not any(c.isupper() for c in password):
                pwd_errors.append("Password must contain at least one uppercase letter.")
            if not any(c.islower() for c in password):
                pwd_errors.append("Password must contain at least one lowercase letter.")
            if not any(c.isdigit() for c in password):
                pwd_errors.append("Password must contain at least one number.")
            if not any(c in "@$!#%*?&" for c in password):
                pwd_errors.append("Password must contain at least one special character (@$!#%*?&).")
            if " " in password:
                pwd_errors.append("Password cannot contain spaces.")

            if pwd_errors:
                print("\n Please fix the following password issues:")
                for err in pwd_errors:
                    print(" -", err,end="\n")
                continue

            print("Password accepted!")
            break  # password loop ends
        
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        
        '''hashlib.sha256() → applies SHA-256 encryption (a strong, one-way hash).

        .encode() → converts the string to bytes (required by hashlib).

        .hexdigest() → converts the hash into a readable hexadecimal string.'''

        file = open(filename,'w')
        file.write("Name : " + name + '\n')
        file.write("Email : " + email + '\n')
        file.write("Password : " + hashed_password + '\n')
        file.close()
        
        print("User File '" + filename + "'Created Successfully")
        print("\n Registration Successful!")
        break  # email loop ends

# register() # For checking if register logic works properly or not