# Day 24 - Smart Expense Tracker
# Using Object-Oriented Programming (OOP)

# Class to store individual expense details
class Expense:
    def __init__(self, category, amount, description):
        self.category = category
        self.amount = amount
        self.description = description



class ExpenseTracker:
    def __init__(self):
        # Empty list to store all expenses
        self.expenses = []

    # Method to add a new expense
    def add_expense(self):
        category = input("Enter category: ")
        amount = float(input("Enter amount: ₹"))
        description = input("Enter description: ")

        # Create an expense object
        expense = Expense(category, amount, description)

        # Store the expense object in the list
        self.expenses.append(expense)

        print("Expense added successfully!")

    # Method to display all expenses
    def show_expenses(self):
        # Check whether the expense list is empty
        if not self.expenses:
            print("No expenses recorded.")
            return

        print("\n--- Expense History ---")

        # Loop through all expenses
        for i, expense in enumerate(self.expenses, start=1):
            print(f"{i}. {expense.category} - ₹{expense.amount:.2f}")
            print(f"   Description: {expense.description}")

    # Method to calculate total expenses
    def total_expenses(self):
        # Add all expense amounts together
        total = sum(expense.amount for expense in self.expenses)

        print(f"\nTotal Expenses: ₹{total:.2f}")

    # Method to calculate expenses category-wise
    def category_summary(self):
        # Dictionary to store total amount for each category
        summary = {}

        # Loop through all expenses
        for expense in self.expenses:
            # Add amount to existing category or create a new category
            summary[expense.category] = (
                summary.get(expense.category, 0) + expense.amount
            )

        print("\n--- Category Summary ---")

        # Display total spending for each category
        for category, amount in summary.items():
            print(f"{category}: ₹{amount:.2f}")


            
tracker = ExpenseTracker()

# Run the program continuously until the user exits
while True:
    print("\n===== SMART EXPENSE TRACKER =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Total Expenses")
    print("4. Category Summary")
    print("5. Exit")

    # Get the user's menu choice
    choice = input("Enter your choice: ")

    # Execute the selected operation
    if choice == "1":
        tracker.add_expense()

    elif choice == "2":
        tracker.show_expenses()

    elif choice == "3":
        tracker.total_expenses()

    elif choice == "4":
        tracker.category_summary()

    elif choice == "5":
        print("Thank you for using Expense Tracker!")
        break

    # Handle invalid menu choices
    else:
        print("Invalid choice. Try again.")
