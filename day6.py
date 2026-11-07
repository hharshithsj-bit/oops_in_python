
class BankAccount:

    def __init__(self, name, account_no, balance):
        self.name = name
        self.account_no = account_no
        self.balance = balance

    def display(self):
        print("\n--- Account Details ---")
        print("Account Holder:", self.name)
        print("Account Number:", self.account_no)
        print("Balance: Rs.", self.balance)

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print("Amount deposited successfully!")
        else:
            print("Invalid deposit amount")

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid withdrawal amount")
        elif amount <= self.balance:
            self.balance -= amount
            print("Amount withdrawn successfully!")
        else:
            print("Insufficient balance")

    def check_balance(self):
        print("Available Balance: Rs.", self.balance)


# Get account details
name = input("Enter account holder name: ")
account_no = int(input("Enter account number: "))
balance = float(input("Enter initial balance: "))

# Create object
account = BankAccount(name, account_no, balance)

while True:
    print("\n--- Banking Menu ---")
    print("1. Display Account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Check Balance")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        account.display()

    elif choice == 2:
        amount = float(input("Enter deposit amount: "))
        account.deposit(amount)

    elif choice == 3:
        amount = float(input("Enter withdrawal amount: "))
        account.withdraw(amount)

    elif choice == 4:
        account.check_balance()

    elif choice == 5:
        print("Thank you for using our bank!")
        break

    else:
        print("Invalid choice!")
