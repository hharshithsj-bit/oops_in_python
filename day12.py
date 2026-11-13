
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_person(self):
        print("Name:", self.name)
        print("Age:", self.age)


class Student(Person):
    def __init__(self, name, age, usn, branch):
        super().__init__(name, age)
        self.usn = usn
        self.branch = branch

    def display_student(self):
        self.display_person()
        print("USN:", self.usn)
        print("Branch:", self.branch)


# Creating an object
student1 = Student(
    "Harshith",
    20,
    "4PS25EC001",
    "Electronics and Communication"
)

# Display student details
print("===== STUDENT DETAILS =====")
student1.display_student()
