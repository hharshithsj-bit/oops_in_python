
class Student:
    def __init__(self, name, usn, marks):
        self.name = name
        self.usn = usn
        self.marks = marks

    def display_details(self):
        print("\n----- Student Details -----")
        print("Name:", self.name)
        print("USN:", self.usn)
        print("Marks:", self.marks)

    def check_result(self):
        if self.marks >= 35:
            print("Result: PASS")
        else:
            print("Result: FAIL")


# Main program
print("STUDENT MANAGEMENT SYSTEM")

name = input("Enter student name: ")
usn = input("Enter USN: ")
marks = float(input("Enter marks: "))

student1 = Student(name, usn, marks)

student1.display_details()
student1.check_result()
