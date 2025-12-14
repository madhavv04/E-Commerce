from product import Product
import os

class ShoppingSystem:

    def __init__(self, user):
        self.user = user
        self.cart = []

        self.products = {
            "1": Product("Jeans", 200),
            "2": Product("Shirt", 500),
            "3": Product("T-shirt", 150),
            "4": Product("Cap", 250)
        }

    def add_to_cart(self, choice):
        product = self.products[choice]
        qty = int(input(f"How many {product.name}s? : "))
        self.cart.append({"product": product, "qty": qty})
        print(f"{qty} {product.name}(s) added!\n")

    def checkout(self):
        print("\n------ BILL ------")
        print(f"Customer: {self.user['name']}  ({self.user['email']})")
        print("-------------------")

        total = 0
        for item in self.cart:
            p = item["product"]
            qty = item["qty"]
            amount = qty * p.price
            total += amount
            print(f"{p.name:<10} Qty: {qty:<3} Price: {p.price:<5} Amount: {amount}")

        print("-------------------")
        print("Total:", total)

        os.makedirs("users", exist_ok=True)
        filename = f"users/{self.user['email']}.txt"

        with open(filename, "a") as f:
            f.write("\n--- Shopping Bill ---\n")
            for item in self.cart:
                p = item["product"]
                qty = item["qty"]
                f.write(f"{p.name} x {qty} = {p.price * qty}\n")
            f.write(f"Total = {total}\n")

        print("\nThank you for shopping!\n")
