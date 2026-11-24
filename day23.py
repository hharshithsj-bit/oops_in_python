# Day 23 - Inheritance and Method Overriding

class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        print("Animal makes a sound")


class Dog(Animal):
    def sound(self):
        print(f"{self.name} says Woof!")


class Cat(Animal):
    def sound(self):
        print(f"{self.name} says Meow!")


# Creating objects
dog = Dog("Rocky")
cat = Cat("Kitty")

# Calling methods
dog.sound()
cat.sound()
