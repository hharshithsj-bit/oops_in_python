

class Animal:
    def sound(self):
        print("Animals make different sounds")


class Dog(Animal):
    def sound(self):
        print("Dog says: Woof Woof!")


class Cat(Animal):
    def sound(self):
        print("Cat says: Meow Meow!")


class Cow(Animal):
    def sound(self):
        print("Cow says: Moo Moo!")

dog = Dog()
cat = Cat()
cow = Cow()

animals = [dog, cat, cow]

for animal in animals:
    animal.sound()
