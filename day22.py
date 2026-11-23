# Day 22 - Python OOP: Inheritence

# Parent class
class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating.")

    def sleep(self):
        print(f"{self.name} is sleeping.")


# Child class
class Dog(Animal):
    def bark(self):
        print(f"{self.name} is barking!")


class Cat(Animal):
    def meow(self):
        print(f"{self.name} is meowing!")


# Creating objects
dog1 = Dog("Rocky")
cat1 = Cat("Kitty")

# Creating methods
dog1.eat()
dog1.sleep()
dog1.bark()

print()

cat1.eat()
cat1.sleep()

cat1.meow()


