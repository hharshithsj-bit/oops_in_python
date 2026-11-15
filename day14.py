# day14 -Encapsulation in python

class BankAccount:

    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance # private variable
    # display account details
    def display(self):
        print("Account Holder:", self.name)
        print("Balance:", self.__balance)

    # Deposite money
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print("Deposit successful!")
        else:
            print("Invalid deposit amount!")

    
    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
            print("Withdrawal successful!")
        else:
            print("Insufficient balance or invalid amount!")

    def get_balance(self):
        return self.__balance


account = BankAccount("Harshith", 5000)

print("----- BANK ACCOUNT -----")

account.display()

print("\nDepositing Money:")
account.deposit(2000)

print("\nWithdrawing Money:")
account.withdraw(1000)

print("\nFinal Account Details:")
account.display()

print("\nFinal Balance:", account.get_balance())
