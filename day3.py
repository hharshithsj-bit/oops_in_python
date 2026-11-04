class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("Student Name:", self.name)
        print("Student Age:", self.age)

    def update_age(self,new_age):
        self.age = new_age
students = []
n = int(input("how many students?"))
for i in range(n):
    name = input("enter student name:")
    age = int(input("enter student age:"))
    student.append(student(name,age))
for s in students:
    s.display()
    
s1 = student[0]
s1.update_age(21)
print("updated info")
s1.display()
