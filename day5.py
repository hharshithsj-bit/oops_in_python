
class Employee:

    def __init__(self, name, emp_id, salary):
        self.name = name
        self.emp_id = emp_id
        self.salary = salary

    def display(self):
        print("\n--- Employee Details ---")
        print("Name:", self.name)
        print("Employee ID:", self.emp_id)
        print("Salary:", self.salary)

    def check_salary(self):
        if self.salary >= 50000:
            print("Salary Category: High")
        elif self.salary >= 25000:
            print("Salary Category: Medium")
        else:
            print("Salary Category: Low")


# Get employee details
name = input("Enter employee name: ")
emp_id = int(input("Enter employee ID: "))
salary = float(input("Enter salary: "))

# Create object
e1 = Employee(name, emp_id, salary)

# Call methods
e1.display()
e1.check_salary()
