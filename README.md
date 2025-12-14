
#  E-Commerce Management System (Python | OOP | CLI)

##  Project Description

This is a **console-based E-Commerce application** developed using Python and Object-Oriented Programming (OOP) concepts.

The system allows users to:

* Register with name, email, and password
* Login securely using hashed passwords
* Shop for products
* Add items to cart
* Generate a bill and save it to a user file

All user data and billing details are stored using **file handling**.


##  Features

* User Registration with validation
* Secure Login using SHA-256 password hashing
* Product selection and cart system
* Checkout and bill generation
* User-specific data storage
* Fully menu-driven CLI application
* Clean OOP-based structure


## Technologies Used

* **Python 3**
* **Object-Oriented Programming (OOP)**
* **File Handling**
* **Hashlib (SHA-256)**
* **OS Module**

## 📂 Project Structure

E_Commerce_Project/

│

├── main.py          # Main application flow

├── register.py      # User registration logic

├── login.py         # User login logic

├── product.py       # Product class

├── shopping.py      # Cart and billing system

│

└── users/           # Stores user files (email.txt)


## File Explanation

### `main.py`

* Entry point of the application
* Displays main menu (Register / Login / Exit)
* Connects all other modules

### `register.py`

* Handles user registration
* Validates name, email, and password
* Hashes password using SHA-256
* Creates a user file in `users/` folder

### `login.py`

* Authenticates user credentials
* Compares hashed password
* Allows login only if credentials match

### `product.py`

* Defines the Product class
* Stores product name and price

### `shopping.py`

* Manages shopping cart
* Allows adding products
* Generates bill
* Saves bill in user file


##  How to Run the Project

### Step 1: Clone or download the project

  git clone <repository-link>

### Step 2: Navigate to project folder

  cd E_Commerce_Project

### Step 3: Run the application

  python main.py

## Sample Flow

1. Start the program
2. Register a new user
3. Login using same credentials
4. Select products
5. Checkout
6. Bill is generated and saved

## Security

* Passwords are **never stored in plain text**
* Uses **SHA-256 hashing** for password security

## Future Enhancements

* Admin panel for managing products
* Store users in JSON or database
* Quantity validation
* Discount and coupon system
* GUI or web version using Flask

---

## Author

**Madhav Jariwala**
Python Developer | OOP Enthusiast

---

