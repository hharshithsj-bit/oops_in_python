# Day 21 - Python Tnheritance

# Parent class
class Animal:
    def eat(self):
        print("Animals can eat food.")

    def sleep(self):
        print("Animals can sleep.")


# Child class
class Dog(Animal):
    def bark(self):
        print("Dog is barking!")

# Create object
my_dog = Dog()

# Access parent class methods
my_dog.eat()
my_dog.sleep()

# Access child class method
my_dog.bark()
