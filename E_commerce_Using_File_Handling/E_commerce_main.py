from register_logic import *
from login_logic import *

User = []   # To store all users who register and shop

while True:
    print("\n------------------------")
    print("Welcome to our E-Commerce Page")
    print("------------------------")
    print("1. Register")
    print("2. Login")
    print("0. Exit")
    print("------------------------")

    Decision = input("Press 1 - Register\nPress 2 - Login\nPress 0 - Exit \n\n--> ")
   
    # ---------------- REGISTER ----------------
    if Decision == "1":
        register()

    # ---------------- LOGIN ----------------
    elif Decision == "2":
        current_user = login()   # returns dictionary {name, email}
        if not current_user:
            continue  # go back to menu if login failed

        # Initialize user's cart and total
        current_user["cart"] = []
        current_user["total"] = 0
        User.append(current_user)

        # ---------------- SHOPPING MENU ----------------
        while True:
            print("----------------")
            print("|  1. Jeans    |  200 each")
            print("|  2. Shirt    |  500 each")
            print("|  3. T-shirt  |  150 each")
            print("|  4. Cap      |  250 each")
            print("|  0. Checkout |")
            print("----------------")

            choice = input("Enter the choice you want : ")

            if choice == '1':
                product = "Jeans"
                price = 200
            elif choice == '2':
                product = "Shirt"
                price = 500
            elif choice == '3':
                product = "T-shirt"
                price = 150
            elif choice == '4':
                product = "Cap"
                price = 250
            elif choice == '0':
                # ---------------- CHECKOUT ----------------
                print("\n----------------------------------")
                print(f" Bill for {current_user['name']} ({current_user['email']})")
                print("----------------------------------")

                if not current_user["cart"]:
                    print("Your cart is empty.")
                else:
                    total_amount = 0
                    print(f"{'Product':<12}{'Qty':<8}{'Price':<10}{'Amount'}")
                    print("-" * 40)
                    for item in current_user["cart"]:
                        pname = item["product"]
                        qty = item["quantity"]
                        price = item["price"]
                        amount = qty * price
                        total_amount += amount
                        print(f"{pname:<12}{qty:<8}{price:<10}{amount}")

                    print("-" * 40)
                    print(f"{'Total Amount':<30}{total_amount}")
                    print("----------------------------------")

                    # Save bill details to user file
                    filename = f"{current_user['email']}.txt"
                    f=open(filename, "a")
                    f.write("\n--- Shopping Cart ---\n")
                    for item in current_user["cart"]:
                        pname = item["product"]
                        qty = item["quantity"]
                        price = item["price"]
                        amount = qty * price
                        f.write(f"{pname:<12}Qty: {qty:<5}Price: {price:<5}Amount: {amount}\n")
                        f.write(f"Total Bill: {total_amount}\n")
                        f.write("--------------------------\n")

                    # Empty the cart after checkout
                    # current_user["cart"].clear()
                    # current_user["total"] = 0

                print("Thank you for shopping with us!\n")
                break

            else:
                print("Invalid choice, try again.\n")
                continue

            qty = int(input(f"How many {product}s you want? : "))
            total = qty * price
            print(f"Amount for {qty} {product}(s): {total}\n")

            # Add to cart
            current_user["cart"].append({
                "product": product,
                "quantity": qty,
                "price": price
            })
            current_user["total"] += total

            print("Added to cart successfully!\n")

    # ---------------- EXIT ----------------
    elif Decision == "0":
        
        print("\nAll users who registered and bought products:\n")
        
        for u in User:
            print(f"User : {u['name']}  ({u['email']})")

            if u["cart"]:
                print(f"{'Product':<12}{'Qty':<8}{'Price':<10}{'Amount'}")
                print("-" * 40)
                total = 0
                for item in current_user["cart"]:
                    pname = item["product"]
                    qty = item["quantity"]
                    price = item["price"]
                    amount = qty * price
                    total += amount
                    print(f"{pname:<12}{qty:<8}{price:<10}{amount}")
                print("-" * 40)
                print(f"Total Amount : {total}")
            else:
                print("No products purchased.")
            print("----------------------------------\n")

        print("Thank you for visiting!")
        current_user["cart"].clear()
        current_user["total"] = 0
        break

    else:
        print("Invalid Input. Please try again.")
