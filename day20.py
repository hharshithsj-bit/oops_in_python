# day 20 - Bank Account Management System
# Concepts: Classes, Objects, Methods, Constructor, Encapsulation
class BankAccount:
    def __init__(self, name, account_number, balance=0):
        self.name = name
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"₹{amount} deposited successfully!")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid withdrawal amount.")
        elif amount > self.balance:
            print("Insufficient balance!")
        else:
            self.balance -= amount
            print(f"₹{amount} withdrawn successfully!")

    def check_balance(self):
        print(f"Current balance: ₹{self.balance}")

    def display_details(self):
        print("\n----- Account Details -----")
        print(f"Name: {self.name}")
        print(f"Account Number: {self.account_number}")
        print(f"Balance: ₹{self.balance}")

# Creating an object        
account1 = BankAccount("Harshith", 123456789, 5000)

while True:
    print("\n===== BANK MENU =====")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Account Details")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        amount = int(input("Enter deposit amount: ₹"))
        account1.deposit(amount)

    elif choice == "2":
        amount = int(input("Enter withdrawal amount: ₹"))
        account1.withdraw(amount)

    elif choice == "3":
        account1.check_balance()

    elif choice == "4":
        account1.display_details()

    elif choice == "5":
        print("Thank you for using our bank!")
        break

    else:
        print("Invalid choice! Try again.")
