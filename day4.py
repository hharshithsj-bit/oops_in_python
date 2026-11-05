class Student:

    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks

    def display(self):
        print("\nStudent Details")
        print("Name:", self.name)
        print("Roll Number:", self.roll_no)
        print("Marks:", self.marks)

    def result(self):
        if self.marks >= 35:
            print("Result: PASS")
        else:
            print("Result: FAIL")


s1 = Student("Harshith", 101, 85)

s1.display()
s1.result()