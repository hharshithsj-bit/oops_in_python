
class Student:
    # Constructor
    def __init__(self, name, usn, branch, marks):
        self.name = name
        self.usn = usn
        self.branch = branch
        self.marks = marks

    # Display student details
    def display(self):
        print("\n----- Student Details -----")
        print("Name:", self.name)
        print("USN:", self.usn)
        print("Branch:", self.branch)
        print("Marks:", self.marks)

    # Check result
    def result(self):
        if self.marks >= 35:
            print("Result: PASS")
        else:
            print("Result: FAIL")


# Creating objects
student1 = Student("Harshith", "1PE25EC001", "ECE", 85)

student2 = Student("Rahul", "1PE25EC002", "CSE", 85)

# Calling methods
student1.display()
student1.result()

student2.display()
student2.result()
