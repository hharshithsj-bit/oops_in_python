
class BankAccount:
    def __init__(self, name, account_number, balance):
        self.name = name
        self.account_number = account_number
        self.balance = balance

    def display_details(self):
        print("\n--- Account Details ---")
        print("Account Holder:", self.name)
        print("Account Number:", self.account_number)
        print("Balance: Rs.", self.balance)

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print("Amount deposited successfully!")
        else:
            print("Invalid deposit amount!")

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid withdrawal amount!")
        elif amount <= self.balance:
            self.balance -= amount
            print("Withdrawal successful!")
        else:
            print("Insufficient balance!")


# Creating an object
account1 = BankAccount("Harshith", 123456, 5000)

while True:
    print("\n===== BANK MENU =====")
    print("1. Display Account Details")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Check Balance")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        account1.display_details()

    elif choice == 2:
        amount = float(input("Enter deposit amount: "))
        account1.deposit(amount)

    elif choice == 3:
        amount = float(input("Enter withdrawal amount: "))
        account1.withdraw(amount)

    elif choice == 4:
        print("Current Balance: Rs.", account1.balance)

    elif choice == 5:
        print("Thank you for using our bank!")
        break

    else:
        print("Invalid choice! Try again.")
