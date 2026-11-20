


class BankAccount:

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"₹{amount} deposited successfully.")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"₹{amount} withdrawn successfully.")
        else:
            print("Insufficient balance or invalid amount.")

    def display(self):
        print("\n--- Account Details ---")
        print("Account Holder:", self.name)
        print("Balance: ₹", self.balance)



account = BankAccount("Harshith", 5000)

account.display()

account.deposit(2000)
account.withdraw(1500)

account.display()
