
class BankAccount:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"₹{amount} deposited successfully!")
        else:
            print("Invalid deposit amount!")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"₹{amount} withdrawn successfully!")
        else:
            print("Insufficient balance or invalid amount!")

    def display_balance(self):
        print(f"\nAccount Holder: {self.name}")
        print(f"Current Balance: ₹{self.balance}")


# Main program
print("===== BANK MANAGEMENT SYSTEM =====")

name = input("Enter account holder name: ")
account = BankAccount(name, 1000)

while True:
    print("\n1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        amount = float(input("Enter deposit amount: "))
        account.deposit(amount)

    elif choice == "2":
        amount = float(input("Enter withdrawal amount: "))
        account.withdraw(amount)

    elif choice == "3":
        account.display_balance()

    elif choice == "4":
        print("Thank you for using our bank!")
        break

    else:
        print("Invalid choice! Try again.")
