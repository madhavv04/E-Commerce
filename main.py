from register import Register
from login import Login
from shopping import ShoppingSystem

class MainApp:
    def start(self):
        while True:
            print("\n1. Register\n2. Login\n0. Exit")
            choice = input("Enter choice: ")

            if choice == "1":
                Register().create_user()

            elif choice == "2":
                user = Login().authenticate()
                if user:
                    shop = ShoppingSystem(user)

                    while True:
                        print("\n1.Jeans \n2.Shirt \n3.T-shirt \n4.Cap \n0.Checkout")
                        c = input("Enter choice: ")

                        if c in ["1", "2", "3", "4"]:
                            shop.add_to_cart(c)
                        elif c == "0":
                            shop.checkout()
                            break
                        else:
                            print("Invalid choice\n")

            elif choice == "0":
                print("Exiting...")
                break

            else:
                print("Invalid Input\n")

if __name__ == "__main__":
    app = MainApp()
    app.start()
